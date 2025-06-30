from rich import print
import requests

def run(email):
    print(f"\n[bold cyan]Cek Kebocoran Data untuk: {email}[/bold cyan]\n")

    url = f"https://breached.me/api/v1/breachedaccount/{email}"
    headers = {"User-Agent": "osintax-tool"}

    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200:
            breaches = r.json()
            print(f"[bold green][+][/bold green] Ditemukan {len(breaches)} kebocoran:")
            for site in breaches:
                print(f"  [white]- {site}[/white]")
        elif r.status_code == 404:
            print("[green][✓] Tidak ditemukan kebocoran.[/green]")
        else:
            print(f"[yellow][!] Status tidak dikenali: {r.status_code}[/yellow]")
    except requests.exceptions.RequestException:
        print("[red][x] Gagal menghubungi API breached.me[/red]")

    print("\n[dim]Selesai cek email.[/dim]\n")

