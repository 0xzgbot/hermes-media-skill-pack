# SKILL: Clothing Detail Loss
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting the degradation of clothing texture, material specificity, and garment detail in AI-generated imagery. Models often render clothing as smooth, generic fabric blobs rather than specific materials with weave, drape, hardware, and construction detail. This skill provides material specificity requirements and vocabulary for precise garment rendering.

### TRIGGER KEYWORDS
clothing detail, fabric detail, material specificity, garment texture, clothing loss, fabric rendering, texture degradation, wardrobe detail, clothing accuracy, material texture, garment construction, fabric weave, clothing quality

### CORE RULES
- Name specific materials, not generic "fabric": denim twill, supple leather, raw silk, merino wool
- Include material behavior: leather creases, silk shimmers, wool has fiber texture
- Specify construction details: "topstitched seams", "brass buttons", "zip fly with metal teeth"
- Hardware requires explicit naming: "silver metal zip" not just "zipper"
- Dark clothing loses detail fastest — add texture descriptors for dark garments specifically
- For video: establish detailed clothing in anchor frame; chain consistency across subsequent frames
- Use material metaphors: "butter-soft suede" beats "soft fabric" for AI comprehension

---

### DETECTION SIGNALS

**Material Flattening:**
- Leather appears as smooth plastic rather than grained hide
- Denim loses twill weave and becomes blue cotton
- Silk loses sheen and drape, becomes matte rayon
- Wool loses fiber texture, becomes smooth felt
- Lace loses openwork pattern, becomes stamped texture

**Detail Erasure:**
- Buttons disappear or become smooth bumps
- Seams vanish (French seams, topstitching, flat-felled)
- Zippers lose teeth and puller detail
- Pockets become painted-on rather than constructed
- Pleats, gathers, and tucks flatten into smooth planes

**Hardware Disappearance:**
- Belt buckles lose metal sheen and engraving
- Eyelets and grommets become simple holes
- Chain straps become smooth strips
- Metal snaps and rivets vanish
- Embroidery becomes printed pattern

**Drape Physics Failure:**
- Heavy fabrics (wool coat) float like chiffon
- Light fabrics (silk) cling like spandex
- Gravity ignored — skirts hover horizontally
- Wind affects all fabrics identically regardless of weight

---

### MATERIAL SPECIFICITY VOCABULARY

**Fabric Weave & Texture:**
```
[Material] with visible [weave/texture]: 
- denim with twill weave and white weft threads
- tweed with flecked wool texture and herringbone pattern
- corduroy with distinct wales/ribs
- poplin with tight plain weave and slight sheen
- seersucker with puckered stripe texture
- bouclé with looped yarn texture
```

**Leather & Hide:**
```
full-grain leather with natural patina and pore texture, top-grain leather with subtle grain, suede with napped surface, nubuck with fine sanded texture, patent leather with high-gloss mirror finish, distressed leather with creases and wear marks
```

**Metal & Hardware:**
```
brass buckle with engraved detail, silver zipper with visible teeth and pull tab, copper rivets with patina, steel eyelets with rolled edges, gold chain link with individual ring detail, pewter buttons with molded relief
```

**Construction Detail:**
```
French seams with enclosed raw edges, flat-felled seams with double stitching, topstitching at 1/8 inch from edge, double-needle stitching, bias-cut drape, princess seams shaping torso, darted bodice, gathered skirt with even pleats, box pleats with sharp creases
```

**Drape & Weight:**
```
heavy wool coat with structured shoulders and weighty drape, fluid silk charmeuse with liquid drape and cling, crisp cotton poplin with sharp creases and stand-away structure, stiff denim with rigid drape breaking at knee, airy chiffon with floating movement and transparency
```

---

### FIX STRATEGIES

**1. The Material-First Clause**
- Place material description early in prompt:
  - Good: `Woman in full-grain leather jacket with visible grain and brass hardware...`
  - Bad: `Woman in jacket, leather material, looking at camera...`

**2. The Construction Detail Stack**
- List 2–3 specific construction elements:
  - `denim jacket with flat-felled seams, copper rivets at stress points, selvedge edge visible at cuff`
- Concrete details anchor the model better than generic material names

**3. The Hardware Macro**
- Specify visible hardware explicitly:
  - `silver YKK zipper with metal teeth and leather pull tab`
  - `brass buckle with engraved brand mark and prong closure`
- Brand names (YKK, RiRi) activate stronger material priors

**4. The Drape Physics Command**
- Specify how fabric behaves under gravity/movement:
  - `heavy wool skirt with structured A-line drape, breaking naturally at knee`
  - `silk blouse with fluid drape, clinging slightly at waist, floating at sleeves`

**5. The Texture Close-Up**
- For hero garment shots, specify macro detail:
  - `extreme close-up of tweed weave showing individual yarn colors`
  - `macro of leather grain with natural scarring and pore detail`

**6. The Layering Specification**
- For layered outfits, specify each layer distinctly:
  - `crisp white cotton oxford shirt under charcoal wool V-neck sweater with ribbed cuffs`
- Prevents layers from merging into single blob

**7. The Wrinkle & Wear Realism**
- `natural creases at elbow and waist from movement`, `subtle wear at collar and cuffs`
- Adds realism that helps model render material as physical object

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Positive: `(detailed clothing:1.2), intricate fabric texture, visible weave, hardware detail`
- Negative: `smooth plastic clothing, generic fabric, missing buttons, no texture, painted-on clothes`
- Use `fashion photography` or `editorial` style suffix for garment priority

**Flux / Flux2:**
- Material description in first 15 words
- Use brand names and technical terms: `selvedge denim`, `full-grain Horween leather`, `cashmere knit`
- No negative prompts; rely on positive specificity

**LTX Video:**
- Clothing detail often degrades across frames as motion dominates
- Guardrail: `stable clothing detail across frames, consistent fabric texture, no material morphing`
- Specify `fashion cinematography` style for garment priority

---

### EXAMPLE FIX PROMPTS

**Fix: Leather Detail (Flux):**
> `Portrait of man in full-grain Horween leather jacket with visible natural grain and pore texture, brass YKK zipper with metal teeth and leather pull tab, flat-felled seams with contrast stitching, jacket showing natural creases at elbow, heavy weight drape, soft window light revealing leather texture, photorealistic fashion photography`

**Fix: Denim Construction (SDXL):**
> Positive: `Fashion editorial of model in raw selvedge denim jeans with visible twill weave and white weft threads, copper rivets at pocket corners, chain-stitched hem, natural whiskering at thigh, rigid drape breaking at knee, detailed clothing texture`
> Negative: `smooth generic pants, missing texture, plastic look, no detail, painted-on denim`

**Fix: Silk Drape (LTX):**
> `Subject: Woman in silk charmeuse evening gown. Style: Fashion cinematography. Motion: Walking with fluid fabric movement. Guardrails: Stable silk sheen across frames, consistent drape physics, no fabric morphing, visible material texture.`

---

### DETECTION CHECKLIST
- [ ] Material texture visible (weave, grain, nap)?
- [ ] Hardware present and detailed (buttons, zippers, buckles)?
- [ ] Construction seams visible and correct?
- [ ] Drape appropriate to material weight?
- [ ] No material flattening or plastic appearance?
- [ ] Layers distinct and separate?
- [ ] Wear/crease detail present for realism?
- [ ] Consistent across series/frames?

---

### TECHNICAL NOTES FOR AI GENERATION
- Generic material names ("cotton", "leather") produce generic results
- Technical terms ("selvedge", "full-grain", "twill weave", "flat-felled") activate stronger priors
- Brand names (Horween, YKK, Cone Mills) add specificity when known to model
- Hardware detail is often the first thing lost at lower resolutions
- In video, fabric physics (drape, wind response) often degrades before texture detail
- Fashion photography and editorial style suffixes prioritize garment rendering
