# Tareas concurrentes
import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

asyncio.run(main())

import asyncio

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    for i in range(1,5):
        await asyncio.gather(
            factorial(i, i),
        )

asyncio.run(main())

# No hay que usar shield() se quita en 3.10, obsoleta en 3.8


# timeout
async def eternity():
    # Sleep for one hour
    a = 2
    print("Eternity")
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    # Si ocurre el timeout cancela la tarea y lanza una excepción asyncio.TimeoutError
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())