# SKILL: FLUX.2 Dev Macro, Texture & Surface Detail
## Version: 1.0 | Hermes Agent Flux2 Extreme Close-Up & Material Fidelity Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for generating extreme close-up, macro, and surface detail imagery with FLUX.2 Dev. This skill encodes the precise shallow-DoF vocabulary, tactile rendering triggers, micro-texture hierarchies, and material interaction physics required for hero detail shots, material libraries, and tactile marketing imagery. Covers organic textures (skin, wood, stone, fabric), synthetic surfaces (metal, glass, plastic, carbon fiber), and hybrid materials with FLUX.2 Dev's specific positive-only constraint architecture.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Macro Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled)
- **Token Priority:** Subject + scale must lead. "Extreme close-up of weathered oak grain" or "Macro detail of human iris" — scale descriptor must be in first 5 tokens.
- **Prompt Length:** 40–70 words for macro shots. Too long and FLUX.2 summarizes away critical micro-detail.
- **Guidance Scale:** 4.0–4.8 for macro (high adherence needed for accurate texture; 4.5 optimal)
- **Steps:** 35–45 for micro-texture fidelity. Shallow DoF transitions need 40+ for smoothness.
- **Resolution:** 1024×1024 base; 1536×1536 for maximum detail extraction.
- **No "white background":** For isolated macro subjects, use "neutral dark field" or "clean clinical background."

**Macro Depth of Field Control:**

| Aperture | DoF at 1:1 Magnification | Effect | Best For |
|----------|-------------------------|--------|----------|
| **f/2.8** | Razor thin, ~1mm | Dreamy isolation, abstract quality | Artistic macro, abstract texture |
| **f/5.6** | Thin, ~2–3mm | Selective focus on key detail | Product detail, jewelry, food |
| **f/8** | Moderate, ~4–5mm | Detail area sharp, transition visible | Material studies, craft documentation |
| **f/11** | Acceptable, ~6–8mm | Most of subject sharp, some background | Flat subjects, coins, stamps |
| **f/16** | Deep for macro, ~10mm+ | Maximum sharpness, diffraction risk | Technical documentation, scientific |

**The Tactile Descriptor Hierarchy:**
These words trigger FLUX.2's surface rendering at highest fidelity:

1. **Physical process:** "Hand-sanded," "cast," "forged," "woven," "grown," "weathered" — implies authentic surface history
2. **Micro-scale features:** "Individual fibers," "crystal facets," "pore structure," "cell walls," "grain boundaries"
3. **Surface topology:** "Raised texture," "recessed grooves," "undulating surface," "peaked ridges"
4. **Light interaction:** "Specular highlight following surface contour," "diffuse scattering in valleys," "translucency at edges"
5. **Scale reference:** "At 10x magnification," "microscopic view," "SEM-like detail" — triggers hyper-detail mode

**Material-Specific Micro-Detail Triggers:**

| Material | Critical Micro-Detail | Light Technique | Scale Reference |
|----------|----------------------|-----------------|-----------------|
| **Human Skin** | Pore structure, sebaceous filaments, vellus hairs, collagen texture | Raking light at 15°, soft fill | 1:1 to 2:1 magnification |
| **Wood Grain** | Growth rings, vessel elements, rays, early/late wood contrast | Raking light showing relief | 1:1 to 3:1 |
| **Stone / Marble** | Crystalline structure, veining, fossil inclusions, polish marks | Diffused even light or raking | 1:1 to 2:1 |
| **Woven Fabric** | Individual warp and weft threads, selvedge, weave pattern | Grazing light showing texture | 2:1 to 5:1 |
| **Leather** | Grain pattern, pore structure, creasing, patina variation | Raking light, warm source | 1:1 to 3:1 |
| **Brushed Metal** | Unidirectional scratch pattern, satin sheen gradient | Softbox showing brush direction | 2:1 to 4:1 |
| **Carbon Fiber** | Weave geometry (twill/plain), fiber direction, resin depth | Grazing light at shallow angle | 3:1 to 5:1 |
| **Glass / Crystal** | Surface tension, micro-bubbles, striations, refractive caustics | Backlight or dark field | 1:1 to 3:1 |
| **Ceramic Glaze** | Crawling, crackle pattern, crystalline formation, thickness variation | Even light showing surface | 2:1 to 4:1 |
| **Biological (leaf, etc.)** | Cell structure, stomata, vein pattern, trichomes | Transmitted backlight | 3:1 to 10:1 |

---

### PROMPT ARCHITECTURE

**Core Macro Template (FLUX.2 Dev):**
```
[Scale declaration]: [Extreme close-up / Macro detail / Microscopic view / 10x magnification] of [subject]
[Subject identity]: [Material type], [specific variety], [condition/state]
[Surface detail]: [Micro-texture descriptors from hierarchy above]
[Light interaction]: [How light behaves on this specific surface]
[Camera]: Shot on [camera], [macro lens]mm, f/[aperture], [magnification ratio]
[DoF description]: [Razor thin / selective / deep focus], [what is sharp vs. soft]
[Background]: [Bokeh character, color, distance]
[Atmosphere]: [Grain, atmosphere, clinical or artistic treatment]
```

**Guardrails (Positive-Only Macro Safety):**
```
natural surface topology, authentic material texture, realistic light interaction,
coherent depth of field transition, believable magnification scale, accurate color representation,
no artificial smoothing of natural texture, no impossible surface perfection,
no synthetic uniformity where variation should exist
```

---

### ADVANCED TECHNIQUES

**1. The Human Iris Universe**
- Setup: Extreme close-up of eye, iris filling entire frame
- Subject: "Brown human iris at extreme magnification, radial muscle fibers visible, pigment variation from amber near pupil to chocolate at edge"
- Detail: "Collarette boundary visible, crypts of Fuchs in stroma, visible blood vessels in sclera at edge of frame, sharp limbal ring"
- Light: "Soft even light from ring flash creating flat illumination, single small catchlight at 2 o'clock position, no harsh shadow"
- Camera: "Shot on Canon EOS R5 with 100mm macro at f/5.6, 2:1 magnification, flat field sharpness on iris plane"
- DoF: "Selective focus — iris front surface razor sharp, sclera and eyelashes softly blurred"
- Emotional: Identity, biological uniqueness, universe in an eye, intimate surveillance
- Best For: Medical, identity, beauty, poetic abstraction

**2. The Weathered Wood Portrait**
- Setup: Extreme close-up of aged timber surface
- Subject: "Century-old oak beam surface, deep patina, hand-hewn texture with adze marks intersecting growth rings"
- Detail: "Individual vessel elements visible as small pores, medullary rays running perpendicular to grain creating quilted pattern, cracks filled with century-old dust"
- Light: "Raking light from extreme shallow angle creating deep relief shadows, warm 2800K tungsten emphasizing amber tones"
- Camera: "Shot on Phase One IQ4 with 120mm macro at f/8, 1.5:1 magnification, flat field correction"
- DoF: "Moderate depth showing surface topology across 5mm plane, background falling to abstract blur"
- Emotional: Time, craft, tree's life history, human touch across generations
- Best For: Heritage, craft, furniture, organic material marketing

**3. The Carbon Fiber Weave Geometry**
- Setup: Technical macro of composite material surface
- Subject: "2x2 twill carbon fiber weave, individual tow bundles 3K carbon, high-gloss resin finish"
- Detail: "Fiber direction changing every two bundles creating diagonal pattern, resin meniscus at fiber intersections, depth of weave visible through translucent resin"
- Light: "Grazing light at 10° from left emphasizing weave topography, second fill from right showing resin gloss, small specular highlights at fiber peaks"
- Camera: "Shot on Sony A7R V with 90mm macro at f/11, 3:1 magnification, focus stacked for total weave sharpness"
- Background: "Pure black, no reflection, carbon appears to float in void"
- Emotional: Precision engineering, motorsport, aerospace, technical excellence
- Best For: Automotive, aerospace, sports equipment, engineering marketing

**4. The Liquid Surface Tension**
- Setup: Macro of liquid behavior — droplet, splash, or meniscus
- Subject: "Water droplet suspended on leaf surface, surface tension creating perfect hemispherical dome"
- Detail: "Internal refraction showing leaf vein pattern magnified and inverted in droplet, contact angle visible where water meets leaf wax, meniscus curve at edge"
- Light: "Backlight through droplet creating bright caustic highlight, front fill showing leaf surface texture, droplet acting as lens"
- Camera: "Shot on Canon EOS R5 with 100mm macro at f/8, 2:1 magnification, focus on droplet front surface"
- Background: "Out-of-focus green leaf bokeh, natural environment suggested"
- Emotional: Fragility, natural physics, miniature world, dew freshness
- Best For: Nature, cosmetics (serum), beverages, organic products

**5. The Woven Thread Architecture**
- Setup: Extreme magnification of textile weave structure
- Subject: "Hand-woven linen fabric, individual flax fibers visible in thread structure, plain weave pattern"
- Detail: "Warp threads running vertical, weft horizontal, slight irregularity in thread spacing from hand process, fiber ends fraying at thread surface, slubbed texture"
- Light: "Grazing light from left at 20° showing thread relief, soft fill from right revealing fiber color variation from natural flax"
- Camera: "Shot on Phase One IQ4 with 120mm macro at f/5.6, 4:1 magnification, shallow DoF isolating one weave intersection"
- Background: "Same fabric continuing out of focus, abstract textile landscape"
- Emotional: Craft, slowness, natural material, hand process
- Best For: Textile brands, sustainable fashion, linen/cotton marketing, craft documentation

**6. The Brushed Metal Direction**
- Setup: Technical macro showing industrial surface finish
- Subject: "Grade 5 titanium surface with unidirectional brushed finish, #4 satin brush pattern"
- Detail: "Parallel scratch marks running left-to-right, slight variation in scratch depth creating satin sheen gradient, surface reflects environment as soft diffuse image"
- Light: "Large softbox from above showing brush direction through elongated specular highlight, no point source to avoid hard reflection"
- Camera: "Shot on Sony A7R V with 90mm macro at f/8, 3:1 magnification, polarizer reducing unwanted surface glare"
- Background: "Neutral gray, minimal, industrial documentation aesthetic"
- Emotional: Precision, industrial design, premium material, manufacturing excellence
- Best For: Industrial design, premium electronics, watchmaking, aerospace

**7. The Biological Micro-World**
- Setup: Extreme magnification of organic surface
- Subject: "Underside of fern frond, sori clusters containing sporangia, individual sporangium visible"
- Detail: "Sori arranged in rows along leaflet midrib, protective indusium flap visible, sporangia as tiny spheres in cluster, cell structure of leaflet surface"
- Light: "Transmitted backlight through thin leaflet tissue showing cell structure, front fill revealing surface texture, light passing through sporangia creating tiny glowing orbs"
- Camera: "Shot on Canon EOS R5 with MP-E 65mm at 5:1 magnification, f/4, focus stacked for complete depth"
- Background: "Bright diffuse backlight creating high-key silhouette effect, pure white"
- Emotional: Hidden worlds, botanical wonder, reproduction, nature's architecture
- Best For: Botanical, scientific, educational, nature documentaries, organic brands

---

### EXAMPLE PROMPTS

**Iris Universe Macro:**
> Extreme close-up of brown human iris filling entire frame, radial muscle fibers visible in stroma, pigment variation from amber near pupil to deep chocolate at limbal edge, collarette boundary creating texture ring, crypts of Fuchs visible as small pits, sclera with fine blood vessels at frame edge, soft even ring flash illumination with small catchlight at 2 o'clock, shot on Canon EOS R5 with 100mm macro at f/5.6 at 2:1 magnification, razor sharp focus on iris front surface with eyelashes softly blurred, biological uniqueness, identity in extreme detail

**Century Oak Wood Portrait:**
> Extreme close-up of century-old oak beam surface at 1.5:1 magnification, hand-hewn texture with adze marks intersecting growth rings, individual vessel elements visible as small pores, medullary rays running perpendicular to grain creating quilted pattern, cracks filled with century-old dust and patina, raking light from extreme shallow angle creating deep relief shadows, warm 2800K tungsten emphasizing amber and honey tones, shot on Phase One IQ4 with 120mm macro at f/8 with flat field correction, moderate depth showing surface topology, time and craft in organic material

**Carbon Fiber Weave Technical:**
> 3:1 magnification macro of 2x2 twill carbon fiber weave with 3K tow bundles, fiber direction changing every two bundles creating diagonal pattern, resin meniscus visible at fiber intersections, depth of weave visible through translucent high-gloss resin, grazing light at 10° from left emphasizing weave topography, small specular highlights at fiber peaks, shot on Sony A7R V with 90mm macro at f/11 focus stacked for total sharpness, pure black background with no reflection, precision engineering and technical excellence, aerospace material aesthetic

---

### TECHNICAL NOTES FOR AI GENERATION
- **Scale declaration first:** "Extreme close-up" or "Macro detail" must be in the first 5 words — FLUX.2 defaults to standard framing without explicit scale instruction.
- **Magnification ratios work:** "2:1 magnification" or "At 5x life size" — FLUX.2 interprets scale language and increases detail rendering accordingly.
- **Specific material names before generic:** "Grade 5 titanium brushed finish" outperforms "brushed metal" — alloy/species specificity triggers accurate rendering.
- **Light angle matters for texture:** "Raking light at 15°" or "Grazing light from left" — shallow angles emphasize surface relief more than frontal lighting.
- **Aperture controls DoF abstraction:** Lower f-numbers (f/2.8–f/4) create artistic abstraction; higher (f/8–f/11) create technical documentation.
- **Focus description essential:** "Razor sharp focus on front surface, background falling to creamy bokeh" — explicit focus plane prevents FLUX.2 from rendering everything equally sharp.
- **Guidance 4.0–4.8 for macro:** Higher than portraits because technical accuracy matters. 4.5 is optimal for most macro work.
- **Steps 35–45:** Micro-texture needs more processing steps. Below 30 = soft detail. Above 45 = diminishing returns.
- **No "highly detailed":** Replace with specific micro-features: "Individual fibers visible" or "Crystal facets catching light" — specificity beats generic quality tokens.
- **Polarizer mention:** "With polarizing filter" helps reduce unrealistic glare on reflective surfaces.
- **Focus stacking language:** "Focus stacked for total sharpness" or "Extended depth of field through stacking" — signals deep-focus macro aesthetic.
- **Biological specimens:** "Transmitted backlight" or "Dark field illumination" — specific microscopy lighting terms trigger accurate biological rendering.
- **Tactile marketing:** For products where touch is the selling point, include tactile adjectives: "Velvet pile you can almost feel," "Rough-hewn texture inviting touch" — FLUX.2 renders visual correlates of tactile experience.
