---
name: local-cinematic-pipeline
description: "Run plan → still → video → audit fully local."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [pipeline, local-ai, cinesmith, flux, ltx, comfyui]
    category: video-generation
    related_skills: [isolated-hermes-home, multi-comfy-orchestration, workflow_ltx_i2v, vision_audit_remediation, character_consistency]
---

# Local Cinematic Pipeline

End-to-end **fully local** production loop: brief → plan → hero still → image-to-video → vision audit → remediate. No required cloud Director, FAL, or Gemini.

Orchestrator is a **custom isolated Hermes** (`isolated-hermes-home`). Renderers are local ComfyUI instances (`multi-comfy-orchestration`).

## When to Use

- User wants a spot, story, or campaign **offline**
- Cinesmith / Forge-style Agency brief on LAN Spark + 3090s
- "Don't call OpenAI / FAL / Kimi" or air-gapped hardware

Don't use for: single still doodles (use Flux.2 skill only); cloud-only Director setups.

## Prerequisites

- Isolated `HERMES_HOME=<project>/hermes_home`
- At least one ComfyUI (`COMFYUI_PRIMARY`) answering `/system_stats`
- Local chat/Director optional: LM Studio `http://localhost:1234` or a local model on Spark
- Models on disk: Flux.2 (or Z-Image Turbo) + LTX 2.3 or 2.5 I2V graph
- This pack installed **into** `$HERMES_HOME/skills`

## Procedure

1. **Isolate.** Set `HERMES_HOME`. Completion: not `~/.hermes`.
2. **Brief.** One paragraph: duration, product, character DNA, delivery aspect. Completion: written to the project, not only chat.
3. **Plan locally.** Shot list from `30_second_tv_spot` / `15_second_social_content` plus lighting + lens skills. No cloud planner required. Completion: numbered shots with lens, key, duration.
4. **Hero stills.** Flux.2 T2I or Z-Image Turbo on the stills instance (`workflow_flux2_text_to_image` / `z_image_turbo`). Lock seed + character pack (`character_consistency`). Completion: one anchor PNG per shot that passes a visual identity check.
5. **Motion.** LTX I2V from the anchor (`workflow_ltx_i2v`). First/last-frame when the end pose is known (`workflow_ltx_first_last_frame`). Wan **2.2** I2V/FLF is the local alternative (`wan_prompt_engineering_master`) — one video family per GPU. Hosted MiniMax H3 / Wan 3.0 are **not** this recipe. Completion: clip duration matches the beat; camera verbs from the **same** family (`ltx23_camera_movement_language` or `wan_camera_motion_control`).
6. **Audit.** `vision_audit_remediation` — identity, hands, text, continuity. Fail → patch prompt/seed/anchor, do not ship. Completion: pass/fail table per shot.
7. **Finish.** Grade (`color_grading_film_emulation`), edit (`video-editing-workflow`), audio (`sound_design`). Completion: deliverable file path.

## Pitfalls

- FAL / OpenAI image in Cinesmith Settings breaks "fully local." Leave them unset.
- Running I2V on the same GPU as Flux weights without unloading will OOM.
- `ltx23` umbrella is an index — load a specialist with `skill_view`, don't treat the umbrella as the sampler.

## Verification

- Zero outbound API keys required for a still + I2V pair
- `HERMES_HOME` isolated
- Two Comfy ports optional but documented if present
- Audit table exists before the user is told "done"
