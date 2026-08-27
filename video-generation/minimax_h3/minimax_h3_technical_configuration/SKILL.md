---
name: minimax_h3_technical_configuration
description: "Set H3 modules, graphs, duration, license."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, h3, comfyui, inference]
    category: video-generation
    related_skills: [minimax_h3_prompt_engineering_master, multi-comfy-orchestration, local-cinematic-pipeline]
---

# MiniMax H3 Technical Configuration

Prompting dialect is the master skill. This file is **which module, graph, duration, and license** you are actually running — the mistakes that make a perfect prompt look like a broken model.

## When to Use

- Local Comfy vs Hailuo/fal vs Diffusers
- First success criteria (stereo MP4)
- Duration not matching the request
- "Same prompt worked on the API"

Don't use for: shot grammar (master), camera verbs (camera skill), `<d>` / soundscape (audio), six-section Ref2VA (reference).

## Three modules

| Module | Open? | Job |
| --- | --- | --- |
| **H3-Context-IR** | No (hosted API) | Parses multimodal mess → structured IR. MiniMax: *critical to final quality*. |
| **H3-Base** | Yes (~33B) | Joint video+audio at **768 px short edge**, 24 fps, 32 kHz stereo |
| **H3-Regenerate-2K** | Hosted | Feeds 768p + original context back in for 2K |

Consequence: **hosted can look great on a lazy brief; local cannot.** Local you write Base or Full-Reference yourself. Official portable skill: MiniMax `h3-prompt-writing` (`base-en.txt`, `ref-en.txt`) — convert briefs **before** hitting Comfy.

fal also lists **h3-max** post-trained endpoints. Same prompt dialect; different weights.

## Checkpoints / workflows

| Job | Graph / variant | Inputs |
| --- | --- | --- |
| Text only | T2VA / T2V template | Prompt |
| First and/or last still | **FL2VA** (`H3-Base-FL2VA`) | 0, 1, or 2 images. Zero = T2V. One = first **or** last. Two = first+last |
| Omni-reference | **Ref2VA** (`H3-Base-Ref2VA`) | ≤9 images, ≤3 videos, ≤3 audios, ≤12 files |

**Wrong checkpoint is the top Comfy fail.** R2V template + FL2VA weights → garbage / silent fail. Diffusers: pass `workflow=` so you do not load both 61.7 GB transformer partitions.

R2V shipped templates may expose **two** image slots; the model accepts **nine**. Extend the graph before blaming the prompt.

## Canvas, duration, audio

| Knob | Spec |
| --- | --- |
| Short edge | 768 px local default. Hosted 2K is a **second module**, not a resolution dropdown on Base |
| Aspects | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 (and others) |
| FPS | **24 only** |
| Duration | **4–15 s**. Native grid **17k+5 frames** — a 5 s request lands ~124 frames / **~5.17 s** |
| Audio | Always on, 32 kHz stereo. Silent MP4 = VAE/graph wiring |
| Prompt length | ~7k characters on fal |
| Negatives / CFG | **None.** Guidance distilled; every step is one forward pass |

Comfy community start: **864×480, 5 s, 20 steps**, `res_multistep` + `simple`. Change **one** knob after the first stereo MP4. SGLang refs may use 50 steps — do not copy that blindly onto a 20-step graph.

SageAttention ~2× if compute-bound; offload-bound runs will not show it.

## Local shop routing

- Iterate H3-Base at 0.4 MP / 5 s / 20 steps on a 3090 or Spark.
- Do not load H3-Base **and** Wan 14B MoE **and** LTX on one 24 GB card (`multi-comfy-orchestration`).
- Stills may still be Flux / Z-Image; H3 is the multimodal video+audio pass (`local-cinematic-pipeline`).
- Isolated Hermes: `isolated-hermes-home`. Do not copy this pack into `~/.hermes` when Cinesmith owns `HERMES_HOME`.

## License (not legal advice)

Open weights: **MiniMax H3 Community License**, not Apache. Typical constraints called out in the model card: territory, attribution, **no distillation**. API/Hailuo is a **different contract**. Read `LICENSE` before shipping a product that redistributes weights or outputs.

## Verification

- Module named in the shot log: IR+Base+2K vs Base-only
- Graph matches assets: FL2VA vs ref2va
- First green run is stereo MP4, not a still
- Duration request inside 4–15 s; expect grid snap
- No negative prompt field in the graph
- License noted if weights leave the machine
