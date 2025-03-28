import asyncio
import timeit

import aiohttp

URL = "http://localhost:8000/delay-me?seconds="
COLORS = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[93m"]
ENDC = "\033[0m"


# 서버가 느리더라도, request할 때 사용하는 라이브러리가 비동기라면, 충분히 빨라질수 있다는 것이군.
class Requester:
    rid: int = 0

    def __init__(self):
        Requester.rid += 1
        self.rid = Requester.rid
        self.color = COLORS[self.rid]

    async def pull_from_server(self, secs: int) -> None:
        url = f"{URL}{secs}"
        prefix = f"{self.color}R{self.rid}: "
        suffix = ENDC
        print(f"{prefix}Requesting '{url}'{suffix}")

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:  # event loop?
                content = await resp.text()
                print(
                    f"{prefix}Request is finally done! Server replied '{content}'{suffix}"
                )


async def main() -> None:
    r1 = Requester()
    # r2 = Requester()
    # r3 = Requester()

    print("=" * 10)
    starttime = timeit.default_timer()

    # await asyncio.gather(
    #     r1.pull_from_server(10), r2.pull_from_server(2), r3.pull_from_server(5)
    # )

    await asyncio.gather(r1.pull_from_server(10))

    print("-" * 10)
    print(f"Time elapsed: {timeit.default_timer() - starttime}")
    print("=" * 10)


if __name__ == "__main__":
    asyncio.run(main())
