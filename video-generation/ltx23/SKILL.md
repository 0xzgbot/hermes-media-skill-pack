---
name: ltx23
description: "LTX 2.3 (Lightricks) video generation cluster umbrella — prompt engineering, character consistency, camera motion, audio-visual sync, subject motion performance, and technical configuration all under one index."
---

# LTX 2.3 — Cluster Umbrella

All LTX 2.3 skill variants live under `ltx23/`. Start with the master prompt-engineering
reference, then branch into the domain-specific skills.

---

## Core Master Reference

**`ltx23-prompt-engineering-master/`** — Canonical master. 16k chars comprehensive.
Covers: single-paragraph flow, present-tense mandate, temporal language strategies,
prompt-length thresholds, token efficiency, style camouflage for negative prompting,
motion priority, multi-modal input syntax, and 6-stage workflow patterns.
Use when starting any LTX video prompt.

---

## Domain Specialists

| Skill | Focus |
|-------|-------|
| `ltx23/prompt-engineering-master/` | Full master — prompt structure, timing, negative-language strategies |
| `ltx23/character_consistency/` | Character continuity across V2V — locked-scene preservation |
| `ltx23/camera_movement_language/` | Precise camera-motion prompt vocabulary (pan, zoom, track, tilt, crane) |
| `ltx23/audio_visual_sync/` | Native audio + video synchronisation, lip-sync, scoring to picture |
| `ltx23/subject_motion_performance/` | Human action & facial performance direction for T2V/V2V |
| `ltx23/technical_configuration/` | Model variants, sampling modes, LoRA workflow, inference architecture |

---

## Shared Standards

- **Distilled vs Full:** 22B distilled runs locally (4–8 steps, CFG 2–5). 9B distilled is cloud-only.
- **3-Stage Sampling:** Pass 1 (denoise 1.0, composition) → Pass 2 (0.65, motion) → Pass 3 (0.35, detail).
- **Hardware lock:** Camera Arri Alexa 65 + Zeiss Master Prime per project.
- **Max frames:** 257 (multiple of 8 + 1). Avoid auto-aspect modes; set lock-in.

---

## Workflow Pipeline

```
Text prompt / creative brief
  │
  ├── flux2dev_prompt_engineering_master (optional text-to-image reference)
  │
  ├── ltx23-prompt-engineering-master  ← main prompt engineer
  │    └── 6-Element structure: Era/Genre → Subject → Action+Emotion
  │                              → Camera Motion → Lighting → Stylized Tone
  │
  ├── ltx23_* (domain specialists)
  │
  └── comfyui / comfyui-master-control (render)
       └── model arg: ltx-2.3-22b-dev-fp8 (content), ltx-2.3-22b-distilled-lora (style)
