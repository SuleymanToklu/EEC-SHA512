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

Bu bölüm, EEC-SHA512 projesinin Streamlit tabanlı web uygulamasının temel özelliklerini gösteren ekran görüntülerini açıklamaktadır. Uygulama, SHA-512 özet fonksiyonu ve eliptik eğri kriptografisi (ECC) ile güvenli hash oluşturma, şifreleme ve şifre çözme işlemlerini destekler. Görseller, uygulamanın kullanıcı dostu arayüzünü, modern tasarımını (glass-card, result-card CSS stilleri) ve işlevselliğini (Python, hashlib, tinyec, Fernet, brainpoolP256r1 eğrisi) sergiler. Aşağıda her görsel, projenin yeteneklerini ve kullanımını net bir şekilde tanıtacak şekilde açıklanmıştır.
Aşağıda uygulamanın bazı ekran görüntülerini bulabilirsiniz:

### Ana Sayfa ve Özellikler

![resim](https://github.com/user-attachments/assets/fbd5f8e3-9a89-4c27-be1c-55d2ced43610)

Ana sayfa, EEC-SHA512 uygulamasının giriş ekranını tanıtır. hero-section CSS stiliyle tasarlanmış başlık, "Kriptografi Merkezi"ni ve "Güvenli şifreleme ve hash fonksiyonları ile verilerinizi koruyun" alt başlığını öne çıkarır. Geliştirici Süleyman Toklu’nun adı zarif bir şekilde belirtilmiştir. feature-grid ile düzenlenmiş üç kart, uygulamanın temel özelliklerini vurgular: SHA-512 ile veri bütünlüğü için hash oluşturma, ECC ile güçlü şifreleme ve metin/dosya desteği. Sol kenar çubuğu, kullanıcıların "SHA512 Özet Fonksiyonu", "Eliptik Eğri Şifreleme" ve "Kriptografi Bilgileri" sekmelerine hızlı erişimini sağlar. Modern ve responsive tasarım, uygulamanın hem teknik hem de genel kullanıcılar için erişilebilir olduğunu gösterir.

### SHA512 Hash Fonksiyonu

![resim](https://github.com/user-attachments/assets/8d0e700a-cf68-4cd9-b5f9-1945bb90fad2)

Bu görsel, SHA512 Özet Fonksiyonu sekmesini gösterir. Kullanıcılar, st.text_area ile metin girerek SHA-512 hash değerini hesaplar (hashlib.sha512 ile). Görselde, örnek bir metin (ör. "Merhaba Dünya!") girilmiş ve "Hash Oluştur" butonu (st.button, gradient stil) ile 128 haneli onaltılık hash sonucu üretilmiştir. Sonuç, result-card içinde gösterilir ve copy-btn ile panoya kopyalanabilir. Metrik kartları (st.metric), metin uzunluğunu, hash uzunluğunu (128 hex karakter) ve işlem süresini (ms cinsinden) sunar. Sağ üstteki info-box, SHA-512’nin 512-bit güvenli hash ürettiğini belirtir. Bu sekme, veri bütünlüğü kontrolü için hızlı ve kullanıcı dostu bir çözüm sunar.

### Dosya Hash Fonksiyonu

![resim](https://github.com/user-attachments/assets/82bd8257-f5cd-4f00-9b1b-3b64feba1ae6)

Dosya hash’leme sekmesi, kullanıcıların st.file_uploader ile TXT, PDF, DOC, DOCX, JPG, PNG veya ZIP dosyalarını yükleyerek SHA-512 hash değerini hesaplamasını sağlar. Bu görsel, dosya seçme arayüzünü gösterir; dosya adı, boyutu ve türü metrik kartlarında (st.metric) listelenir. glass-card stili, arayüzü modern ve düzenli tutar. Kullanıcılar, "Dosya Hash'le" butonu ile işlemi başlatır. Bu özellik, büyük dosyaların hızlı ve güvenli hash’lenmesini destekler, dosya bütünlüğü doğrulama gibi senaryolar için idealdir.

![resim](https://github.com/user-attachments/assets/d8ad6a4f-12a1-43d4-8d2f-fa255601d42a)

Bu görsel, dosya hash’leme işleminin sonucunu sergiler. Yüklenen dosyanın SHA-512 hash değeri (hashlib.sha512), result-card içinde 128 haneli onaltılık bir dize olarak gösterilir. "Kopyala" butonu (copy-btn) ve JSON indirme seçeneği, sonucu kolayca kullanmayı sağlar. Metrik kartları, dosya boyutunu, hash uzunluğunu ve işlem süresini detaylandırır. info-box, işlemin başarılı olduğunu bildirir. Bu görsel, uygulamanın büyük veri setleriyle çalışmadaki verimliliğini ve kullanım kolaylığını vurgular.

### ECC Şifreleme

![resim](https://github.com/user-attachments/assets/c700448a-c13b-4475-8817-0f9729e0cdbf)

ECC Şifreleme sekmesi, brainpoolP256r1 eğrisi (tinyec.registry) kullanılarak metin şifrelemeyi gösterir. Görselde, kullanıcıların metni girdiği st.text_area ve "Şifrele" butonu (st.button) yer alır. İşlem, ecc_encrypt fonksiyonuyla çalışır: özel anahtar (privKey) ve genel anahtar (pubKey) üretilir, paylaşılan nokta (sharedPoint) ile SHA-512 anahtarı oluşturulur ve Fernet ile şifreleme yapılır. glass-card stili, arayüzü şık tutar; info-box, ECC’nin RSA’ya göre üstünlüğünü vurgular. Bu görsel, güvenli şifreleme için kullanıcı dostu bir arayüz sunar.

![resim](https://github.com/user-attachments/assets/174e8320-0d25-4706-8f45-a61fe22c3c28)

Bu görsel, ECC şifreleme işleminin sonuçlarını gösterir. Şifrelenmiş metin (base64 formatında), özel anahtar ve genel anahtar (x,y koordinatları) result-card içinde sunulur. Metrik kartları, orijinal ve şifreli metin uzunluklarını ile işlem süresini belirtir. JSON formatında tüm bilgiler (st.code) görüntülenir, kullanıcıların şifreleme verilerini kaydetmesini sağlar. info-box, özel anahtarın güvenli saklanması gerektiğini hatırlatır. Bu görsel, ECC’nin güçlü şifreleme yeteneklerini ve uygulamanın sonuç sunumundaki netliğini sergiler.

![resim](https://github.com/user-attachments/assets/c32fd9b7-a64b-4da3-b8eb-780dbe9b2623)

Bu görsel, ECC şifreleme sekmesinin başka bir görünümünü sunar, muhtemelen farklı bir metin veya yapılandırma ile. Kullanıcı, st.text_area ile metni girer ve brainpoolP256r1 eğrisiyle şifreleme yapar. Sonuçlar, şifrelenmiş metin, anahtarlar ve JSON çıktısı olarak result-card içinde gösterilir. Görsel, uygulamanın farklı veri girişleriyle tutarlı çalıştığını ve modern tasarımıyla (glass-card, gradient butonlar) kullanıcı deneyimini iyileştirdiğini vurgular.

### ECC Şifre Çözme

![resim](https://github.com/user-attachments/assets/38cabb7f-1283-4997-9ca6-b58b6877f18e)

ECC Şifre Çözme sekmesi, şifrelenmiş metni (base64 formatında), özel anahtarı ve genel anahtarı (x,y formatında) girmek için alanlar sunar (st.text_area, st.text_input). Görselde, kullanıcıların bu alanları doldurduğu ve "Şifre Çöz" butonunu (st.button) kullandığı arayüz gösterilir. ecc_decrypt fonksiyonu, Fernet ile şifreyi çözer. info-box, genel anahtar formatı için ipuçları verir. glass-card stili, arayüzü düzenli tutar. Bu görsel, şifre çözme işleminin kullanıcı dostu yapısını öne çıkarır.

![resim](https://github.com/user-attachments/assets/1ee10afe-183f-4eb9-8c1b-70202aa425d5)

Bu görsel, ECC şifre çözme işleminin sonucunu gösterir. Çözülmüş metin, result-card içinde sunulur ve copy-btn ile kopyalanabilir. Metrik kartları, şifreli ve çözülmüş metin uzunluklarını ile işlem süresini detaylandırır. info-box, işlemin başarılı olduğunu bildirir. Hata durumunda, error-box olası nedenleri (yanlış anahtar, hatalı format) listeler. Görsel, ECC’nin güvenli ve hızlı şifre çözme yeteneğini ve uygulamanın hata yönetimini vurgular.

### Kriptografi Bilgi Merkezi

![resim](https://github.com/user-attachments/assets/f0119f84-b298-47b5-b7c1-3c7e27f7a56a)

Kriptografi Bilgi Merkezi sekmesi, kullanıcıları SHA-512 ve ECC hakkında bilgilendirir. Bu görsel, "SHA512 Hakkında" sekmesini gösterir (st.tabs). SHA-512’nin özellikleri (512-bit hash, tek yönlü fonksiyon, kullanım alanları: şifre saklama, dijital imzalar) açıklanır. Bir demo alanı (st.text_input), örnek metinle (Merhaba Dünya!) SHA-512 hash’ini üretir (st.code). glass-card stili, içeriği düzenli tutar. Bu görsel, uygulamanın eğitim odaklı yönünü ve kullanıcı dostu bilgi sunumunu sergiler.

![resim](https://github.com/user-attachments/assets/ac253a08-b898-4754-881e-44b45bf5f04e)

Bu görsel, "ECC Hakkında" sekmesini sunar. ECC’nin avantajları (küçük anahtar boyutu, hızlı işlem, yüksek güvenlik) ve brainpoolP256r1 eğrisinin parametreleri (curve.field.p, curve.g.x, curve.g.y) açıklanır. Örnek bir anahtar çifti (st.code) ve şifreleme/çözme akışı sunulur. Görsel, teknik detayları sade bir şekilde görselleştirir ve uygulamanın ECC implementasyonunun gücünü (tinyec, Fernet) vurgular.

![resim](https://github.com/user-attachments/assets/08782ee4-7395-48e7-ab19-fbbece635097)

Bu görsel, "Güvenlik İpuçları" sekmesini gösterir. Kullanıcılara güçlü parola oluşturma, 2FA kullanımı, veri yedekleme gibi pratik öneriler sunulur (info-box ile). glass-card stili, içeriği modern ve okunabilir tutar. Görsel, uygulamanın sadece bir araç değil, aynı zamanda güvenlik bilinci oluşturan bir platform olduğunu gösterir.

![resim](https://github.com/user-attachments/assets/d7d3a737-9a83-41b9-a307-24ed44842481)

Bu görsel, Kriptografi Bilgi Merkezi’nin başka bir yönünü, muhtemelen SHA-512 veya ECC’nin pratik uygulamalarını veya karşılaştırmalarını (ör. ECC vs. RSA) sunar. Tablo veya infografik formatında bilgiler, glass-card içinde düzenlenmiştir. Görsel, uygulamanın eğitim değerini ve kriptografik teknolojilerin gerçek dünyadaki kullanımını vurgulayarak kullanıcıları bilgilendirir.

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
