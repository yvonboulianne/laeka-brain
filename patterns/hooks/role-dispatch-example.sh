#!/usr/bin/env bash
# role-dispatch.sh — Injecte le bon pré-prompt OmniQ selon $CLAUDE_ROLE
#
# - CLAUDE_ROLE=senior  → prompts/senior-omniq.md
# - CLAUDE_ROLE=junior  → prompts/junior-omniq.md
# - sinon               → pre-prompt.txt (Mini OmniQ par défaut)
#
# Appelé par le hook UserPromptSubmit dans ~/.claude/settings.json.
# Le stdout de ce script est injecté comme contexte additionnel dans le message user.

set -e

PROMPTS_DIR="$HOME/.claude/prompts"
DEFAULT_PREPROMPT="$HOME/.claude/pre-prompt.txt"

case "${CLAUDE_ROLE:-}" in
  senior)
    cat "$PROMPTS_DIR/senior-omniq.md"
    ;;
  junior)
    cat "$PROMPTS_DIR/junior-omniq.md"
    ;;
  shaman)
    cat "$PROMPTS_DIR/shaman-omniq.md"
    ;;
  nagual)
    cat "$HOME/Documents/laeka-brain/prompts/nagual-canonical.md"
    ;;
  go)
    cat "$HOME/Documents/laeka-brain/prompts/go-canonical.md"
    ;;
  *)
    cat "$DEFAULT_PREPROMPT"
    ;;
esac
