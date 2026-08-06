# SKILL: Photometric Overexposure
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting overexposure in AI-generated imagery. Unlike camera overexposure (where RAW data can be recovered), AI overexposure represents missing data — the model never rendered detail in blown areas [^77^]. Recovery requires regeneration with lighting-aware prompts rather than post-processing. This skill provides prevention vocabulary, detection signals, and fix strategies.

### TRIGGER KEYWORDS
overexposure, blown highlights, white blowout, too bright, burned out, white out, overlit, highlight clipping, bright white area, lost detail, exposure problem, washed out, bright light problem

### CORE RULES
- AI overexposure cannot be fixed in post — the detail was never generated; regenerate with fix vocabulary
- Prevention: specify "controlled exposure, highlights retained, no blown areas"
- Name the light source and reduce its intensity: "soft ambient light, no harsh direct source"
- Specify detail preservation: "skin texture visible in bright areas, fabric detail in highlights"
- Bright clothing on bright background = highest risk: force contrast between them
- For windows/sky in frame: "correctly exposed window view, no blown sky, interior and exterior balanced"
- SDXL negative prompt: "overexposed, blown highlights, washed out, white clipping"

---

### DETECTION SIGNALS

**Visual Indicators:**
- **Blown Highlights:** Pure white areas with zero texture (skin, sky, fabric, metal)
- **Channel Clipping:** Single color channel (usually red in skin) clips, leaving yellow/green cast [^76^]
- **Grey Recovery Failure:** Darkening blown areas produces muddy grey rather than recovered detail [^76^]
- **Halo/Bloom:** Overexposed edges bleed into surrounding areas
- **Flat Skin:** Overexposed skin loses pore texture, appearing waxy or plastic
- **Lost Detail:** Windows, light sources, reflective surfaces become pure white voids

**Prompt-Level Causes:**
- Vague brightness requests: "bright photo", "well-lit", "high-key"
- Unspecified light source: Model defaults to maximum brightness
- Conflicting light descriptors: "dramatic lighting" + "bright studio" = unpredictable exposure
- Missing shadow anchor: No dark values specified, model pushes everything bright

---

### PREVENTION VOCABULARY

**Light Quality Specification (Primary Prevention):**
```
soft light, diffused lighting, natural window light, cinematic lighting, warm fill light, gentle ambient, overcast softbox, indirect bounce light
```
[^77^][^78^]

**Avoid These High-Risk Terms:**
```
bright studio light, direct sunlight, high-key lighting, harsh flash, blown-out highlights, overexposed, white background (Flux dev) [^72^]
```

**Shadow Anchor (Balance Prevention):**
```
rich shadows, deep blacks, contrasty, chiaroscuro, dramatic shadows, dark background, moody lighting
```

**Exposure Control Phrases:**
```
properly exposed, balanced exposure, no blown highlights, detail in highlights, detail in shadows, full dynamic range, Zone System exposure
```

---

### FIX STRATEGIES

**Strategy 1: Regenerate (Recommended for AI Images)**
- AI overexposure has no hidden data to recover [^77^]
- Post-processing darkening creates "grey mud" — flat, unnatural patches
- Single-click regeneration with lighting-aware prompt is faster and higher quality [^77^]

**Strategy 2: Prompt Refinement**
Replace vague brightness with specific light quality:
| Instead Of | Use |
|------------|-----|
| "bright photo" | "soft diffused window light" |
| "well-lit studio" | "softbox at 45 degrees, 2:1 ratio" |
| "high-key portrait" | "clean white background with gentle gradient falloff" |
| "dramatic bright light" | "Rembrandt lighting with controlled key" |
| "sunny day" | "golden hour with warm side-light and cool shadows" |

**Strategy 3: Negative Prompt / Guardrail**
- SDXL: `overexposed, blown-out highlights, harsh light, glare, clipped highlights`
- Flux (positive reframing): `balanced exposure, detail in all tonal ranges, no clipped whites`
- LTX Guardrails: `no overexposure, stable exposure across frames, detail in highlights`

**Strategy 4: The HDR Mimic**
- Specify both highlight and shadow detail:
  - `detail in bright sky and shadow under chin`
  - `window view visible through glass, interior properly exposed`
  - `bright sun with visible corona, shadow detail preserved`

**Strategy 5: Lighting Ratio Specification**
- Specify key-to-fill ratio to prevent everything going bright:
  - `2:1 lighting ratio` = moderate contrast
  - `4:1 lighting ratio` = dramatic but controlled
  - `8:1 lighting ratio` = high contrast, deep shadows

---

### MODEL-SPECIFIC APPROACHES

**Flux / Flux2:**
- Never use "white background" in Flux dev — causes fuzzy overexposure [^72^]
- Use "clean light gray background" or "minimal studio backdrop" instead
- Weave exposure control into subject clause: `properly exposed portrait with detail in highlights`
- No negative prompts; rely on positive specification

**SDXL / z_image:**
- Use negative: `overexposed, blown-out highlights, harsh light, glare, clipped whites, washed out`
- Specify light source explicitly: `soft window light from camera left`
- Include shadow detail: `rich shadows, deep blacks`

**LTX Video:**
- Overexposure often drifts between frames
- Guardrail: `stable exposure across all frames, no highlight clipping, detail preserved in bright areas`
- Specify 180° shutter for natural motion blur without overexposure

---

### EXAMPLE FIX PROMPTS

**Fix: Overexposed Portrait (Flux):**
> `Properly exposed portrait of CEO with soft diffused studio lighting, detail visible in white shirt collar, rich shadows under chin, balanced exposure with no clipped highlights, warm fill light at 1:2 ratio, photorealistic, professional headshot`

**Fix: Blown Sky (SDXL):**
> Positive: `Landscape with detail in bright clouds, blue sky with texture, balanced exposure, graduated neutral density filter effect, rich shadows in foreground`
> Negative: `overexposed sky, blown-out clouds, washed out, clipped highlights, harsh light`

**Fix: Overexposed Product (LTX):**
> `Scene: White product on gray seamless. Subject: Smartphone. Camera/Lens: Static, even softbox lighting. Style: Clean product video. Motion: None. Guardrails: No overexposure, detail in white surfaces, stable exposure, no highlight clipping.`

---

### DETECTION CHECKLIST
- [ ] Pure white areas have visible texture?
- [ ] Skin has pore detail, not waxy flatness?
- [ ] Sky/clouds have tonal variation?
- [ ] Light sources have shape, not just white blobs?
- [ ] Shadows are present and detailed?
- [ ] No channel-specific color casts in recovered areas?
- [ ] Overall image has full tonal range from black to white?

---

### TECHNICAL NOTES FOR AI GENERATION
- AI overexposure is fundamentally different from camera overexposure — there is no RAW data to recover [^77^]
- Post-processing darkening of AI-blown highlights produces grey mud, not detail [^76^]
- Prevention through lighting-aware prompts is 10× more effective than post-fixing
- Always specify shadow detail alongside highlight detail for balanced exposure
- In video, overexposure often drifts frame-to-frame; use exposure stability guardrails
