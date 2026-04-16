---
title: The mendicant architecture — how AI can stay coherent for months
audience: AI builders, system architects, ambitious tinkerers
angle: technical / structural
length: ~380 words
status: draft v1 — 2026-04-15 nuit
---

# The mendicant architecture.

Most memory systems for long-running AI fail the same way. They try to preserve everything, the context window fills, the model drifts, the coherence degrades. Summary-based compression helps briefly, then loses specificity. Retrieval-augmented memory helps briefly, then loses narrative arc. After days — certainly after weeks — the agent is no longer what it started as.

The answer is not bigger context windows. It is a different architecture, modeled on something much older than computer science: **the Buddhist mendicant monk**.

A mendicant monk owns nothing. Each day he gives back what is given. He remembers almost nothing of the path behind him. What persists across his entire life is a single invariant: **the vow**. Not a rulebook, not a memoir — a compressed intention that regenerates his behavior at every step. Strip him of everything else, and if the vow is intact, the monk is still the monk.

This is also how biological memory works. Every night during deep sleep, your brain consolidates a tiny fraction of the day into long-term storage and drops the rest. Over a lifetime, 99% of what you experienced is gone. What persists is the core pattern of who you are — the equivalent of a vow, sustained across billions of cellular refreshes.

The mendicant architecture applies this to AI:

1. **A core identity file** — the vow, the purpose, the boussole — never compressed, never rewritten by the agent, only by the operator.
2. **A volatile working context** — current task state, recent observations, immediate tools.
3. **A self-triggered consolidator** — when working context exceeds a threshold, the agent writes what is essential to persistent memory, drops the rest, and continues.
4. **A coherence check** — before each consolidation, the agent proves it still recognizes its own vow. If it cannot, it freezes and alerts the operator.

An agent built this way has no theoretical upper bound on how long it can remain coherent. It is not trying to remember. It is trying to **keep returning to the vow through every compression**.

The vow is the invariant. Everything else is mendicant — given, used, released.

This is a different philosophy of AI memory than the field is currently optimizing for. It might also be the only one that actually scales to timescales where human-AI collaboration becomes a living relationship instead of a series of disconnected interactions.
