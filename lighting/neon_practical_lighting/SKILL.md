# SKILL: Neon & Practical Lighting
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Mastery of gas-discharge and incandescent practical light sources as primary or motivated illumination. Covers neon tubing (argon/mercury blue, neon red-orange), LED practicals, tungsten practicals, and fluorescent sources. Emphasizes color bleed between sources, bloom/glow control, and iris specification for bokeh character.

### TRIGGER KEYWORDS
practical lighting, neon tube, neon light, neon sign, practical light, motivated lighting, neon glow, colored light, LED light, tungsten bulb, fluorescent, glow, bloom, halo, in-frame light source, color cast

### CORE RULES
- Practical lights must be visible in frame — they are both source and subject
- Neon red-orange (610–640nm) and argon blue (450–490nm) are the two signature gas types
- Bloom and glow are characteristics, not errors: overexpose practicals slightly for authenticity
- Color bleed from neon contaminates nearby surfaces — specify which surfaces pick up which colors
- Iris at T2–T2.8 creates bokeh from out-of-focus practicals in background
- Mixed sources create complex color environments; describe each source independently
- Fluorescent flicker at 50–60Hz creates subtle strobing — use for unease or period authenticity

---

### TECHNICAL PARAMETERS

**Neon Source Characteristics:**
- Neon Gas: 610nm–640nm (warm red-orange), high saturation
- Argon/Mercury: 450nm–490nm (cool blue), often with phosphor coating for pink/purple
- Helium: 587nm (warm yellow-orange)
- Xenon: Broad spectrum, 5000K–6000K, strobe-like quality
- Tube Diameter: 8mm–15mm standard; 25mm for high-output
- Ballast Flicker: 50Hz/60Hz imperceptible, but creates micro-strobing on high-speed footage

**Color Bleed Physics:**
- Spill Radius: Inverse square law with atmospheric scatter
- Surface Reflection: Glossy surfaces reflect 80–90% of neon hue
- Skin Interaction: Blue neon casts sickly cyan on skin; red neon creates warm flush
- Mixed Source: Adjacent neon colors create additive mixing zones (red + blue = magenta spill)

**Bloom Control:**
- Optical Bloom: Created by bright sources exceeding sensor/film latitude
- Diffusion Bloom: Atmospheric haze or lens diffusion filters (Pro-Mist, Black Satin)
- Digital Bloom: Post-process glow with threshold at 80–90% luminance
- Bloom Radius: Tight (50px) for sharp sources; Wide (200px+) for dreamy atmosphere

**Iris Specification for Bokeh:**
- f/1.2–f/1.8: Circular bokeh, soft edges, significant cat's eye at frame edges
- f/2.8: Octagonal bokeh (8-blade iris), defined edges
- f/4–f/5.6: Geometric bokeh, hard edges, source shape visible
- Anamorphic: Oval bokeh, horizontal flare streaks
- Vintage Lens: Swirly bokeh, onion rings, chromatic aberration

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Interior/Exterior] scene lit primarily by [neon color] practical sources, 
[subject] illuminated by [specific light type: neon sign/LED strip/tungsten lamp/fluorescent], 
color bleed casting [hue] onto [surfaces], 
[bloom level: subtle/controlled/extreme] glow from bright sources, 
[aperture specification] creating [bokeh shape] background bokeh from distant lights, 
motivated shadows following [source direction], 
mix of [color temperature 1] and [color temperature 2] creating color contrast, 
cinematic night photography, lens flare from bright sources, 
photorealistic light behavior
```

**Negative Prompts:**
```
flat lighting, single color cast without motivation, 
unrealistic glow without source, daylight balance, 
overexposed neon losing color saturation, clean studio lighting, 
white light without color temperature
```

---

### ADVANCED TECHNIQUES

**1. Multi-Source Color Contrast**
- Primary: Warm tungsten practical (2800K)
- Accent: Cool neon/LED (6000K–10000K)
- Ratio: 2:1 warm:cool for naturalistic; 1:1 for stylized cyberpunk
- Transition Zone: Where colors meet, create subtle magenta/cyan mixing

**2. Practical Motivation**
- Every light source visible in frame must motivate shadows
- Lamp in frame = key light on face at correct angle
- Neon sign behind subject = rim light with color cast
- Phone screen = under-light with cyan cast and eye reflection

**3. Bloom Hierarchy**
- Level 1: Source itself (100% luminance, slight blur)
- Level 2: Immediate halo (50% luminance, 20px radius)
- Level 3: Atmospheric glow (20% luminance, 100px+ radius)
- Control: "subtle bloom" vs "dreamlike heavy diffusion"

**4. Iris Bokeh Specification**
- Specify lens type for bokeh character:
  - "Canon 50mm f/1.2L creamy bokeh"
  - "Helios 44-2 swirly bokeh"
  - "Anamorphic oval bokeh with horizontal flare"

---

### COLOR COMBINATION MATRIX
| Primary | Accent | Mood | Genre |
|---------|--------|------|-------|
| Warm Neon (red) | Cool Shadow (blue) | Romantic danger | Noir, Thriller |
| Cool Neon (blue) | Warm Skin (amber) | Clinical intimacy | Sci-Fi, Drama |
| Green Neon | Magenta Fill | Toxic, surreal | Horror, Cyberpunk |
| Pink Neon | Cyan Reflection | Retro-futuristic | Synthwave, 80s |
| White LED | Warm Practical | Contemporary realism | Documentary, Drama |

---

### EXAMPLE PROMPTS

**Cyberpunk Portrait:**
> Portrait in neon-lit alley, subject lit by pink neon sign from camera left creating magenta key light on face, cool blue LED strip from above providing rim separation, warm tungsten practical in background creating amber bokeh orbs through window, heavy atmospheric bloom from humid air, f/1.4 circular bokeh with soft edges, color bleed from pink neon staining concrete wall, cinematic cyberpunk aesthetic, photorealistic skin with subtle color cast, lens flare from bright sources

**Practical Interior:**
> Cozy interior scene lit entirely by practical sources, subject reading by warm tungsten table lamp (2800K) creating soft side-lighting, cool blue moonlight leaking through window as subtle fill, warm lamp casting long shadows on textured wall, subtle bloom around filament visible in frame, f/2.8 creating soft bokeh from distant kitchen lights, realistic falloff, cinematic color science with warm-cool contrast

---

### TECHNICAL NOTES FOR AI GENERATION
- Always specify light source motivation ("lit by...")
- Include "color cast on skin" to prevent neutral skin under colored light
- Mention "bokeh" explicitly with shape descriptor
- Use "practical sources" to ensure lights exist in the scene, not invisible studio lights
- Specify "atmospheric haze" or "humidity" to justify bloom beyond simple glow
