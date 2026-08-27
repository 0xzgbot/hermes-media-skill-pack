---
name: workflow_flux2_text_to_image
version: 2.0
description: "Run Flux.2 text-to-image on ComfyUI, FAL as fallback."
references:
  - references/fal-runtime-path.md
---
# Flux.2 Text-to-Image Workflow Reference

ComfyUI + comfy-cli for production Flux.2 text-to-image execution, with FAL image_generate fallback when ComfyUI is offline.

## Canonical Workflow: ComfyUI Local or Cloud

Run via `comfy-cli` lifecycle + `run_workflow.py` execution scripts.

| Path | Server | Auth | Notes |
|------|--------|------|-------|
| ComfyUI Local | 127.0.0.1:8188 | None | Install via `comfy-cli install --nvidia` |
| ComfyUI LAN | <ip>:8188 | None | May be remotely accessible |
| Comfy Cloud | cloud.comfy.org | API key | Paid tier required for /api/prompt |

```bash
# Health check
python3 scripts/health_check.py
python3 scripts/check_deps.py workflow_api.json

# Run
python3 scripts/run_workflow.py --workflow workflow_api.json --args '{"prompt":"..."}'
```

## Fallback Path: FAL image_generate (Nous Subscription)

When ComfyUI **[SERVER:OFFLINE]**: `image_generate` provides direct Flux.2 access with no local GPU needed.

**Capabilities (confirmed 2026-05-18):**
- Model: FAL-routed (not user-selectable)
- Aspect ratios: `landscape`, `portrait`, `square` (tool-validated)
- Returns: HTTP URL to generated PNG
- Backend handles: steps ~45–50, guidance ~7.5, stylize 150–200
- Negative prompts: embedded in main prompt text only

**When to use:**
| Situation | Path |
|-----------|------|
| ComfyUI UP + models installed | ComfyUI (`run_workflow.py`) |
| ComfyUI DOWN, Nous active | `image_generate` (FAL) |
| img2img / controlnet / LoRA | ComfyUI only |
| Batch / sweep | `image_generate` + parallel calls |

See `references/fal-runtime-path.md` for the full version log and backend difference matrix.