import asyncio
import time


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')
    await asyncio.sleep(20)
    print("sec")

async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')
    await asyncio.sleep(20)
    print("sec")

async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))
    await task1
    await task2
    #
    # await fun1(4)
    # await fun2(4)


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))