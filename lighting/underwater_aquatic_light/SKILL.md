# SKILL: Underwater & Aquatic Light
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Mastery of light behavior in aqueous environments. Covers color absorption by depth, caustic light patterns from surface refraction, volumetric scattering, and the unique optical properties of water (refractive index 1.33). Essential for underwater cinematography, aquarium photography, and submerged scene generation.

### TRIGGER KEYWORDS
underwater, aquatic, submerged, ocean, diving, caustic light, underwater photography, beneath the water, water surface, swimming, aquarium, marine, deep water, blue water, underwater scene, bioluminescence

### CORE RULES
- Red absorbed at 15ft, orange at 25ft, yellow at 35ft: deeper = more blue-dominant palette
- Caustic light patterns (flickering bright lines) appear on any underwater surface from surface refraction
- Volumetric scattering: particles in water make light beams visible — essential for depth atmosphere
- Artificial light (strobes, video lights) restores warm colors absorbed by depth
- Surface-to-underwater transition: bright overexposed surface seen from below, deep blue surroundings
- Bioluminescence: cool blue-green point lights in deep/dark water add otherworldly quality
- Bubbles, particles, and marine snow add scale and volumetric texture

---

### TECHNICAL PARAMETERS

**Color Absorption by Depth (Open Water):**
- Red: Absorbed at ~15 ft / 4.5m (first to disappear)
- Orange: Absorbed at ~25 ft / 7.6m
- Yellow: Absorbed at ~35–45 ft / 10–14m
- Green: Absorbed at ~70–75 ft / 21–23m
- Blue: Penetrates deepest, dominates below 30m
- Horizontal Distance Rule: Light travels to subject AND back — double the distance

**Refraction & Caustics:**
- Refractive Index: Water (1.33) vs Air (1.0)
- Apparent Magnification: Objects appear ~33% larger and ~25% closer
- Caustics: Converging light patterns from surface waves acting as lenses
- Caustic Pattern: Dancing rippled light on submerged surfaces
- Snell's Window: 96° underwater view cone to surface (circular fisheye effect)

**Volumetric Properties:**
- Backscatter: Light reflecting off suspended particles toward camera
- Tyndall Effect: Visible light beams through particulate matter
- Color Temperature Shift: 5500K surface → 10000K+ at depth (blue/cyan dominant)
- Contrast Reduction: Scattering reduces contrast with distance

**Artificial Underwater Lighting:**
- Strobe Color Temperature: 5000K–6000K (daylight balanced)
- Red Filter: Restores absorbed reds in ambient light photography
- Positioning: 45° above subject, arms-length distance to minimize backscatter
- Falloff: Rapid due to water absorption + inverse square law

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Underwater/Submerged/Aquatic] scene at [depth], 
[subject] suspended in [water type: clear/turbulent/deep ocean/freshwater/pool], 
caustic light patterns dancing across [surface/subject] from surface refraction, 
color shift to [dominant hue] at depth with [remaining colors] filtered out, 
volumetric light beams penetrating water column, 
particulate matter catching light creating [backscatter/bokeh particles], 
refractive distortion at water-air boundary, 
[additional lighting: strobe/ambient/natural] illuminating subject, 
underwater cinematography aesthetic, 
realistic aquatic physics
```

**Negative Prompts:**
```
full spectrum color at depth, red colors in deep water, 
dry lighting, surface lighting without water distortion, 
clear air instead of water, unrealistic color saturation at depth, 
shadows without caustic patterns, no volumetric haze
```

---

### ADVANCED TECHNIQUES

**1. Shallow Water (0–15 ft / 0–4.5m)**
- Red still present but attenuated
- Warm-cool contrast possible with artificial light
- Strong caustic patterns from surface
- Clear visibility, some backscatter
- Color temperature: 6000K–8000K

**2. Mid-Water (15–40 ft / 4.5–12m)**
- Red/orange gone from ambient
- Subject appears blue-green without artificial light
- Caustics still present but softer
- Increasing particulate haze
- Color temperature: 8000K–12000K

**3. Deep Water (40+ ft / 12m+)**
- Blue/cyan dominant, monochromatic ambient
- Artificial light essential for color
- Caustics minimal or absent
- Heavy volumetric haze
- Color temperature: 10000K–20000K

**4. Surface Interface (Split-Level/Over-Under)**
- Snell's window circular distortion above waterline
- Sharp refractive line at water surface
- Above water: Normal color, bright sky
- Below water: Blue shift, caustics, distortion
- Technical challenge: Exposure balance between zones

**5. Pool/Clear Water**
- Cyan/blue cast from pool walls
- Artificial lighting often tungsten (warm-cool contrast)
- Caustics from surface agitation
- Clean, minimal particulate
- Color temperature: 7000K–10000K ambient

---

### DEPTH-TO-COLOR CHART
| Depth | Ambient Color | Lost Colors | Artificial Light Needed |
|-------|---------------|-------------|------------------------|
| 0–5m | Cyan-Blue | Slight red loss | Optional for warmth |
| 5–10m | Blue-Green | Red gone | Recommended for skin |
| 10–20m | Cyan | Red/Orange gone | Essential for color |
| 20–30m | Deep Blue | Red/Orange/Yellow weak | Essential |
| 30m+ | Blue-Monochrome | Green attenuating | Only source of color |

---

### EXAMPLE PROMPTS

**Shallow Reef:**
> Underwater scene at 10 feet depth, coral reef illuminated by dappled sunlight creating caustic patterns on sandy bottom, vibrant fish with accurate color (red, orange, yellow visible in shallow water), volumetric light beams penetrating clear turquoise water, slight particulate backscatter creating atmospheric bokeh, surface visible above with Snell's window distortion, underwater photography with wide-angle dome port, realistic refraction and magnification, cinematic documentary style

**Deep Ocean:**
> Deep underwater scene at 30 meters, diver illuminated by single strobe light revealing skin tones against deep blue monochromatic ambient, red and orange completely filtered out of background, caustic patterns absent at depth, heavy volumetric haze with floating marine snow catching strobe light, dramatic contrast between lit subject and dark water, technical diving photography, realistic aquatic physics, moody deep ocean atmosphere

**Surface Split:**
> Split-level over-under photograph, half above water showing golden hour sky and clouds, half below showing underwater world with blue-cyan color cast and caustic light patterns on submerged rocks, sharp refractive line at water surface with Snell's window circular distortion, subject swimming at interface between two worlds, dome port optical effect, realistic water physics, cinematic wide shot

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify depth explicitly to justify color loss
- Use "caustic patterns" or "light caustics" for surface refraction effect
- Include "particulate matter" or "marine snow" for volumetric depth
- Mention "blue color cast" or "cyan ambient" to prevent full-spectrum color at depth
- Use "Snell's window" for surface interface shots
- Specify water clarity ("clear water", "turbulent", "murky") for scattering control
