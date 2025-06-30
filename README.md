# Kriptografi ve SHA512 Uygulaması

Bu proje, eliptik eğri kriptografisi (ECC) ve SHA512 özet fonksiyonu ile şifreleme, şifre çözme ve hash işlemleri yapabilen modern bir web uygulamasıdır.

## İçindekiler

- [Özellikler](#özellikler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Ekran Görüntüleri](#ekran-görüntüleri)
- [Teknolojiler](#teknolojiler)
- [Katkı Sağlama](#katkı-sağlama)
- [Lisans](#lisans)

## Özellikler

- SHA512 ile metin ve dosya hash'leme
- Eliptik eğri kriptografisi ile metin şifreleme ve çözme
- Modern, kullanıcı dostu ve responsive arayüz
- Dosya yükleme desteği
- Sonuçları panoya kopyalama
- JSON formatında çıktı desteği

## Kurulum

1. Gerekli Python paketlerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
2. Uygulamayı başlatın:
    ```bash
    streamlit run app.py
    ```

## Kullanım

1. Uygulama açıldığında sol menüden yapmak istediğiniz işlemi seçin:
    - SHA512 Özet Fonksiyonu
    - Eliptik Eğri Şifreleme
    - Kriptografi Bilgileri

2. SHA512 Özet Fonksiyonu:
    - Metin veya dosya seçin
    - Hash oluşturun ve sonucu görüntüleyin

3. Eliptik Eğri Şifreleme:
    - Şifreleme veya şifre çözme işlemini seçin
    - Gerekli alanları doldurun ve işlemi başlatın

4. Sonuçları panoya kopyalayabilir veya JSON olarak görebilirsiniz.

## Ekran Görüntüleri

Aşağıda uygulamanın bazı ekran görüntülerini bulabilirsiniz:

### Ana Sayfa ve Özellikler

![resim](https://github.com/user-attachments/assets/fbd5f8e3-9a89-4c27-be1c-55d2ced43610)

`Ekran görüntüsü: Ana sayfa ve özellikler bölümü`

### SHA512 Hash Fonksiyonu

![resim](https://github.com/user-attachments/assets/8d0e700a-cf68-4cd9-b5f9-1945bb90fad2)

`Ekran görüntüsü: SHA512 hash işlemi ve sonucu`

### Dosya Hash Fonksiyonu

![resim](https://github.com/user-attachments/assets/82bd8257-f5cd-4f00-9b1b-3b64feba1ae6)

![resim](https://github.com/user-attachments/assets/d8ad6a4f-12a1-43d4-8d2f-fa255601d42a)

`Ekran görüntüsü: Dosya hash işlemi ve sonucu`

### ECC Şifreleme

![resim](https://github.com/user-attachments/assets/c700448a-c13b-4475-8817-0f9729e0cdbf)

![resim](https://github.com/user-attachments/assets/174e8320-0d25-4706-8f45-a61fe22c3c28)
![resim](https://github.com/user-attachments/assets/c32fd9b7-a64b-4da3-b8eb-780dbe9b2623)

`Ekran görüntüsü: ECC ile metin şifreleme`

### ECC Şifre Çözme

![resim](https://github.com/user-attachments/assets/38cabb7f-1283-4997-9ca6-b58b6877f18e)
![resim](https://github.com/user-attachments/assets/1ee10afe-183f-4eb9-8c1b-70202aa425d5)

`Ekran görüntüsü: ECC ile şifre çözme`

### Kriptografi Bilgi Merkezi

![resim](https://github.com/user-attachments/assets/f0119f84-b298-47b5-b7c1-3c7e27f7a56a)

![resim](https://github.com/user-attachments/assets/ac253a08-b898-4754-881e-44b45bf5f04e)
![resim](https://github.com/user-attachments/assets/08782ee4-7395-48e7-ab19-fbbece635097)

![resim](https://github.com/user-attachments/assets/d7d3a737-9a83-41b9-a307-24ed44842481)




`Ekran görüntüsü: Kriptografi bilgi merkezi sekmeleri`

## Teknolojiler

- Python 3
- Streamlit
- tinyec
- cryptography

## Katkı Sağlama

Katkı sağlamak isterseniz, lütfen bir fork oluşturun ve pull request gönderin.

## Geliştirici

Süleyman Toklu

## Lisans

Bu proje MIT lisansı ile lisanslanmıştır.
