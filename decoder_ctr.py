# Qilin Ransomware Decryption Tool
# Yazar: [Sizin GitHub Kullanıcı Adınız]
# Tarih: 2023-10-27
# Açıklama: Belirli bir Qilin fidye yazılımı varyantını çözmek için yazılmış bir dekoder.
# Not: Bu araç, orijinal verilerin 'is_zeroing' nedeniyle yok edildiği durumlarda
# şifreli veriyi çözer ancak anlamlı veri kurtaramaz.

import os
import base64
from Crypto.Cipher import AES

# --- YAPILANDIRMA ---
# Fidye yazılımının kullandığı parola/anahtar (URL-Safe Base64 formatında)
PASSWORD_STRING = "xsJzS3dWwSRGApZfuJfGJYUjMOgR3u_6"

# Şifreli dosyaların bulunduğu klasör
INPUT_DIR = "sifreli_dosyalar"

# Çözülmüş dosyaların kaydedileceği klasör
OUTPUT_DIR = "cozulmus_dosyalar"

# Fidye yazılımının dosyaların sonuna eklediği uzantı
RANSOMWARE_EXTENSION = ".sIQn_PPwXy"
# --------------------

def main():
    """
    Ana fonksiyon: Şifreleme anahtarını hazırlar ve dosyaları işler.
    """
    try:
        # Anahtar URL-Safe Base64 formatında olduğu için urlsafe_b64decode kullanıyoruz.
        key = base64.urlsafe_b64decode(PASSWORD_STRING)
        print(f"[+] Anahtar başarıyla çözüldü. Uzunluk: {len(key)} byte")
    except Exception as e:
        print(f"[!] Hata: Anahtar çözülemedi. Hata: {e}")
        return

    # Çıktı klasörünü oluştur
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[+] '{OUTPUT_DIR}' klasörü oluşturuldu.")

    # Girdi klasöründeki dosyaları işle
    for filename in os.listdir(INPUT_DIR):
        input_path = os.path.join(INPUT_DIR, filename)
        if not os.path.isfile(input_path):
            continue

        # Orijinal dosya adını fidye uzantısını çıkararak elde et
        original_filename = filename
        if RANSOMWARE_EXTENSION and filename.endswith(RANSOMWARE_EXTENSION):
            original_filename = filename[:-len(RANSOMWARE_EXTENSION)]
        
        output_path = os.path.join(OUTPUT_DIR, original_filename)

        print(f"\n--- Dosya işleniyor: {filename} ---")
        try:
            decrypt_file_ctr(input_path, output_path, key)
            print(f"[+] '{filename}' başarıyla çözüldü ve '{output_path}' yoluna kaydedildi.")
        except Exception as e:
            print(f"[!] '{filename}' dosyası çözülemedi. Hata: {e}")

def decrypt_file_ctr(input_path, output_path, key):
    """
    Tek bir dosyayı AES-CTR modunda çözer.
    """
    with open(input_path, 'rb') as f_in:
        encrypted_data = f_in.read()

    # EN KRİTİK KISIM: Nonce'u ve şifreli veriyi ayır
    # Qilin varyantı için nonce, dosyanın ilk 8 byte'ıdır.
    nonce_size = 8 
    nonce = encrypted_data[:nonce_size]
    ciphertext = encrypted_data[nonce_size:]

    print(f"    [i] Nonce (ilk {nonce_size} byte): {nonce.hex()}")
    print(f"    [i] Şifreli veri boyutu: {len(ciphertext)} byte")

    # AES-CTR deşifreleyiciyi oluştur
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

    # Veriyi deşifre et
    decrypted_data = cipher.decrypt(ciphertext)

    # Çözülmüş veriyi yeni dosyaya yaz
    with open(output_path, 'wb') as f_out:
        f_out.write(decrypted_data)

if __name__ == "__main__":
    main()
