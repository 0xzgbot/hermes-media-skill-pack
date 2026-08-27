---
name: vision_audit_remediation
description: "Vision-check renders and fix failures, don't ship."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [audit, vision, consistency, cinesmith, qa]
    category: consistency-quality
    related_skills: [cinematic_consistency_protocol, character_consistency, anatomical_errors, local-cinematic-pipeline]
---

# Vision Audit and Remediation

After every still or clip, **look at the pixels** (Hermes `vision_analyze` or equivalent) and either pass or remediate. Do not mark a shot done because the Comfy job returned 200.

Cinesmith calls this the vision-audit gate. This skill is the portable version.

## When to Use

- Any local cinematic pipeline step that wrote an image or video
- Character series, product heroes, I2V, first-last clips
- User says "check this" / "why does this look wrong"

Don't use for: audio-only; prompt drafting before any render exists.

## Prerequisites

- File path to the render (PNG, JPG, or a representative video frame)
- Shot brief: identity locks, text-in-frame, forbidden artifacts
- Related fix skills loaded as needed (`anatomical_errors`, `character_consistency`, …)

## Procedure

1. Sample. Stills: full frame. Video: first, 50%, last (plus any title card). Completion: paths listed.
2. Score these axes (pass/fail, one line each):
   - **Identity** — face/body/product vs DNA
   - **Hands / anatomy**
   - **Text / logos** — gibberish type fails
   - **Lighting continuity** vs previous shot
   - **Motion** (video) — smear, morph, teleport
   - **Palette / grade** vs lock
   Completion: a six-row table in the thread or shot log.
3. Fail any axis → remediate **one** cause per retry (seed, prompt clause, new anchor, different instance). Don't change five things. Completion: retry note names the single change.
4. Recheck the failed axis only, then a full pass. Completion: all six pass or the user accepts a documented waiver.
5. Never skip audit because the model is "local so it's fine." Completion: no "done" without the table.

## Pitfalls

- Auditing the prompt instead of the file
- Passing identity because "it's the same seed" — seeds drift across graphs
- Shipping I2V that only looks good on frame 0
- Cloud vision APIs if the user demanded fully local — use the local vision tool / a frame open in the UI

## Verification

- Table exists for the deliverable
- Failures have a retry with a single named change
- Waiver, if any, is explicit
