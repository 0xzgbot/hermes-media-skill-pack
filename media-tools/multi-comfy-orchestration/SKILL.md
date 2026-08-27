---
name: multi-comfy-orchestration
description: "Route jobs across DGX Spark and dual-3090 Comfy."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [comfyui, dgx-spark, rtx-3090, orchestration, local-ai]
    category: media-tools
    related_skills: [comfyui, local-cinematic-pipeline, isolated-hermes-home]
---

# Multi-Comfy Orchestration

Run **several ComfyUI instances** on mixed local hardware and pick the right one per job. Typical shop: **NVIDIA DGX Spark** (planning / Flux / Z-Image) plus **dual RTX 3090s** (one GPU per Comfy process, image vs video).

An isolated Hermes agent (`isolated-hermes-home`) is the router. It must not assume a single `localhost:8188`.

## When to Use

- More than one ComfyUI HTTP port is live (8188, 8189, …)
- Hardware mix: DGX Spark + 3090s, or two 3090s, or Spark-only
- Queueing stills and LTX/Wan video without stalling one box
- User mentions Spark, 3090, multi-instance Comfy, or "fully local"

Don't use for: a single hobby Comfy on one port (use `comfyui` instead).

## Prerequisites

- Each Comfy answers `GET /system_stats` (or `/object_info`)
- Env (names are conventional; map to your `.env`):
  - `COMFYUI_PRIMARY` — default stills (often Spark or 3090-A `:8188`)
  - `COMFYUI_SECONDARY` — second GPU / video (`:8189`)
  - Optional `COMFYUI_SPARK` — DGX Spark if primary is a 3090
- Isolated Hermes: `HERMES_HOME` is the **project** home, not `~/.hermes`

## How to Run

Frame checks through the `terminal` tool:

```text
terminal(command="curl -sS -m 3 $COMFYUI_PRIMARY/system_stats", timeout=8)
terminal(command="curl -sS -m 3 $COMFYUI_SECONDARY/system_stats", timeout=8)
```

## Procedure

1. Inventory instances. Completion: a table of `{name, url, gpu, role}` with a live stats response each.
2. Assign roles (adjust to VRAM):
   | Role | Default hardware | Port habit |
   | --- | --- | --- |
   | Flux.2 / Z-Image stills | DGX Spark **or** 3090-A | 8188 |
   | LTX I2V / first-last | 3090-B (24 GB) | 8189 |
   | Overflow / Turbo | Spark or whichever is idle | 8188 or 8190 |
   Completion: every workflow skill has a target URL, not "the" Comfy.
3. Pin workflows to roles. Flux.2 T2I → stills instance. LTX I2V and first/last-frame → video instance. Do not load a 257-frame LTX graph on a box already holding Flux weights if VRAM will spill.
4. One Comfy **process per GPU**. Two graphs on one 3090 OOM or thrash. Completion: `nvidia-smi` shows one compute pid per GPU (plus Spark).
5. Fail closed. If the video instance is down, queue LTX; do not silently run I2V on the stills box. Completion: user sees which URL failed, not a generic Comfy error.
6. Hermes stays isolated. Completion: routing lives in project `.env` + this skill; `~/.hermes` unchanged.

## Pitfalls

- "Spark" in Cinesmith docs means the Comfy box. **DGX Spark** is the NVIDIA workstation. Say which one.
- Cloud FAL fallback is optional and **not** fully local. Don't enable it unless the user asks.
- WebSocket history is per instance. Don't poll 8188 for a prompt_id submitted to 8189.
- Free-tier Comfy Cloud is 1 concurrent job — irrelevant when fully local; ignore those limits.

## Verification

- Two+ `/system_stats` succeed on different ports
- A Flux still and an LTX clip can be in flight on different GPUs
- `HERMES_HOME` is the project tree
