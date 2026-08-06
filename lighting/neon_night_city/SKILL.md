# SKILL: Neon Night City
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Mastery of urban night environments dominated by artificial illumination: neon signage, streetlights, vehicle headlights, LED displays, and building illumination. Characterized by wet surface reflections, atmospheric haze, color bleed between competing sources, and the unique mood of nocturnal urban spaces. Essential for cyberpunk, noir, and contemporary urban cinematography.

### TRIGGER KEYWORDS
night city, neon city, city at night, urban night, streetlight, neon signs, night photography, rain at night, wet street, city lights reflection, nighttime urban, city glow, Tokyo night, NYC night, noir city, urban darkness

### CORE RULES
- Multiple competing color sources create the signature mixed-light palette: sodium orange, neon red/blue, LED cool white
- Wet surfaces double every light source through reflection — rain unlocks full visual complexity
- Atmospheric haze (steam, fog, light pollution) makes light beams visible and creates depth
- Human figures appear small and isolated against the scale of lit architecture
- Color temperature varies wildly per zone: no single correct white balance
- Practical lights must be visible and motivated in frame — not just implied
- Noir rule: every shadow may hide something; light selectively reveals

---

### TECHNICAL PARAMETERS

**Primary Source Types:**
- Neon Signage: 450nm–640nm (blue through red), gas-discharge spectrum
- Sodium Vapor: 589nm (monochromatic yellow-orange), street lighting
- LED Billboard: RGB mixed, 5500K–6500K white, saturated colors
- Vehicle Headlight: 4000K–6000K (LED/HID), tungsten 2800K (older)
- Building Interior: Warm tungsten spill, 2800K–3200K
- Street/Security: Cool white/blue LED, 5000K–7000K

**Wet Pavement Reflections:**
- Surface: Asphalt, concrete, cobblestone (each reflects differently)
- Condition: Recent rain, puddles, damp sheen
- Reflection Type: Mirror (smooth water) vs Diffuse (rough wet surface)
- Color Multiplication: Reflected neon doubles color saturation on ground
- Specular Highlight: Streetlights create long vertical highlights on wet ground
- Ripple Distortion: Moving water breaks reflection into abstract color shards

**Sign Bleed & Spill:**
- Radius: 5–50 feet depending on sign brightness and atmospheric haze
- Surface Interaction: Matte surfaces absorb color; glossy surfaces reflect
- Skin Cast: Subject near pink neon = magenta skin tint; blue = cyan tint
- Mixing Zones: Intersection of multiple signs creates additive color (red+blue=magenta)
- Falloff: Inverse square with atmospheric scatter softening edges

**Atmosphere Haze:**
- Source: Humidity, fog, pollution, steam, rain
- Effect: Light scatter creates visible beams and glow halos
- Color Enhancement: Haze scatters colored light, intensifying neon ambience
- Depth Layering: Distant signs become soft color blobs; near signs stay sharp
- Mood: Mystery, claustrophobia, dreamlike abstraction

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Urban night scene in [city type: Tokyo alley/New York street/cyberpunk metropolis], 
subject illuminated by competing [neon/LED/sodium] light sources, 
wet [asphalt/cobblestone/concrete] reflecting [colors] in [mirror/abstract] patterns, 
neon sign bleed casting [color] onto [surfaces/subject], 
atmospheric [fog/rain/haze/steam] scattering light into soft halos, 
background layers of [distant signs/streetlights/building windows] creating depth, 
[vehicle/steam/people] adding motion and life, 
cool [blue/cyan] shadows contrasting with warm [orange/pink] highlights, 
cinematic night photography, 
photorealistic urban atmosphere
```

**Negative Prompts:**
```
daylight, clear dry pavement, no reflections, 
single light source, even studio lighting, white balance neutral, 
countryside, natural landscape, clean modern interior, 
overexposed neon losing color, flat lighting, no atmosphere
```

---

### ADVANCED TECHNIQUES

**1. Cyberpunk Alley**
- Dominant: Magenta/pink neon from signage above
- Accent: Cyan LED strips, cool blue security light
- Ground: Wet asphalt reflecting both colors in mirror pools
- Atmosphere: Heavy haze, steam from vents
- Subject: Partially lit by neon, face with color cast
- Emotional: Future-noir, technological dystopia, sensory overload

**2. Noir Street**
- Dominant: Sodium vapor streetlights (monochromatic yellow)
- Accent: Single shop window (warm tungsten spill)
- Ground: Wet cobblestone with long vertical highlights
- Atmosphere: Light fog, rain mist
- Subject: Fedora silhouette, trench coat, shadowed face
- Emotional: Mystery, 1940s nostalgia, moral ambiguity

**3. Rainy Intersection**
- Multiple sources: Traffic lights, headlights, neon signs, storefronts
- Ground: Torrential rain creating moving reflections, ripples
- Effect: All colors fractured and multiplied across wet surface
- Atmosphere: Heavy rain, mist from tires
- Subject: Umbrella silhouette, caught in crosswalk light
- Emotional: Solitude, urban overwhelm, transient moment

**4. Steam & Neon**
- Source: Single bright neon sign behind steam source
- Effect: Steam diffuses neon into giant soft color blob
- Subject: Emerging from steam, partially obscured
- Ground: Wet pavement catching only direct reflection
- Emotional: Industrial, mysterious, liminal space

**5. High-Rise Vista**
- Background: Cityscape of thousands of window lights
- Foreground: Subject on balcony/rooftop
- Light: Ambient urban glow (no single source)
- Atmosphere: Distant haze, light pollution creating orange sky glow
- Emotional: Contemplation, isolation in crowds, urban sublime

---

### COLOR PALETTE MATRIX
| Primary Neon | Secondary | Ground Reflection | Mood | Genre |
|--------------|-----------|-------------------|------|-------|
| Magenta | Cyan | Pink-Blue mirror | Cyberpunk | Sci-Fi |
| Red | Blue | Purple wet asphalt | Danger/Noir | Thriller |
| Green | Orange | Yellow-Green shimmer | Toxic/Weird | Horror |
| Warm White | Sodium Yellow | Gold mirror pools | Nostalgia | Drama |
| Multi-RGB | White | Rainbow fracture | Celebration | Commercial |

---

### EXAMPLE PROMPTS

**Cyberpunk Alley:**
> Cyberpunk alley at night, subject walking through narrow corridor lit by overhead pink neon signs casting magenta bleed onto wet concrete walls, cyan LED strips providing cool rim light from behind, ground covered in mirror-like puddles reflecting neon in abstract color patterns, heavy atmospheric haze scattering light into soft halos, distant blurred neon creating bokeh depth layers, steam rising from street vents catching backlight, cinematic night photography, photorealistic urban decay, color contrast between warm pink and cool cyan, 35mm f/1.4 with natural lens flare

**Noir Rain Scene:**
> Film noir street scene at night, heavy rain falling on wet cobblestone street reflecting sodium vapor streetlights in long golden vertical highlights, single warm tungsten light spilling from shop window illuminating subject's face from side, atmospheric fog softening distant building lights, subject in trench coat with hat casting shadow over eyes, monochrome warm tone with subtle color, cinematic noir aesthetic, rain droplets catching light, photorealistic wet surface reflections, moody urban atmosphere

---

### TECHNICAL NOTES FOR AI GENERATION
- Always specify "wet" or "rain" for reflections — AI defaults to dry
- Use "neon bleed" or "color spill" for atmospheric color cast
- Include "haze" or "fog" to justify soft halos beyond simple glow
- Mention specific surface type (asphalt, cobblestone) for reflection character
- Use "layers of depth" or "bokeh" for background city complexity
- Specify "steam" or "smoke" for volumetric light scatter
