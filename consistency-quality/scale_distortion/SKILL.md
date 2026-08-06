# SKILL: Scale Distortion
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting scale ambiguity and proportion errors in AI-generated imagery. Scale distortion occurs when the model renders objects, characters, or environments with incorrect relative sizes — tiny humans next to small objects, giant furniture, or ambiguous scale that leaves viewers unable to determine actual size. This skill provides reference object injection techniques and proportion anchoring vocabulary.

### TRIGGER KEYWORDS
scale distortion, proportion error, wrong size, scale problem, size reference, scale ambiguity, proportion mismatch, relative size, scale fix, environment scale, character scale, scale anchor, miniature problem, giant problem

### CORE RULES
- Always include a scale reference when absolute size matters: human figure, coffee cup, doorway
- Describe relative sizes explicitly: "character fills two-thirds of frame height"
- Named proportional relationships: "table comes to character's waist", "doorframe twice character height"
- Wide angle distortion can make near objects appear larger — specify lens to control scale impression
- Environmental scale tells a story: oversized environment = vulnerability; normal = grounded
- For product shots: always include a human hand or common object for scale
- Avoid ambiguous foreground/background size differences without explanation

---

### DETECTION SIGNALS

**Relative Scale Errors:**
- Human hand smaller than smartphone
- Door handle at knee height
- Chair seat at shoulder height
- Car wheels smaller than hubcaps
- Building windows person-sized

**Absolute Scale Ambiguity:**
- Object floating in void with no reference
- Macro subject without context — is it a mountain or a pebble?
- Insect rendered without familiar size reference
- Product without hand, coin, or ruler for scale

**Proportion Drift:**
- Head too large or small for body
- Limbs lengthening or shortening between generations
- Furniture growing or shrinking relative to characters
- Architectural elements (stairs, doors) at wrong human scale

**Video-Specific Scale Drift:**
- Character growing or shrinking across frames
- Objects changing size during camera movement
- Perspective shift causing scale confusion

---

### REFERENCE OBJECT INJECTION VOCABULARY

**Human Scale References:**
```
hand holding [object], person standing next to [object], adult human figure for scale, child reaching for [object], person's foot next to [object], hand touching [object]
```

**Standard Object References:**
```
smartphone for scale, US quarter coin for scale, credit card for scale, ruler in frame, 12-inch measuring tape, standard coffee mug, #2 pencil, AA battery, soda can, wine bottle
```

**Architectural Scale References:**
```
standard 80-inch door, 36-inch countertop height, 8-foot ceiling, human figure in doorway, person sitting in chair, hand on doorknob at standard height
```

**Natural Scale References:**
```
blade of grass for scale, raindrop on surface, dewdrop on leaf, ant crawling on [object], human finger touching [object], hand cupping [object]
```

**Product Scale References:**
```
on standard desk surface, next to keyboard and mouse, in palm of hand, on dining table with place setting, in car cupholder, on bookshelf with books
```

---

### FIX STRATEGIES

**1. The Familiar Object Anchor**
- Place a universally understood object in frame:
  - `smartphone lying next to product for scale`
  - `human hand reaching toward building entrance`
  - `quarter coin placed beside jewelry for size reference`
- Most reliable scale fix for product and macro photography

**2. The Human Figure Anchor**
- Include human for immediate scale comprehension:
  - `person standing at base of waterfall`
  - `hiker on mountain ridge showing scale of peaks`
  - `child playing next to sculpture`
- Human scale is neurologically hardwired; most intuitive reference

**3. The Architectural Standard**
- Reference built environment standards:
  - `8-foot door frame with person walking through`
  - `kitchen counter at standard 36-inch height`
  - `ceiling at standard 9 feet`
- Prevents furniture and interior scale drift

**4. The Measurement Explicit**
- State dimensions in prompt:
  - `30-meter tall statue with person at base`
  - `2-inch gemstone held between thumb and forefinger`
  - `compact car, 15 feet long, parked on street`
- Direct dimension claims anchor model's size priors

**5. The Perspective Consistency**
- Specify camera height and distance:
  - `shot from 6-foot eye level, 10 feet from subject`
  - `overhead shot from 8 feet above table`
- Prevents perspective distortion that implies wrong scale

**6. The Multi-Object Comparison**
- `product next to competing product of known size`
- `insect on leaf next to dewdrop`
- Relative size between known objects anchors unknown object

**7. The Proportion Lock**
- For characters: `head proportionate to body at 1:7.5 ratio`
- For architecture: `doors at standard human scale, windows at standard proportions`
- Explicit ratio claims prevent proportion drift

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Positive: `(accurate scale:1.2), proper proportions, human-scale reference`
- Negative: `giant furniture, tiny human, wrong proportions, distorted scale, ambiguous size`
- Include reference object early in environment clause

**Flux / Flux2:**
- Place reference object in subject or environment clause (first 15 words)
- Use concrete nouns: `smartphone`, `coffee cup`, `human hand`
- Specify dimensions directly: `30cm tall`, `2 inches wide`

**LTX Video:**
- Scale can drift across frames as camera moves
- Guardrail: `stable scale across frames, consistent proportions, no size morphing`
- Reference object should remain in frame throughout clip for scale stability

---

### EXAMPLE FIX PROMPTS

**Fix: Product Scale (Flux):**
> `Product photography of titanium water bottle, 750ml capacity, placed next to standard smartphone for scale, bottle 26cm tall, hand reaching for bottle showing grip size, on clean kitchen counter at standard 36-inch height, photorealistic, accurate proportions`

**Fix: Macro Scale (SDXL):**
> Positive: `Extreme macro of jumping spider on fingertip, human fingerprint ridges visible for scale, spider 5mm body length, shallow depth of field, accurate scale reference, natural history photography`
> Negative: `ambiguous scale, giant spider, wrong proportions, no reference object`

**Fix: Architectural Scale (LTX):**
> `Scene: Modern museum lobby. Subject: 15-foot abstract sculpture with person walking past for scale. Camera/Lens: Wide shot from 6-foot eye level, 24mm. Style: Architectural photography. Motion: Slow walk-through. Guardrails: Stable scale, consistent human proportions, no size drift.`

---

### DETECTION CHECKLIST
- [ ] Human figures proportionate to environment?
- [ ] Reference object present for ambiguous subjects?
- [ ] Familiar objects at correct relative size?
- [ ] Architectural elements at standard human scale?
- [ ] No giant furniture or tiny humans?
- [ ] Product dimensions inferable from context?
- [ ] Scale consistent across series/frames?
- [ ] Perspective not distorting apparent scale?

---

### TECHNICAL NOTES FOR AI GENERATION
- Human figures are the most reliable scale anchors — include whenever possible
- Standard objects (phone, coin, hand) work when humans are inappropriate
- Explicit dimension claims in prompt ("30cm tall") anchor model priors
- Scale distortion often co-occurs with perspective errors — check both
- In video, scale drift is often caused by camera movement without stable reference
- For product shots, always include hand or familiar object for size context
