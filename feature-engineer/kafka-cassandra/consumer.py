from kafka import KafkaConsumer, consumer
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
import os
import datetime

KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')

# cassandra connection
cloud_config= {
    'secure_connect_bundle': 'secure-connect-recommendation-v0.zip'
}
auth_provider = PlainTextAuthProvider(
    "wysGSOxHcTanIsqxASCbbHUb",
    "oyjzCmWkz_ZFsrnv13gJ8eGI7Kb3gxkstGoO3Y.FaG-aS.2RR+gY.7qCiBdgULjKANnCZ36ZlLBFY+U5wCuYeR3czTQIyCJHz1FdPcpDIiAU9t2F-9Dn_t_XYFLCCR50",
)
cluster = Cluster(
    cloud=cloud_config,
    auth_provider=auth_provider,
)
session = cluster.connect()
print(">>>>>>>>> Cassandra connected")

def consume_kafka():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True, # auto acknowledge the event
        group_id='group-0',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    return consumer

for item in consume_kafka():
    event = item.value

    print(event)

    session.execute(
        f"""
        INSERT INTO minichat.{KAFKA_TOPIC} (user_id, anime_id, happened_at)
        VALUES (%s, %s, %s)
        """,
        (
            int(event['user_id']),
            int(event['anime_id']),
            datetime.datetime.fromtimestamp(event['happened_at'])
        )
    )