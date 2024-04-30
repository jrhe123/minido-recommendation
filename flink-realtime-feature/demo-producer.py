import random
from json import dumps

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: dumps(x).encode("utf-8"),
)


for _ in range(100000000000):
    data = {}
    data["user_id"] = str(random.sample([1, 2, 3], 1)[0])
    data["anime_id"] = str(random.sample([1, 2, 3], 1)[0])
    data["happened_at"] = "1"

    producer.send("clicks", value=data)
    print(data)

    sleep_ms = 1.0 * random.randint(1, 400)
    sleep(sleep_ms / 1000.0)
