# from sys import api_version
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

client = KafkaAdminClient(
    bootstrap_servers=["localhost:9092"],
    api_version=(0, 9),
)
print("API version:", client.config["api_version"])
print(client.list_topics())
# breakpoint()

topic_list = []
topic_list.append(NewTopic(name="g5-topic-1", num_partitions=1, replication_factor=1))

client.create_topics(new_topics=topic_list, validate_only=False)
print("\nTopic created!\n")
print(client.list_topics())