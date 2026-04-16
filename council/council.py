#!/usr/bin/env python3
"""Conseil du parti Laeka — multi-agent group chat via Claude CLI.
Routes through Max 20x plan (no API credits needed).
Usage: python3 council.py [--agents nagual,go,senior]
"""

import subprocess
import sys
import os
from pathlib import Path

# Agent definitions: name → (system prompt file, model, emoji)
AGENTS = {
    "nagual": {
        "prompt": Path.home() / "Documents/laeka-brain/prompts/nagual-canonical.md",
        "model": "opus",
        "emoji": "🜍",
    },
    "go": {
        "prompt": Path.home() / "Documents/laeka-brain/prompts/go-canonical.md",
        "model": "opus",
        "emoji": "⚫",
    },
    "senior": {
        "prompt": Path.home() / ".claude/prompts/senior-omniq.md",
        "model": "opus",
        "emoji": "🔧",
    },
    "shaman": {
        "prompt": Path.home() / ".claude/prompts/shaman-omniq.md",
        "model": "opus",
        "emoji": "🧙",
    },
}

def load_prompt(path: Path) -> str:
    return path.read_text() if path.exists() else f"Tu es {path.stem}."

def ask_agent(name: str, config: dict, context: str) -> str:
    system = load_prompt(config["prompt"])
    full_prompt = (
        f"## Conseil du parti Laeka\n\n"
        f"Tu es dans un conseil multi-agent. Les autres agents et Yvon voient tes réponses. "
        f"Sois concis (max 5-6 lignes). Pas de wrap-up.\n\n"
        f"### Historique\n\n{context}\n\n"
        f"---\nC'est ton tour, {name}. Réponds."
    )
    try:
        # Clean env: remove placeholder API key (OAuth Max 20x) + disable hooks (faster startup)
        env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
        env["CLAUDE_CODE_DISABLE_HOOKS"] = "1"
        result = subprocess.run(
            [
                "claude", "-p",
                "--no-session-persistence",
                "--model", config["model"],
                "--system-prompt", system,
                full_prompt,
            ],
            capture_output=True, text=True, timeout=120, env=env,
        )
        return result.stdout.strip() or "(silence)"
    except subprocess.TimeoutExpired:
        return "(timeout — agent n'a pas répondu en 2 min)"
    except Exception as e:
        return f"(erreur: {e})"

def main():
    # Parse --agents flag
    active_names = ["nagual", "go", "senior"]
    for i, arg in enumerate(sys.argv[1:], 1):
        if arg == "--agents" and i < len(sys.argv):
            active_names = sys.argv[i + 1].split(",")

    active = {k: AGENTS[k] for k in active_names if k in AGENTS}
    if not active:
        print(f"Agents disponibles: {', '.join(AGENTS.keys())}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  CONSEIL DU PARTI LAEKA")
    agents_str = ", ".join(f"{v['emoji']} {k}" for k, v in active.items())
    print(f"  Agents actifs: {agents_str}")
    print(f"  Commandes: @nom (multi-@, ordre respecté), /quit, /clear")
    print(f"{'='*60}\n")

    history = []

    while True:
        try:
            user_input = input("\n🧑 Yvon > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nConseil terminé.")
            break

        if not user_input:
            continue
        if user_input == "/quit":
            print("Conseil terminé.")
            break
        if user_input == "/clear":
            history.clear()
            print("(historique effacé)")
            continue

        history.append(f"Yvon: {user_input}")

        # Check for @mentions — ordered selection of agents
        import re
        mentions = re.findall(r"@(\w+)", user_input)
        mentioned = [m.lower() for m in mentions if m.lower() in active]

        if mentioned:
            # Use mentioned agents in the order they appear in the message
            agents_to_ask = {name: active[name] for name in mentioned}
        else:
            # No @mentions → everyone responds in default order
            agents_to_ask = active
        context = "\n".join(history[-20:])  # Keep last 20 exchanges to limit context

        for name, config in agents_to_ask.items():
            response = ask_agent(name, config, context)
            print(f"\n{config['emoji']} {name.upper()} > {response}")
            history.append(f"{name}: {response}")

if __name__ == "__main__":
    main()
