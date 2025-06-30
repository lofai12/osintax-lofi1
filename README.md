# 🛡️ OSINTax - Ethical OSINT & Recon Tool by Lofi

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![OSINT](https://img.shields.io/badge/OSINT-Toolkit-orange)
![Platform](https://img.shields.io/badge/Linux-Kali%20Linux-red?logo=linux)
![Status](https://img.shields.io/badge/Development-Active-success)
![License](https://img.shields.io/github/license/lofai12/osintax-lofi1)

> **OSINTax** adalah toolkit OSINT berbasis terminal yang simpel, modular, dan etis.  
> Cocok buat pentester, bug hunter, dan investigator digital yang ingin melakukan recon dengan cara cepat dan terstruktur.

---

## 🚀 Fitur

- 🔍 Cek username di berbagai platform
- 📧 Cek email bocor / leak (pwned checker)
- 🌐 Domain Lookup (Whois + DNS)
- 🤖 AI Chat OSINT (Groq / LLaMA3)
- 🛠️ Modul Recon Terminal (port scan, whois, dll)

---

## ⚙️ Instalasi (Linux)

```bash
git clone https://github.com/lofai12/osintax-lofi1.git
cd osintax-lofi1

# (Opsional) Buat virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependensi
pip install -r requirements.txt

# Setup API Key dan variabel environment
cp .env.example .env
nano .env  # Isi key dari Groq / OpenRouter
```

---

## ▶️ Cara Menjalankan

```bash
python3 main.py
```

Kamu akan melihat tampilan seperti:

```
🤖 OSINTax CLI by Lofi
1. AI Chat Assistant
2. Username Check
3. Email Leak Check
4. Domain Recon
0. Exit
```

---

## 📁 Struktur Proyek

```
osintax-lofi1/
├── main.py
├── modules/
│   ├── ai_chat.py
│   ├── username_check.py
│   ├── email_leak.py
│   └── domain_lookup.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚠️ Catatan Penting

- ✅ Gunakan OSINTax hanya untuk hal-hal **etis dan legal**
- 🧱 Modul mudah dikembangkan — lu bisa nambahin:
  - subdomain_enum.py
  - ip_lookup.py
  - google_dork_gen.py
- 🧪 Tes utama di Kali Linux, tapi bisa di semua OS Linux lain

---

## 🧠 Dibuat oleh [Lofi](https://github.com/lofai12)

_"Hacking is not about breaking. It's about understanding."_ — Unknown

---

## ☕ Dukung & Kontribusi

Kalau lu suka project ini, kasih ⭐ dong  
Mau bantu? Fork → upgrade → Pull Request, kita bangun bareng OSINTax jadi tool OSINT terbaik di GitHub 💪
