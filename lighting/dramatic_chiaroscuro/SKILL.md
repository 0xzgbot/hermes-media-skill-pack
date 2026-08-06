# SKILL: Dramatic Chiaroscuro
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
The Baroque technique of extreme light-dark contrast using a single dominant source. Derived from Italian *chiaro* (light) and *scuro* (dark). Creates psychological depth, volumetric form, and narrative tension. Associated with Caravaggio, Rembrandt, and modern film noir. Prioritizes shadow as an active compositional element rather than absence of light.

### TRIGGER KEYWORDS
chiaroscuro, dramatic lighting, Rembrandt lighting, single light source, film noir lighting, dramatic shadow, dark portrait, spotlight, Caravaggio lighting, theatrical light, high contrast, dark and moody, tenebrism, shadow play

### CORE RULES
- Single dominant source; any fill is minimal and preserves shadow depth
- Shadow occupies majority of frame — 50-80% darkness is correct
- Rembrandt triangle: lit triangle on shadow-side cheek, no wider than eye, no taller than nose
- Key light at 45°–90° from camera axis, above eye level for drama
- No flat ambient light — any bounce must be very weak
- Shadow is active and intentional, not absence of light
- Texture revelation: light grazing surfaces at 5–15° reveals skin, fabric, stone detail

---

### TECHNICAL PARAMETERS

**Single Source Characteristics:**
- Source Type: Hard directional (bare bulb, window, candle, spotlight)
- Source Size: Small relative to subject = harder shadows, more drama
- Distance: Inverse square law creates rapid falloff
- Angle: 45°–90° from camera axis (side or three-quarter)
- Height: Above eye level for Rembrandt triangle; below for horror/unnatural

**Shadow Depth Control:**
- Deep Black: No fill, 16:1+ ratio (Caravaggio style)
- Textured Shadow: Minimal fill or reflected ambient (Rembrandt style)
- Shadow Detail: Zone II–III on Ansel Adams scale (barely perceptible detail)
- Core Shadow: Darkest area, no detail, pure black
- Penumbra: Soft edge of shadow (controlled by source size)

**Texture Revelation:**
- Grazing Angle: Light at 5°–15° to surface plane reveals maximum texture
- Surface Imperfections: Wrinkles, fabric weave, stone grain, skin pores
- Specular Highlight: Controlled by source size and surface glossiness
- Three-Dimensionality: Single source creates clear light-to-dark gradient across form

**The Rembrandt Triangle:**
- Definition: Illuminated triangle on shadow-side cheek, below eye
- Dimensions: No wider than eye, no longer than nose
- Creation: Key at 45°, above eye level, nose shadow connects to cheek shadow
- Variation: Break "rules" by moving source for emotional effect

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Dramatic chiaroscuro [portrait/still life/scene], 
single [source type] light source from [direction] creating extreme contrast, 
deep rich shadows consuming [percentage] of frame, 
[subject] emerging from darkness into a beam of [warm/cool/neutral] light, 
texture of [material/skin/fabric] revealed by grazing light angle, 
Rembrandt triangle of light on shadow-side cheek [if portrait], 
sharp shadow edges with soft subtle penumbra, 
volumetric atmosphere catching light rays, 
Baroque painting aesthetic, cinematic noir lighting, 
psychological depth and mystery
```

**Negative Prompts:**
```
flat lighting, even illumination, multiple light sources without motivation, 
overexposed shadows, HDR look, fill light eliminating shadow mystery, 
high-key lighting, softbox look, clean studio lighting, 
white background, colorful ambient fill
```

---

### ADVANCED TECHNIQUES

**1. Caravaggio Spotlight**
- Single hard source from high angle
- Subject isolated in pool of light
- Background: Pure black, no detail
- Emotional effect: Divine revelation, theatrical drama
- Ratio: 32:1 or greater

**2. Rembrandt Psychological Portrait**
- Single window or soft directional source
- Warm golden light (candle/window quality)
- Rich brown shadows with subtle warm reflected fill
- Triangle of light on shadow cheek
- Emotional effect: Introspection, wisdom, humanity
- Ratio: 8:1 to 16:1

**3. Film Noir Hard Shadow**
- Venetian blind shadow patterns ("barndoor" effect)
- Hard single source through slats or bars
- Deep shadows with sharp edges
- Smoke/atmosphere for visible light beams
- Emotional effect: Suspense, entrapment, moral ambiguity
- Ratio: 16:1 to 32:1

**4. Volumetric God-Ray**
- Single source through atmospheric medium (dust, smoke, water)
- Visible light beam (Tyndall effect)
- Subject partially illuminated within beam
- Emotional effect: Supernatural, sacred, revelation
- Ratio: Variable within beam

**5. Subsurface Texture Reveal**
- Single source at extreme grazing angle to surface
- Reveals: Canvas weave, wood grain, skin pores, fabric texture
- Shadow becomes textural map of surface topology
- Emotional effect: Raw authenticity, age, material truth

---

### SHADOW-TO-LIGHT RATIO SCALE
| Ratio | Style | Shadow Detail | Use Case |
|-------|-------|---------------|----------|
| 16:1 | Caravaggio | Pure black, no detail | Maximum drama, religious |
| 8:1 | Rembrandt | Minimal detail, warm | Psychological portrait |
| 4:1 | Cinematic | Some detail, textured | Film noir, dramatic scene |
| 2:1 | Soft Chiaroscuro | Moderate detail | Moody editorial, artistic |

---

### EXAMPLE PROMPTS

**Rembrandt Portrait:**
> Baroque-inspired portrait in dramatic chiaroscuro, single window light from camera left at 45° above eye level, deep warm golden light illuminating subject's face while rich brown shadows consume the right side, Rembrandt triangle of warm light visible below right eye, skin texture and pores revealed by directional light, subject emerging from pure black background, volumetric dust catching light beam, psychological depth, painterly quality reminiscent of Dutch Golden Age, cinematic color science with warm highlights and cool shadow depths

**Noir Scene:**
> Film noir interrogation scene, single bare bulb hanging from ceiling creating harsh downward light, deep shadows under eyes and chin, sharp shadow edges on concrete wall behind subject, smoke in air catching light creating visible beams, subject half-lit half-hidden in darkness, high contrast black and white aesthetic with subtle warm tone, cinematic 35mm film grain, dramatic chiaroscuro lighting, suspenseful atmosphere

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "single light source" explicitly to prevent AI from adding invisible fills
- Specify "deep shadows" or "pure black shadows" to control shadow density
- Include "grazing light" or "raking light" for texture revelation
- Mention painter references ("Caravaggio style", "Rembrandt lighting") for aesthetic anchoring
- Use "volumetric" or "atmospheric" for visible light beams
- Specify warm or cool shadow color to prevent gray flat shadows
