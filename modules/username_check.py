from rich import print
import requests

def run(username):
    print(f"\n[bold cyan]Hasil Pencarian Username: {username}[/bold cyan]\n")

    platforms = {
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "X.com": f"https://x.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Telegram": f"https://t.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Threads": f"https://www.threads.net/@{username}"
    }

    headers = {"User-Agent": "Mozilla/5.0"}

    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"[green][+][/green] {platform}: [underline]{url}[/underline]")
            elif response.status_code == 404:
                print(f"[red][-][/red] {platform}: Not Found")
            else:
                print(f"[yellow][!][/yellow] {platform}: Unexpected status code {response.status_code}")
        except requests.exceptions.RequestException:
            print(f"[red][x][/red] {platform}: Error connecting")

    print("\n[dim]Pencarian selesai.[/dim]\n")
