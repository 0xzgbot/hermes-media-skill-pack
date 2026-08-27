---
name: ltx25_beat_scripting
description: "Script LTX 2.5 clips to story beats, not shots."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ltx, ltx-2.5, beats, video, comfyui]
    category: video-generation
    related_skills: [ltx23, workflow_ltx_i2v, workflow_ltx_first_last_frame, 30_second_tv_spot]
---

# LTX 2.5 Beat Scripting

LTX **2.5** (when the graph is installed) is happier with **beat-timed** motion language than with a dumped shot list. Time the prompt to the story beat sheet (`15_second_social_content`, `30_second_tv_spot`) instead of one run-on paragraph.

Keep LTX 2.3 specialists for camera verbs, identity, and sampler math (`ltx23_*`). This skill is the 2.5 timing layer.

## When to Use

- Comfy graph or Settings says LTX 2.5 / `ltx25`
- Multi-second clips that must hit VO or music cues
- Cinesmith beat-based scripting / Script Studio videos

Don't use for: 2.3-only boxes (use `ltx23-prompt-engineering-master`); stills.

## Prerequisites

- Beat sheet with seconds (even rough: 0–2 hook, 2–6 product, 6–8 button)
- Anchor stills per beat, or first-last pairs
- Video Comfy instance with the 2.5 graph
- Present-tense motion language (LTX still hates "will pan")

## Procedure

1. Split the script into beats with in/out seconds. Completion: table `beat | t0 | t1 | action | camera`.
2. One LTX job per beat (or one job only if a single beat). Don't cram a 30s spot into one 257-frame generate. Completion: job count = beat count (or documented merge).
3. Prompt each job: action + camera for **that window only**. No wardrobe novel. Completion: prompt length stays in the 2.3 master thresholds.
4. Stitch in `video-editing-workflow`. Audio from `ltx23_audio_visual_sync` / `sound_design`. Completion: cuts land on beat times ±2 frames.
5. If 2.5 isn't installed, fall back to 2.3 I2V with the same beat table. Completion: user is told which graph ran.

## Pitfalls

- One mega-prompt for the whole spot → mushy motion, missed cues
- Mixing 2.3 and 2.5 sampler settings
- Ignoring first-last when a beat must land on a poster frame

## Verification

- Each beat has a clip or a waiver
- Picture hits the beat times vs the sheet
- Graph name (2.3 vs 2.5) recorded
