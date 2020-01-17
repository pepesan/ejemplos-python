# coding: utf8

import os
import sys
curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.split(curr_dir)[0])

import itertools
import asyncio as aio
from asyncio_pool import AioPool
#<<from_here
async def worker(n):  # dummy worker
    await aio.sleep(1 / n)
    return n


async def spawn_n_usage(todo=[range(1,51), range(51,101), range(101,200)]):
    futures = []
    async with AioPool(size=20) as pool:
        for tasks in todo:
            for i in tasks:  # too many tasks
                # Returns quickly for all tasks, does not wait for pool space.
                # Workers are not spawned, they wait for pool space in their
                # own background tasks.
                fut = await pool.spawn_n(worker(i))
                futures.append(fut)
        # At this point not a single worker should start.

        # Context manager calls `join` at exit, so this will finish when all
        # workers return, crash or cancelled.

    assert sum(itertools.chain.from_iterable(todo)) == \
        sum(f.result() for f in futures)
    for f in futures:
        print(f.result())

if __name__ == "__main__":
    aio.get_event_loop().run_until_complete(aio.gather(spawn_n_usage()))