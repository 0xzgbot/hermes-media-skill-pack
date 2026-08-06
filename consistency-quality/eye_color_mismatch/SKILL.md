# SKILL: Eye Color Mismatch
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of detecting and correcting inconsistent or incorrect eye color in AI-generated characters. Eye color is a high-saliency feature that viewers notice immediately when wrong. Models often drift eye color between generations, ignore specified colors, or blend multiple colors into muddy heterochromia. This skill provides detection signals, fix vocabulary, and prevention strategies.

---

### DETECTION SIGNALS

**Visual Drift Indicators:**
- **Color Bleed:** Eyes appear a mix of two colors (e.g., blue-green instead of pure blue)
- **Lighting Override:** Eye color changes based on environmental light (warm light turns brown eyes amber, cool light turns them gray)
- **Asymmetry:** One eye different color from the other (unintentional heterochromia)
- **Desaturation:** Specified vivid eye color (emerald, violet) renders as dull gray-brown
- **Pupil Color Confusion:** Iris color bleeds into pupil or sclera
- **Reflection Dominance:** Catchlight or environmental reflection overpowers true iris color

**Prompt-Level Detection:**
- Eye color mentioned late in prompt (low weight in Flux)
- Eye color buried inside long character description
- No reinforcement of eye color in negative or secondary prompts
- Multiple characters in scene with unspecified eye colors causing model confusion

---

### FIX VOCABULARY

**Primary Fix — Explicit Reinforcement:**
```
[color] eyes, [color] irises, distinct [color] eye color, clearly [color] eyes
```

**Secondary Fix — Material Reference:**
```
sapphire blue eyes, emerald green eyes, amber gold eyes, steel gray eyes, obsidian black eyes, honey brown eyes, violet purple eyes, ice blue eyes
```

**Tertiary Fix — Anatomical Anchoring:**
```
[color] iris with dark limbal ring, [color] eyes with visible pupil, [color] eye color consistent in both eyes, symmetrical [color] eyes
```

**Quaternary Fix — Lighting Isolation:**
```
[color] eyes catching light, [color] irises visible despite [lighting condition], eye color clearly [color] regardless of environmental light
```

**Prevention — Early Placement:**
In Flux, place eye color in first 10 words:
```
Portrait of woman with vivid emerald green eyes...
```
Not:
```
Portrait of woman in sunset, wearing leather jacket, looking at camera with emerald green eyes...
```

---

### ADVANCED FIX TECHNIQUES

**1. The Dual-Lock Method**
- Positive: Specify eye color 2× in different phrasings
- Example: `sapphire blue eyes, distinctly blue irises`
- Reinforces color through repetition without prompt weight brackets (Flux-safe)

**2. The Material Metaphor**
- Use gemstone/mineral names for precise color
- `sapphire` = deep blue | `emerald` = vivid green | `amber` = warm gold-brown | `obsidian` = deep black | `steel` = cool gray | `honey` = warm light brown | `amethyst` = purple | `topaz` = golden yellow

**3. The Limbal Ring Anchor**
- Include `dark limbal ring` or `defined iris edge`
- Prevents color bleed into sclera and pupil
- Adds anatomical realism that grounds the color

**4. The Catchlight Separation**
- Specify `catchlight reflecting in [color] eyes` rather than just `[color] eyes`
- Forces model to render both reflection and base color distinctly

**5. The Symmetry Command**
- `symmetrical eye color`, `both eyes [color]`, `identical [color] irises`
- Prevents unintentional heterochromia

**6. The Color-Environment Decoupling**
- `eye color remains [color] regardless of lighting`, `[color] eyes not affected by warm/cool ambient light`
- Prevents environmental color cast from overriding eye color

---

### MODEL-SPECIFIC STRATEGIES

**Flux / Flux2:**
- Place eye color in subject clause (first 5–10 words)
- Use material metaphor (gemstone names) — Flux responds strongly to concrete nouns
- No negative prompts available natively; use positive reframing
- Repeat eye color twice in prompt for reinforcement

**SDXL / z_image:**
- Can use prompt weights: `(sapphire blue eyes:1.3)`
- Negative prompt: `mismatched eyes, heterochromia, color bleed, muddy eye color`
- Place in both positive (early) and negative (prevent drift)

**LTX Video:**
- Eye color must be specified in Subject clause of 6-part shot-note
- Guardrail: `consistent eye color across all frames, no eye color drift`
- Character seed locking helps maintain eye color across video

---

### EXAMPLE FIX PROMPTS

**Fix: Drifted Eye Color (Flux):**
> `Portrait of young woman with vivid sapphire blue eyes with dark limbal ring, both eyes identically blue, blue irises clearly visible, soft window light, photorealistic, sharp focus on eyes`

**Fix: Desaturated Eye Color (SDXL):**
> Positive: `(emerald green eyes:1.3), vivid green irises, gemstone green eye color, symmetrical`
> Negative: `brown eyes, gray eyes, desaturated eyes, muddy eye color, heterochromia`

**Fix: Environmental Bleed (LTX):**
> `Subject: Woman with amber gold eyes, eye color remains warm amber regardless of neon lighting. Guardrails: Consistent eye color across frames, no color bleed from environment.`

---

### DETECTION CHECKLIST
- [ ] Both eyes same color?
- [ ] Color matches prompt specification?
- [ ] Color not overridden by lighting?
- [ ] Iris distinct from pupil and sclera?
- [ ] Color vivid and saturated as specified?
- [ ] No unintentional heterochromia?
- [ ] Color consistent across series/frames?

---

### TECHNICAL NOTES FOR AI GENERATION
- Eye color is statistically low-weight in most models unless explicitly reinforced
- Material metaphors (gemstones) activate stronger color priors than abstract color words
- Always check eye color first in QA — viewers notice eye color errors before almost any other artifact
- In video workflows, eye color drift is often the first sign of character consistency breakdown
