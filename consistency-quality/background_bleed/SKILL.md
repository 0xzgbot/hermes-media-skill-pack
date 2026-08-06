# SKILL: Background Bleed
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting background elements that intrude into the subject, or subject elements that leak into the background. Background bleed manifests as color contamination, texture migration, object merging, and environmental features attaching to the subject. Proper subject isolation is essential for clean commercial imagery.

### TRIGGER KEYWORDS
background bleed, color bleed, texture migration, subject merging, background contamination, color contamination, object merging, background intrusion, fringing, color spill, background edge, subject isolation failure

### CORE RULES
- Strong contrast between subject and background prevents most bleed
- Describe subject edges explicitly: "clean edge separation between subject and background"
- Name the background independently from the subject in the prompt
- Avoid prompt adjacency: don't put subject and background descriptors in same clause
- For Flux: positive isolation phrase "subject cleanly isolated from background, distinct separation"
- Color proximity causes bleed: avoid subject and background sharing similar hues
- Depth/spatial separation in prompt reduces model's tendency to merge adjacent elements

---

### DETECTION SIGNALS

**Color Bleed:**
- Background color tinting subject edges (green screen spill, sky blue on shoulders)
- Subject color contaminating background (red dress turning wall pink)
- Environmental hue on skin (neon signs casting magenta on face in unintended ways)

**Texture Migration:**
- Background pattern appearing on subject clothing (brick texture on jacket)
- Subject texture leaking to background (fur detail appearing on wall)
- Ground plane texture climbing subject (grass growing on shoes, then up pants)

**Object Merging:**
- Subject merging with background objects (person fused with tree, chair, wall)
- Background objects growing out of subject (branches from head, wires from arms)
- Foreground objects attaching to subject (table edge becoming part of leg)

**Edge Contamination:**
- Fringing (colored halo around subject edges)
- Jagged or dissolved boundaries between subject and background
- Semi-transparent subject edges blending with background

---

### FIX VOCABULARY

**Subject Isolation Phrases:**
```
subject clearly separated from background, sharp edge between subject and environment, subject in sharp focus with background softly blurred, clean silhouette, subject isolated against [background], distinct boundary
```

**Depth Separation:**
```
shallow depth of field, subject sharp background soft, f/1.8 aperture, bokeh background, foreground subject midground background layers, atmospheric perspective
```

**Color Separation:**
```
[subject color] contrasting with [background color], complementary colors, subject warm against cool background, subject cool against warm background, no color bleed, clean color separation
```

**Environmental Control:**
```
simple background, uncluttered environment, minimal background, solid color backdrop, clean studio backdrop, negative space behind subject
```

---

### FIX STRATEGIES

**1. The Depth of Field Shield**
- `shallow depth of field, f/1.4, subject sharp background creamy bokeh`
- Blurred background cannot bleed texture or detail onto subject
- Most reliable isolation technique for portraits and products

**2. The Contrast Barrier**
- Specify color contrast between subject and background:
  - `subject in warm tones against cool blue background`
  - `dark subject against light background`
  - `light subject against dark background`
- High contrast prevents edge merging

**3. The Negative Space Command**
- `generous negative space around subject`, `subject isolated in center with empty background`
- Physical distance in frame prevents bleed

**4. The Edge Sharpness Reinforcement**
- `crisp edge between subject and background`, `clean cut between figure and ground`
- Explicitly requests sharp boundary

**5. The Background Simplification**
- `simple gradient background`, `solid color backdrop`, `minimal environment`
- Complex backgrounds have more elements that can bleed

**6. The Layered Depth**
- `foreground subject, midground [element], background [element], clear separation between planes`
- Forces model to think in depth layers

**7. The Rim Light Separation**
- `rim light separating subject from background`, `backlight creating halo around subject`
- Physical light barrier between subject and environment

---

### MODEL-SPECIFIC STRATEGIES

**Flux / Flux2:**
- Use `subject isolated against [specific background]` early in prompt
- Specify depth of field in technical clause
- No negative prompts for bleed; use positive isolation language

**SDXL / z_image:**
- Negative: `merged with background, fused with environment, color bleed, texture migration, cluttered background`
- Positive: `clean separation, sharp edges, distinct subject`
- Use `subject in foreground` to force depth hierarchy

**LTX Video:**
- Background bleed often increases across frames as model "forgets" depth
- Guardrail: `stable subject-background separation across frames, no edge contamination, consistent depth of field`
- Specify `locked focus on subject` to prevent background sharpness drift

---

### EXAMPLE FIX PROMPTS

**Fix: Color Bleed (Flux):**
> `Portrait of woman in red dress isolated against cool blue studio backdrop, sharp edge between subject and background, no color bleed, shallow depth of field f/1.8, subject sharp background creamy bokeh, clean color separation, photorealistic`

**Fix: Texture Migration (SDXL):**
> Positive: `Product photography of leather bag on clean white surface, sharp focus on bag, background pure white with no texture migration, clean separation, no pattern bleed`
> Negative: `texture on background, pattern bleed, merged with surface, cluttered background, color contamination`

**Fix: Edge Contamination (LTX):**
> `Subject: Dancer in white costume. Camera/Lens: Static, medium shot, f/2.8. Style: Clean studio. Motion: Spinning. Guardrails: No costume merging with background, stable edge definition, no fringing, consistent subject isolation.`

---

### DETECTION CHECKLIST
- [ ] Subject edges crisp and defined?
- [ ] No background color on subject edges?
- [ ] No subject texture on background?
- [ ] Subject not merged with background objects?
- [ ] Depth separation visible (sharp subject, soft background)?
- [ ] No fringing or halo around subject?
- [ ] Background simplified enough to prevent bleed?

---

### TECHNICAL NOTES FOR AI GENERATION
- Background bleed is most common with complex, detailed backgrounds
- Shallow depth of field is the single most effective bleed prevention technique
- Color contrast between subject and background prevents edge merging
- In video, background bleed often worsens as the model attends less to depth over time
- For product photography, pure white or black backgrounds minimize bleed but can cause overexposure in Flux [^72^] — use light gray instead
