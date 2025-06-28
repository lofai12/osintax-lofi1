from rich import print
from rich.prompt import Prompt
import os
import time
from modules import username_check, email_breach, domain_profiler, gpt_summary, email_intel, google_dork, ai_chat

hasil_domain = {}
hasil_email = {}

def main():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("""

[bold cyan]
 ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓████████▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░   
 
                                    by lofi
[/bold cyan]
        
        """)
        print("[bold magenta]Menu OSINTax[/bold magenta]")
        print("""
[bold blue]
[1] Cek Username Sosmed
[2] Cek Email Leak
[3] Cek Domain WHOIS/DNS
[4] Google Dork Generator
[5] Ringkas Info (Groq LLaMA)
[6] Email Profiling (OSINT)
[7] Interaksi Bebas dengan AI
[99] Keluar
[/bold blue]
""")

        pilihan = Prompt.ask("[bold yellow]Pilih opsi >> [/bold yellow]")

        if pilihan == "1":
            username = Prompt.ask("[bold green]Masukkan username[/bold green]")
            username_check.run(username)
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "2":
            email = Prompt.ask("[bold green]Masukkan email[/bold green]")
            hasil_email.clear()
            hasil_email.update({"email": email})
            email_breach.run(email)
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "3":
            domain = Prompt.ask("[bold green]Masukkan domain (contoh: contoh.com)[/bold green]")
            hasil_domain.clear()
            hasil_domain.update({"domain": domain})
            domain_profiler.run(domain)
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "4":
            google_dork.run()
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "5":
            if not hasil_domain and not hasil_email:
                print("[red]Silakan jalankan opsi 2 atau 3 terlebih dahulu untuk ringkasan info.[/red]")
            else:
                gpt_summary.run(domain_info=hasil_domain, email_info=hasil_email)
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "6":
            email = Prompt.ask("[bold green]Masukkan email untuk profiling[/bold green]")
            email_intel.run(email)
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "7":
            ai_chat.run()
            input("\n[dim]Tekan Enter untuk lanjut...[/dim]")

        elif pilihan == "99":
            print("\n[bold green]Terima kasih telah menggunakan OSINTax by lofi![/bold green]")
            break

        else:
            print("[red]Pilihan tidak valid.[/red]")
            time.sleep(1)

if __name__ == "__main__":
    main()
