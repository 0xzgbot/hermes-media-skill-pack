# SKILL: Color Palette Injection
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Mastery of color control through natural language translation, HEX code injection, and palette psychology. AI models can interpret both explicit color names and HEX codes [^70^], but natural language descriptions of color relationships yield more coherent results than isolated color words. This skill provides the bridge between designer palettes and AI-comprehensible color language.

### TRIGGER KEYWORDS
color palette, color control, HEX code, color injection, palette psychology, color descriptor, color temperature, color saturation, specific color, brand color, warm palette, cool palette, monochromatic, complementary colors, color tone

### CORE RULES
- Translate HEX → natural language: temperature + saturation + brightness + material reference (#D4AF37 = "warm soft gold, like gilded leaf")
- Natural language beats isolated HEX in most models — but Flux and Midjourney can use HEX directly
- Specify color relationships, not just individual colors: "warm amber dominant with cool teal accent"
- Saturation needs a descriptor: "vivid/muted/desaturated/pastel" — not just the color name
- Color temperature is critical: "warm amber" vs. "cool steel blue" vs. "neutral white"
- Avoid color without context: "blue" is meaningless; "deep navy blue, slightly desaturated" works
- Material reference anchors color: "slate gray", "rust orange", "sage green" — instantly understandable

---

### HEX-TO-NATURAL-LANGUAGE TRANSLATION

**Core Principle:** AI models interpret HEX codes directly in some platforms (Flux, Midjourney, GPT-image) [^70^], but natural language descriptions of color temperature, saturation, and relationship produce more nuanced results across all models.

**Translation Method:**
1. Identify base HEX color
2. Determine color family (red, blue, green, etc.)
3. Add temperature (warm/cool)
4. Add saturation (vivid/muted/pastel/desaturated)
5. Add brightness (deep/light/bright/dark)
6. Add material or natural reference (ochre, slate, coral, sage)

---

### HEX TRANSLATION TABLE

| HEX | Natural Language | Temperature | Saturation | Material Ref |
|-----|------------------|-------------|------------|----------------|
| #FF0000 | Vivid crimson red | Warm | High | Ruby, blood, poppy |
| #DC143C | Deep crimson | Warm | High | Ruby, rose, velvet |
| #FF4500 | Burnt orange-red | Warm | High | Terracotta, rust, flame |
| #FF8C00 | Dark orange | Warm | High | Pumpkin, autumn leaf |
| #FFD700 | Golden yellow | Warm | High | Gold, sunflower, amber |
| #FFFF00 | Bright lemon | Neutral | High | Lemon, canary |
| #9ACD32 | Yellow-green | Warm | Medium | Olive, pistachio, moss |
| #228B22 | Forest green | Cool | Medium | Pine, emerald, ivy |
| #006400 | Dark green | Cool | Low | Hunter, pine, seaweed |
| #00CED1 | Deep turquoise | Cool | High | Caribbean water, gemstone |
| #0000FF | Pure blue | Cool | High | Sapphire, cobalt, electric |
| #4169E1 | Royal blue | Cool | High | Cornflower, denim |
| #4B0082 | Deep indigo | Cool | Medium | Violet, midnight, ink |
| #800080 | Rich purple | Cool | Medium | Amethyst, royal, plum |
| #FF1493 | Deep pink | Warm | High | Hot pink, magenta, fuchsia |
| #FFC0CB | Soft pink | Warm | Low | Blush, rose quartz, ballet |
| #F5F5DC | Beige cream | Warm | Low | Linen, ivory, parchment |
| #D2691E | Chocolate brown | Warm | Medium | Cocoa, leather, walnut |
| #808080 | Neutral gray | Neutral | Zero | Slate, concrete, silver |
| #36454F | Charcoal | Cool | Low | Slate, gunmetal, storm |
| #000000 | Pure black | Neutral | Zero | Onyx, obsidian, ink |
| #FFFFFF | Pure white | Neutral | Zero | Snow, porcelain, pearl |

---

### PALETTE ARCHETYPE LANGUAGE

**Monochromatic:**
```
monochromatic [color] palette, varying shades of [color] from deep [dark variant] to pale [light variant], tonal harmony, single hue family
```
Example: `monochromatic blue palette, varying shades of navy to pale sky blue, tonal harmony`

**Analogous:**
```
analogous palette of [color A], [color B], and [color C], adjacent hues on color wheel, harmonious transition, warm-to-cool gradient
```
Example: `analogous palette of deep teal, seafoam green, and sage, harmonious transition`

**Complementary:**
```
complementary [color A] and [color B] palette, high contrast warm against cool, vibrant opposition, electric tension
```
Example: `complementary burnt orange and deep teal palette, high contrast warm against cool`

**Triadic:**
```
triadic palette of [color A], [color B], and [color C], evenly spaced on color wheel, vibrant balance, playful energy
```
Example: `triadic palette of crimson, emerald, and royal blue, vibrant balance`

**Split-Complementary:**
```
split-complementary [base color] with [accent A] and [accent B], dominant [base] with subtle opposing accents, controlled tension
```
Example: `split-complementary deep blue with burnt orange and golden yellow accents`

**Tetradic / Double-Split:**
```
rich tetradic palette of [A], [B], [C], [D], four-color harmony, complex balance, maximalist color story
```

---

### MOOD-BASED COLOR LANGUAGE

**Warm & Cozy:**
```
warm palette of amber, terracotta, burnt orange, and cream, hearth-like glow, autumnal warmth, golden hour tones
```

**Cool & Clinical:**
```
cool palette of slate blue, surgical white, and steel gray, clinical precision, arctic calm, laboratory aesthetic
```

**Dark & Moody:**
```
dark moody palette of deep plum, charcoal, and wine red, chiaroscuro color, nocturnal atmosphere, velvet darkness
```

**Bright & Optimistic:**
```
bright optimistic palette of sunflower yellow, sky blue, and grass green, primary color joy, spring freshness, childlike energy
```

**Muted & Sophisticated:**
```
muted sophisticated palette of dusty rose, sage green, and warm taupe, desaturated elegance, vintage tone, understated luxury
```

**Neon & Electric:**
```
neon electric palette of hot magenta, cyan, and acid green, synthetic glow, cyberpunk energy, blacklight vibrance
```

**Pastel & Dreamy:**
```
pastel dreamy palette of lavender, peach, and mint, soft desaturated candy tones, cotton candy atmosphere, gentle gradient
```

**Earth & Natural:**
```
earth palette of ochre, sienna, olive, and stone, organic mineral tones, soil and leaf, grounded warmth
```

---

### BRAND COLOR INJECTION

**For Flux (HEX Support):**
Flux supports HEX codes directly in prompts [^70^]. Use format:
```
[Subject] in [HEX] and [HEX] color scheme, [additional descriptors]
```
Example: `Product photography of sneakers in #FF6B35 and #004E89 color scheme, vibrant sport aesthetic`

**For SDXL / z_image (Natural Language):**
SDXL does not reliably parse HEX. Translate to natural language:
```
[Subject] in vibrant coral and deep navy color scheme, high contrast brand palette
```

**For LTX Video:**
Color consistency across frames requires explicit palette anchoring:
```
Style: Consistent [color A] and [color B] palette throughout, no color drift between frames, stable white balance.
```

---

### COLOR CONTROL TECHNIQUES

**1. Dominant + Accent Method:**
```
dominant [main color] with [accent color] highlights, 80/20 color distribution
```

**2. Color Temperature Contrast:**
```
warm [color] subject against cool [color] background, complementary temperature contrast
```

**3. Atmospheric Color:**
```
[color] atmospheric haze, [color] light spill, [color] bounce on skin, monochromatic environment
```

**4. Material Color:**
```
[color] velvet, [color] brushed metal, [color] translucent glass, material dictating color behavior
```

**5. Seasonal Color:**
```
spring palette of new green and blossom pink, summer of deep blue and sun gold, autumn of rust and amber, winter of ice blue and bare branch gray
```

---

### EXAMPLE PROMPTS

**Monochromatic Brand:**
> `Minimalist product photography of wireless speaker, monochromatic navy blue palette varying from midnight to pale slate, tonal harmony with single copper accent, clean studio lighting, matte and gloss texture interplay, professional brand aesthetic`

**Complementary Cinematic:**
> `Cinematic portrait in complementary teal and burnt orange palette, subject lit by warm tungsten practical while background bathed in cool neon teal, high contrast color opposition, film noir aesthetic with modern color grading, skin tones balanced between warm and cool`

**Earth Palette Documentary:**
> `Documentary photography of Moroccan spice market, earth palette of ochre, sienna, turmeric gold, and terracotta, organic mineral tones, warm dusty atmosphere, saturated but natural, no synthetic neon, National Geographic color science`

**Neon Cyberpunk:**
> `Cyberpunk street scene at night, neon electric palette of hot magenta (#FF00FF), cyan (#00FFFF), and acid green (#39FF14), synthetic glow on wet pavement, blacklight vibrance, high saturation with deep black shadows, CRT screen reflections, vaporwave aesthetic`

**Pastel Ghibli:**
> `Pastel dreamy landscape with floating islands above cloud sea, palette of lavender (#E6E6FA), peach (#FFDAB9), and mint (#F5FFFA), soft desaturated candy tones, cotton candy atmosphere, gentle gradient sky, Studio Ghibli-inspired watercolor aesthetic`

---

### TECHNICAL NOTES FOR AI GENERATION
- Flux: HEX codes work directly; place them near subject for strongest activation [^70^]
- SDXL: Use natural language translations; HEX may be ignored or misinterpreted
- LTX: Specify "stable palette" or "consistent color" to prevent frame-to-frame drift
- All models: Color words early in prompt carry more weight than late color words
- Use material references ("ruby", "slate", "ochre") for more reliable color activation than abstract color names
- Specify "monochromatic", "complementary", "analogous" for coherent palette relationships
