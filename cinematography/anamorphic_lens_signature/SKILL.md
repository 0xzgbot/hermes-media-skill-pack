# SKILL: Anamorphic Lens Signature
## Version: 1.0 | Hermes Agent Camera & Lens Language

---

### DESCRIPTION
Mastery of anamorphic optics that squeeze the horizontal field of view during capture and desqueeze in post-production, creating the distinctive ultra-widescreen cinematic aesthetic. Characterized by oval bokeh, horizontal streak flares, elliptical catchlights, and a unique spatial compression that reads as "big movie" grammar. Essential for epic, noir, sci-fi, and premium commercial work.

---

### TECHNICAL PARAMETERS

**Squeeze Ratios & Aspect Ratios:**
- 1.33x Squeeze: Standard entry anamorphic; yields 2.35:1 from 16:9 sensor [^24^]
- 1.5x Squeeze: Classic cinema; yields 2.66:1 from 16:9
- 2.0x Squeeze: Premium cinema (CinemaScope); yields 2.39:1 from 4:3
- Desqueeze Requirement: Image must be horizontally stretched by reciprocal factor in post
- Sensor Pairing: 1.33x designed for 16:9; 2.0x designed for 4:3 open gate

**Oval Bokeh Characteristics:**
- Shape: Elliptical point-spread function (horizontal elongation proportional to squeeze factor)
- Cause: Cylindrical optical elements compress one axis during acquisition
- Aperture Interaction: Wider apertures (T2–T2.8) produce more pronounced ovals
- Edge Behavior: Cat's eye effect at frame periphery (ovals clip to almond shape)
- Color: Bokeh inherits anamorphic lens's distinct coating color science (warm/cool bias)

**Horizontal Flare Systems:**
- Blue Streak Flare: Classic anamorphic signature; bright sources produce horizontal blue line [^24^]
- Silver Flare: Neutral white/silver streak; modern, less vintage look
- Flare-Suppressed: Coated to minimize flare for controlled environments
- Source Requirements: Point light source or hard specular highlight needed to trigger
- Streak Length: Proportional to source brightness and lens T-stop
- Multi-Source: Overlapping streaks create complex horizontal light lattice

**Cinematic Compression:**
- Horizontal FOV Expansion: Same focal length captures ~33% more horizontal scene (1.33x)
- Depth Perception: Slightly altered; backgrounds feel closer horizontally than vertically
- Facial Distortion Control: Quality anamorphics minimize "anamorphic mumps" (facial widening) [^24^]
- Edge-to-Edge: Premium lenses maintain sharpness across squeezed field

**Focus Breathing:**
- Definition: Change in image magnification during focus pull
- Anamorphic Tendency: Historically significant breathing due to complex optics
- Modern Control: Cinema anamorphics suppress breathing for professional use [^24^]
- Creative Use: Slight breathing can add subconscious unease

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Anamorphic cinematography, [scene description], 
shot through 1.33x anamorphic lens creating 2.35:1 widescreen aspect ratio, 
distinctive oval bokeh in background highlights [horizontal elongation], 
horizontal lens flare streaks from [bright sources] cutting across frame, 
elliptical catchlights in eyes reflecting window/light sources, 
cinematic compression creating epic scope, 
[blue/silver/suppressed] flare characteristic, 
shallow depth of field with anamorphic bokeh quality, 
professional cinema color science, 
[subject] framed in ultra-wide composition
```

**Negative Prompts:**
```
spherical lens look, circular bokeh, vertical flares, 
standard 16:9 aspect ratio, sharp circular catchlights, 
no lens character, clean modern lens without personality, 
flat lighting, overexposed highlights without flare, 
video game look, TV aesthetic
```

---

### ADVANCED TECHNIQUES

**1. Classic Blue-Streak Noir**
- Flare: Blue horizontal streak from practical lights
- Bokeh: Oval city lights in background
- Aspect: 2.35:1 letterboxed composition
- Emotional: Retro-cinematic, 1970s–1980s thriller
- Best For: Night city, car interiors, neon environments

**2. Flare-Suppressed Naturalism**
- Flare: Minimal or absent; coating suppresses artifacts
- Bokeh: Oval but subtle
- Use: When story takes precedence over lens personality
- Emotional: Contemporary, grounded, documentary-adjacent
- Best For: Drama, naturalistic work, period pieces

**3. Extreme Oval Bokeh Portrait**
- Aperture: Wide open (T1.8–T2)
- Background: Point light sources (city, Christmas lights, candles)
- Effect: Background becomes abstract horizontal ovals
- Emotional: Dreamlike, romantic, subjective
- Best For: Intimate moments, memory sequences, beauty

**4. Anamorphic Macro (Modern Specialty)**
- Lens: 65mm T2.8 Macro Anamorphic (1.33x) [^24^]
- Capability: 1:4 magnification with anamorphic character
- Bokeh: Extreme oval at close focus distances
- Flare: Blue streaks even in macro range
- Emotional: Cinematic intimacy, texture revelation
- Best For: Product detail, food, eyes, small objects with epic scope

**5. Multi-Streak Light Lattice**
- Setup: Multiple practical lights in frame (chandelier, streetlights, headlights)
- Effect: Overlapping horizontal streaks create geometric pattern
- Bokeh: Ovals align into rows
- Emotional: Overwhelming, complex, urban density
- Best For: Cityscapes, crowded interiors, celebration

---

### ANAMORPHIC vs SPHERICAL COMPARISON
| Characteristic | Anamorphic | Spherical |
|----------------|------------|-----------|
| Bokeh | Oval, horizontal | Circular |
| Flare | Horizontal streak | Blob/halo |
| Aspect Ratio | 2.35:1–2.66:1 | 1.85:1–16:9 |
| Catchlights | Elliptical | Round |
| Horizontal FOV | Expanded by squeeze factor | Native focal length |
| Lens Personality | High, distinctive | Lower, neutral |

---

### EXAMPLE PROMPTS

**Cyberpunk City:**
> Anamorphic night city cinematography, subject walking through rain-slicked neon alley, shot on 1.33x anamorphic lens in 2.35:1 widescreen, distinctive oval bokeh from neon signs stretching horizontally in background, bright pink and cyan neon sources creating horizontal blue-silver flare streaks across frame, elliptical catchlights in subject's eyes, wet pavement reflecting anamorphic ovals, cinematic compression making narrow alley feel epic in scope, shallow T2 depth of field, professional cinema color science, cyberpunk noir aesthetic

**Intimate Portrait:**
> Anamorphic close-up portrait, subject in candlelit room, 85mm anamorphic at T1.8, extreme oval bokeh from candle flames stretching into soft horizontal ellipses, warm amber horizontal flare streak from brightest candle, elliptical catchlights in eyes showing flame shape, 2.35:1 composition with subject positioned in golden ratio, shallow depth isolating face from background, vintage cinema lens character, romantic painterly quality, photorealistic skin texture

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify "1.33x anamorphic" or "2x anamorphic" to trigger aspect ratio and optical character
- Use "oval bokeh" explicitly — AI defaults to circular
- Mention "horizontal flare" or "streak flare" to get anamorphic line artifacts rather than spherical bloom
- Include "2.35:1" or "CinemaScope" for widescreen composition
- Use "elliptical catchlights" for eye detail accuracy
- Specify flare color (blue, silver, gold) to control vintage vs modern feel
