# SKILL: Positive Prompt Structure
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Mastery of token-weight hierarchy and clause ordering for AI image generation models. Different architectures read prompt sequences with different attention patterns — Flux weighs early tokens heavily [^57^], SDXL distributes more evenly but still prioritizes lead tokens, and LTX video requires discrete clause blocks for spatial coherence [^68^]. This skill provides the universal Subject → Action → Environment → Lighting → Style → Quality framework with model-specific adaptations.

### TRIGGER KEYWORDS
prompt structure, prompt order, token weight, prompt hierarchy, clause ordering, subject first, Flux prompt, SDXL prompt, LTX prompt, prompt architecture, prompt framework, prompt template, how to structure prompt

### CORE RULES
- Universal structure: Subject → Action → Environment → Lighting → Style → Quality
- Flux: first 10–15 tokens carry maximum weight — subject and key attribute go first
- SDXL: (keyword:weight) syntax available; use 1.1–1.3 range, avoid extremes
- LTX video: use discrete labeled clauses: "Subject:", "Action:", "Environment:", "Guardrails:"
- Most important attribute goes first — whatever you most need the model to get right
- Comma separation between concepts; period/line break for larger clause boundaries
- Quality tokens go last — they're important but shouldn't override subject/style position

---

### THE UNIVERSAL HIERARCHY

**Flux / Flux2 Priority Order (Critical):**
Flux weighs earlier tokens more heavily than later ones [^57^]. Burying the subject at the end is the most common structural mistake.

```
[SUBJECT] → [ACTION/POSE] → [ENVIRONMENT] → [LIGHTING] → [STYLE] → [QUALITY] → [TECHNICAL SPECS]
```

**SDXL / SD1.5 / z_image Priority Order:**
More forgiving distribution, but subject-first still improves coherence. Use emphasis brackets `(word)` or `(word:1.2)` for key terms.

```
[QUALITY TOKENS] → [SUBJECT] → [ACTION] → [ENVIRONMENT] → [LIGHTING] → [STYLE] → [TECHNICAL SPECS]
```

**LTX Video Priority Order (6-Part Shot-Note):**
Discrete clauses help LTX tokenize constraints, improving spatial coherence and motion stability [^68^].

```
Scene: [ENVIRONMENT ANCHOR]
Subject: [SUBJECT + ACTION]
Camera/Lens: [TECHNICAL SPECS]
Style: [VISUAL STYLE]
Motion: [MOTION/TIME CUES]
Guardrails: [NEGATIVES/GUARDRAILS]
```

---

### CLAUSE-BY-CLAUSE BREAKDOWN

**1. SUBJECT (Clause 1 — Highest Weight)**
- Definition: Who or what is the image about
- Flux Rule: Must be first 3–5 words. Never bury subject after long description [^57^]
- SDXL Rule: Can follow quality tokens, but must appear before environment
- LTX Rule: "Subject: [description]" discrete clause [^68^]
- Examples:
  - Good: `Portrait of a middle-aged marathon runner...` [^57^]
  - Bad: `At dawn in the city with empty storefronts, a marathon runner...` [^57^]

**2. ACTION / POSE (Clause 2)**
- Definition: What the subject is doing
- Importance: Establishes dynamism and narrative
- Examples: `catching his breath`, `sitting cross-legged`, `sprinting toward camera`, `wielding a glowing sword`

**3. ENVIRONMENT (Clause 3)**
- Definition: Where the scene occurs
- Scope: Can include foreground, midground, background layers
- Examples: `city street at dawn with empty storefronts behind him`, `misty mountain temple courtyard`, `cramped cyberpunk alley with neon reflections in puddles`

**4. LIGHTING (Clause 4)**
- Definition: How the scene is illuminated
- Components: Source (sun, neon, candle), quality (soft, harsh, diffused), direction (backlit, side-lit, overhead), color temperature (warm 3200K, cool 6000K)
- Examples: `soft backlight with cool blue tones`, `hard noon sun creating deep shadows`, `volumetric god-rays through cathedral windows`

**5. STYLE / MOOD (Clause 5)**
- Definition: Aesthetic category and emotional register
- Sub-components: Art medium (oil painting, digital art, photograph), era (1920s noir, 1980s synthwave), mood (melancholic, triumphant, eerie)
- Examples: `cinematic noir aesthetic`, `Studio Ghibli-inspired watercolor`, `1970s documentary photography`

**6. QUALITY / TECHNICAL SPECS (Clause 6 — Lowest Weight in Flux)**
- Definition: Production value signals and camera/lens parameters
- Flux Warning: These work better when woven into earlier clauses rather than tacked on the end [^57^]
- Examples: `shot on Sony A7IV with 85mm f/1.8 lens`, `8k resolution, sharp focus, photorealistic`, `35mm film grain, shallow depth of field`

---

### MODEL-SPECIFIC SYNTAX RULES

**Flux / Flux2:**
- No prompt weights: `(word:1.2)` and `(word)++` do NOT work [^72^]
- No negative prompts natively: Use positive phrasing instead [^57^]
- Multi-language: Write in native language; no translation needed [^70^]
- HEX codes: Supported for brand colors [^70^]
- Avoid "white background" in Flux dev: Causes fuzzy outputs [^72^]
- Structure: `[Technical framework]: [Main subject and action], [environmental effects], [special elements]. Technical specifications and conditions.` [^66^]

**SDXL / z_image:**
- Prompt weights supported: `(word:1.2)`, `(word)`, `((word))`
- Negative prompts essential: Separate negative prompt field required
- Resolution sweet spot: ~1024×1024 (1MP) [^58^]
- Multiples of 8: Width/height must be divisible by 8 [^58^]
- Pony model quality tokens: `score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up` [^69^]

**LTX Video:**
- Discrete clauses: Scene / Subject / Camera / Style / Motion / Guardrails [^68^]
- Motion tokens critical: `steady dolly`, `tripod-locked`, `constant speed pan`, `180° shutter equivalent`, `natural motion blur` [^68^]
- Camera paths reduce jitter: Explicit `dolly`, `crane`, `orbit` reduce temporal jitter ~22% [^68^]
- Guardrails against shimmer: Lens and aperture language cut edge shimmer ~18% [^68^]
- Default resolution: 1216 × 704 at 30 FPS [^67^]

---

### PROMPT TEMPLATES BY MODEL

**Flux Template:**
```
[Subject], [action/pose], [environment with specific details], [lighting source and quality], [style/mood], [camera/lens/technical specs]
```
Example: `Portrait of a middle-aged marathon runner catching his breath, sweat on his forehead, city street at dawn with empty storefronts behind him, soft backlight with cool blue tones, shot on Sony A7IV with 85mm f/1.8 lens` [^57^]

**SDXL Template:**
```
[Quality tokens], [subject], [action], [environment], [lighting], [style], [technical specs]
```
Example: `masterpiece, best quality, 8k uhd, portrait of a female samurai, standing in defensive stance, bamboo forest at twilight, dappled golden hour light filtering through canopy, cinematic historical drama aesthetic, shot on ARRI Alexa with 50mm f/1.4, shallow depth of field`

**LTX Video Template:**
```
Scene: [environment anchor]
Subject: [subject + action]
Camera/Lens: [camera movement + lens specs]
Style: [visual style + color palette]
Motion: [motion cues + speed descriptors]
Guardrails: [quality negatives + artifact prevention]
```
Example: `Scene: Coastal California cliff at golden hour. Subject: Lone surfer walking toward ocean with board under arm. Camera/Lens: Steady dolly tracking from behind at eye level, 35mm f/2.8. Style: Documentary surf cinematography, warm amber and teal palette. Motion: Natural walking pace, 180° shutter motion blur, waves crashing in background. Guardrails: No jitter, no shimmer, stable horizon.` [^68^]

---

### ANTI-PATTERNS (What Not To Do)

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Kitchen sink approach — throwing every keyword in | More words ≠ better; dilutes attention [^66^] | Focus on clear vision; delete redundant terms |
| Burying subject at end of long prompt | Flux deprioritizes late tokens [^57^] | Lead with subject every time |
| Static descriptions without movement | Results feel frozen [^66^] | Include motion, interaction, temporal cues |
| Conflicting styles mixed together | Model defaults to mush | Pick one style family; commit fully |
| "White background" in Flux dev | Causes fuzzy outputs [^72^] | Use "clean light gray background" or "minimal studio backdrop" |
| Prompt weights in Flux | Not supported; may cause errors [^72^] | Use emphasis phrases: "with strong emphasis on" |
| Generating square then cropping | AI optimizes composition for ratio [^58^] | Generate at target aspect ratio natively |

---

### EXAMPLE PROMPTS BY MODEL

**Flux (Photorealistic Portrait):**
> Close-up portrait of elderly fisherman, weathered hands mending nets, Mediterranean harbor at dawn with pastel fishing boats, warm 3500K side-light from rising sun, documentary photography aesthetic, shot on Leica M10 with 50mm f/1.4 lens, sharp focus on hands, natural skin texture

**SDXL (Fantasy Illustration):**
> masterpiece, best quality, score_9, score_8_up, epic fantasy illustration of dragon rider, soaring above crystalline mountain peaks, bioluminescent aurora in night sky, volumetric moonlight and ice reflections, digital painting by Greg Rutkowski and Alphonse Mucha, 8k, highly detailed, dramatic composition

**LTX (Cinematic Video):**
> Scene: Rain-slicked Tokyo alley at midnight. Subject: Lone figure in trench coat walking away from camera. Camera/Lens: Slow push-in from 10 meters, 85mm f/1.4 anamorphic. Style: Cinematic cyberpunk noir, cyan and magenta neon palette with heavy atmospheric haze. Motion: Steady walking pace, 180° shutter, steam rising from vents. Guardrails: No temporal jitter, stable framing, no edge shimmer.

---

### TECHNICAL NOTES FOR AI GENERATION
- Always lead with subject; never bury it
- For Flux, keep total prompt under 150 tokens when possible; early density matters more than length
- For SDXL, quality tokens at the front act as "priming" for the model
- For LTX, discrete line breaks between clauses improve tokenization [^68^]
- Use concrete nouns and specific adjectives; avoid abstract concepts alone
