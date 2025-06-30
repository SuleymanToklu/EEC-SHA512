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

<!-- Buraya ana sayfa ekran görüntüsünü ekleyin -->
`Ekran görüntüsü: Ana sayfa ve özellikler bölümü`

### SHA512 Hash Fonksiyonu

<!-- Buraya SHA512 hash ekran görüntüsünü ekleyin -->
`Ekran görüntüsü: SHA512 hash işlemi ve sonucu`

### Dosya Hash Fonksiyonu

<!-- Buraya dosya hash ekran görüntüsünü ekleyin -->
`Ekran görüntüsü: Dosya hash işlemi ve sonucu`

### ECC Şifreleme

<!-- Buraya ECC şifreleme ekran görüntüsünü ekleyin -->
`Ekran görüntüsü: ECC ile metin şifreleme`

### ECC Şifre Çözme

<!-- Buraya ECC şifre çözme ekran görüntüsünü ekleyin -->
`Ekran görüntüsü: ECC ile şifre çözme`

### Kriptografi Bilgi Merkezi

<!-- Buraya bilgi merkezi ekran görüntüsünü ekleyin -->
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