from google.cloud import pubsub_v1 as pubsub
import itertools


def main():
    publisher = pubsub.PublisherClient()

    project_id = "example-project"
    topic_id = "testing"

    publisher = pubsub.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)

    try:
        topic = publisher.create_topic(request={"name": topic_path})
        print(f"Created topic: {topic.name}")
    except:
        print("Topic already exists")

    print("Run 5 non-blocking")
    for _ in itertools.repeat(None, 5):
        future = publisher.publish(topic_path, b"non-blocking")
        print(future.result())

    print("Run 5 blocking")
    for _ in itertools.repeat(None, 5):
        future = publisher.publish(topic_path, b"blocking")
        print(future.result())


if __name__ == "__main__":
    main()
