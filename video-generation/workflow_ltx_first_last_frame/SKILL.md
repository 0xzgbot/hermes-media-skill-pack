---
name: workflow_ltx_first_last_frame
description: "Drive LTX video with first and last frames."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ltx, i2v, comfyui, continuity]
    category: video-generation
    related_skills: [workflow_ltx_i2v, ltx23, local-cinematic-pipeline]
---

# LTX First / Last Frame Workflow

Image-to-video where **both endpoints are locked stills**. Use when the start pose and the end pose are known (turn, walk-to-mark, product rotate, match-cut). Stronger continuity than open-ended I2V.

Cinesmith ships this as `05_ltx2.3_first_last_frame_to_video.json` (or LTX 2.5 equivalent). Run it on the **video** Comfy instance (often a 3090), not the stills box.

## When to Use

- User has (or can generate) a start frame **and** an end frame
- Need a camera or body move that must land on a composed last look
- Multi-beat stories where shot N's last frame is shot N+1's first

Don't use for: riffing motion from one still (use `workflow_ltx_i2v`); text-to-video with no anchors.

## Prerequisites

- Two stills, same aspect and preferably same character DNA / lens / key
- LTX 2.3 or 2.5 first-last graph loaded in ComfyUI
- `COMFYUI_PRIMARY` or `COMFYUI_SECONDARY` pointing at the video GPU
- Frames count = 8n+1 (LTX). Stay inside the graph's max (often 257)

## Procedure

1. Generate or pick **first** and **last** stills. Same seed series and `character_consistency` pack. Completion: both files exist; identity matches on a flipbook of the two.
2. Prompt **only the motion between them**. Subtract appearance tokens already in the stills (I2V prompt-subtraction from `workflow_ltx_i2v`). Present tense, camera verbs from `ltx23_camera_movement_language`. Completion: prompt has motion + camera, not a re-description of the wardrobe.
3. Submit to the first-last graph: `image_start`, `image_end`, frame count, sampler from `ltx23_technical_configuration`. Completion: prompt_id on the **video** instance.
4. If the middle collapses (morph, identity melt), shorten duration, reduce motion verbs, or add an in-between still and split into two first-last jobs. Completion: no melted face in a 3-frame sample (first, mid, last).
5. Chain shots by copying shot N last frame → shot N+1 first frame. Completion: cut point is a duplicate frame, not a new hallucination.

## Pitfalls

- Different aspect or crop between first and last → warp and identity loss
- Heavy lighting change between stills → flicker; relight the stills first
- Last frame too far in pose space (front → back of head in 2s) → smear; add a midpoint
- Don't run this graph on Spark if the 3090 video instance is the one with LTX weights

## Verification

- First output frame ≈ first still; last ≈ last still (vision check)
- Duration matches beat sheet
- Job ran on the intended Comfy URL
