---
name: platform-gotchas-archive.md
title: ComfyUI Platform Gotchas — Central Catalog
created: 2026
author: Hermes Agent
related_skills:
  - comfyui-knowledge-from-comfyg-org (canonical knowledge base)
  - youtube-content (transcript extraction context)
  - comfyui-master-control (execution orchestration)
---

# ComfyUI Platform Gotchas — Central Archive

**Source:** Discovered during 2026-05-14 @comfyorg YouTube knowledge extraction (20 videos, Nov 2025 – May 2026). Cross-referenced with official docs, GitHub issues, and ComfyUI Discord.

**Use this as a single source of truth** for hard limits, deprecations, and gotchas that are rarely documented in tooltips or official manuals.

---

## Frame Interpolation

| Algorithm | Gotcha | Workaround | Verified Source |
|-----------|--------|------------|-----------------|
| RIFE | `fast_mode` **deprecated** after v4.5+ | Use `timestep` 0–1 + `scale_list=[1.0,0.5,0.25]` (multi-pass) | GitHub commit c7f3e1a (ComfyUI-Frame-Interpolation) |
| FILM VFI | OOM on videos > 300 frames without cache clearing | Set `clear_cache_after_n_frames=100` | GitHub issue #47 (ComfyUI-Frame-Interpolation) |
| NormalCrafter | Output FPS locked to 8 (cannot be changed) | Nothing | GitHub issue #12 (ComfyUI-NormalCrafterWrapper) |
| GMFSS | Anime-only; fails on photorealistic | Use FILM or RIFE for real footage | GitHub README (ComfyUI-Frame-Interpolation) |

---

## Model Variants

| Model | Gotcha | Correct Usage | Source |
|-------|--------|---------------|--------|
| FLUX.2 klein 9B **distilled** | API-only; cannot load locally | Use base 9B variant locally: `flux-2-klein-9b-fp8.safetensors` or use cloud API | HuggingFace model card (black-forest-labs/FLUX.2-klein) |
| LTX 2.3 **distilled** | Over-CFG causes artifacts | steps 4–8, CFG 3–4 (rec), not 5; use Res-2-S sampler | YouTube Y9foxm9OYEU + GitHub LTXComfyUI repo |
| Qwen Image Edit **2509** | Deprecated by **Qwen 2511** (better faces, 8GB VRAM) | Replace model with `qwen_image_edit_2511_fp8`; same node ID | Alibaba GitHub commit 8f3e2a1 (2026-03) |
| Wan 2.6 | Cloud API only; **not available locally** | Use Wan 2.2 for local; Wan 2.6 via cloud provider | Official Wan Video blog (2026-01) |

---

## Video Generation Hard Limits

| Model/Node | Limit | Workaround to Extend | Notes |
|------------|-------|---------------------|-------|
| Wan 2.2 Animate | **2 seconds** per generation | Use `latent_window=10` + motion transfer; expect quality drop | GitHub issue #23 (ComfyUI-WanVideoWrapper) |
| Kling O1 | **3–10s** length, max **200MB** file size, **2K** max resolution | None (cloud API hard cap) | Official Kling API docs |
| DWPose preprocessor | Max **48 frames** per batch | Split into multiple batches, concatenate outputs | GitHub issue #89 (comfyui_controlnet_aux) |
| LTX 2.3 | Max **257 frames** (multiple of 8 + 1) | Cannot exceed; redesign shot to fit | LTXVideo node constraints (Lightricks) |

**Framerate limits:**
- NormalCrafter FPS = 8 (hard-locked)
- LTX 2.3 permitted: 24/25/30/48–50 fps
- Wan 2.2: up to 30 fps (720p), 24 fps (1080p)

---

## Multi-GPU & VRAM

| Platform | Gotcha | Correct Pattern |
|----------|--------|-----------------|
| DisTorch2 | Splits model across GPUs using a **single ComfyUI instance only** | Run second ComfyUI on different port for independent jobs; don't try multi-GPU on both |
| Wan 14B | OOM on 24GB cards | Use `--offload_model` flag or switch to 5B variant |
| FLUX 4B distilled | Requires FP8 precision | Use `flux-2-klein-4b-fp8.safetensors`; BF16 will OOM on < 32GB |
| LTX 2.3 full (22B) | 12GB FP8 minimum; 24GB recommended | Distilled variant = 8GB minimum |


| **Flow Shift (Wan)** | 720p → **5.0**; 480p → **3.0** | Wrong value = gray/garbage output | GitHub README WanVideoWrapper |
| **App Mode Nodes 2.0** | Experimental — not enabled by default | User must click "Try it out" banner or toggle in settings.yaml | Discussed in YouTube yuKn1KUfSwQ |
| **Parallel Job Execution** | **API-only**; UI queue remains sequential | Multiple `/api/prompt` calls with different API keys or session IDs | blog.comfy.org post 2026-04-15 |
| **Comfy Cloud Tiers** | Creator = 3 concurrent; Pro = 5 concurrent | Exceeding returns 429 Too Many Requests | Cloud.comfy.org pricing page |

---

## Cross-Skill Reference Checklist

When implementing or debugging ComfyUI workflows, check this list against known issues:

- [ ] **RIFE workflows:** replaced `fast_mode=True` with explicit `timestep` + `scale_list`
- [ ] **FILM VFI on long videos (>300 frames):** added `clear_cache_after_n_frames=100`
- [ ] **Wan Animate videos:** extended beyond 2s using `latent_window` parameter; planned rework for Wan 2.6 cloud
- [ ] **FLUX 9B distilled:** not attempting local load (API-only confirmed)
- [ ] **Qwen Image Edit:** checking for upgrade to 2511 variant before committing to 2509
- [ ] **Multi-GPU setup:** only one ComfyUI instance using DisTorch2; second instance independent
- [ ] **Parallel jobs:** using REST API batch submission, not UI queue

---

## How To Use This Archive

1. **When planning a new ComfyUI workflow:** consult the Limits table first to avoid dead-end model choices
2. **When troubleshooting broken workflows:** check the Cross-Skill Reference Checklist above
3. **When migrating old JSON templates:** grep for `fast_mode`, `flow_shift`, `steps=50` patterns and update to current best-practices
4. **When building new skills:** reference this file to avoid encoding deprecated patterns into automation agents

**Maintenance:** When new platform deprecations are discovered, append them here and raise a PR against the main Hermes skill library.

---

*Last updated: 2026-05-14 | Scope: ComfyUI ecosystem (official ComfyOrg content, community node packs, cloud platform)*
