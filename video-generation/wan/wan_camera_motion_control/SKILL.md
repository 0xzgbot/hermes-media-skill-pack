---
name: wan_camera_motion_control
description: "Control Wan camera, FLF, and Animate."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wan, camera, flf2v, animate, comfyui]
    category: video-generation
    related_skills: [wan_prompt_engineering_master, workflow_ltx_i2v, workflow_ltx_first_last_frame]
---

# Wan Camera, FLF2V, and Animate

Picture prompting is the master skill. This file is **how the camera and body move** on Wan 2.2 graphs and how **3.0** treats camera as a control vs a sentence.

## When to Use

- Pan / zoom / orbit must be **repeatable**
- First–last interpolation (FLF2V)
- Character replace (Animate **Mix**) or puppeteer (Animate **Move**)
- 3.0 inventing cuts and dollies you did not ask for

Don't use for: look/style (master), 3.0 voice/SFX/music (`wan_audio_direction`), `@` jobs (`wan_reference_control`).

## Wan 2.2 Fun Camera (Comfy)

Comfy **WanCameraEmbedding** / Fun Camera workflows take **discrete** moves (pan, zoom, etc.). Then the **text prompt is acting and scene**, not a second camera novel.

Rule: **node XOR prompt**, not both arguing.

| Intent | Do this |
| --- | --- |
| Same move every take | Set it on the camera node; prompt `fixed framing except the node move` |
| Organic handheld | Prompt the shake; leave node on none / static |
| Locked tripod | Node static + prompt `fixed shot, no reframing` |

One move per clip. Stacked pan+zoom+orbit is the 2.2 wobble pattern.

Prompt camera (when not using the node): one verb + speed. `slow push in`, `static locked-off`, `gentle pan right`. Do not write MiniMax's `with small amplitude at slow speed` essay unless you are actually on H3.

## FLF2V (2.2 native template)

`WanFirstLastFrameToVideo`: start LoadImage + end LoadImage. Same 14B I2V high/low pair as I2V.

Prompt the **in-between**:

```
Smooth move from the start pose to the end pose. Camera locked. Lighting continuous. No morphing faces.
```

VRAM: template defaults small; 720p when the video 3090 is free. Endpoints must **match aspect**. Huge pose jumps in 2 s smear — split beats.

## Animate-14B

| Mode | Inputs | Prompt role |
| --- | --- | --- |
| **Mix** | Driving video + character image + usually mask/background video | Replace the person; keep the plate's motion |
| **Move** | Character image + motion video; disconnect background_video / character_mask per Comfy Mix→Move switch | Puppeteer the still |

Prompt: identity locks + `match timing of the driving clip`. Do not rewrite choreography the video already has.

LightX2V I2V distill LoRA is common on these graphs (4-step). CFG 1 → no negatives.

## Wan 3.0 camera

- UI **Camera** control (OpenArt / host) beats typing three conflicting moves — same move every take.
- Unspecified: model **picks** cuts and motion. Force `one continuous take` and/or `fixed shot`.
- Headline capability is a **30 s single take** (一镜到底): one named move that can actually finish (slow push, pan, track). Do not ask for a whip-pan every two seconds across 30 s.
- Start **and** end frames can coexist with other `@` refs on some UIs — label which still is open, which is close, which is character. Some APIs forbid mixing `frameImages` with `referenceImages` — see `wan_reference_control`.
- I2V: `Slow push in.` or `fixed shot.` Appearance stays in the image.

## Verification

- 2.2 Fun Camera: node move listed in the shot log, prompt has no second camera stack
- FLF: first/last files + aspect match
- Animate: Mix vs Move named; driving clip fps ≥ 16 if required by host
- 3.0: either Camera UI set or a single verbal move, plus cut policy
- One move per clip / shot
