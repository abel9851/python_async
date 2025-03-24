import asyncio


async def anyfunc():
    return 1


# r = anyfunc()
# print(r)  # <coroutine object anyfunc at 0x1027566c0>
# print(type(r))  # <class 'coroutine'>
# #  <sys>:0: RuntimeWarning: coroutine 'anyfunc' was never awaited


# async def main():
#     anyfunc()


# # 내가 await할 때 마다 eventloop에게 coroutine을 처리하도록 요청하고 나에게 결과를 돌려달라고 하는 것이다.
# # 그리고 await 키워드가 없다면 never awaited라고 출려되며 이는 결코 실행되지 않는다.
# if __name__ == "__main__":
#     asyncio.run(
#         main()
#     )  # RuntimeWarning: coroutine 'anyfunc' was never awaited    anyfunc() RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# eventloop -> task(coroutine)
# create_task 대신에 await 키워드를 사용하면 이는 task가 되고, event loop에 양도된다?
# await <coroutine>을 사용하면 event loop에게 다음에 어떤 것을 할지 결정해줘! 라고 부탁하는 것이다.
# async def로 정의하면 coroutine object가 된다. await 혹은 create_task함수를 사용하면 event loop에게 양도하는 것이다.
# sync는 차례대로 명령을 실행하는 거고, async는 event loop에게 제어권을 넘겨주는 것이다.
# 그렇다면 eventloop란 무엇일까?
async def main():
    r = anyfunc()
    task = asyncio.create_task(r)  # coroutine은 event loop에 양도된다.
    print(type(task))  # <class '_asyncio.Task'>

    print(await task)  # 1


if __name__ == "__main__":
    asyncio.run(main())
