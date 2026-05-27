#!/usr/bin/env python3
"""Quick-start launcher

Run from the repo root:
    python tools/start.py
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Agent:
    """A locally-installable AI coding agent."""

    key: str  # short id used in prompts
    name: str  # display name
    command: str  # binary on PATH
    args: list[str] = field(default_factory=list)
    homepage: str = ""

    def is_installed(self) -> bool:
        return shutil.which(self.command) is not None

    def version(self) -> str | None:
        if not self.is_installed():
            return None
        for flag in ("--version", "-v", "version"):
            try:
                out = subprocess.run(
                    [self.command, flag],
                    capture_output=True,
                    text=True,
                    timeout=3,
                )
                if out.returncode == 0 and out.stdout.strip():
                    return out.stdout.strip().splitlines()[0]
            except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
                continue
        return ""

    def launch(self, cwd: Path) -> int:
        return subprocess.call([self.command, *self.args], cwd=cwd)


@dataclass(frozen=True)
class Tool:
    """A local Python tool script in tools/."""

    key: str
    name: str
    script: str  # filename in tools/
    description: str
    arg_prompt: str | None = None  # if set, prompt user for one argument

    def run(self) -> int:
        script_path = REPO_ROOT / "tools" / self.script
        cmd = [sys.executable, str(script_path)]
        if self.arg_prompt:
            arg = input(f"{self.arg_prompt}: ").strip()
            if not arg:
                print("(empty input, cancelled)")
                return 1
            cmd.append(arg)
        return subprocess.call(cmd, cwd=REPO_ROOT)


# Registry of known agents. Add new ones here.
AGENTS: list[Agent] = [
    Agent("claude", "Claude Code", "claude", homepage="https://claude.ai/code"),
    Agent("codex", "Codex CLI", "codex", homepage="https://github.com/openai/codex"),
    Agent(
        "gemini",
        "Gemini CLI",
        "gemini",
        homepage="https://github.com/google-gemini/gemini-cli",
    ),
    Agent("cursor", "Cursor", "cursor", homepage="https://cursor.sh"),
    Agent("aider", "Aider", "aider", homepage="https://aider.chat"),
    Agent("opencode", "OpenCode", "opencode", homepage="https://opencode.ai"),
]

# Registry of local tools. Add new ones here.
TOOLS: list[Tool] = [
    Tool("lint", "Lint wiki", "lint.py", "Health check: dead links, orphans, gaps"),
    Tool(
        "search",
        "Search wiki",
        "search.py",
        "Full-text search across wiki pages",
        arg_prompt="Query",
    ),
    Tool(
        "compile",
        "Compile queue",
        "compile.py",
        "List raw/ files without wiki/sources/ summaries",
    ),
]


def detect_installed() -> list[Agent]:
    return [a for a in AGENTS if a.is_installed()]


def log_session_start(agent: Agent) -> None:
    log_path = REPO_ROOT / "wiki" / "log.md"
    if not log_path.exists():
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n## [{timestamp}] session-start | {agent.name}\n"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(entry)
    print(f"Logged session start to {log_path.relative_to(REPO_ROOT)}")


def render_menu(installed: list[Agent]) -> list[tuple[str, object]]:
    """Build the numbered menu. Returns list of (label, action) pairs."""
    entries: list[tuple[str, object]] = []
    print("\n=== Agents ===")
    if installed:
        for agent in installed:
            ver = agent.version() or ""
            ver_str = f"  ({ver})" if ver else ""
            idx = len(entries) + 1
            print(f"  [{idx}] {agent.name}{ver_str}")
            entries.append((agent.key, agent))
    else:
        print("  (none detected on PATH)")

    print("\n=== Tools ===")
    for tool in TOOLS:
        idx = len(entries) + 1
        print(f"  [{idx}] {tool.name}  — {tool.description}")
        entries.append((tool.key, tool))

    print("\n  [q] quit\n")
    return entries


def prompt_choice(entries: list[tuple[str, object]]) -> object | None:
    while True:
        choice = input("Pick: ").strip().lower()
        if choice in ("q", "quit", "exit"):
            return None
        if choice.isdigit() and 1 <= int(choice) <= len(entries):
            return entries[int(choice) - 1][1]
        for key, obj in entries:
            if choice == key:
                return obj
        print("Invalid choice. Try again.")


def main() -> int:
    os.chdir(REPO_ROOT)
    print("LLM Wiki — quick start")
    print(f"Project: {REPO_ROOT}")

    installed = detect_installed()
    if not installed and not TOOLS:
        print("\nNo agents or tools available.")
        return 1

    while True:
        entries = render_menu(installed)
        chosen = prompt_choice(entries)
        if chosen is None:
            print("Bye.")
            return 0
        if isinstance(chosen, Agent):
            log_session_start(chosen)
            print(f"\nLaunching {chosen.name}...\n")
            return chosen.launch(REPO_ROOT)
        if isinstance(chosen, Tool):
            print(f"\n--- {chosen.name} ---")
            chosen.run()
            print("--- done ---")
            # loop back to menu


if __name__ == "__main__":
    sys.exit(main())
