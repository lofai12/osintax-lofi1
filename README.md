# 🛡️ OSINTax - Ethical OSINT & Recon Tool by Lofi

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OSINT](https://img.shields.io/badge/OSINT-Toolkit-orange)
![License](https://img.shields.io/github/license/lofai12/osintax-lofi1)
![Built on Kali](https://img.shields.io/badge/Built%20with-Kali%20Linux-red?logo=linux)

> **OSINTax** adalah toolkit OSINT berbasis CLI untuk investigasi digital secara **etis dan efisien**.  
> Dibuat oleh **Lofi** untuk membantu proses recon, enum, dan eksplorasi target secara profesional.

---

## 🚀 Fitur

- 🔍 Cek username di banyak platform
- 📧 Cek email breach (leak / pwned)
- 🌐 Lookup domain (whois, DNS)
- 🤖 AI Chat (Groq / LLaMA3 support)
- 🛠️ Recon ringan berbasis terminal

---

## ⚙️ Instalasi (Linux)

```bash
git clone https://github.com/lofai12/osintax-lofi1.git
cd osintax-lofi1

# (Opsional) Buat virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install library
pip install -r requirements.txt

# Setup file konfigurasi
cp .env.example .env
nano .env  # isi API key Groq (kalau pakai AI)

# Cara menjalankan
python3 main.py

❗ Catatan
Jangan upload .env ke publik

Selalu gunakan OSINTax secara etis dan legal

Bisa dikembangkan ke mode GUI atau Flask Web App


