from confluent_kafka import Producer

# Kafka yapılandırması
kafka_bootstrap_servers = 'kafka:9092'
kafka_topic = 'kafka_topic'

# Üretici yapılandırması
producer_config = {
    'bootstrap.servers': kafka_bootstrap_servers
}

# Üretici oluşturma
producer = Producer(producer_config)

# Mesajı gönderme işlemi
message = "h"
producer.produce(kafka_topic, value=message.encode('utf-8'))
producer.flush()

# Üreticiyi kapatma
producer.close()
