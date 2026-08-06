# SKILL: Golden Hour Mastery
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Mastery of the "magic hour" period when the sun sits between approximately −6° and +6° solar elevation above the horizon. Produces soft, warm, directional light with long shadows and natural rim lighting. The atmosphere scatters shorter wavelengths, leaving warm gold-amber tones that flatter skin and sculpt texture.

### TRIGGER KEYWORDS
golden hour, magic hour, sunset light, sunrise light, warm light, amber light, backlight portrait, rim light, sun flare, long shadows, warm golden, dusk light, hour of gold, natural rim, outdoor warm portrait

### CORE RULES
- Color temperature 3500K–5000K — warm amber, never white or cold
- Light direction is low-angle: 5°–20° above horizon produces signature long shadows
- Natural rim lighting: backlit or side-lit subjects with luminous edge definition
- Sky gradient: warm near horizon transitioning to cooler blue at zenith
- Shadow fill is warm, not neutral: bounce or gold reflector maintains 3200K–4000K in shadows
- Lens flare or soft bloom is expected and desirable at this angle
- Magic hour is brief: specify whether sunrise (cool-to-warm) or sunset (warm-to-cool)

---

### TECHNICAL PARAMETERS

**Solar Geometry:**
- Elevation Range: −6° to +6° above horizon (true golden hour)
- Color Temperature: 3500K–5000K (sunrise), shifting warmer as sun drops
- Shadow Ratio: 2:1 to 4:1 (natural, unassisted)
- Light Quality: Soft-directional with exponential falloff

**Rim Light Ratios:**
- Hair/Edge Rim: 1–2 stops brighter than key face exposure
- Shoulder Rim: 0.5–1 stop over key
- Lens Flare Threshold: f/16–f/22 for sunstar effects; f/2.8–f/4 for soft flare bloom

**Warm Shadow Fill:**
- Bounce Source: Gold reflector (maintains 3200K–4000K warmth in shadows)
- White Reflector: Neutral fill, preserves cooler ambient in shadow
- Fill Ratio: 1:2 to 1:4 (fill:key) to retain dimension without flatness
- Shadow Color Temperature: 4000K–4500K (cooler than highlights, natural contrast)

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Golden hour [portrait/landscape/cinematic scene], sun at [low angle/backlight/side-light], 
warm amber-gold light wrapping subject, long dramatic shadows stretching across [surface], 
rim light outlining [hair/shoulders/edges] with luminous halo, 
soft warm fill in shadow areas maintaining subtle detail, 
sky gradient from deep orange-amber near horizon to cool blue zenith, 
atmospheric haze catching light rays, 
[specify subject] bathed in directional warm light, 
photographic realism, cinematic color science, 
[ lens: 85mm f/1.4 | 35mm f/2 | 24mm f/1.4 for landscape ]
```

**Negative Prompts:**
```
harsh midday sun, overhead lighting, blown highlights, cool blue cast, 
flat lighting, short shadows, white balance errors, 
squinting expression, chromatic aberration (unless intentional)
```

---

### ADVANCED TECHNIQUES

**1. Backlit Rim Configuration**
- Position subject between camera and sun
- Expose for subject face (spot meter)
- Background permitted to bloom 1–2 stops over
- Use lens hood or partial flagging for controlled flare

**2. Side-Lighting for Texture**
- Sun at 90° to camera axis
- Reveals surface texture in landscapes and skin
- Shadow becomes compositional element
- Ideal for: architecture, environmental portraits, terrain

**3. Front-Lighting for Glow**
- Subject faces sun directly
- Even, flattering illumination
- Best for: beauty portraits, product photography
- Risk: subject squinting — mitigate with timing or closed eyes/looking away

**4. Time-Blend Composite Logic**
- Blue hour background + golden hour subject (for cityscapes)
- Requires separate exposure brackets in real cinematography
- For AI generation: specify "sky transitioning from blue to gold"

---

### LIGHTING RATIO CHART
| Setup | Key:Fill | Rim:Key | Mood |
|-------|----------|---------|------|
| Natural (no assist) | 4:1 | 2:1 | Dramatic, cinematic |
| Assisted (gold bounce) | 2:1 | 1.5:1 | Romantic, flattering |
| Overexposed background | 1:1 | 3:1 | Ethereal, dreamlike |
| Silhouette | 0:1 | ∞ | Graphic, mysterious |

---

### EXAMPLE PROMPTS

**Portrait:**
> Golden hour portrait, young woman with wind-blown hair, sun at 15° above horizon behind her creating luminous rim light on hair and shoulders, warm amber light wrapping her cheek, gold reflector bouncing soft fill into shadow side of face, long shadows on golden grass, sky burning orange-pink, 85mm f/1.4, shallow depth of field, cinematic color grading, warm shadow detail, photorealistic skin texture

**Landscape:**
> Golden hour landscape, sun setting over coastal cliffs, side-lighting revealing rock texture, long shadows stretching across wet sand, warm light catching wave crests, atmospheric haze with visible light rays, sky gradient from deep amber to violet-blue, 24mm f/11, focus stacking sharpness, cinematic wide shot

---

### TECHNICAL NOTES FOR AI GENERATION
- Emphasize "solar elevation low" to prevent midday-looking output
- Specify color temperature in Kelvin when possible (3800K–4500K)
- Include "atmospheric perspective" for depth
- Mention "long shadows" explicitly — AI often defaults to short shadows
- Use "wrap-around light" to indicate softness despite directionality
