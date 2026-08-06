# SKILL: Studio Softbox Setups
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Professional studio lighting using softbox-modified strobes or continuous sources. Defines precise key/fill/rim ratios based on subject type (portrait, beauty, fashion, product). Covers softbox sizes, positioning angles, and shadow control for flattering, dimensional illumination.

### TRIGGER KEYWORDS
softbox, studio lighting, key light, fill light, rim light, studio portrait, beauty lighting, fashion lighting, clamshell lighting, butterfly lighting, Rembrandt setup, loop lighting, split lighting, studio setup, strobe, continuous light

### CORE RULES
- Key light size determines shadow quality: small softbox = harder shadows, large = softer wrap
- Lighting ratios: 1:1 (beauty, flat), 2:1 (commercial), 3:1 (portrait drama), 4:1+ (noir/dramatic)
- Octaboxes produce round catchlights — the beauty standard; strip boxes produce elongated specular
- Clamshell = two softboxes above and below face: shadow-free beauty with eye sparkle
- Rim/hair light separates subject from background — always 1–2 stops brighter than key
- Background light is independent: set separately from subject lighting
- Specify catchlight shape in eye as quality control: round = octabox, rectangular = large softbox

---

### TECHNICAL PARAMETERS

**Softbox Size & Quality:**
- Small (1×1 ft / 30×30cm): Harder edge, defined shadows, specular highlights
- Medium (2×3 ft / 60×90cm): General purpose, moderate softness
- Large (4×6 ft / 120×180cm): Very soft wrap, minimal shadows
- Octagonal (5–6 ft): Round catchlights, fashion/beauty standard
- Strip (1×4 ft): Edge light, rim, precise control

**Key Light Positioning:**
- Angle: 30°–45° from camera axis
- Height: 1–2 ft above subject eye level (creates eye catchlight at 10 or 2 o'clock)
- Distance: 4–8 ft (inverse square law control)
- Modifier: Large octabox or parabolic for beauty; medium softbox for general

**Fill Light Positioning:**
- Angle: Opposite key, near camera axis (0°–15°)
- Height: At or below subject eye level
- Distance: 6–10 ft (softer, less intense)
- Modifier: Large softbox, umbrella, or bounce card

**Rim/Hair Light Positioning:**
- Angle: 45°–90° behind subject, opposite key side
- Height: 2–3 ft above head
- Distance: 6–8 ft
- Modifier: Strip softbox or grid spot (prevents lens flare)
- Flag: Black card between rim light and lens essential

---

### LIGHTING RATIO CHART BY SUBJECT

**Portrait (General):**
- Key:Fill = 2:1 to 4:1
- Key:Rim = 1:1 to 2:1
- Result: Dimensional but flattering, moderate shadow

**Beauty/Cosmetics:**
- Key:Fill = 1:1 to 2:1
- Key:Rim = 1:1
- Result: Even skin, minimal texture, prominent catchlights
- Special: Clamshell setup (key above, fill below, both frontal)

**Fashion/Editorial:**
- Key:Fill = 4:1 to 8:1
- Key:Rim = 2:1 to 4:1
- Result: Dramatic, high contrast, defined cheekbones
- Special: Often add background light for separation

**Product/Still Life:**
- Key:Fill = 2:1 to 16:1 (depending on material)
- Key:Rim = 1:1 to 3:1
- Result: Shape definition, material texture revelation
- Special: Gradient lighting for reflective surfaces

**Male Portrait/Gritty:**
- Key:Fill = 8:1 to 16:1
- Key:Rim = 1:1
- Result: Hard shadows, masculine definition, texture emphasis

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Professional studio [portrait/beauty/fashion/product] photography, 
[subject] lit with [softbox size/type] key light at [angle] creating [shadow description], 
[fill description] filling shadows to [ratio], 
[rim/hair light description] providing edge separation, 
[background light description if applicable], 
clean [color/grey/white/black] background, 
[aperture] for [depth of field description], 
high-end retouching aesthetic, 
sharp focus on [eyes/product detail], 
professional studio quality
```

**Negative Prompts:**
```
amateur lighting, overhead lighting, harsh shadows, 
flat lighting, double catchlights from wrong angle, 
lens flare in studio, mixed color temperature errors, 
clipped highlights on skin, unnatural skin smoothing
```

---

### ADVANCED TECHNIQUES

**1. Clamshell Beauty Setup**
- Key: Large octabox above, 30° down
- Fill: White reflector or second softbox below, 30° up
- Result: Even, shadowless beauty light with symmetrical catchlights
- Ratio: 1:1 to 2:1

**2. Paramount/Butterfly Setup**
- Key: Large softbox directly above camera, 30°–45° down
- Fill: Reflector below chin
- Result: Butterfly shadow under nose, classic Hollywood glamour
- Ratio: 2:1 to 4:1

**3. Loop Lighting**
- Key: 30°–45° from camera, slightly above eye level
- Fill: Minimal or reflector
- Result: Small nose shadow looping toward cheek (not touching)
- Ratio: 2:1 to 4:1
- Most flattering for average faces

**4. Split Lighting**
- Key: 90° from camera axis
- Fill: None or minimal
- Result: Half face lit, half in shadow
- Ratio: 8:1 to 16:1
- Dramatic, masculine, artistic

**5. Rembrandt Lighting**
- Key: 45° from camera, above eye level
- Fill: Reflector or minimal
- Result: Triangle of light on shadow-side cheek (nose shadow connects to cheek shadow)
- Ratio: 4:1 to 8:1

---

### EXAMPLE PROMPTS

**Beauty Clamshell:**
> Professional beauty portrait, model lit with clamshell lighting setup, large octagonal softbox above creating soft even key light with round catchlights in eyes, white reflector below bouncing fill up into chin and neck shadows, 1:1 key-to-fill ratio, seamless white background, 100mm macro lens at f/8, razor sharp focus on eyes, high-end cosmetics photography, flawless but natural skin texture, professional studio lighting

**Fashion Dramatic:**
> High-fashion editorial portrait, model in dramatic 4:1 lighting ratio, large parabolic softbox at 45° camera left creating defined cheekbone shadow, minimal fill preserving contrast, strip softbox from behind camera right creating crisp rim light on shoulder and hair, black background absorbing light, 85mm f/1.8 at f/5.6 for sharpness, moody editorial aesthetic, professional studio quality

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify modifier type ("octabox", "strip softbox", "parabolic") for catchlight shape
- Include "catchlights in eyes" to bring life to portraits
- Mention background color explicitly (seamless white, grey, black)
- Use "professional studio" to trigger clean, controlled aesthetic
- Specify lens and aperture for depth of field control
- Include "sharp focus on eyes" for portrait priority
