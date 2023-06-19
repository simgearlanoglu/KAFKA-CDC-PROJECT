#Aşağıdaki kod, MongoDB'ye bağlanır ve belirtilen veritabanı ve koleksiyonu izler.
#İzleme işlemi sırasında herhangi bir belge eklendiğinde, bu belgeyi Kafka'ya gönderir. 
#os.environ fonksiyonu, çevre değişkenlerine erişmek için kullanılır 
#ve bu sayede MongoDB ve Kafka bağlantı bilgilerinizi dışarıdan alabilirsiniz.
import time
import json
from pymongo import MongoClient
from kafka import KafkaProducer

mongo_host = 'mongodb://localhost:27017'
mongo_db = 'openSource'
mongo_collection = 'kafkaproject'

kafka_bootstrap_servers = 'localhost:9092'
kafka_topic = 'kafka_topic'

producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

client = MongoClient(mongo_host)
db = client[mongo_db]
collection = db[mongo_collection]

def process_new_documents():
    
    last_document_id = None 

    while True:
      
        query = {}  
        if last_document_id:
            query['_id'] = {'$gt': last_document_id}

        new_documents = collection.find(query)

        for doc in new_documents:
            
            message = {'document': doc}
            producer.send(kafka_topic, value=message)
            last_document_id = doc['_id']

        time.sleep(10)

if __name__ == '__main__':
    process_new_documents()
