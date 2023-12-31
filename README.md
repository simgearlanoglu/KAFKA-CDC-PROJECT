# Proje Hakkında
Bu proje, Apache kafka ile yapılmış basit bir CDC uygulamasıdır. A ve B uygulamalarını Docker kullanarak birlikte çalıştırmanızı sağlar. A uygulaması MongoDB veritabanındaki bir collection'ı sorgular ve yeni dökümanları Apache Kafka'ya yayınlar. B uygulaması ise Apache Kafka'dan gelen mesajları konsola yazdırır.

# Projenin Amacı

A Uygulaması: MongoDB veritabanındaki belirli bir koleksiyonu her 10 saniyede bir sorgular.
Her sorgulama işlemi, bir önceki çalışmadan sonra eklenmiş yeni belgeleri tespit etmek için kullanılır.
Yeni belgeleri JSON formatında Kafka'ya yayınlamak için Apache Kafka'ya bağlanır ve mesajları yayınlar.
Bu işlem sürekli olarak devam eder ve MongoDB'deki koleksiyonda yeni belgeler olduğunda Kafka'ya yeni mesajlar gönderir.

B Uygulaması: Apache Kafka'dan mesajları tüketmek için 3 kopya çalışır.
Her kopya, Kafka'dan gelen mesajları alır ve bu mesajları System Out (konsol) üzerinde yazdırır.
Bu sayede, A uygulaması tarafından yayınlanan mesajları B uygulaması tüketir ve konsola yazdırır.

Docker İmajları: A ve B uygulamaları uygun Docker imajlarına dönüştürülür.
Docker imajları, her uygulama için ayrı Dockerfile'lar kullanılarak oluşturulur.
Dockerfile'lar, uygulama bağımlılıklarını ve çalıştırılması gereken komutları içerir.
Her uygulama, kendi Docker imajı olarak paketlenir ve Docker imaj deposunda tutulur.

Docker Compose: Üretilen A ve B uygulamaları, belirlenen Kafka Docker imajıyla birlikte Docker Compose kullanılarak yapılandırılır.
Docker Compose dosyası, A ve B uygulamalarını ve Kafka'yı aynı ortamda çalıştırmak için kullanılır.
Docker Compose, konteynerlerin ağ bağlantılarını yapılandırır ve uygulamaların birlikte çalışmasını sağlar.

Bu sayede, projeyi başlatmak için tek bir komutla tüm sistem çalıştırılabilir.
Projenin bu şekilde çalışması, A uygulamasının MongoDB'den yeni verileri alıp Kafka'ya yayınlamasını ve B uygulamasının Kafka'dan mesajları tüketip konsola yazdırmasını sağlar. Docker ve Docker Compose kullanarak bu uygulamaları birlikte çalıştırabilir ve kolayca dağıtabilirsiniz. 

## Ön Koşullar

- Docker kurulu olmalıdır: [Docker](https://www.docker.com/get-started)
- Docker Compose kurulu olmalıdır: [Docker Compose](https://docs.docker.com/compose/install/)
- Apache Kafka kurulu olmalıdır: [Apache Kafka](https://kafka.apache.org/)
- MongoDB kurulu olmalıdır: [MongoDB](https://www.mongodb.com/)

## Kurulum

- İlk olarak projeyi klonlayın:
```sh
git clone https://github.com/simgearlanoglu/KAFKA-CDC-PROJECT.git
```

2-Daha sonra projenin bulunduğu dizine girin.
```sh
cd KAFKA-CDC-PROJECT
```

3-Son olarak projeyi çalıştırın.
```sh
docker compose up
```
- Uygulamayı Sonlandırmak için aşağıdaki kodu kullanabilirsiniz.
```sh
docker compose up
```

## Sorun Giderme

- Uygulamaların çıktısını görüntülemek için `docker-compose logs` komutunu kullanabilirsiniz.
- Herhangi bir hata durumunda, uygulamaların loglarını (`app/logs/` dizininde) kontrol edin.

## Katkılar

Herhangi bir hata veya iyileştirme için pull talepleri açmaktan çekinmeyin.

