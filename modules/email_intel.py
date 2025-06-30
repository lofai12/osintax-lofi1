from rich import print
import hashlib
import socket
import dns.resolver
import requests
import re
import whois

from urllib.parse import quote

def run(email):
    print(f"\n[bold cyan]Email OSINT Profiling untuk: {email}[/bold cyan]\n")

    # 1. Validasi Format Email
    if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email):
        print("[red][x] Format email tidak valid[/red]")
        return
    else:
        print("[green][✓] Format email valid[/green]")

    # 2. Gravatar
    email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"
    try:
        res = requests.get(gravatar_url, timeout=5)
        if res.status_code == 200:
            print(f"[+] Gravatar Ditemukan: [underline]{gravatar_url}[/underline]")
        else:
            print("[-] Gravatar: Tidak ditemukan")
    except:
        print("[x] Error mengakses Gravatar")

    # 3. MX Record
    domain = email.split('@')[-1]
    mx_hosts = []
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        mx_hosts = [r.exchange.to_text() for r in answers]
        print(f"[+] MX Record: {', '.join(mx_hosts)}")
    except:
        print("[-] Tidak ada MX Record (mungkin domain mati)")

    # 4. A Record & Reverse DNS
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] A Record (IP): {ip}")
        try:
            reverse = socket.gethostbyaddr(ip)[0]
            print(f"[+] Reverse DNS: {reverse}")
        except:
            print("[-] Reverse DNS: Tidak ditemukan")
    except:
        print("[-] Gagal mendapatkan A Record")

    # 5. Cek apakah domain aktif
    try:
        r = requests.get(f"https://{domain}", timeout=5)
        if r.status_code < 400:
            print(f"[+] Website Aktif: https://{domain} [status: {r.status_code}]")
        else:
            print(f"[-] Website tidak responsif: Status {r.status_code}")
    except:
        print("[x] Gagal menghubungi website domain")

    # 6. WHOIS info
    try:
        w = whois.whois(domain)
        print("[bold yellow]\n📜 WHOIS Info:[/bold yellow]")
        print(f"- Domain: {w.domain_name}")
        print(f"- Registrar: {w.registrar}")
        print(f"- Org: {w.org}")
        print(f"- Country: {w.country}")
    except:
        print("[-] Gagal mengambil data WHOIS")

    # 7. Link Tambahan untuk Investigasi
    print("\n[bold magenta]🔍 Link OSINT Tambahan:[/bold magenta]")
    print(f"[blue]- HaveIBeenPwned:[/blue] https://haveibeenpwned.com/unifiedsearch/{quote(email)}")
    print(f"[blue]- GitHub Search:[/blue] https://github.com/search?q={quote(email)}")
    print(f"[blue]- Facebook Search:[/blue] https://www.facebook.com/search/top?q={quote(email)}")
    print(f"[blue]- Twitter/X Search:[/blue] https://x.com/search?q={quote(email)}")
    print(f"[blue]- LinkedIn Dork:[/blue] https://www.google.com/search?q=site:linkedin.com+{quote(domain)}")
    print(f"[blue]- TXT/SPF Record:[/blue] https://mxtoolbox.com/SuperTool.aspx?action=txt%3a{quote(domain)}")

    # 8. Google Dork
    dork = f"site:pastebin.com | site:github.com | site:stackoverflow.com \"{email}\""
    print(f"\n[bold green]Dork Google:[/bold green]\n[white]{dork}[/white]")

    print("\n[dim]Selesai profiling email & domain. Lanjutkan investigasi manual jika perlu.[/dim]\n")
