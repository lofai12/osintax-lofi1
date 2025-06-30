import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.prompt import Prompt
from rich.markdown import Markdown

# Init
load_dotenv()
console = Console()

# ✅ API key diambil dari environment variable, bukan ditulis langsung
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

# Cek API Key
if not API_KEY:
    console.print("[bold red]❌ API key tidak ditemukan di .env![/]")
    exit()

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Fungsi nanya ke AI
def ask_ai(prompt):
    if not prompt.strip():
        return "[!] Prompt kosong, ketik sesuatu dulu."

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()["choices"][0]["message"]["content"]
        return result.strip()
    except requests.exceptions.RequestException as e:
        return f"[ERROR] {e}"

# Chat CLI
def chat_loop():
    console.print("[bold cyan]🤖 OSINTax AI Chat - by Lofi[/bold cyan]\n[dim]Ketik 'exit' untuk keluar[/dim]\n")
    while True:
        try:
            user_input = Prompt.ask("[bold green]You[/bold green]")
            if user_input.lower() in ["exit", "quit"]:
                console.print("[bold yellow]👋 Keluar...[/]")
                break
            reply = ask_ai(user_input)
            console.print(Markdown(f"**AI:** {reply}"))
        except KeyboardInterrupt:
            console.print("\n[bold red]⛔ Dihentikan oleh user.[/]")
            break

# Run
if __name__ == "__main__":
    chat_loop()
