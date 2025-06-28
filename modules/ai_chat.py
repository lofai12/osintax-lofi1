import requests
from rich import print
from rich.prompt import Prompt

GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def run():
    print("[bold magenta]Mode Interaksi Bebas dengan AI (Groq LLaMA)[/bold magenta]")
    print("[dim]Ketik 'exit' untuk keluar dari mode ini.[/dim]\n")

    history = [{"role": "system", "content": "Kamu adalah asisten OSINT yang ramah dan membantu."}]

    while True:
        user_input = Prompt.ask("[bold cyan]Kamu[/bold cyan]")

        if user_input.strip().lower() == "exit":
            print("[green]Keluar dari mode interaksi bebas.[/green]")
            break

        history.append({"role": "user", "content": user_input})

        try:
            response = requests.post(
                GROQ_API_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama3-8b-8192",  # ✅ model valid
                    "messages": history
                },
                timeout=15
            )

            if response.status_code == 200:
                result = response.json()
                reply = result["choices"][0]["message"]["content"]
                history.append({"role": "assistant", "content": reply})
                print(f"\n[bold green]AI:[/bold green] {reply}\n")
            else:
                print(f"[red]Gagal: {response.status_code} - {response.text}[/red]")

        except Exception as e:
            print(f"[red]Kesalahan saat menghubungi API: {e}[/red]")
