---
name: negative_prompt_library
description: "Apply targeted negatives, not kitchen-sink bans."
version: 1.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [prompt-engineering, media, cinematic]
    category: prompt-engineering
---

# SKILL: Negative Prompt Library
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Comprehensive artifact suppression libraries organized by workflow type. Negative prompts act as soft constraints — the model assigns lower weight to excluded features [^73^]. However, Flux is guidance-distilled and does not natively support negative prompts [^57^]; LTX video uses guardrails rather than traditional negatives [^68^]; while SDXL/z_image rely heavily on negative prompt fields for quality control [^56^][^65^]. This skill provides per-workflow negative strategies.

### TRIGGER KEYWORDS
negative prompt, negative prompt library, artifact suppression, quality negative, bad anatomy negative, what to avoid, suppression vocabulary, SDXL negatives, Flux workaround, guardrails, LTX negative, negative terms

### CORE RULES
- Flux has no native negative prompt — use positive reframing: "correct anatomy" not "no bad anatomy"
- SDXL: minimal negatives beat maximal ones — overloading degrades overall quality
- LTX video uses "guardrails" field, not traditional negatives
- Never use vague negatives: "bad quality" less effective than "blurry, jpeg artifacts, low resolution"
- Model-specific anatomy negatives for SDXL: "bad anatomy, poorly drawn hands, deformed, extra limbs"
- Quality baseline for SDXL: "worst quality, low quality, normal quality" as starter suppression
- Negative prompts degrade gracefully: too many negatives = muddier output, not cleaner

---

### WORKFLOW TYPE: SDXL / z_image / SD 1.5

**Universal Quality Baseline (Use on every generation):**
```
lowres, blurry, jpeg artifacts, watermark, text, signature, cropped, cut off, out of frame, duplicate, mirrored, extra objects, bad anatomy, bad proportions, worst quality, low quality, normal quality, username, artist name, error, missing fingers, missing arms, missing legs, extra digits, fewer digits
```

**Portrait / Character Negatives:**
```
cgi, render, cartoon, painting, asymmetrical eyes, misaligned eyes, disfigured, deformed face, ugly, waxy skin, plastic skin, blurry face, cloned face, mutated hands, fused fingers, too many fingers, long neck, cross-eyed, blank eyes, bad mouth, bad nose, bad teeth, extra nipples, bad knee, extra knee, mutated knee
```

**Photorealistic Negatives:**
```
cartoon, anime, illustration, sketch, 3d render, digital art, painting, drawing, unrealistic, oversaturated, neon colors, fluorescent, harsh lighting, oversharpened, plastic look, doll-like, mannequin, uncanny valley, fake, synthetic
```

**Landscape / Environment Negatives:**
```
blurry background, fog, mist, haze, overcast, flat lighting, oversaturated sky, watermark, text, signature, cropped, out of frame, duplicate elements, mirrored composition, cluttered, busy background, lens flare abuse, chromatic aberration
```

**Architecture / Interior Negatives:**
```
curved walls, leaning buildings, impossible geometry, distorted perspective, fisheye, warped lines, bad proportions, tiny doors, giant windows, floating furniture, cluttered, messy, lowres, blurry, jpeg artifacts, watermark
```

**NSFW / Content Safety Negatives (For family-friendly workflows):**
```
nsfw, nude, naked, topless, bottomless, underwear, lingerie, bikini, cleavage, suggestive, provocative, explicit, gore, blood, violence, mutilation, corpse, death, scary, horror, disturbing
```

---

### WORKFLOW TYPE: FLUX / FLUX2

**Critical Note:** Flux does not natively support negative prompts. Its architecture is guidance-distilled and will throw errors if negative_prompt is passed to standard FluxPipeline [^57^].

**Strategy: Positive Reframing (Replace negatives with positive targets)**

| Instead of This (Negative) | Say This (Positive) |
|---------------------------|---------------------|
| blurry, low quality | sharp focus, crisp detail, high resolution, 8k uhd |
| bad hands, deformed | accurate hands, natural proportions, anatomically correct |
| watermark, text, signature | clean image, no text, unmarked |
| cartoon, anime | photorealistic, realistic photograph, documentary style |
| oversaturated | muted colors, natural color balance, accurate tones |
| cluttered background | clean background, minimal environment, uncluttered |
| distorted face | symmetrical face, natural features, photorealistic skin |

**Flux-Specific Artifact Prevention (Positive Phrasing):**
```
sharp focus, crisp detail, accurate anatomy, natural proportions, symmetrical face, clean composition, no text, no watermark, photorealistic skin texture, realistic lighting, natural color balance, stable composition, coherent architecture
```

**Advanced Flux Negative Hack (ComfyUI / production):**
If using sd-dynamic-thresholding in ComfyUI, you can increase CFG above 1.0 and use negative prompts with Flux [^71^]. Settings reference:
- Mimic mode: Half Cosine Up
- CFG mode: Half Cosine Up
- Interpolate phi: 0.7
- This enables traditional negative prompting but requires careful saturation management [^71^]

---

### WORKFLOW TYPE: LTX VIDEO

**Critical Note:** LTX uses "Guardrails" rather than traditional negative prompts. These are positive-phrased constraints placed in the final clause of the 6-part shot-note [^68^].

**Temporal Stability Guardrails:**
```
no temporal jitter, stable framing, locked tripod, steady camera, no frame skip, no flicker, consistent exposure
```

**Edge & Shimmer Guardrails:**
```
no edge shimmer, no moiré, no aliasing, clean edges, no chromatic aberration, no color banding
```

**Anatomy & Physics Guardrails:**
```
stable anatomy, consistent proportions, no morphing, no floating limbs, grounded physics, natural motion blur
```

**Quality Guardrails:**
```
no blur, sharp throughout, no pixelation, no compression artifacts, clean detail, no noise
```

**LTX Full Guardrail Example:**
```
Guardrails: No temporal jitter, stable horizon, no edge shimmer, no moiré on architecture, consistent character proportions across frames, natural 180° shutter motion blur, no chromatic aberration.
```

---

### NEGATIVE PROMPT PRESETS BY USE CASE

**Use Case: Product Photography**
```
lowres, blurry, jpeg artifacts, watermark, text, signature, cropped, out of frame, duplicate, bad anatomy, bad proportions, worst quality, low quality, cartoon, 3d render, illustration, painting, sketch, unrealistic, plastic look, cheap materials, fingerprints, dust, scratches
```

**Use Case: Fashion / Editorial**
```
lowres, blurry, bad anatomy, bad proportions, worst quality, low quality, normal quality, asymmetrical eyes, misaligned eyes, deformed hands, extra fingers, missing fingers, waxy skin, plastic skin, cloned face, mutated, ugly, duplicate, watermark, text, signature, cropped, out of frame, bad knee, extra knee
```

**Use Case: Food / Culinary**
```
lowres, blurry, jpeg artifacts, watermark, text, signature, bad anatomy, plastic look, synthetic food, cartoon, 3d render, illustration, unappetizing, rotten, mold, flies, dirty kitchen, cluttered background, oversaturated, neon colors, fluorescent lighting
```

**Use Case: Architecture / Real Estate**
```
lowres, blurry, jpeg artifacts, watermark, text, signature, curved walls, leaning buildings, impossible geometry, distorted perspective, fisheye, warped lines, bad proportions, floating furniture, cluttered, messy, cartoon, 3d render, illustration, oversaturated, neon
```

**Use Case: Concept Art / Illustration**
```
lowres, blurry, jpeg artifacts, watermark, text, signature, bad anatomy, bad proportions, worst quality, low quality, photorealistic, 3d render, photograph, realistic, cloned face, mutated, ugly, duplicate, cropped, out of frame, bad hands, deformed hands
```

---

### MODULAR WORKFLOW PATTERN

For API and automated workflows, structure negatives as modular presets [^56^]:

```python
# Pseudocode pattern
base_negative = "lowres, blurry, jpeg artifacts, watermark, text, signature"
targeted_terms = select_by_use_case(use_case)  # portrait, product, landscape, etc.
optional_flags = user_specified_flags  # nsfw filter, style exclusions
negative_prompt = base_negative + targeted_terms + optional_flags
```

**Logging Rule:** Track which negatives fix which artifacts per model. Build an internal library over time [^56^].

---

### EXAMPLE PROMPTS WITH NEGATIVES

**SDXL Portrait:**
> Positive: `masterpiece, best quality, 8k uhd, portrait of young woman, soft smile, freckles, red hair blowing in wind, lavender field at golden hour, warm backlight, shallow depth of field, shot on Canon R5 with 85mm f/1.2`
> Negative: `lowres, blurry, jpeg artifacts, watermark, text, signature, bad anatomy, bad proportions, asymmetrical eyes, misaligned eyes, deformed hands, extra fingers, waxy skin, plastic skin, cloned face, mutated, ugly, cartoon, 3d render, illustration`

**Flux Portrait (No Negative — Positive Reframing):**
> `Sharp focus portrait of young woman with natural skin texture, soft genuine smile, visible freckles, red hair blowing in wind with individual strands crisp, standing in lavender field at golden hour, warm 3500K backlight creating rim light on hair, shallow depth of field, shot on Canon R5 with 85mm f/1.2 lens, photorealistic, anatomically correct, symmetrical face, clean unmarked image`

**LTX Video (Guardrails):**
> `Scene: Lavender field at golden hour. Subject: Young woman walking through rows. Camera/Lens: Steady dolly tracking, 85mm f/1.8. Style: Cinematic portrait, warm amber and violet palette. Motion: Natural walking pace, hair moving with wind. Guardrails: No temporal jitter, stable framing, no edge shimmer, consistent character proportions, natural motion blur.`

---

### TECHNICAL NOTES FOR AI GENERATION
- SDXL: Order matters in negatives — place most critical exclusions first [^65^]
- Flux: Do not pass negative_prompt to standard pipeline; use positive reframing [^57^]
- Flux Advanced: Dynamic thresholding enables negatives but requires CFG tuning [^71^]
- LTX: Guardrails go in the final clause, not a separate negative field [^68^]
- All models: Broad negatives like "bad quality" often reduce character along with defects; use targeted terms [^56^]
