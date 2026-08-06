# SKILL: FLUX.2 Dev Fashion & Beauty Editorial
## Version: 1.0 | Hermes Agent Flux2 Fashion Photography Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for generating high-end fashion editorial and beauty imagery with FLUX.2 Dev. This skill encodes the precise fabric rendering vocabulary, model direction language, makeup detail triggers, and editorial composition grammar required for runway lookbooks, beauty campaigns, and magazine-quality fashion photography. Covers garment draping physics, skin prep levels for beauty, pose architecture, and the specific positive-only constraint system for fashion artifact prevention.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Fashion Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled)
- **Token Priority:** Subject identity + garment description must lead. "Model wearing structured camel wool overcoat" not "Fashion editorial of a model in a coat."
- **Prompt Length:** 50–90 words for fashion editorial. Beauty close-ups 40–60 words.
- **Guidance Scale:** 3.8–4.5 for fashion (balance creative interpretation with garment accuracy)
- **Steps:** 30–38 for fabric texture and drape fidelity.
- **Resolution:** 1024×1280 for vertical editorial; 1280×1024 for horizontal. Match publication aspect ratio.
- **HEX Codes:** Essential for brand color accuracy in fashion. Tie to specific garment panels.

**The Fashion Pose Vocabulary:**

| Pose Category | Description Prompt | Energy Level | Best For |
|--------------|-------------------|-------------|----------|
| **The Static Editorial** | "Standing with weight on back foot, front foot pointed, shoulders relaxed, gaze directed past camera" | Low, controlled | Lookbooks, catalog, minimalist |
| **The Power Stance** | "Wide stance, hands on hips, chin slightly raised, direct confrontational gaze" | High, assertive | Power dressing, suits, empowerment |
| **The Walking Stride** | "Mid-stride captured in motion, one leg forward, arms in natural swing, hair in motion" | Medium, dynamic | Street style, movement, energy |
| **The Reclining Lounge** | "Reclined on surface, body elongated, one arm supporting head, relaxed languid pose" | Low, sensual | Lingerie, luxury, perfume |
| **The Three-Quarter Turn** | "Body turned 45° from camera, head turned back toward lens, shoulder leading" | Medium, flattering | Classic portraiture, most body types |
| **The Detail Showcase** | "Hand raised to display accessory, wrist and forearm extended, garment sleeve featured" | Low, focused | Jewelry, watches, handbags |
| **The Candid Moment** | "Laughing with head tilted back, genuine unposed expression, hair in disarray" | High, authentic | Lifestyle, denim, casual brands |
| **The Architectural Shape** | "Arms extended creating geometric shape with body, extreme posture, sculptural form" | High, avant-garde | Avant-garde, couture, art fashion |

**Fabric Rendering Trigger Words:**

| Fabric | Primary Trigger | Drape Behavior | Light Response |
|--------|----------------|---------------|----------------|
| **Silk / Satin** | Liquid drape, luminous sheen, flowing movement | Falls in fluid cascades, follows gravity | High specular highlight, reflects environment |
| **Wool / Cashmere** | Soft nap, fuzzy surface, substantial weight | Structured but soft, holds shape with softness | Diffuse reflection, no sharp highlights |
| **Denim** | Twill weave visible, indigo dye depth, rigid drape | Holds structure, breaks at knees/elbows | Raking light shows weave texture |
| **Leather** | Full-grain texture, natural creasing, patina | Stiff drape, holds angular shapes | Sharp specular highlight, shows wear patterns |
| **Linen** | Slubbed texture, natural irregularity, crisp hand | Wrinkles authentically, airy volume | Bright diffuse, shows texture in folds |
| **Tulle / Organza** | Transparent layers, volumetric structure, ethereal | Holds shape away from body, architectural | Backlight shows transparency layers |
| **Sequin / Beaded** | Reflective discs, dimensional texture, sparkle | Follows body contour, adds bulk | Point source creates scatter sparkle |
| **Velvet** | Dense pile, light-absorbing depth, rich color | Heavy drape, falls straight, no flyaway | No specular — light sinks into surface |
| **Technical / Athletic** | Smooth synthetic, four-way stretch, matte or gloss | Follows body exactly, compression fit | Even illumination, shows muscle beneath |
| **Knit / Jersey** | Loop structure, stretch recovery, casual ease | Drapes close to body, shows form | Soft light, shows knit pattern at close range |

**Skin Prep Levels for Beauty Photography:**

| Level | Description | Skin Descriptors | Best For |
|-------|------------|------------------|----------|
| **Level 0 — Raw** | No makeup, natural texture, authenticity | "Bare skin, visible pores, natural oil, no makeup, authentic texture" | Skincare, clean beauty, natural brands |
| **Level 1 — Minimal** | Tinted moisturizer, slight evenness | "Barely-there makeup, skin showing through, natural glow, minimal coverage" | Everyday beauty, "no-makeup" makeup |
| **Level 2 — Polished** | Foundation, concealer, natural finish | "Flawless but natural skin, even tone, subtle luminosity, polished complexion" | Standard beauty, most cosmetics |
| **Level 3 — Glamour** | Full coverage, contour, highlight | "Immaculate complexion, sculpted cheekbones, highlighted brow bone, glam finish" | Red carpet, evening, luxury |
| **Level 4 — Editorial** | Artistic, exaggerated, transformative | "Porcelain canvas, dramatic contour, artistic makeup application, transformative beauty" | High fashion, avant-garde, artistic |

**Makeup Detail Triggers:**
- **Eyes:** "Smoky eyeshadow gradient from charcoal to bronze, winged liquid liner with sharp flick, individual false lashes visible at lash line"
- **Lips:** "Matte terracotta lipstick #B85C38 with defined Cupid's bow, slight overlining, no gloss"
- **Brows:** "Feathered brow hairs brushed upward, microbladed hair strokes visible, natural arch"
- **Skin:** "Subtle highlighter on cheekbone catching light, matte finish with no powder visible"
- **Nails:** "Almond-shaped nails in deep burgundy #722F37, glossy top coat, cuticles neat"

---

### PROMPT ARCHITECTURE

**Core Fashion Editorial Template (FLUX.2 Dev):**
```
[Model identity]: [Age range, ethnicity, body type, hair color/style, distinctive features]
[Wearing]: [Garment description — fabric, color/HEX, cut, silhouette, key detail]
[Pose]: [Specific pose from vocabulary above, body language, gaze direction]
[Environment]: [Studio / location / set design, color palette, props]
[Lighting]: [Key source + quality + direction + color temp], [mood of light]
[Camera]: Shot on [camera system], [lens] at f/[aperture], [shot type]
[Style]: [Editorial reference — Vogue / Harper's / street style / lookbook]
[Atmosphere]: [Wind, movement, haze, grain, film stock if applicable]
[Mood]: [Emotional register — confident / vulnerable / powerful / playful]
```

**Core Beauty Close-Up Template:**
```
[Model identity]: [Age, ethnicity, skin tone, eye color, hair pulled back or styled]
[Skin prep level]: [Level 0–4 description]
[Makeup]: [Eyes / lips / brows / skin / nails — specific colors and techniques]
[Lighting]: [Beauty lighting setup — butterfly / Rembrandt / split / clamshell]
[Camera]: Shot on [camera], [macro lens] at f/[aperture], extreme close-up
[Background]: [Clean / gradient / contextual]
[Detail]: [Specific feature to hero — lips / eyes / skin texture / brows]
```

**Guardrails (Positive-Only Fashion Safety):**
```
natural fabric draping, realistic garment construction, coherent seam lines,
accurate proportion fitting, authentic material behavior, believable weight and movement,
correct anatomy under clothing, natural pose mechanics, realistic hair-fabric interaction,
no floating hems, no impossible seams, no texture blurring on detail areas
```

---

### ADVANCED TECHNIQUES

**1. The Runway Exit Shot**
- Setup: Model at end of runway, full body, dramatic lighting
- Model: "Androgynous model, 185cm, slicked-back hair, strong cheekbones"
- Garment: "Structured oversized blazer in charcoal wool #4A4A4A, wide-leg trousers pooling at ankle, no shirt beneath blazer"
- Pose: "Walking stride captured mid-step, one leg forward, arms swinging naturally, gaze fixed forward past camera"
- Light: "Dramatic overhead spotlight creating pool of light around model, deep black void beyond spot edge, high contrast"
- Camera: "Shot on Hasselblad X2D with 80mm at f/4, full body, slight low angle emphasizing height and power"
- Atmosphere: "Dust particles visible in spotlight beam, silence and tension of empty runway"
- Emotional: Power, fashion as armor, androgynous strength, theatrical presentation
- Best For: Runway documentation, designer portfolios, fashion week coverage

**2. The Beauty Macro Detail**
- Setup: Extreme close-up of makeup detail, face filling frame
- Model: "Young Black woman, deep brown skin with warm undertone, hair pulled back in tight bun"
- Makeup: "Graphic eyeliner in electric cobalt #0047AB, sharp geometric wing extending to temple, matte nude lip #C4A484, skin luminous with no powder visible"
- Light: "Clamshell beauty lighting — large soft source above with reflector below, even illumination, subtle shadow under cheekbone"
- Camera: "Shot on Phase One IQ4 with 120mm macro at f/8, extreme close-up of eye and cheek area"
- Background: "Clean neutral warm gray, no distraction from graphic makeup"
- Emotional: Precision, artistry, bold self-expression, contemporary beauty
- Best For: Beauty campaigns, makeup brand launches, editorial beauty stories

**3. The Couture Detail Showcase**
- Setup: Close-up of craftsmanship detail in haute couture garment
- Garment: "Hand-beaded haute couture gown, thousands of crystal beads forming floral pattern, silk tulle base, twelve layers of petticoat"
- Detail: "Extreme close-up of bodice beading — individual crystal facets catching light, threadwork visible, bead pattern forming climbing rose"
- Light: "Raking light from shallow angle showing three-dimensionality of beadwork, warm tungsten 3200K, deep shadows between beads"
- Camera: "Shot on Hasselblad X2D with 120mm macro at f/11, 1:1 magnification"
- Background: "Dark velvet absorbing light, beads appear to float in darkness"
- Emotional: Obsessive craft, luxury as labor, invisible hours, precious rarity
- Best For: Couture houses, luxury positioning, craftsmanship stories

**4. The Street Style Candid**
- Setup: Authentic street fashion, unposed, environmental context
- Model: "Tokyo street style subject, early 20s, layered outfit, distinctive personal style"
- Garment: "Oversized vintage denim jacket over neon green technical vest, baggy cargo pants, chunky platform sneakers, multiple silver chains"
- Environment: "Shibuya crossing at dusk, neon signs reflecting in puddles, crowd motion blur in background"
- Pose: "Candid mid-stride, checking phone, unaware of camera, natural posture"
- Light: "Mixed neon sources — magenta from left, cyan from right, warm tungsten from storefront behind"
- Camera: "Shot on Fujifilm X-T5 with 23mm f/2 at f/2.8, slightly tilted frame, documentary aesthetic"
- Emotional: Authenticity, subculture, individual expression, urban energy
- Best For: Streetwear brands, youth culture, urban lifestyle, trend documentation

**5. The Minimalist Lookbook**
- Setup: Clean studio, garment-forward, no distraction
- Model: "Elongated figure, neutral expression, minimal makeup, hair pulled back"
- Garment: "Cashmere turtleneck sweater in oatmeal #E6DCC4, relaxed fit, ribbed collar and cuffs, natural drape"
- Pose: "Static editorial stance, weight on back foot, arms relaxed at sides, three-quarter turn"
- Light: "Large softbox from camera-left creating gentle modeling, soft fill from right, minimal shadow"
- Background: "Clean warm white seamless, no texture, no gradient, pure garment focus"
- Camera: "Shot on Phase One IQ4 with 80mm at f/8, full body, eye-level"
- Emotional: Quiet luxury, essentialism, investment dressing, timelessness
- Best For: Luxury basics, cashmere, minimal brands, capsule collections

**6. The Avant-Garde Shape**
- Setup: Extreme silhouette, sculptural fashion, art reference
- Model: "Tall thin model, pale skin, hair styled into architectural shape"
- Garment: "Sculptural foam construction in optic white, exaggerated shoulders creating triangular silhouette, no recognizable clothing elements"
- Pose: "Arms extended creating geometric shape with body, profile view emphasizing silhouette, ballet-inspired foot position"
- Light: "Harsh directional light creating sharp shadow, single hard source from left, pure black background"
- Camera: "Shot on Hasselblad X2D with 50mm at f/11, full body silhouette, centered"
- Emotional: Fashion as sculpture, boundary-pushing, art object, deconstruction
- Best For: Avant-garde designers, art-fashion collaborations, museum exhibitions

**7. The Lingerie / Intimate**
- Setup: Soft, sensual, respectful, luxury positioning
- Model: "Woman in late 20s, confident relaxed expression, hair in natural waves"
- Garment: "French lace bodysuit in deep burgundy #722F37, delicate Chantilly lace pattern, silk satin panels"
- Pose: "Reclining on velvet chaise, body elongated, one arm above head, gaze soft and direct"
- Light: "Large soft source from above and left creating gentle wrap-around, warm 2800K tungsten, deep shadows in fabric folds"
- Camera: "Shot on Canon EOS R5 with 85mm f/1.2 at f/2.0, medium shot, slight high angle"
- Atmosphere: "Soft focus background, velvet texture visible, intimate but empowered mood"
- Emotional: Confidence, self-possession, luxury intimacy, feminine power
- Best For: Lingerie brands, perfume, luxury boudoir, female-focused campaigns

---

### EXAMPLE PROMPTS

**Runway Power Exit:**
> Androgynous model with slicked-back hair and strong cheekbones wearing structured oversized charcoal wool blazer #4A4A4A with wide-leg trousers pooling at ankle and no shirt beneath, walking stride captured mid-step with one leg forward and arms swinging naturally, gaze fixed forward with confrontational confidence, dramatic overhead spotlight creating pool of light around figure with deep black void beyond spot edge, dust particles visible in light beam, shot on Hasselblad X2D with 80mm at f/4 from slight low angle showing full body, high contrast runway lighting, fashion as armor, theatrical presentation power

**Beauty Graphic Eye Macro:**
> Extreme close-up of young Black woman with deep brown skin and warm undertone, hair pulled back in tight bun, graphic eyeliner in electric cobalt #0047AB with sharp geometric wing extending to temple, matte nude lip #C4A484, skin luminous with no powder visible, clamshell beauty lighting with large soft source above and silver reflector below creating even illumination, subtle shadow under cheekbone defining bone structure, shot on Phase One IQ4 with 120mm macro at f/8, clean neutral warm gray background, precision makeup artistry, bold contemporary self-expression

**Minimalist Cashmere Lookbook:**
> Elongated model with neutral expression and minimal makeup wearing oatmeal cashmere turtleneck sweater #E6DCC4 in relaxed fit with ribbed collar and natural drape, static editorial stance with weight on back foot and three-quarter turn, large softbox from camera-left creating gentle modeling on fabric texture, soft fill from right with minimal shadow, clean warm white seamless background with no texture or gradient, shot on Phase One IQ4 with 80mm at f/8 full body eye-level, quiet luxury essentialism, timeless investment dressing, pure garment focus

---

### TECHNICAL NOTES FOR AI GENERATION
- **Model identity before garment:** "Model wearing red dress" underperforms "Woman in structured crimson silk gown" — garment detail should appear within first 12 tokens.
- **Fabric before color:** "Silk gown in crimson" outperforms "Crimson silk gown" for FLUX.2 — material identity triggers rendering pipeline before color assignment.
- **Pose described behaviorally:** "Weight on back foot, shoulders relaxed" outperforms "standing pose" — FLUX.2 interprets body mechanics from behavioral descriptions.
- **Hair-fabric interaction:** Mention hair touching fabric or wind direction for naturalism: "Hair blowing across shoulder, interacting with silk collar."
- **Guidance 3.8–4.5:** Below 3.5 = garment details drift. Above 5.0 = over-saturated, unrealistic fabric rendering.
- **No "white background":** Use "clean warm white seamless," "neutral studio backdrop," or "minimal environment."
- **Beauty lighting named:** "Clamshell," "Butterfly," "Rembrandt," "Split" — FLUX.2 recognizes classic beauty lighting patterns.
- **Film stock for editorial mood:** "Kodak Portra 400" for warm editorial; "Fujifilm Pro 400H" for cool editorial.
- **For lookbook consistency:** Lock model description, camera, lighting, and background. Vary only garment and pose.
- **Accessory detail:** "Hand raised to display gold bracelet, wrist extended, forearm visible, bracelet catching light" — explicit hand position prevents anatomical issues.
- **Shoe visibility:** In full-body fashion, mention "shoes visible" or specific footwear — FLUX.2 often omits or blurs feet unless explicitly directed.
