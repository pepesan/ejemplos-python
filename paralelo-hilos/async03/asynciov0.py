import asyncio # dependencia

async def main(): # función asíncrona
    print('hello')
    await asyncio.sleep(1) # ejecución suspendida
    print('world')

asyncio.run(main())

