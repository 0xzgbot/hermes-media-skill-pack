# SKILL: FLUX.2 Dev Prompt Engineering Master
## Version: 1.0 | Hermes Agent Universal Flux2 Prompt Optimization Doctrine

---

### DESCRIPTION
The master reference for FLUX.2 Dev prompt engineering across all domains. This skill distills the deep research on FLUX.2 Dev's 32B guidance-distilled architecture, token-weight hierarchy, optimal parameter configurations, JSON structured prompting, and the positive-only constraint system into a single authoritative reference. Use this skill as the foundation before invoking any domain-specific FLUX.2 Dev skill. Covers prompt length optimization, camera specification syntax, color control, text-in-image rendering, multi-language support, and the complete anti-pattern catalog.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Model Architecture (What Makes It Different):**
- **Parameters:** 32 billion (vs. FLUX.1's 12B) — significantly higher capacity for detail adherence
- **Architecture:** Rectified flow transformer + Mistral-3's 24B vision-language model
- **Guidance:** Distilled — runs guidance scale 3–5 natively (not 7–12 like SDXL)
- **Negatives:** No native negative prompt support — all suppression must be positive-framed
- **Prompt Encoding:** Dual encoder (T5 + CLIP) — natural language descriptions outperform keyword lists
- **Token Limit:** T5 encoder supports 512 tokens; FLUX.2 Dev summarizes prompts >200 words internally
- **Weight Syntax:** Does NOT support `(word:1.2)`, `++`, `--`, or any bracket-weight syntax
- **Resolution:** Native up to 4MP (Pro), 1024–1536 base recommended for Dev
- **Text Rendering:** Best-in-class open model — quotes, font specification, placement all functional
- **HEX Support:** Direct hex color codes followed with high fidelity when tied to elements
- **Multi-Language:** Native multilingual understanding without translation

**The Token-Weight Hierarchy (Critical):**
FLUX.2 Dev applies extreme early-token weighting. The first 10–15 tokens determine 60%+ of the output character.

| Token Position | Weight | What to Place | Example |
|---------------|--------|---------------|---------|
| **1–5** | Maximum (≈35%) | Subject identity + scale | "Titanium smartwatch" / "Wide establishing shot" |
| **6–10** | Very High (≈20%) | Key descriptor / action | "floating at angle" / "lone rider on horseback" |
| **11–20** | High (≈20%) | Secondary subject detail | "matte black ceramic bezel" / "crossing desert plain" |
| **21–40** | Moderate (≈15%) | Environment / context | "against clean neutral gray" / "at golden hour" |
| **41–70** | Low (≈7%) | Technical / camera | "Shot on Phase One IQ4" / "85mm at f/1.4" |
| **71+** | Minimal (≈3%) | Atmosphere / mood | "melancholic twilight atmosphere" |

**Optimal Prompt Length by Use Case:**

| Length | Word Count | Use Case | Risk |
|--------|-----------|----------|------|
| **Ultra-Short** | < 15 words | Style exploration, quick concepts | Model hallucinates extensively |
| **Short** | 15–30 words | Drafts, mood boards, rapid iteration | Limited control over specifics |
| **Sweet Spot** | 30–80 words | Most production work, ideal balance | Optimal control with no summarization |
| **Long** | 80–120 words | Complex scenes, multiple subjects | Minor summarization risk |
| **Too Long** | 120–200 words | Detailed architectural, multi-character | Internal summarization drops elements |
| **Excessive** | 200+ words | Everything specified | FLUX.2 compresses heavily; details lost |

**Guidance Scale Calibration:**

| Scale Range | Effect | Best For | Risk |
|-------------|--------|----------|------|
| **2.5–3.0** | High creative freedom, loose adherence | Artistic exploration, happy accidents | Subject drift, ignored details |
| **3.0–3.5** | Balanced creative freedom | Mood shots, atmospheric work | Minor detail loss acceptable |
| **3.5–4.0** | Recommended default for most work | Cinematic stills, portraits, editorial | Sweet spot for most domains |
| **4.0–4.5** | Strong adherence, slight saturation | Product photography, architecture, technical | Slight over-saturation possible |
| **4.5–5.0** | Maximum adherence, highest saturation | Brand assets, HEX accuracy critical | Risk of posterization, plastic skin |
| **5.0–7.0** | Extreme adherence, over-processed | NOT RECOMMENDED for FLUX.2 Dev | Over-saturated, artifact-heavy |
| **7.0+** | Broken — do not use | Never | Severe over-saturation, doubled elements |

**Step Count Optimization:**

| Steps | Quality | Speed | Recommended Use |
|-------|---------|-------|-----------------|
| **16–20** | Draft quality, soft detail | Very fast | Concept exploration, composition testing |
| **20–24** | Acceptable, some softness | Fast | Rapid iteration, style matching |
| **24–28** | Good quality, adequate detail | Moderate | Quick production, social media |
| **28–35** | Production quality, crisp detail | Standard | Final assets, most professional work |
| **35–40** | Maximum detail, grain fidelity | Slower | Macro, texture, technical documentation |
| **40–50** | Diminishing returns | Slowest | Only when micro-detail is paramount |

---

### THE POSITIVE-ONLY CONSTRAINT SYSTEM

FLUX.2 Dev does not support negative prompts natively. Every exclusion must be reframed as a desired positive quality.

**Universal Positive Reframe Dictionary:**

| Problem Area | Negative (Never Use) | Positive Reframe (Always Use) |
|-------------|---------------------|------------------------------|
| **Blur** | not blurry, no blur | sharp focus, crisp detail, tack-sharp |
| **Low quality** | not low quality, no low quality | high fidelity, detailed rendering, precise execution |
| **Anatomy errors** | no extra fingers, bad anatomy | natural human anatomy, correct digit count, balanced proportions |
| **Text/watermark** | no text, no watermark | clean image, no visible text, pure visual content |
| **Plastic skin** | not plastic, no AI look | natural skin texture, visible pores, organic surface |
| **Over-saturation** | not oversaturated | natural color balance, realistic saturation, true-to-life tones |
| **Artifacts** | no artifacts, no distortion | clean rendering, coherent geometry, stable composition |
| **White background issues** | not white background | clean neutral backdrop, minimal environment, light gray seamless |
| **Floating objects** | not floating | grounded on surface, natural contact shadow, weight and mass |
| **Conflicting styles** | not mixed styles | cohesive visual approach, unified aesthetic, consistent style |

**The Guardrails Clause (Append to Every Prompt):**
```
natural proportions, coherent spatial logic, realistic light behavior,
authentic material texture, stable composition, accurate perspective,
no artificial smoothing, no impossible geometry, no conflicting light sources
```

---

### PROMPT ARCHITECTURE

**The Universal FLUX.2 Dev Template:**
```
[Subject + identity] — FIRST 5 TOKENS, MAXIMUM WEIGHT
[Action / pose / state] — Tokens 6–10, very high weight
[Key detail / feature] — Tokens 11–20, high weight
[Environment / setting] — Tokens 21–40, moderate weight
[Camera + lens + aperture] — Tokens 41–60, moderate weight
[Lighting: source + direction + quality + color temp] — Tokens 61–80, low weight
[Style / film stock / era] — Tokens 81–100, low weight
[Atmosphere / effects / grain] — Tokens 101–120, minimal weight
[Guardrails clause] — Final tokens, minimal but present
```

**JSON Structured Prompt Template (For Complex Scenes):**
```json
{
  "scene": "Overall environment description",
  "subjects": [
    {
      "type": "subject_category",
      "description": "Detailed subject description",
      "position": "foreground/midground/background",
      "color": "#HEXCODE"
    }
  ],
  "style": "Photographic or artistic approach",
  "colors": {
    "palette": ["#HEX1", "#HEX2", "#HEX3"],
    "dominant_hue": "Descriptive color name",
    "color_temperature": "XK"
  },
  "lighting": {
    "key_light": "Source, direction, quality",
    "fill_ratio": "Key:Fill ratio",
    "color_temp_k": "NumberK",
    "practical_sources": "Visible light sources in scene"
  },
  "camera": {
    "lens": "Focal length and type",
    "aperture": "f-stop",
    "shot_type": "Wide/medium/close-up/etc.",
    "angle": "Eye-level/low/high/Dutch"
  },
  "atmosphere": {
    "haze": "None/volumetric/light",
    "grain": "Fine/medium/heavy",
    "effects": "Lens flare, chromatic aberration, vignette"
  }
}
```

---

### ADVANCED TECHNIQUES

**1. The Camera-First Photorealism Hack**
- Principle: Camera specifications trigger FLUX.2's photorealistic rendering pipeline more reliably than quality tokens.
- Technique: Always include "Shot on [specific camera], [lens] at f/[aperture]" in the first half of the prompt.
- Comparison:
  - Weak: "Photorealistic portrait of a woman, high quality, detailed"
  - Strong: "Portrait of a woman, shot on Canon EOS R5 with 85mm f/1.2 at f/2.0, detailed"
- Why it works: FLUX.2 was trained on image-caption pairs where camera EXIF data frequently appeared. Camera names are strong conditioning tokens.

**2. The Behavioral Light Description**
- Principle: Describing what light DOES outperforms naming what light IS.
- Technique: Replace lighting names with behavioral descriptions.
- Comparison:
  - Weak: "Golden hour lighting, warm tones"
  - Strong: "Warm golden sunset light streaming through tall windows, casting long shadows across hardwood floor, dust particles visible in light beam"
- Why it works: FLUX.2's VLM backbone processes scene descriptions as spatial arrangements. Behavioral light descriptions encode spatial relationships.

**3. The HEX Color Lock**
- Principle: FLUX.2 follows HEX codes with high fidelity when properly formatted.
- Technique: Tie HEX to specific elements, not used standalone.
- Comparison:
  - Weak: "#FF6B35 and #004E89"
  - Strong: "Running shoe with primary upper in exact color #FF6B35, accent swoosh in #004E89, white midsole"
- Why it works: HEX codes without element binding are interpreted as general color mood. Element binding creates precise color assignment.

**4. The Text-in-Image Precision Method**
- Principle: FLUX.2 has best-in-class text rendering among open models.
- Technique: Use quotation marks, specify placement, define typography.
- Rules:
  - Always quote exact text: "The sign reads 'OPEN LATE'"
  - Specify font separately: "in bold sans-serif font"
  - ALL CAPS in prompt = ALL CAPS in image
  - Shorter text = more accurate: 2–5 words most reliable
  - Placement: "At top of poster," "Centered on banner"
  - Clean background behind text improves accuracy significantly

**5. The Three-Pass Iteration Protocol**
- Pass 1 — Foundation: Basic prompt with core subject, camera, and light. Generate at 20 steps, guidance 3.5.
- Pass 2 — Refinement: Analyze output. Add missing details. Adjust light direction. Generate at 28 steps, guidance 4.0.
- Pass 3 — Polish: Fine-tune atmosphere, add grain/effects, perfect color. Generate at 35 steps, guidance 4.0–4.5.
- Cost efficiency: Pass 1 uses fast generation. Only Pass 3 uses maximum quality settings.

**6. The Multi-Language Native Prompt**
- Principle: FLUX.2 understands prompts in multiple languages without translation.
- Technique: Write naturally in your native language maintaining the same structure.
- Examples work in: French, German, Spanish, Italian, Portuguese, Dutch, Russian, Chinese, Japanese, Korean, Thai, Arabic, Hindi
- Structure remains: Subject → Action → Style → Context regardless of language
- Cultural references function natively: "Seoul rooftop garden at sunset" works in Korean with identical visual output

**7. The Temporal Consistency Chain**
- Principle: When generating multiple related images (storyboard, campaign, lookbook), consistency tokens lock visual identity.
- Technique: Include a scene identifier and locked parameters in every prompt:
```
Scene 3B — Interior Night. Camera locked: ARRI Alexa 65, Cooke S4/i 50mm, Kodak Vision3 500T.
Subject: [varies per shot]. Light: [varies within 200K]. Atmosphere: [consistent haze level].
```
- Why it works: FLUX.2 processes scene identifiers as contextual anchors. Repeating locked parameters reinforces conditioning.

---

### ANTI-PATTERN CATALOG

**Forbidden Patterns in FLUX.2 Dev Prompting:**

| Anti-Pattern | Why It Fails | The Fix |
|-------------|-------------|---------|
| **"Cinematic" standalone** | Too vague; FLUX.2 defaults to generic movie still | Replace with specific film stock + lens + aspect ratio |
| **"Beautiful," "stunning," "amazing"** | Quality judgment words carry zero visual information | Replace with specific technical parameters |
| **"White background"** | Causes fuzziness and quality degradation in Dev | Use "clean neutral studio environment" or "light gray seamless" |
| **Keyword soup** | "Woman, dress, red, beautiful, high quality, 8k" — FLUX.2 processes natural language, not keyword lists | Write in complete descriptive sentences |
| **Midjourney parameter flags** | `--ar 16:9`, `--v 6`, `--no text` are ignored and waste tokens | Describe composition: "2.39:1 aspect ratio composition" |
| **Prompt weights `(word:1.2)`** | FLUX.2 does not support weight syntax; may confuse model | Use natural emphasis: "prominently featuring," "especially detailed" |
| **Conflicting light descriptions** | "Bright midday sun AND moody dark shadows" — FLUX.2 averages into muddy neutral | Pick ONE lighting scenario; describe it thoroughly |
| **Burying subject at end** | "In a beautiful garden with flowers and sunlight, a woman sits" — subject gets minimal weight | Lead with subject: "A woman sits in a garden..." |
| **Abstract style without anchor** | "Make it look professional" provides no visual instruction | Anchor to specific camera: "Shot on Phase One IQ4, Schneider 80mm" |
| **Negatives in positive-only model** | "No extra fingers" can paradoxically trigger finger artifacts | Reframe: "Natural hand anatomy with correct five-finger count" |
| **Overloading >200 words** | FLUX.2 summarizes long prompts; details get compressed or dropped | Keep to 30–80 words; use JSON for complex multi-element scenes |
| **Generic quality tokens** | "8K, ultra HD, highly detailed, masterpiece" — FLUX.2 ignores these | Replace with specific detail descriptors: "Individual hair strands visible" |

---

### EXAMPLE PROMPTS

**Weak vs. Strong Comparison (Portrait):**

❌ Weak:
> Beautiful portrait of a woman, high quality, detailed, professional photography, 8k, stunning

✅ Strong:
> Portrait of a 35-year-old woman with auburn hair, shot on Canon EOS R5 with 85mm f/1.2 at f/2.0, soft window light from camera-left creating gentle Rembrandt pattern, visible skin texture with natural pores and subtle freckles, warm 4000K light, shallow depth of field with cream-colored bokeh background, individual hair strands catching light, sharp focus on near eye with visible catchlight, natural human anatomy, no artificial smoothing

**Weak vs. Strong Comparison (Product):**

❌ Weak:
> A black coffee mug on white background, high quality, product photo, professional, detailed

✅ Strong:
> Matte black ceramic coffee mug with visible throwing rings and slight irregular rim, steam rising from hot coffee surface, sitting on polished concrete countertop with subtle reflection, three-point softbox lighting with diffused key from left and soft fill from right, shot on Phase One IQ4 with 120mm macro at f/5.6, clean neutral studio environment with soft gradient, sharp focus on mug surface and steam texture, commercial product photography, natural shadow grounding the mug

**Weak vs. Strong Comparison (Architecture):**

❌ Weak:
> Beautiful modern house on hill, stunning architecture, high quality, amazing view, professional

✅ Strong:
> Modernist concrete villa cantilevered over coastal cliff, board-formed concrete texture with visible timber grain pattern, floor-to-ceiling glass curtain wall reflecting ocean and sky, warm 3000K golden hour light from west illuminating concrete facade, shot on technical camera with 24mm tilt-shift at f/11 maintaining vertical lines, two-point perspective from approach path, native coastal vegetation in foreground, deep blue Pacific Ocean in background, Kodak Vision3 250T film stock with fine grain, architectural photography, awe-inspiring coastal integration

---

### TECHNICAL NOTES FOR AI GENERATION
- **This skill is the foundation:** Always consult this skill before any domain-specific FLUX.2 Dev skill. The principles here govern all domain-specific applications.
- **Subject-first is non-negotiable:** The first 10 tokens determine the entire output character. Never bury the subject.
- **Camera specs > quality tokens:** "Shot on Canon EOS R5" triggers better photorealism than "photorealistic, 8K, highly detailed" combined.
- **Behavioral descriptions > naming:** Describe what light DOES, what fabric DOES, what shadow DOES — not what they ARE.
- **JSON for complexity:** When a scene has 3+ subjects, 2+ light sources, or brand-critical HEX colors, use JSON structured prompts.
- **Guidance 3.5–4.5 is the safe zone:** Below 3.0 = drift. Above 5.0 = over-processing artifacts.
- **Steps 28–35 for production:** Below 25 = soft. Above 40 = diminishing returns with increased artifact risk.
- **Always append guardrails:** The positive-only guardrails clause should end every prompt as a safety net.
- **Iterate in three passes:** Foundation (fast/cheap) → Refinement → Polish (slow/expensive).
- **For batch consistency:** Use identical locked parameters across all prompts in a series. Vary only the intended variable.
- **Multi-language is native:** No translation needed. FLUX.2 processes the semantic content regardless of language.
- **Text rendering:** Quotes + placement + font + short length = highest accuracy for in-image text.
- **Never use "white background" in Dev:** This is the single most damaging phrase for FLUX.2 Dev output quality. Always reframe.
- **When in doubt, be specific:** "Red" → "Crimson silk with slight orange undertone." "Tall building" → "42-story glass tower with setbacks at 15th and 30th floors."
