import asyncio
import aiohttp
import uvloop
import datetime

from colorama import init
from colorama import Fore, Back, Style


async def main(loop: str, colour: str):
    print(
        colour + f"Begging to do web requests with {loop}",
        flush=True,
    )
    start_time = datetime.datetime.now()
    urls = [
        "https://jsonplaceholder.typicode.com/photos",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/todos",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/users",
    ]
    tasks = [get_web_stuff(url) for url in urls]
    await asyncio.gather(*tasks)
    end_time = datetime.datetime.now() - start_time

    print(
        colour
        + f"Ending web requests. Total time: {end_time.total_seconds(): .2} sec.",
        flush=True,
    )
    print(Style.RESET_ALL)


async def get_web_stuff(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()

            json = await response.json()
            return json


if __name__ == "__main__":
    init()
    asyncio.run(main("asyncio", Back.GREEN + Fore.WHITE))
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    asyncio.run(main("uvloop", Back.CYAN + Fore.WHITE))
