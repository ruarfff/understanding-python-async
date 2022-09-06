import time
import datetime
import asyncio

from fastapi import FastAPI
from google.cloud import pubsub_v1

from colorama import Fore, Back

app = FastAPI()


@app.get("/")
async def root():
    start_time = datetime.datetime.now()
    print(
        Back.GREEN + Fore.WHITE + f"Hello world started at: {start_time}.",
        flush=True,
    )
    # await asyncio.sleep(4)
    return {"message": "Hello World"}


@app.get("/slow")
async def slow():
    start_time = datetime.datetime.now()
    print(
        Back.LIGHTMAGENTA_EX + Fore.WHITE + f"Slow started at: {start_time}.",
        flush=True,
    )
    time.sleep(4)
    return {"message": "So slow"}


@app.get("/sync-slow")
def sync_slow():
    start_time = datetime.datetime.now()
    print(
        Back.LIGHTRED_EX + Fore.WHITE + f"Sync slow started at: {start_time}.",
        flush=True,
    )
    time.sleep(4)
    return {"message": "So slow"}


@app.get("/async-slow")
async def async_slow():
    start_time = datetime.datetime.now()
    print(
        Back.LIGHTYELLOW_EX + Fore.WHITE + f"Async slow started at: {start_time}.",
        flush=True,
    )
    await asyncio.sleep(4)
    return {"message": "So slow but async"}


@app.get("/fast")
async def fast():
    start_time = datetime.datetime.now()
    print(
        Back.BLUE + Fore.WHITE + f"Fast started at: {start_time}.",
        flush=True,
    )
    return {"message": "No waiting here"}


def create_standard_subscription() -> None:
    project_id = "example-project"
    topic_id = "testing"
    subscription_id = "testing-subscription"

    publisher = pubsub_v1.PublisherClient()

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    topic_path = publisher.topic_path(project_id, topic_id)
    try:
        subscriber.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )
    except:
        print("Subscription already exists")

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        start_time = datetime.datetime.now()
        if message.data.decode("utf-8") == "non-blocking":
            print(
                Back.BLUE + Fore.WHITE + f"Starting async message at: {start_time}.",
                flush=True,
            )
            message.ack()
        elif message.data.decode("utf-8") == "blocking":
            print(
                Back.LIGHTMAGENTA_EX
                + Fore.WHITE
                + f"Starting sync message at: {start_time}.",
                flush=True,
            )
            time.sleep(5)
            message.ack()

    subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")


create_standard_subscription()
