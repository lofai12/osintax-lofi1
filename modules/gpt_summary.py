import os
from rich import print
from dotenv import load_dotenv
import requests

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    print("[red]GROQ_API_KEY tidak ditemukan. Set di .env file terlebih dahulu.[/red]")


def build_summary_block(domain_info, email_info):
    summary_input = f"""
Berikut ini adalah hasil OSINT terhadap target:

📌 Domain Info:
- A Record: {domain_info.get('a_record', '-')}
- MX Record: {domain_info.get('mx_record', '-')}
- NS Record: {domain_info.get('ns_record', '-')}
- TXT Record: {domain_info.get('txt_record', '-')}
- WHOIS Org: {domain_info.get('org', '-')}
- WHOIS Registrar: {domain_info.get('registrar', '-')}
- Negara: {domain_info.get('country', '-')}

📩 Email Info:
- Validitas: {email_info.get('valid', '-')}
- Disposable: {email_info.get('disposable', '-')}
- Temp Mail: {email_info.get('temp', '-')}
- Provider: {email_info.get('provider', '-')}

Tolong ringkas informasi ini dan simpulkan dengan gaya singkat, tajam, dan mudah dipahami.
"""
    return summary_input


def run(prompt=None, domain_info=None, email_info=None):
    print("\n[bold cyan]Ringkasan via GPT (Groq LLaMA4):[/bold cyan]")
    try:
        if not prompt:
            if not domain_info and not email_info:
                print("[red]Tidak ada data domain/email untuk diringkas. Jalankan opsi 2 atau 3 terlebih dahulu.[/red]")
                return
            prompt = build_summary_block(domain_info or {}, email_info or {})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        data = {
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            print(f"\n[green]{reply}[/green]\n")
        else:
            print(f"[red]Gagal meminta ke Groq: {response.status_code} - {response.text}[/red]")
    except Exception as e:
        print(f"[red]Error: {e}[/red]")

# Dari main.py contoh integrasi:
# import modules.gpt_summary as gpt_summary
# gpt_summary.run(domain_info=hasil_domain, email_info=hasil_email)
