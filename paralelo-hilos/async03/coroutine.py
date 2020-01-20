import asyncio

# Definimos una función asíncrona
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

#Ejecutamos la función asíncrona
asyncio.run(main())

import asyncio
import time

# Función asíncrona
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

# Definición de Main
async def main():
    print(f"started at {time.strftime('%X')}")
    # lanza aíncrona 1
    await say_after(1, 'hello')
    # lanza aíncrona 1
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# create_task ejecuta corutinas de manera concurrente como Task
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# Los awaitables son objetos que se pueden utilizar con await
# Hay tres tipos coroutine, Task y Futures
import asyncio

async def nested():
    return 42

async def main():
    # Aquí esperamos a que se termine de ejecutar nested()
    print(await nested())  # will print "42".

asyncio.run(main())


# Task es otro tipo de awaitable
import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    print(await task)

asyncio.run(main())

# Future son objetos que son necesarios en las funciones de callback
# que son usadas con async03/await

import asyncio

async def nested():
    return 42

async def main():
    await nested()

    # this is also valid:
    await asyncio.gather(
        nested(),
        # otra_corutina()
    )
asyncio.run(main())


