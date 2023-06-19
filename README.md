# Proje Hakkında
Bu proje, Apache kafka ile yapılmış basit bir CDC uygulamasıdır. A ve B uygulamalarını Docker kullanarak birlikte çalıştırmanızı sağlar. A uygulaması MongoDB veritabanındaki bir collection'ı sorgular ve yeni dökümanları Apache Kafka'ya yayınlar. B uygulaması ise Apache Kafka'dan gelen mesajları konsola yazdırır.

## Ön Koşullar

- Docker kurulu olmalıdır: [Docker](https://www.docker.com/get-started)
- Docker Compose kurulu olmalıdır: [Docker Compose](https://docs.docker.com/compose/install/)
- Apache Kafka kurulu olmalıdır: [Apache Kafka](https://kafka.apache.org/)
- MongoDB kurulu olmalıdır: [MongoDB](https://www.mongodb.com/)

## Kurulum

1-İlk olarak projeyi klonlayın.
2-Projenizin bulunduğu dizine gidin cd kafka-CDC
3-Son olarak projeyi çalıştırın. docker compose up
4-Uygulamayı Sonlandırmak için: docker compose down

## Sorun Giderme

- Uygulamaların çıktısını görüntülemek için `docker-compose logs` komutunu kullanabilirsiniz.
- Herhangi bir hata durumunda, uygulamaların loglarını (`app/logs/` dizininde) kontrol edin.

## Katkılar

Herhangi bir hata veya iyileştirme için pull talepleri açmaktan çekinmeyin.

