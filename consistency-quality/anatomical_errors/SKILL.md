# SKILL: Anatomical Errors
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of detecting and correcting the most common anatomical failures in AI image generation: extra limbs, merged fingers, missing digits, deformed joints, and asymmetric features. These errors are the primary quality gate for commercial AI imagery. This skill provides detection taxonomies, model-specific fix strategies, and post-processing workflows [^82^].

---

### ERROR TAXONOMY

**Hands & Fingers (Highest Failure Rate):**
- Extra fingers (6+ digits)
- Merged fingers (fused together like mittens)
- Missing fingers (3 or fewer visible)
- Distorted thumb (wrong position, too long, backward)
- Clubbed or blob hands (no individual fingers)
- Wrist anomalies (too thin, broken angle, extra joints)

**Limbs & Body:**
- Extra arms/legs
- Missing arms/legs
- Merged limbs (two legs fused)
- Joint inversion (knee bending backward, elbow hyperextension)
- Proportion drift (tiny head, giant hands, elongated torso)
- Asymmetry (one arm longer than other, uneven shoulders)

**Face & Head:**
- Misaligned eyes (asymmetrical, different heights)
- Merged facial features (nose and mouth fused)
- Extra or missing facial elements (third eye, no nose)
- Jaw deformation (too wide, too narrow, broken angle)
- Neck issues (too long, too thin, broken)

---

### FIX STRATEGIES BY MODEL

**SD 1.5 & Anime Models:**
Negative prompt is the primary defense:
```
(worst quality, low quality:1.4), bad anatomy, bad hands, missing fingers, extra digit, fewer digits, fused fingers, mutated hands, poorly drawn face, asymmetric eyes, deformed
```
[^82^]

**SDXL & Juggernaut Models:**
Keep negatives minimal — overloading degrades overall quality [^82^]:
```
bad anatomy, poorly drawn hands, text, watermark, deformed, plastic skin
```

**Flux / Flux2:**
No native negative prompts. Use positive reframing:
```
accurate anatomy, natural proportions, correctly drawn hands with five distinct fingers, anatomically correct fingers, symmetrical facial features, proper joint alignment
```

**Post-Processing — ADetailer (WebUI/production):**
The 2026 standard for automatic hand/face fixing [^82^]:
1. Install ADetailer extension
2. Enable `face_yolov8n.pt` for faces, `hand_yolov8n.pt` for hands
3. Set Inpainting Denoising Strength to **0.35–0.45**
   - Too high (0.8+): New hand disconnects from original lighting
   - Too low: Distortions remain unfixed [^82^]

---

### ADVANCED FIX TECHNIQUES

**1. The Hand Hiding Strategy**
- If hands consistently fail, compose them out of frame
- `hands in pockets`, `arms crossed behind back`, `hands holding object obscuring fingers`
- Most reliable fix for difficult poses

**2. The Specific Finger Count**
- Explicitly state: `five fingers on each hand`, `correctly drawn hand with five separate fingers`
- More specific than "good hands" — models respond to concrete counts

**3. The Joint Lock**
- Specify joint angles explicitly: `elbow bent at 90 degrees`, `knee flexed naturally`, `wrist straight`
- Prevents impossible joint configurations

**4. The Symmetry Anchor**
- `symmetrical face`, `eyes at equal height`, `shoulders level`, `arms equal length`
- Prevents asymmetric drift

**5. The Partial View**
- `hand partially visible`, `fingers gripping edge of table` (only 2–3 fingers shown)
- Reduces anatomical complexity the model must solve

**6. The Glove/Prop Strategy**
- `wearing leather gloves`, `hand wrapped in bandage`, `holding sword hilt`
- Obscures finger detail while maintaining pose intent

**7. The Anatomy-First Prompt Placement**
- Place anatomical accuracy early in prompt:
  - Good: `Anatomically correct woman with five fingers on each hand, standing...`
  - Bad: `Woman standing in field with correct anatomy and five fingers...`

---

### DETECTION CHECKLIST

**Hands:**
- [ ] Correct finger count (5 per hand)?
- [ ] Fingers distinct and separate?
- [ ] Thumb in correct anatomical position?
- [ ] Wrist natural thickness and angle?
- [ ] Proportionate to body?

**Limbs:**
- [ ] Correct limb count (2 arms, 2 legs)?
- [ ] Joints bend in correct direction?
- [ ] Equal length and proportion?
- [ ] No fusion or merging?

**Face:**
- [ ] Eyes aligned horizontally?
- [ ] Facial features distinct and separate?
- [ ] Nose, mouth, eyes in correct relative positions?
- [ ] Jawline natural?
- [ ] Neck proportionate?

---

### EXAMPLE FIX PROMPTS

**SDXL Portrait with Hand Fix:**
> Positive: `masterpiece, best quality, portrait of woman, anatomically correct hands with five distinct fingers, hands resting on table, fingers naturally spread, symmetrical face, proper proportions`
> Negative: `bad anatomy, poorly drawn hands, missing fingers, extra digits, fused fingers, deformed, asymmetric eyes`

**Flux Full Body with Anatomy Focus:**
> `Anatomically correct full-body portrait of athlete, accurate human proportions, correctly drawn hands with five separate fingers, proper joint alignment, symmetrical facial features, standing in natural pose, photorealistic, sharp focus`

**LTX Video Character:**
> `Subject: Anatomically correct woman walking, five fingers visible on each hand, natural gait, proper limb proportions. Guardrails: No extra limbs, no merged fingers, stable anatomy across frames.`

---

### TECHNICAL NOTES FOR AI GENERATION
- Hands are the #1 anatomical failure point across all models
- SDXL: Minimal negatives > maximal negatives; overloading hurts overall quality [^82^]
- Flux: Rely on positive anatomical phrasing; no negative prompt safety net
- ADetailer at 0.35–0.45 denoising is the current gold standard for automated hand repair [^82^]
- When anatomy fails repeatedly, change pose to reduce complexity rather than fighting the model
- For commercial work, always QA hands first — they are the most common rejection reason
