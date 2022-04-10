import asyncio
import datetime
import time

from colorama import init
from colorama import Fore, Back, Style


async def main():

    print(Back.GREEN + Fore.WHITE + "Starting synchronous work.", flush=True)

    start_time = datetime.datetime.now()

    synchronous_work()
    synchronous_work()

    end_time = datetime.datetime.now() - start_time

    print(
        Back.GREEN
        + Fore.WHITE
        + f"Ending synchronous work. Total time: {end_time.total_seconds(): .2} sec.",
        flush=True,
    )

    print(Back.MAGENTA + Fore.WHITE + "Starting awaiting async functions.", flush=True)

    start_time = datetime.datetime.now()

    await async_work(Back.LIGHTYELLOW_EX + Fore.WHITE)
    await async_work(Back.LIGHTRED_EX + Fore.WHITE)

    end_time = datetime.datetime.now() - start_time

    print(
        Back.MAGENTA
        + Fore.WHITE
        + f"Ending awaiting async functions. Total time: {end_time.total_seconds(): .2} sec.",
        flush=True,
    )

    print(Back.LIGHTBLUE_EX + Fore.WHITE + "Starting running async.", flush=True)

    start_time = datetime.datetime.now()

    tasks = [
        async_work(Back.LIGHTYELLOW_EX + Fore.WHITE),
        async_work(Back.LIGHTRED_EX + Fore.WHITE),
    ]

    await asyncio.gather(*tasks)

    end_time = datetime.datetime.now() - start_time

    print(
        Back.LIGHTBLUE_EX
        + Fore.WHITE
        + f"Ending running async. Total time: {end_time.total_seconds(): .2} sec.",
        flush=True,
    )

    print(Style.RESET_ALL)


def synchronous_work():
    print(Back.CYAN + Fore.WHITE + "Pretending to wait.")
    time.sleep(2)


async def async_work(colour: str = Fore.WHITE):
    print(colour + "Pretending to wait async.")
    await asyncio.sleep(2)


if __name__ == "__main__":
    init()
    asyncio.run(main())
