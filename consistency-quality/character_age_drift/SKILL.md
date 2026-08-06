# SKILL: Character Age Drift
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting age inconsistency in AI-generated characters across multiple images or video frames. Age drift is a form of identity degradation where a character's apparent age shifts — younger or older — between generations despite identical age specifications. This is particularly critical in video workflows where temporal coherence requires stable biological age [^87^].

### TRIGGER KEYWORDS
age drift, character aging, age inconsistency, age change, looking younger, looking older, age continuity, youth creep, age lock, character age, consistent age, age stability, aging character, skin age

### CORE RULES
- Vague age descriptors cause drift: "young adult" is interpreted differently each time
- Anchor age with specific decade + anatomical detail: "35-year-old, slight smile lines, firm jawline"
- Lighting changes cause apparent age shift: soft light reads younger, harsh light reads older
- Include anatomical age anchors: "visible nasolabial folds", "smooth forehead", "no gray hair"
- Expression affects perceived age: smile creates fuller cheeks (younger); serious = hollow cheeks (older)
- For series: lock age description in the identity clause that repeats across all prompts
- Specify explicitly: "age-stable across all frames" in video sequence prompts

---

### DETECTION SIGNALS

**Visual Drift Indicators:**
- **Youth Creep:** Character appears progressively younger across generations (smoother skin, fuller face, larger eyes)
- **Age Acceleration:** Character appears progressively older (more wrinkles, sagging, graying)
- **Inconsistent Skin Texture:** Same character has pore detail in one image, porcelain smoothness in another
- **Facial Proportion Shift:** Eye-to-nose ratio changes, jawline softens or sharpens unpredictably
- **Hair Color Drift:** Subtle graying or darkening between frames
- **Submandibular Fat Pad:** Volume under chin changes, altering apparent age [^87^]

**Prompt-Level Causes:**
- Vague age descriptors: "young adult", "middle-aged" (model interprets differently each time)
- Lighting changes affecting apparent age (soft light = younger, harsh light = older)
- Expression changes (smile = fuller cheeks = younger, serious = hollow cheeks = older)
- Environment context shifts (playground = younger, office = older)
- Missing age-anchoring anatomical details

---

### FIX VOCABULARY — YOUTH SIGNALS

**For Characters That Should Appear Young:**
```
youthful appearance, smooth skin, full cheeks, round face, large eyes, small nose, soft jawline, no wrinkles, no crow's feet, no forehead lines, plump lips, clear complexion, baby fat in cheeks
```

**Age Anchors by Decade:**
| Target Age | Primary Anchors | Secondary Anchors |
|------------|-----------------|-------------------|
| Child (5–10) | round face, large eyes, small nose, no wrinkles, baby teeth | smooth skin, short stature, playful expression |
| Teen (13–19) | acne possible, angular face emerging, growth spurt proportions | mixed child/adult features, expressive, energetic |
| Young Adult (20–30) | smooth skin, defined jawline, no wrinkles, full hair | energetic posture, modern style, minimal aging signs |
| Adult (30–45) | subtle smile lines, slight forehead texture, mature eyes | confident posture, established style, minimal gray |
| Middle Age (45–60) | crow's feet, forehead lines, slight jowls, skin texture | gray at temples possible, reading glasses, gravitas |
| Senior (60–80) | wrinkles, age spots, thinning hair, sagging skin, veins | wisdom lines, gentle posture, silver/white hair |
| Elder (80+) | deep wrinkles, translucent skin, pronounced veins, stooped | hearing aid possible, cane, historical context |

---

### FIX STRATEGIES

**1. The Biological Prior Injection**
- Specify anatomical age markers explicitly [^87^]:
  - `submandibular fat pad volume consistent with age 35`
  - `skin elasticity appropriate for age 45`
  - `facial bone structure of mature adult`
- These concrete biological terms anchor the model more reliably than abstract age words

**2. The Age Lock Phrase**
- `appears exactly [age] years old`, `biological age [number]`, `chronological age [number] with [specific features]`
- More specific than "middle-aged" or "young"

**3. The Expression Normalization**
- Use neutral expression references for consistency [^83^]:
  - `neutral expression, mouth closed, relaxed face`
  - A big smile in one reference can push cheek volume wider across all generations [^83^]

**4. The Lighting Consistency**
- Same lighting = same apparent age
- `soft even lighting` minimizes age variation
- `harsh side-light` reveals texture and can age appearance

**5. The Reference Quantity Rule**
- 3 references = baseline consistency
- 6+ references = proportion drift typically resolved [^83^]
- Include multiple angles: front, 3/4 left, 3/4 right, profile [^83^]

**6. The Seed + Prompt Lock**
- Lock seed for character series
- Keep age descriptors identical across all variations
- Vary only: action, environment, clothing (never age-related descriptors)

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Use prompt weights: `(age 35:1.2)`, `(mature adult:1.3)`
- Negative: `teenager, child, elderly, aged, wrinkled skin, gray hair` (if targeting younger)
- Character sheet workflow: Generate hero image → 3/4 views → profile with locked seed [^83^]

**Flux / Flux2:**
- No prompt weights; rely on explicit anatomical description
- Place age anchors in first 10 words
- Use concrete biological terms rather than abstract age categories

**LTX Video:**
- Age drift is amplified across temporal dimension [^87^]
- Cross-frame attention locking forces identical facial landmark coordinates [^87^]
- Guardrail: `consistent biological age across all frames, no aging or de-aging drift`
- Character seed locking essential for video age stability

---

### EXAMPLE FIX PROMPTS

**Fix: Youth Creep in Adult Character (Flux):**
> `Portrait of woman with biological age 42, subtle crow's feet at eye corners, slight forehead lines, mature jawline defined but not sharp, skin with natural texture appropriate for age 40s, no porcelain smoothness, no baby fat, photorealistic, soft even lighting`

**Fix: Age Consistency Series (SDXL):**
> Base: `masterpiece, best quality, portrait of man age 35, defined jawline, no wrinkles, no gray hair, mature young adult`
> Variation A: `...standing in office, professional attire, same face age 35`
> Variation B: `...at gym, athletic wear, same face age 35, same skin texture`
> Negative: `teenager, child, elderly, aged, wrinkled, gray hair, baby face`

**Fix: Video Age Stability (LTX):**
> `Subject: Woman biological age 50, consistent submandibular volume, stable skin texture, no age drift. Guardrails: Same apparent age across all frames, no facial feature morphing, stable proportions.`

---

### DETECTION CHECKLIST
- [ ] Character appears same age across all images/frames?
- [ ] Skin texture consistent (not smooth in one, wrinkled in another)?
- [ ] Facial proportions stable (eye size, jawline, cheek volume)?
- [ ] Hair color/texture consistent?
- [ ] No expression-based age distortion (smile = younger)?
- [ ] Lighting not artificially aging or de-aging?
- [ ] References normalized for expression and lighting? [^83^]

---

### TECHNICAL NOTES FOR AI GENERATION
- Age is highly sensitive to lighting, expression, and context — control these variables
- Biological prior injection (anatomical terms) anchors age more reliably than abstract descriptors [^87^]
- 6+ reference images from multiple angles resolve proportion drift [^83^]
- In video, age drift is often the first temporal coherence failure [^87^]
- Always normalize references: same expression, same lighting, same color space [^83^]
