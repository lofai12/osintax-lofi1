import socket
import whois
import dns.resolver
import requests
from rich import print
from urllib.parse import quote

def get_dns(domain):
    records = {}
    types = ['A', 'MX', 'NS', 'CNAME', 'TXT']
    for rtype in types:
        try:
            answers = dns.resolver.resolve(domain, rtype, raise_on_no_answer=False)
            records[rtype] = [str(r) for r in answers]
        except:
            records[rtype] = []
    return records

def is_site_up(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        return r.status_code == 200
    except:
        return False

def fallback_rdap(domain):
    try:
        r = requests.get(f"https://rdap.org/domain/{domain}", timeout=5)
        if r.status_code == 200:
            data = r.json()
            return {
                "domain": data.get("ldhName", "None"),
                "registrar": data.get("registrar", {}).get("name", "None"),
                "org": data.get("entities", [{}])[0].get("vcardArray", [])[1][1][3] if data.get("entities") else "None",
                "country": data.get("entities", [{}])[0].get("vcardArray", [])[1][6][3] if data.get("entities") else "None"
            }
    except:
        pass
    return {
        "domain": "None",
        "registrar": "None",
        "org": "None",
        "country": "None"
    }

def run(domain):
    print(f"\n[bold cyan]Domain OSINT Profiling untuk:[/bold cyan] {domain}\n")

    # DNS Records
    dns_data = get_dns(domain)
    for rtype in ['A', 'MX', 'NS', 'CNAME', 'TXT']:
        if dns_data[rtype]:
            print(f"[green]+ {rtype} Record:[/green] {', '.join(dns_data[rtype])}")
        else:
            print(f"[red]- Tidak ada {rtype} Record[/red]")

    # Website check
    up = is_site_up(domain)
    print(f"[green]+ Website bisa diakses[/green]" if up else "[red]- Gagal menghubungi website domain[/red]")

    # WHOIS
    try:
        w = whois.whois(domain)
        whois_info = {
            "domain": w.domain_name if w.domain_name else "None",
            "registrar": w.registrar if w.registrar else "None",
            "org": w.org if w.org else "None",
            "country": w.country if w.country else "None"
        }
        if all(v in [None, "None"] for v in whois_info.values()):
            whois_info = fallback_rdap(domain)
    except:
        whois_info = fallback_rdap(domain)

    print("\n\U0001F4DC [bold]WHOIS Info:[/bold]")
    for k, v in whois_info.items():
        print(f"- {k.capitalize()}: {v if v else 'None'}")

    # Links
    encoded = quote(domain)
    print("\n\U0001F50D [bold]Link OSINT Tambahan:[/bold]")
    print(f"- VirusTotal: https://www.virustotal.com/gui/domain/{encoded}")
    print(f"- AbuseIPDB: https://www.abuseipdb.com/check/{encoded}")
    print(f"- DNSdumpster: https://dnsdumpster.com")
    print(f"- Shodan Dork: https://www.shodan.io/search?query=hostname:{encoded}")
    print(f"- Google Dork: site:{encoded}")

    print("\n[bold green]Selesai profiling domain.[/bold green]")
