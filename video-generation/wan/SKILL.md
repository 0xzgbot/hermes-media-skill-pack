---
name: wan
description: "Index Wan 2.2 local and Wan 3.0 control."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wan, alibaba, video, prompting, comfyui]
    category: video-generation
    related_skills: [wan_prompt_engineering_master, wan_camera_motion_control, wan_audio_direction, wan_reference_control, local-cinematic-pipeline, multi-comfy-orchestration]
---

# Wan — Cluster Umbrella

**Wan** is Alibaba Tongyi's video family. Prompting control **changes by generation**. Do not paste LTX paragraphs or MiniMax H3 shot-blocks (`At 00:03.500`, `<d>[English]`) as drop-ins.

| Line | Open local Comfy? | What it is | Prompting skill |
| --- | --- | --- | --- |
| **Wan 2.2** | Yes (Apache 2.0) | MoE 14B T2V/I2V (high-noise + low-noise), TI2V-5B, FLF2V, Animate, S2V | Master + camera |
| **Wan 2.5 / 2.6** | No | Closed API, native AV on 2.5 | Hosted; 3.0-style labels if the UI is multimodal |
| **Wan 2.7** | Partial (Thinking Mode) | CoT planning before denoise; 15 s class | Master: `enable_thinking`, sequential first/then |
| **Wan 3.0 / 3.0 Prime** | Hosted (fal / Model Studio) | **Current new Wan (Aug 2026):** up to **30 s**, up to **20 refs**, native audio, prompt expansion + thinking | Master + audio + reference |

For this shop: **2.2 on dual 3090s / Spark** for local iterate; **3.0 Prime on fal** (or Model Studio) for long multimodal keepers. Isolated Hermes does not change the model — it only routes (`multi-comfy-orchestration`).

| Skill | When |
| --- | --- |
| `wan_prompt_engineering_master` | Any Wan generate. 2.2 UMT5 vs 2.7 thinking vs 3.0 shots/`@` tags. |
| `wan_camera_motion_control` | Fun Camera vs prompt camera; FLF2V; Animate Mix/Move; 3.0 Camera UI. |
| `wan_audio_direction` | 3.0 three-layer sound; 2.2 is usually silent unless S2V. |
| `wan_reference_control` | 3.0 Omni-Reference (20 files + doc/web); 2.2 I2V/FLF stills. |
