---
name: minimax_h3
description: "Index MiniMax H3: shots, camera, audio, refs."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, hailuo, h3, video, prompting]
    category: video-generation
    related_skills: [minimax_h3_prompt_engineering_master, minimax_h3_camera_movement_language, minimax_h3_audio_direction, minimax_h3_reference_control, minimax_h3_technical_configuration]
---

# MiniMax H3 — Cluster Umbrella

MiniMax **H3** (Hailuo 3) is a **unified omni-modal video model**: text + images + video + audio → **4–15 s**, **24 fps**, **32 kHz stereo**. Hosted finish can be **2K**. Open **H3-Base** is a **768 px short-edge** ceiling.

This folder is **prompting control**. H3 is not LTX (no single-paragraph dump) and not Wan (no `@Image1` / `[0-5s]` dialect on Base). Start with the master.

| Skill | When |
| --- | --- |
| `minimax_h3_prompt_engineering_master` | Any generate. Choose Base vs Full-Reference **before** writing. |
| `minimax_h3_camera_movement_language` | Motion type + amplitude + speed in English. Cuts vs camera. |
| `minimax_h3_audio_direction` | Always-on stereo. Soundscape vs score vs `<d>` dialogue. |
| `minimax_h3_reference_control` | Identity, R2V, six-section Full-Reference, localized edits. |
| `minimax_h3_technical_configuration` | IR vs Base vs 2K, FL2VA vs ref2va, duration grid, license. |

## Architecture (do not collapse)

H3 is **three modules**, not one checkpoint:

1. **H3-Context-IR** — hosted prompt compiler. Not in the open-weights drop. Same words can look great on Hailuo/fal and broken in Comfy.
2. **H3-Base** (~33B) — open weights. Executes the structured IR. Native short edge **768 px**.
3. **H3-Regenerate-2K** — hosted upscale. Not a missing Comfy node.

Against H3-Base you **are** Context-IR. Write the official format.

## Pick the format first

Uploaded files do **not** pick the task. Role does.

| Role of the stills | Format |
| --- | --- |
| None | Base **T2VA** — three fields, no alignment line |
| Exact first frame | Base **I2VA** — official first-frame instruction, then three fields |
| Exact first **and** last | Base **FL2VA** — prefer **one continuous shot** |
| Exact last frame only | Base **L2VA** — image belongs to **final** `[Shot N]`, not Shot 1 |
| Identity / style / motion / voice / edit source | **Full-Reference** — six sections, not a longer Base prompt |

Wrong checkpoint is the most common Comfy fail: **FL2VA vs ref2va**.
