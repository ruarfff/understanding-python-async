from google.cloud import pubsub_v1 as pubsub
import itertools


def main():
    publisher = pubsub.PublisherClient()

    project_id = "example-project"
    aio_topic_id = "testing_aio"

    publisher = pubsub.PublisherClient()

    print("setup a new topic to show how to mess things up")
    aio_topic_path = publisher.topic_path(project_id, aio_topic_id)

    try:
        aio_topic = publisher.create_topic(request={"name": aio_topic_path})
        print(f"Created topic: {aio_topic.name}")
    except:
        print("Topic already exists")

    print("Run 1 aio-blocking")
    for _ in itertools.repeat(None, 1):
        future = publisher.publish(aio_topic_path, b"blocking")
        print(future.result())

    print("Run 5 non-blocking")
    for _ in itertools.repeat(None, 5):
        future = publisher.publish(aio_topic_path, b"non-blocking")
        print(future.result())


if __name__ == "__main__":
    main()
