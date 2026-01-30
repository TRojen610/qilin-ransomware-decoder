
# Qilin Fidye Yazılımı Deşifre Aracı

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/Lisans-MIT-green)

Bu depo, **Qilin** fidye yazılımının belirli bir varyantı için geliştirilmiş bir deşifre aracı içerir.

> **⚠️ Önemli Uyarı:** Bu araç, belirli bir fidye yazılımı örneğinin ve yapılandırmasının tersine mühendisliği sonucunda geliştirilmiştir. Diğer Qilin varyantlarında çalışmayabilir. Ayrıca, bu fidye yazılımının `is_zeroing: true` özelliği nedeniyle orijinal veriler kalıcı olarak yok edilmiştir. Bu araç, *şifreli metni* başarıyla çözer ancak kurtarılan veri anlamsız/bozuk olacaktır. Yalnızca eğitim ve araştırma amaçlı kullanın.

## Nasıl Çalışır?

Bu araç, fidye yazılımından elde edilen detaylı bir log dosyası baz alınarak tersine mühendislik yapılmıştır. Şifreleme parametreleri şunlardır:

*   **Fidye Yazılımı:** Qilin
*   **Şifreleme Algoritması:** AES-192-CTR
*   **Anahtar:** `xsJzS3dWwSRGApZfuJfGJYUjMOgR3u_6` (URL-Safe Base64 kodlu)
*   **Nonce:** Her şifreli dosyanın ilk 8 byte'ı.
*   **Fidye Uzantısı:** `.sIQn_PPwXy`

Araç, anahtarı ve nonce'u şifreli dosyadan okur, AES-CTR şifreleyiciyi yeniden oluşturur ve veriyi çözer.

## Gereksinimler

*   Python 3.x
*   pycryptodome kütüphanesi

Gerekli kütüphaneyi pip ile kurabilirsiniz:


pip install pycryptodome

--------------------------------------------------------------------------------------------------
Kullanım
Deşifre aracını kullanmak için şu adımları izleyin:

Depoyu klonlayın:
```bash
git clone https://github.com/TRojen610/qilin-decryptor.git
cd qilin-decryptor
Şifreli dosyalar için bir klasör oluşturun:

-------------------------------------------------------------------------------------------
mkdir sifreli_dosyalar
Şifreli dosyaları yerleştirin: Şifreli dosyaların (örn: dokuman.pdf.sIQn_PPwXy) kopyalarını sifreli_dosyalar klasörünün içine atın.
Uyarı: Her zaman şifreli dosyaların kopyalarıyla çalışın. Asıl dosyaları kullanmayın.
Betiği çalıştırın:
--------------------------------------------------------------------------------------------

python decoder_ctr.py
Çıktıyı kontrol edin: Çözülen dosyalar, fidye uzantısı kaldırılmış olarak (örn: dokuman.pdf) cozulmus_dosyalar klasörüne kaydedilecektir.
Sorumluluk Reddi
Bu araç sadece eğitim ve araştırma amaçlı sağlanmıştır. Yazardan, bu yazılımın kötüye kullanımından veya neden olduğu hasardan sorumlu tutulamaz. Analiz edilen fidye yazılımı (is_zeroing: true), orijinal verileri yok ettiği için başarılı bir deşifre bile orijinal dosya içeriğini geri getiremeyecektir.

Lisans
Bu proje MIT Lisansı altında lisanslanmıştır - ayrıntılar için LICENSE dosyasına bakın.
