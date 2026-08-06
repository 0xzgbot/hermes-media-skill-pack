# SKILL: FLUX.2 Dev Product & Hero Photography
## Version: 1.0 | Hermes Agent Flux2 Commercial & E-Commerce Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for generating commercial-grade product photography with FLUX.2 Dev. This skill encodes the precise studio lighting vocabulary, material rendering triggers, reflection control strategies, and HEX-color-accurate product representation required for hero shots, e-commerce catalogs, and campaign assets. Covers white-background alternatives (critical for FLUX.2 Dev), surface interaction physics, packaging detail, and the specific positive-only constraint architecture for product artifact prevention.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Product Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled)
- **Token Priority:** Product identity must lead. "Titanium smartwatch" or "Matte black ceramic vase" must be the first 3–5 tokens.
- **Prompt Length:** 40–70 words for single-product hero shots. Multi-product layouts up to 100 words.
- **Guidance Scale:** 4.0–5.0 for products (higher adherence needed for brand accuracy; 4.5 is the sweet spot)
- **Steps:** 30–40 for material fidelity and surface detail. Reflections and transparency need 35+.
- **Resolution:** 1024×1024 base for most products; 1536×1536 for detail-heavy items (jewelry, watches, tech). Generate at final aspect ratio.
- **HEX Color Support:** FLUX.2 Dev follows HEX codes with high fidelity when tied to specific elements.

**The "White Background" Problem & Solutions:**
FLUX.2 Dev produces fuzzy, washed-out results when prompted with "white background." Use these tested reframes:

| Forbidden Phrase | Replacement | Result |
|-----------------|-------------|--------|
| "white background" | "clean neutral studio environment" | Crisp edges, no fuzziness |
| "white background" | "minimal light gray seamless backdrop" | Slight tonal separation |
| "white background" | "pure white cyclorama with soft gradient falloff" | Professional studio look |
| "white background" | "isolated on clean bright surface" | Product-forward, no backdrop issues |
| "white background" | "clinical product photography setting" | Medical/tech aesthetic |
| "white background" | "infinite white curve with subtle shadow" | Classic e-commerce look |

**Material Rendering Trigger Words:**

| Material | Primary Trigger | Secondary Triggers | Light Interaction |
|----------|----------------|-------------------|-------------------|
| **Brushed Metal** | brushed aluminum/titanium finish | unidirectional scratch pattern, satin sheen | Softbox from above showing brush direction |
| **Polished Chrome** | mirror-polished chrome | high reflectivity, sharp environmental reflections | Hard source creating distinct specular highlight |
| **Matte Ceramic** | matte bisque finish | micro-texture surface, non-reflective | Large soft source, even illumination, soft shadow |
| **Glass / Crystal** | optical clarity, refractive index | caustic light patterns, internal reflections | Backlight or strong side light showing transmission |
| **Leather** | full-grain leather texture | natural hide pattern, patina, pore structure | Raking light across surface showing texture |
| **Carbon Fiber** | woven carbon fiber twill | directional weave pattern, matte-black depth | Grazing light emphasizing weave geometry |
| **Wood** | bookmatched walnut grain | open-pore texture, natural figuring | Warm light from side showing grain depth |
| **Fabric / Textile** | woven cotton/linen/silk texture | thread count visible, natural drape | Soft even light, subtle shadow in folds |
| **Liquid / Beverage** | surface tension meniscus | condensation droplets, light refraction | Backlight for transparency, side light for body |
| **Gemstone / Jewelry** | faceted brilliant cut | dispersion, fire, scintillation | Point source creating sparkle, dark field setup |

**Surface & Shadow Control:**
- **Contact shadow:** Small, dark shadow directly beneath product where it touches surface — signals weight and grounding
- **Cast shadow:** Larger, softer shadow extending from product — signals light direction and environment scale
- **Reflection shadow:** Mirror image of product on glossy surface — doubles visual weight, adds luxury
- **No shadow = floating:** Always include shadow language for grounded realism

**Three-Point Studio Light for Products:**
```
Key light: Large softbox from camera-left 45° above product, creating primary highlight and form shadow
Fill light: White reflector or second softbox at lower intensity from camera-right, filling shadows to show detail
Rim/back light: Small hard source from behind product, separating from background, creating edge glow
```

---

### PROMPT ARCHITECTURE

**Core Product Hero Template (FLUX.2 Dev):**
```
[Product identity]: [Specific product name/type], [material], [color/HEX], [size/scale], [key feature]
[Position/pose]: [Centered/angled/dynamic], [orientation], [interaction with surface]
[Surface]: [Marble/concrete/wood/glass/fabric], [color], [texture], [reflection quality]
[Lighting]: [Three-point description], [key direction + quality], [fill ratio], [rim presence]
[Camera]: Shot on [Phase One IQ4 / Canon EOS R5 / etc.], [lens]mm macro/standard, f/[aperture]
[Style]: [Commercial product photography / editorial still life / hero shot / catalog]
[Background]: [Clean neutral / gradient / environmental context / lifestyle setting]
[Detail]: [Specific feature to highlight: stitching, button, screen, texture, label]
```

**Guardrails (Positive-Only Product Safety):**
```
clean product edges, consistent material surface, natural shadow grounding,
realistic scale proportions, accurate color representation, sharp focus on product,
coherent reflection behavior, believable light interaction with material,
no floating objects, no distorted perspective, no artificial glow around edges
```

**E-Commerce Multi-Angle Prompt Variations:**
For generating consistent product across angles, lock these and vary only angle:
- Product description (identical)
- Material and color (identical)
- Lighting setup (identical)
- Camera system (identical)
- Background (identical)

Vary: angle descriptor ("front three-quarter," "top-down flat lay," "detail macro," "lifestyle in use")

---

### ADVANCED TECHNIQUES

**1. The Floating Hero Shot**
- Setup: Product suspended in clean space, dramatic lighting
- Product: "Matte black wireless headphones, #1A1A1A, floating at 15° angle"
- Light: "Dramatic side lighting from left creating strong form shadow on right, subtle rim light from behind outlining ear cup profile, soft fill maintaining shadow detail"
- Surface: "No surface — pure floating presentation with soft contact shadow beneath suggesting levitation"
- Camera: "Shot on Phase One IQ4 with 120mm macro at f/8, sharp focus throughout product"
- Background: "Clean neutral gray gradient from light to dark, no environmental distraction"
- Emotional: Premium, technological, aspirational, weightless innovation
- Best For: Tech launches, hero banners, flagship product reveals

**2. The Lifestyle Context Shot**
- Setup: Product in authentic use environment
- Product: "Artisan ceramic coffee mug, matte terracotta #C45D3A, hand-thrown irregular texture"
- Environment: "On weathered oak farmhouse table, morning sunlight streaming through linen curtain, steam rising from coffee"
- Light: "Warm 4000K morning sun from window left, soft fill from white wall right, steam backlit showing particles"
- Camera: "Shot on Canon EOS R5 with 50mm f/1.2 at f/2.8, shallow depth of field with mug sharp, background softly blurred"
- Context: "Hand reaching for mug, morning newspaper partially visible, authentic lived-in kitchen"
- Emotional: Warmth, authenticity, everyday luxury, craft appreciation
- Best For: Food & beverage, home goods, lifestyle brands, artisan products

**3. The Material Macro Reveal**
- Setup: Extreme close-up of material texture as hero
- Product: "Full-grain Italian leather wallet, #3D2B1F dark brown, natural hide pores and creasing visible"
- Light: "Raking light from shallow angle emphasizing surface topography, warm 3200K tungsten, deep shadows in grain valleys"
- Camera: "Shot on Canon EOS R5 with 100mm macro at f/5.6, 1:1 magnification, flat field sharpness"
- Detail: "Stitching detail visible — waxed linen thread, saddle stitch pattern, hand-burnished edges"
- Background: "Dark velvet surface, absorbs light, no reflection competition"
- Emotional: Craft, heritage, tactile desire, quality obsession
- Best For: Leather goods, luxury accessories, craft products, material marketing

**4. The Splash / Action Product Shot**
- Setup: Product interacting with liquid or motion
- Product: "Clear glass bottled water, condensation droplets on surface, water splash erupting from open top"
- Light: "High-speed flash freeze lighting, hard source from behind showing liquid transparency, front fill showing bottle label"
- Camera: "Shot on Phase One IQ4 with 120mm macro at f/11, high-speed capture freezing splash mid-air"
- Action: "Water crown splash frozen at peak, droplets suspended in air, surface tension visible on ascending column"
- Background: "Deep blue gradient #001F3F, water droplets catching light like jewels"
- Emotional: Refreshment, purity, energy, natural power
- Best For: Beverages, cosmetics, sports products, any liquid product

**5. The Tech Product Studio Shot**
- Setup: Clean, precise, specification-forward technology product
- Product: "Slim aluminum laptop computer, space gray #8E8E93, open at 110° angle, screen displaying colorful abstract wallpaper"
- Surface: "Polished black granite reflecting product base, subtle mirror image"
- Light: "Three-point setup: large softbox from above creating even illumination across keyboard, fill from front preventing screen reflection, subtle rim from behind defining thin edge profile"
- Camera: "Shot on Sony A7R V with 90mm macro at f/8, product photography perspective, slight high angle showing keyboard and screen"
- Detail: "Individual key backlight visible, USB-C ports on side in sharp focus, hinge mechanism precision"
- Background: "Infinite white curve, professional tech product aesthetic"
- Emotional: Precision, innovation, professional capability, design excellence
- Best For: Electronics, computers, phones, professional equipment

**6. The Jewelry Dark Field Shot**
- Setup: Gemstone or precious metal against dark background
- Product: "Round brilliant cut diamond engagement ring, platinum band, fire and scintillation visible"
- Light: "Dark field lighting — bright source from behind and below ring, dark background, only refracted and reflected light visible in stone and metal"
- Camera: "Shot on Hasselblad X2D with 120mm macro at f/11, focus stacking for total sharpness"
- Detail: "Facet pattern visible in pavilion and crown, dispersion creating rainbow fire, platinum luster with subtle texture"
- Background: "Pure black velvet, no reflection, no detail, infinite depth"
- Emotional: Eternity, commitment, precious rarity, light captured
- Best For: Jewelry, gemstones, luxury watches, precious metals

**7. The Packaging Unboxing Narrative**
- Setup: Product reveal through packaging layers
- Product: "Premium skincare serum bottle, frosted glass #F5F5F5, gold foil label, dropper cap"
- Packaging: "Opened rigid box with tissue paper partially unfolded, product nestled in custom cutout, unboxing moment frozen"
- Light: "Soft even studio light from large source above, gentle shadows in box interior, gold foil catching warm highlights"
- Camera: "Shot on Canon EOS R5 with 100mm macro at f/5.6, 45° angle showing both product and packaging interior"
- Detail: "Embossed logo on box lid, tissue paper texture, dropper pipette visible through frosted glass"
- Background: "Soft neutral surface, slightly darker than product for separation"
- Emotional: Discovery, luxury experience, anticipation, gift-worthy
- Best For: Cosmetics, luxury goods, subscription boxes, premium brands

---

### EXAMPLE PROMPTS

**Floating Tech Hero:**
> Titanium smartwatch with sapphire crystal face and matte black ceramic bezel, floating at slight angle against clean neutral gray gradient background, shot on Phase One IQ4 with 120mm macro at f/8, dramatic side lighting from left creating sharp specular highlight on titanium case and strong form shadow, subtle rim light from behind defining watch edge profile, soft contact shadow beneath suggesting weight, individual links of titanium bracelet visible with brushed finish texture, watch face displaying 10:10 with crisp numerals, premium commercial product photography, no environmental distraction, precision engineering aesthetic

**Lifestyle Coffee Context:**
> Hand-thrown ceramic coffee mug in matte terracotta #C45D3A with visible throwing rings and slight irregular rim, sitting on weathered oak farmhouse table with deep grain texture, warm morning sunlight streaming through sheer linen curtain from window left, steam rising from dark coffee surface backlit showing particles, shallow depth of field with mug in sharp focus and kitchen softly blurred in background, shot on Canon EOS R5 with 50mm f/1.2 at f/2.8, natural 4000K morning light, authentic lived-in atmosphere, lifestyle product photography, warmth and craft appreciation

**Jewelry Dark Field:**
> Round brilliant cut diamond solitaire engagement ring in platinum six-prong setting, dark field lighting with bright source from below creating internal fire and scintillation, rainbow dispersion visible in crown facets, platinum band showing subtle brushed texture, pure black velvet background absorbing all light, shot on Hasselblad X2D with 120mm macro at f/11, focus stacking sharpness throughout, facets visible in pavilion and crown, eternal precious rarity, luxury jewelry photography, no reflection competition, light captured in stone

---

### TECHNICAL NOTES FOR AI GENERATION
- **Product name first:** "Titanium smartwatch" outperforms "A smartwatch made of titanium" — first tokens carry 3x more weight.
- **HEX codes tied to elements:** "Primary color #FF6B35 on shoe upper" works far better than "#FF6B35" alone. Tie HEX to specific surfaces.
- **Material mentions early:** Material identity should appear within first 15 tokens for accurate surface rendering.
- **Never "white background":** Use "clean neutral studio environment," "light gray seamless," or "infinite white curve with subtle shadow."
- **Shadow = grounding:** Products without shadow language float unrealistically. Always include "natural shadow beneath," "contact shadow," or "soft cast shadow."
- **Reflection realism:** "Mirror reflection on polished surface" or "soft diffuse reflection on matte surface" — specify reflection character to match material.
- **Guidance 4.0–5.0 for products:** Higher than portrait guidance because brand accuracy and prompt adherence matter more than creative interpretation.
- **Steps 35+ for transparency:** Glass, liquid, and gemstone rendering requires more steps for accurate light transmission physics.
- **For multi-product layouts:** Use JSON structured prompt with `subjects` array for precise positioning and color control per item.
- **E-commerce consistency:** Generate hero first, then use I2V or img2img with locked seed for angle variations while maintaining identical product identity.
- **Label/text on products:** Use quotation marks around exact text: "Label reads 'ORGANIC COLD-PRESSED' in small serif font." Short text (2–5 words) renders most accurately.
