---
name: image-generation-workflow
description: Use when generating or refining images with AI.
version: 1.0.0
author: Hermes Agent community
created: 2026
tags: [image-generation, ai-art, flux, sdxl]
---

# Image Generation Workflow — General Purpose

## Prompt Structure for Image Models

### Text-to-Image Formula
```
[Subject description], [action/pose], [setting/environment], 
[camera angle/lens], [lighting], [style/aesthetic], 
[quality tokens]
```

**Example:**
"A weathered fisherman mending nets at dawn, standing on a wooden dock in a foggy harbor, low angle shot from water level, soft diffused morning light with hints of orange through fog, photorealistic documentary photography style, sharp focus, natural colors"

### Quality Token Sets by Model Type

**Photorealistic:**
- "photorealistic," "8k resolution," "highly detailed," "sharp focus"
- "shot on [camera], [lens]" — adds camera-specific characteristics
- "natural lighting," "film grain," "color graded"

**Illustration/Art:**
- "digital painting," "concept art," "illustrated by [artist style]"
- "vibrant colors," "detailed background," "artstation trending"
- Specify medium: "watercolor," "oil painting," "pencil sketch," "vector art"

**3D/Render:**
- "3D render," "octane render," "ray tracing," "global illumination"
- "unreal engine 5," "cinematic lighting," "volumetric fog"
- Material descriptions: "matte black metal," "translucent glass," "brushed aluminum"

## Image-to-Image Workflow

### When to Use img2img vs txt2img
| Scenario | Approach | Why |
|----------|----------|-----|
| Starting from scratch | txt2img | Full creative control |
| Refining composition | img2img (low denoise 0.3-0.5) | Keep structure, change details |
| Style transfer | img2img (medium denoise 0.5-0.7) | Apply new aesthetic to existing layout |
| Upscaling/enhancing | img2img (high denoise 0.6-0.8) + upscale model | Add detail while preserving composition |

### Denoising Strength Guide
```
0.0 - 0.2: Minimal change, minor tweaks only
0.3 - 0.5: Moderate changes, keep core structure
0.5 - 0.7: Significant changes, new style/elements
0.7 - 0.85: Major transformation, loose reference
0.85+: Almost entirely new image, reference is inspiration only
```

## Batch Generation Patterns

### Grid Testing (A/B Variants)
Generate multiple variants systematically by changing ONE variable at a time:
```
Base prompt + [variant A] → Image 1
Base prompt + [variant B] → Image 2  
Base prompt + [variant C] → Image 3
```
This isolates which element drives the quality difference.

### Iterative Refinement Loop
```
1. Generate base image (txt2img)
2. Evaluate against criteria
3. Identify specific issues (too dark, wrong angle, poor composition)
4. Adjust prompt for ONE issue
5. Use img2img with low denoise to apply fix
6. Repeat until acceptable
```

## Model Selection Guide

| Task | Best Models | Notes |
|------|------------|-------|
| Photorealistic portraits | Flux.1, SDXL | Best anatomy and skin rendering |
| Product photography | SDXL, Flux.1 | Clean backgrounds, sharp detail |
| Concept art / illustration | Midjourney-style models | Creative freedom, artistic styles |
| Architectural visualization | SDXL + ControlNet | Precise geometry control |
| Upscaling/enhancing | Real-ESRGAN, SwinIR | 2x-4x upscaling with detail recovery |

## Common Image Generation Issues & Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Blurry/soft output | Low resolution setting, high denoise in img2img | Use higher base res (1024+), lower denoise |
| Wrong anatomy (hands, faces) | Model limitation with complex structures | Simplify composition, use inpainting to fix |
| Inconsistent style across batch | Random seed variation too high | Fix seed for consistency, or accept randomness as feature |
| Text in image is garbled | Most models can't render text well | Add text in post-processing; avoid asking model to render it |
| Unwanted artifacts at edges | Model extrapolation limits | Use tighter framing, add "clean edges" to prompt |

## Post-Processing Pipeline

After generation, run through:
1. **Upscale** — 2x or 4x with dedicated upscaler model
2. **Color correction** — Adjust exposure, contrast, saturation to match brand/style guide
3. **Cropping/composition** — Final framing for intended use (social media, print, web)
4. **Quality check** — Review at full resolution for artifacts, noise, inconsistencies
