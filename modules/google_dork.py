from rich import print
from rich.prompt import Prompt
import os

def generate_dorks(domain: str, kategori: int):
    dorks = []

    if kategori == 1:
        dorks = [
            f"site:{domain} inurl:admin",
            f"site:{domain} inurl:login",
            f"site:{domain} intitle:Login",
        ]
    elif kategori == 2:
        dorks = [
            f"site:{domain} intitle:index.of",
            f"site:{domain} ext:pdf | ext:docx | ext:xlsx",
            f"site:{domain} ext:sql | ext:log | ext:bak",
        ]
    elif kategori == 3:
        dorks = [
            f"site:{domain} inurl:config",
            f"site:{domain} inurl:backup",
            f"site:{domain} inurl:private",
        ]
    elif kategori == 4:
        dorks = [
            f"site:{domain} ext:php | ext:asp | ext:aspx",
            f"site:{domain} \"powered by\"",
            f"site:{domain} inurl:wp-content",
        ]
    elif kategori == 5:
        dorks = [
            f"site:{domain} @gmail.com",
            f"site:{domain} @yahoo.com",
            f"site:{domain} @hotmail.com",
        ]
    elif kategori == 6:
        dorks = [
            f"site:{domain} intext:\"sql syntax near\"",
            f"site:{domain} intext:\"Warning: mysql_connect()\"",
            f"site:{domain} intext:\"You have an error in your SQL syntax\"",
        ]
    else:
        print("[red]Kategori tidak valid.[/red]")
        return

    print("\n[bold green]Hasil Google Dork:[/bold green]")
    for dork in dorks:
        print(f"[+] {dork}")

    save = Prompt.ask("[yellow]Simpan ke file dork.txt?[/yellow] (y/n)", default="n")
    if save.lower() == "y":
        with open("dork.txt", "w") as f:
            f.write("\n".join(dorks))
        print("[cyan]Disimpan ke dork.txt[/cyan]")

def run():
    while True:
        print("""
[bold yellow]Pilih Kategori Dork:[/bold yellow]
[1] Login/Admin Page
[2] File Exposure
[3] Sensitive Directories
[4] Tech/Platform Info
[5] Email Leaks
[6] SQL Error Dork
[99] Kembali
        """)

        pilihan = Prompt.ask("[bold yellow]>> Pilihan[/bold yellow]", default="99")
        if pilihan == "99":
            break
        try:
            kategori = int(pilihan)
            domain = Prompt.ask("Masukkan domain target (contoh: example.com)")
            generate_dorks(domain.strip(), kategori)
        except ValueError:
            print("[red]Input tidak valid.[/red]")
