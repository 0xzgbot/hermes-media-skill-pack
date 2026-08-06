# SKILL: Quality Token Sets
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Model-specific quality token combinations that prime the diffusion model for high-fidelity output. These are not magic words — they are statistical anchors that shift the generation distribution toward high-detail, well-composed outputs. Each model family has distinct token vocabularies that actually move the needle.

### TRIGGER KEYWORDS
quality tokens, quality boost, masterpiece, best quality, high quality, 4K, 8K, photorealistic, sharp focus, detailed, quality prompt, production quality, cinematic quality, professional quality

### CORE RULES
- Quality tokens are model-specific: "masterpiece, best quality" works for SD 1.5/SDXL; less impact on Flux
- Flux responds to descriptive quality terms: "photorealistic", "sharp focus", "professional photography"
- Avoid over-stacking quality tokens — diminishing returns after 3–4 terms
- Photorealism tokens: "photorealistic, photographic, DSLR quality, sharp focus, natural light"
- Cinematic tokens: "cinematic, film still, movie quality, professional cinematography"
- Illustration quality tokens: "highly detailed illustration, concept art, production art quality"
- Place quality tokens at end of prompt — they reinforce, not lead

---

### SDXL / z_image / SD 1.5 QUALITY SETS

**Universal Quality Anchor (Front-Load These):**
```
masterpiece, best quality, ultra-detailed, 8k uhd, highres, absurdres
```

**Photorealistic Quality Set:**
```
masterpiece, best quality, photorealistic, realistic, 8k uhd, raw photo, DSLR, highres, sharp focus, crisp detail, lifelike texture, professional photography, studio quality
```

**Illustration / Anime Quality Set:**
```
masterpiece, best quality, ultra-detailed, intricate details, highres, official art, pixiv, artstation, deviantart, highly detailed background, perfect composition, vibrant colors
```

**Pony Diffusion Model Quality Set (Critical):**
Pony uses a unique scoring system as quality classifier [^69^]:
```
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_anime, source_pony, source_furry
```
- `score_9` = highest quality anchor
- `score_4_up` = minimum quality floor
- `source_` tags specify content domain
- Negative: `score_1, score_2, score_3, score_4, score_5, score_6, bad quality, watermark, signature, low quality, low-res` [^69^]

**3D Render Quality Set:**
```
masterpiece, best quality, octane render, unreal engine 5, 3d render, ray tracing, global illumination, subsurface scattering, physically based rendering, 8k uhd, sharp focus
```

**Oil Painting / Classical Quality Set:**
```
masterpiece, best quality, oil on canvas, museum quality, fine art, masterwork, highly detailed, intricate brushwork, rich pigment, gallery lighting, 8k uhd scan
```

---

### FLUX / FLUX2 QUALITY SETS

**Critical Note:** Flux does not need traditional quality tokens as heavily as SDXL. Instead, weave quality descriptors into the subject and technical spec clauses [^57^]. However, these positive-framed terms reinforce fidelity:

**Flux Photorealistic Set:**
```
sharp focus, crisp detail, photorealistic, anatomically correct, natural proportions, realistic skin texture, professional photography, 8k resolution, unmarked clean image, accurate lighting, true-to-life colors
```

**Flux Illustration Set:**
```
highly detailed, intricate linework, vibrant accurate colors, clean composition, professional illustration, gallery quality, precise rendering, deliberate brushwork, masterful technique
```

**Flux Technical Spec Integration (Most Effective):**
Rather than tacking quality tokens at the end, integrate into technical clause:
```
...shot on [camera] with [lens], 8k resolution, sharp focus throughout, professional color grading, unmarked clean image
```

**Flux Pro Ultra (4MP Native) [^58^]:**
For Flux 1.1 Pro Ultra, specify resolution directly:
```
...4k resolution, highly detailed, crisp at 100% zoom, pixel-perfect detail
```

---

### LTX VIDEO QUALITY SETS

**Temporal Quality Anchors:**
```
30fps, smooth motion, stable camera, professional cinematography, broadcast quality, no jitter, no flicker, consistent exposure
```

**Spatial Quality Anchors:**
```
4k resolution, sharp throughout frame, clean edges, no moiré, no aliasing, professional lens, high bitrate look, cinematic compression quality
```

**Motion Quality Anchors:**
```
natural motion blur, 180° shutter equivalent, constant speed, smooth pan, steady tracking, professional camera movement, cinematic pacing
```

**LTX Combined Quality Block:**
```
4k cinematic video, 30fps, smooth stable motion, professional camera work, sharp detail throughout, clean edges, natural motion blur, broadcast quality, no temporal artifacts
```

---

### TESTED COMBINATIONS BY WORKFLOW

**SDXL Photorealistic Portrait (Tested):**
```
masterpiece, best quality, photorealistic, 8k uhd, raw photo, DSLR, sharp focus, crisp detail, lifelike texture, professional photography, [SUBJECT], [ACTION], [ENVIRONMENT], [LIGHTING], shot on Sony A7IV with 85mm f/1.8
```

**SDXL Anime Character (Tested):**
```
masterpiece, best quality, ultra-detailed, intricate details, official art, pixiv, artstation, highly detailed background, perfect composition, vibrant colors, 1girl, [DESCRIPTION], [CLOTHES], [POSE], [BACKGROUND]
```

**Pony Diffusion Character (Tested):**
```
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, source_anime, BREAK, 1girl, [DESCRIPTION], [CLOTHES], [POSE], [BACKGROUND], masterpiece, best quality
```

**Flux Photorealistic (Tested):**
```
Sharp focus photorealistic [SUBJECT] with natural skin texture and accurate anatomy, [ACTION], [ENVIRONMENT], [LIGHTING], shot on [CAMERA] with [LENS], 8k resolution, professional color grading, clean unmarked image, true-to-life colors
```

**LTX Cinematic Video (Tested):**
```
Scene: [ENVIRONMENT]. Subject: [SUBJECT + ACTION]. Camera/Lens: [MOVEMENT + LENS]. Style: 4k cinematic, [STYLE]. Motion: 30fps, smooth stable [MOTION], natural motion blur. Guardrails: No jitter, no shimmer, sharp throughout.
```

---

### QUALITY TOKEN EFFICIENCY RULES

1. **Front-load for SDXL:** Quality tokens at the very beginning prime the model [^69^]
2. **Weave for Flux:** Integrate quality into subject and technical clauses; end-tacking is weak [^57^]
3. **Be specific, not vague:** "Sharp focus on eyes" > "high quality"
4. **Avoid redundancy:** "masterpiece, best quality, ultra high quality, super quality" — pick 2–3 strongest
5. **Match domain:** Anime tokens for anime models; photo tokens for photorealistic models
6. **Test and log:** Same prompt with/without quality tokens; measure difference [^56^]

---

### EXAMPLE PROMPTS

**SDXL + Quality Set (Fantasy):**
> `masterpiece, best quality, ultra-detailed, intricate details, 8k uhd, highres, official art, artstation, epic fantasy landscape of floating islands above crystalline ocean, waterfalls cascading into clouds, bioluminescent flora, twin moons in twilight sky, volumetric lighting, digital painting by Greg Rutkowski, perfect composition, vibrant saturated colors, highly detailed background`

**Flux + Quality Integration (Product):**
> `Razor-sharp product photography of titanium mechanical watch with visible brushing marks on case and sapphire crystal clarity, floating against pure black void, single spotlight creating precise specular highlights, macro detail of crown threads and dial indices, 8k resolution, professional studio lighting, clean unmarked image, true-to-life color accuracy, shot on Phase One with 120mm macro`

**LTX + Quality Block (Documentary):**
> `Scene: Himalayan village at dawn. Subject: Elderly monk ringing temple bell. Camera/Lens: Static tripod-locked wide shot, 24mm f/2.8. Style: 4k documentary cinematography, warm amber and cool shadow palette. Motion: 30fps, single bell swing in slow motion, natural 180° shutter blur. Guardrails: No jitter, no flicker, sharp throughout, stable exposure.`

---

### TECHNICAL NOTES FOR AI GENERATION
- SDXL: "masterpiece, best quality" is statistically validated as effective priming
- Pony: Never omit score_9 through score_4_up; these are model-native quality classifiers [^69^]
- Flux: Quality tokens work better as woven descriptors than standalone prefixes [^57^]
- LTX: Temporal quality tokens (30fps, smooth motion) are as important as spatial ones [^68^]
- All models: 3–5 quality tokens is the sweet spot; beyond 10 tokens yields diminishing returns
