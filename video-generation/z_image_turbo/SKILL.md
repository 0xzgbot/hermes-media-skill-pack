---
name: z_image_turbo
description: "Generate fast local stills with Z-Image Turbo."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [z-image, flux, comfyui, stills, dgx-spark]
    category: video-generation
    related_skills: [workflow_flux2_text_to_image, flux2dev_cinematic_still_mastery, local-cinematic-pipeline]
---

# Z-Image Turbo Stills

**Z-Image Turbo** (and Flux.2 Klein when that graph is loaded) is the **fast local still** path: drafts, boards, and iteration. Final hero anchors still prefer full Flux.2 Dev when quality wins over speed.

Runs on **DGX Spark** or a 3090 stills instance. Not a video model.

## When to Use

- Storyboards, thumbnails, prompt iteration, "give me 8 options"
- Spark box online, user wants stills without waiting on Flux.2 Dev
- Cinesmith provider `spark:z_image` / `z_image_turbo`

Don't use for: final print hero if Flux.2 Dev is available; LTX motion (wrong model).

## Prerequisites

- ComfyUI with the Z-Image Turbo (or Klein) workflow
- `COMFYUI_PRIMARY` or `COMFYUI_SPARK` healthy
- Same prompt grammar as Flux.2 (`positive_prompt_structure`) — short, ordered, no dump of quality adjectives

## Procedure

1. Target the stills instance. Completion: `/system_stats` on that URL.
2. Prompt like Flux.2: subject → light → lens → grade. Klein/Turbo punish long prompts. Completion: under ~80 tokens unless the graph says otherwise.
3. Batch 4–8 seeds for boards; lock one seed before I2V. Completion: chosen PNG path recorded as the shot anchor.
4. Promote to Flux.2 Dev only when the board pick is the hero. Completion: user knows which file is "board" vs "hero."
5. Hand the hero to `workflow_ltx_i2v` or `workflow_ltx_first_last_frame`. Completion: I2V uses the hero, not a random Turbo reject.

## Pitfalls

- Treating Turbo as the finish model → plastic skin, weak hands. Audit (`vision-audit-remediation`) before motion.
- Mixing Klein and Dev seeds as if they were interchangeable — they're not.
- Loading Z-Image and LTX on one 24 GB GPU together.

## Verification

- Board batch exists; one file marked hero
- Hero identity survives a vision check before I2V
