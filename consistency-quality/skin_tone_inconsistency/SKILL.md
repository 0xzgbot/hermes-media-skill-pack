# SKILL: Skin Tone Inconsistency
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting skin tone drift across AI-generated character series, video frames, and multi-subject scenes. Skin tone inconsistency is a critical failure in commercial and ethical AI imagery — it undermines character consistency, misrepresents identity, and signals low production quality. This skill provides detection methods, reference anchoring vocabulary, and normalization workflows [^80^][^83^].

### TRIGGER KEYWORDS
skin tone, skin color, skin inconsistency, tone drift, skin color change, complexion, skin tone lock, melanin, dark skin, light skin, skin consistency, tone mismatch, racial representation, complexion accuracy

### CORE RULES
- Anchor skin tone with specific descriptors, not generic: "deep brown skin with warm undertones" not "dark skin"
- Lighting changes apparent skin tone: warm light adds amber, cool light adds gray — compensate in prompt
- Use the Fitzpatrick scale reference for consistency: Type I–VI with descriptive adjectives
- Place skin tone description early in prompt — especially important for Flux
- For video: "skin tone consistent across all frames, no color drift" is a required guardrail
- Multi-character scenes: name each character's skin tone separately to prevent averaging
- Environmental color cast (neon, warm sunset) must be separated from true skin tone in description

---

### DETECTION SIGNALS

**Across-Series Drift:**
- Same character appears warmer (orange/yellow) in one image, cooler (pink/blue) in another
- Skin appears ashy or desaturated in some generations, rich in others
- Lighting changes create perceived ethnicity shifts
- White balance inconsistency between frames

**Within-Image Errors:**
- Face different color from hands or neck
- Uneven color patches on skin (mottling, blotching)
- Environmental color cast overwhelming natural skin tone
- Overexposed skin losing melanin detail (appearing lighter than specified)

**Video-Specific Drift:**
- Skin tone shifts between frames as lighting changes
- Warm-to-cool oscillation across clip
- Sudden "reset" of skin tone at scene transitions

---

### REFERENCE ANCHORING VOCABULARY

**Skin Tone Description (Use Specific, Respectful Language):**
```
[specific tone] skin, [warm/cool/neutral] undertone, [rich/deep/light/fair] complexion
```

**Fitzpatrick Scale Anchors (Clinical):**
```
Fitzpatrick Type I (very fair, always burns), Type II (fair, usually burns), Type III (medium, sometimes burns), Type IV (olive, rarely burns), Type V (brown, very rarely burns), Type VI (deep brown/black, never burns)
```

**Natural Language Anchors:**
| Tone | Warm Undertone | Cool Undertone | Neutral Undertone |
|------|----------------|----------------|-------------------|
| Very Fair | porcelain with peach, ivory with gold | porcelain with pink, fair with rose | fair with beige, ivory with neutral |
| Light | light with honey, peachy fair | light with pink, fair with berry | light with beige, neutral fair |
| Medium | medium with golden, olive with warm | medium with rose, olive with cool | medium with beige, neutral olive |
| Tan | tan with caramel, golden brown | tan with red, bronze with cool | tan with neutral, warm beige |
| Deep | deep with warm, rich chocolate | deep with cool, espresso with blue | deep with neutral, rich brown |
| Very Deep | very deep with warm, dark ebony | very deep with cool, deep onyx | very deep with neutral, dark brown |

**Ethnicity + Tone Combination (When Relevant):**
```
East Asian skin with warm golden undertone, South Asian skin with rich olive depth, African skin with deep warm brown tone, European skin with fair pink undertone, Latin American skin with medium golden warmth, Middle Eastern skin with olive neutral depth
```

---

### FIX STRATEGIES

**1. The Reference Normalization Workflow**
- Normalize all reference images to same color space (sRGB) [^83^]
- Match white balance across entire reference set [^83^]
- Batch-process references through color correction before feeding to model [^83^]
- This is the #1 fix for skin tone drift [^80^]

**2. The Undertone Lock**
- Specify undertone explicitly: `warm golden undertone`, `cool pink undertone`, `neutral beige undertone`
- Undertone is more stable than surface color across lighting changes

**3. The Lighting Consistency Rule**
- Same lighting type across series = same skin tone
- `soft even lighting` minimizes tone variation
- `harsh direct sun` creates high contrast that can alter perceived tone

**4. The Desaturation Guardrail**
- If tone keeps drifting warm/cool: `desaturate skin slightly in anchor` [^80^]
- Lower saturation discourages sudden warm/cool shifts

**5. The Melanin Detail Preservation**
- `rich melanin detail visible`, `skin texture with natural pigmentation`, `no washed-out skin tone`
- Prevents overexposure from lightening skin beyond specification

**6. The Multi-Reference Triangulation**
- 6+ references from multiple angles resolve proportion and tone drift [^83^]
- Include: front, 3/4 left, 3/4 right, profile, close-up, medium shot

**7. The White Balance Anchor**
- `correct white balance`, `neutral gray reference in frame`, `color-calibrated lighting`
- Provides objective color reference within image

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Positive: `(warm brown skin:1.2), rich melanin, natural skin texture`
- Negative: `ashy skin, washed out, pale, bleached, color cast, orange skin, gray skin`
- Use reference images with matched lighting and color space [^83^]

**Flux / Flux2:**
- Place skin tone in subject clause (first 10 words)
- Use specific natural language: `deep ebony skin with warm undertone`
- No negative prompts; rely on positive specificity and reference normalization

**LTX Video:**
- Skin tone drift is common across temporal dimension
- Guardrail: `consistent skin tone across all frames, stable white balance, no color temperature drift`
- Character seed locking + reference normalization essential

---

### EXAMPLE FIX PROMPTS

**Fix: Tone Drift Series (Flux):**
> `Portrait of woman with medium olive skin with warm golden undertone, rich natural pigmentation, skin texture visible, consistent warm complexion, soft even lighting, no color cast, photorealistic, accurate skin tone`

**Fix: Ashy Recovery (SDXL):**
> Positive: `(deep brown skin:1.3), rich melanin detail, warm undertone, natural skin texture, accurate color rendering`
> Negative: `ashy skin, gray skin, washed out, pale, bleached, color cast, incorrect white balance`

**Fix: Video Tone Stability (LTX):**
> `Subject: Woman with tan caramel skin, warm undertone. Style: Consistent skin tone across all frames. Guardrails: Stable white balance, no warm/cool drift, accurate melanin rendering, no desaturation.`

---

### DETECTION CHECKLIST
- [ ] Skin tone matches specification across all images?
- [ ] Face, hands, neck same tone?
- [ ] No environmental color cast overwhelming natural tone?
- [ ] Melanin detail preserved (not washed out)?
- [ ] Undertone consistent (warm/cool/neutral)?
- [ ] References normalized to same color space? [^83^]
- [ ] White balance stable across series/frames?
- [ ] No perceived ethnicity shift between generations?

---

### TECHNICAL NOTES FOR AI GENERATION
- Skin tone inconsistency is often caused by mixed reference color spaces, not model failure [^83^]
- sRGB normalization of all references is the most effective prevention [^83^]
- Undertone specification is more stable than surface color across lighting changes
- Overexposure is the primary cause of unintended skin lightening
- In video, skin tone drift often signals broader white balance instability
- Always use respectful, specific language for skin tone — avoid vague or potentially offensive terms
