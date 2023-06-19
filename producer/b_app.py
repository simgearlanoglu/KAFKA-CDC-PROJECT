#Belirttiğiniz Kafka konusundan gelen mesajlar, JSON formatında çözümlenerek konsola yazdırılır. 
#Bu şekilde, B uygulamasının Kafka'dan mesajları tüketip konsola yazdırması sağlanmış olur.

import json
from kafka import KafkaConsumer

kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'kafka_topic'

consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_bootstrap_servers,
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
def consume_messages():
    for message in consumer:
        print(message.value)

if __name__ == '__main__':
    consume_messages()
