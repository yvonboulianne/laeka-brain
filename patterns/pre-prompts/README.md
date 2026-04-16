# Pre-prompt Patterns for Claude Code

Laeka Brain uses role-based pre-prompts injected via hooks at every message.
Each role (Senior, Junior, Shaman, Go, Nagual) has its own pre-prompt that defines behavior, voice, and cognitive lenses.

## Architecture

1. A wrapper script sets `CLAUDE_ROLE=<role>` and launches `claude`
2. A `UserPromptSubmit` hook reads `$CLAUDE_ROLE` and `cat`s the matching pre-prompt file
3. A `SessionStart` hook displays a one-time briefing at session start
4. Each pre-prompt includes an **auto-metaprogramming** section that tells the agent to edit its own file when receiving durable feedback

## Key Concepts

- **Role dispatch**: `CLAUDE_ROLE` env var → hook selects the right pre-prompt → injected at every message
- **Auto-metaprogramming**: agents edit their own pre-prompt files for permanent behavior changes
- **Incarnations**: each role is a specialized "incarnation" of Claude with its own personality, expertise, and rules
- **Party structure**: multiple incarnations coordinated by a Nagual (high-altitude coordinator)

See `../metaprogramming/00-metaprogramming.md` for the full auto-metaprogramming doctrine.
