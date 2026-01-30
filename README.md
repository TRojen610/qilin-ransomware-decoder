# Qilin Ransomware Decryptor (Research Variant)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Research%20Only-orange)

A **research-focused decryptor** developed for a **specific Qilin ransomware variant**, based on reverse engineering of an observed sample and its runtime logs.

> ⚠️ This tool is **not a universal Qilin decryptor**.

---

## ⚠️ Disclaimer

This project is provided **strictly for educational and malware research purposes**.

- Works **only** for the analyzed Qilin variant  
- **Not compatible** with other Qilin samples  
- The ransomware uses `is_zeroing: true`, meaning **original data is permanently destroyed**
- Decryption succeeds **cryptographically**, but recovered files will be **corrupted / meaningless**

**Do not expect data recovery.**

---

## 🔍 Technical Overview

| Component | Value |
|---------|------|
| Malware Family | Qilin |
| Cipher | AES-192-CTR |
| Key Encoding | URL-safe Base64 |
| Nonce | First 8 bytes of each encrypted file |
| Ransom Extension | `.sIQn_PPwXy` |

**Encryption Key (sample-specific): xsJzS3dWwSRGApZfuJfGJYUjMOgR3u_6 **

The decryptor reconstructs the AES-CTR stream using the extracted nonce and static key derived during analysis.

---

## 📦 Requirements

- Python 3.x  
- `pycryptodome`

```bash
pip install pycryptodome

git clone https://github.com/TRojen610/qilin-ransomware-decoder.git
cd qilin-decryptor

mkdir sifreli_dosyalar
python decoder_ctr.py
Place encrypted files (*.sIQn_PPwXy) into sifreli_dosyalar/
Decrypted output is written to cozulmus_dosyalar/
Output filenames have the ransom extension removed
⚠️ Always work on copies of encrypted files.


🎯 Intended Audience
Malware researchers
Reverse engineers
Blue team / DFIR analysts
Students studying ransomware internals

❗ Legal Notice
The author assumes no responsibility for:
misuse of this software
damages caused directly or indirectly
illegal or unethical usage
This repository does not promote ransomware activity.

📜 License

MIT License
See LICENSE for details.
