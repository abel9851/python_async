import asyncio
import timeit

import requests

URL = "http://localhost:8000/delay-me?seconds="
COLORS = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[93m"]
ENDC = "\033[0m"


class Requester:
    rid: int = 0

    def __init__(self):
        Requester.rid += 1
        self.rid = Requester.rid
        self.color = COLORS[self.rid]

    async def pull_from_server(self, secs: int) -> None:
        """
        Assigning a method as 'async' does no magic trick.
        This function is still SYNC.
        """
        url = f"{URL}{secs}"
        prefix = f"{self.color}R{self.rid}: "
        suffix = ENDC
        print(f"{prefix}Requesting '{url}'{suffix}")

        # Declaring a function with async def does no magic trick, you need a lib that supports it.
        content = requests.get(
            url
        ).text  # 이녀석이 request를 하는 메인인데, 이 라이브러리 안에서 비동기 처리를 하지 않는다면 겉으로 비동기 처리를 해도 속도는 빨라지지 않는다.
        print(f"{prefix}Request is finally done! Server replied '{content}'{suffix}")


async def main() -> None:
    r1 = Requester()
    r2 = Requester()
    r3 = Requester()

    print("=" * 10)
    starttime = timeit.default_timer()

    await asyncio.gather(
        r1.pull_from_server(10), r2.pull_from_server(2), r3.pull_from_server(5)
    )
    print("-" * 10)
    print(f"Time elapsed: {timeit.default_timer() - starttime}")
    print("=" * 10)


if __name__ == "__main__":
    asyncio.run(main())
