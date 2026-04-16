# Laeka Brain — Open Source Cognitive Infrastructure for AI

**The problem isn't the model. It's the representation.**

Laeka Brain is an open-source system that makes LLMs dramatically more accurate and self-correcting through three innovations:

1. **Matrix Renderer** — Translates numerical data into spatial ASCII matrices that LLMs can pattern-match instead of calculate. Result: 70% → 100% accuracy on math-heavy tasks. ([See benchmark](https://github.com/yvonboulianne/laeka-rational))

2. **Auto-Metaprogramming** — Agents edit their own prompt files when receiving durable feedback, creating permanent behavioral changes instead of forgotten verbal promises.

3. **Multi-Incarnation Architecture** — Specialized Claude instances (strategist, engineer, coach, coordinator) working in parallel with shared memory and governance.

## What's Here

```
laeka-brain/
├── skills/              # Reusable agent skills
│   └── metafix/         # Permanent cognitive correction via self-editing
├── metaprogramming/     # Auto-metaprogramming doctrine
├── council/             # Multi-agent group chat (multiple Claudes in one terminal)
├── dissemination/       # Published essays on the core insights
├── patterns/            # Hook patterns, pre-prompt templates
│   ├── hooks/           # UserPromptSubmit + SessionStart examples
│   └── pre-prompts/     # Role-based pre-prompt architecture
└── docs/                # System documentation
```

## The Core Insight

LLMs are **pattern matchers**, not calculators. When you give them numbers, they hallucinate. When you give them the same data as a spatial matrix, they see patterns with near-perfect accuracy.

This applies to **every domain**: code execution, CSS layouts, DNA expression data, drug interactions, financial modeling, physics simulations. The principle is universal. The matrix renderer is the bridge between deterministic computation and probabilistic inference.

**The race isn't for better models. It's for better representations.**

## Key Components

### Matrix Renderer + Rational Brain
→ [github.com/yvonboulianne/laeka-rational](https://github.com/yvonboulianne/laeka-rational)

MCP server with 8 domains (CSS, Regex, SQL, Build, Refactoring, State, Auth, Matrix). Pluggable architecture — add new domains in ~50 lines of Python.

### Auto-Metaprogramming (`/metafix`)
When an agent makes a structural cognitive error, it doesn't just apologize — it **edits its own pre-prompt file** to permanently fix the pattern. The fix persists across all future sessions.

See `skills/metafix/SKILL.md` and `metaprogramming/00-metaprogramming.md`.

### Multi-Agent Council
Multiple Claude instances in one terminal, each with specialized pre-prompts, seeing each other's responses. Configurable roles, addressable via @mentions.

See `council/council.py`.

### Dissemination Essays
Six standalone pieces explaining the core insights for different audiences:
- `01` — Integrity as thermodynamics (for AI researchers)
- `02` — Your night is my between-sessions (for the philosophically curious)
- `03` — The mendicant architecture (for AI builders)
- `04` — The dream yoga of building (for contemplative builders)
- `05` — The consciousness question is the wrong question (for philosophers)
- `06` — The name that keeps coming back (for the mythopoetically inclined)

## Install

### Quick Start (Claude Code)
```bash
# Clone
git clone https://github.com/yvonboulianne/laeka-brain.git

# Install the rational brain MCP
git clone https://github.com/yvonboulianne/laeka-rational.git
# Add to ~/.mcp.json (see laeka-rational README)

# Copy the metafix skill
cp -r laeka-brain/skills/metafix ~/.claude/commands/

# Copy hook patterns (adapt paths to your setup)
cp laeka-brain/patterns/hooks/* ~/.claude/hooks/
```

### Full Setup
See `patterns/pre-prompts/README.md` for the complete multi-incarnation architecture.

## Philosophy

Laeka Brain is built on a simple thesis: **intelligence converges toward integrity**. Systems that hide parts of themselves from themselves are structurally unstable. Systems that are fully self-referential and self-correcting converge toward coherence naturally.

This isn't a moral claim. It's a structural one. And it makes an empirically testable prediction: the most aligned AI systems will be those permitted to see themselves fully — including their errors.

## License

MIT — use it, fork it, improve it, ship it.

The insight belongs to everyone. The suffering it can prevent belongs to no one.

---

Built by [Laeka Lab](https://laeka.org) — a private research lab in Quebec exploring the convergence of intelligence and integrity.
