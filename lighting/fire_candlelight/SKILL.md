# SKILL: Fire & Candlelight
## Version: 1.0 | Hermes Agent Lighting System

---

### DESCRIPTION
Mastery of flame-based illumination: candles, fireplaces, torches, campfires, and gas flames. Covers the unique flicker character, extreme warm color cast (1800K–2800K), organic shadow movement, and the multi-layered nature of fire lighting (base coals + active flame + ambient bounce). Essential for period pieces, intimate scenes, and atmospheric horror.

### TRIGGER KEYWORDS
candlelight, firelight, fire, candle, campfire, torch, fireplace, flame, warm fire, flickering light, lantern, gas lamp, intimate fire, period lighting, 1800K, fire lit, fire glow

### CORE RULES
- Color temperature 1850K–2000K for candle: extreme warm amber, no neutral tones
- Fire light always flickers: shadows are never static in flame-lit scenes
- Rapid inverse-square falloff: faces lit, background nearly black
- Multi-layer structure: blue-white base flame → orange-yellow body → amber ambient bounce
- Small source = hard shadow edges despite warm quality
- Smoke haze scatters light into visible volumetric glow — add sparingly for atmosphere
- Period and horror aesthetics both use fire; adjust shadow depth for mood (deeper = horror)

---

### TECHNICAL PARAMETERS

**Flame Color Temperature:**
- Candle Flame: 1850K–2000K (yellow-orange core, blue-white at base)
- Oil Lamp: 2000K–2500K
- Campfire: 1800K–2800K (varies by fuel, oxygen)
- Gas Flame: 1900K–2200K (cleaner, less flicker)
- Fireplace: 1500K–2000K (red coals) + 2500K–3000K (active flame)

**Flicker Character:**
- Frequency: 2–10 Hz (irregular, organic)
- Amplitude: 0.5–2 stops variation in intensity
- Pattern: Non-repeating, chaotic (never sine wave or regular)
- Shadow Movement: Flame height variation creates shifting shadow length
- Multiple Sources: Random phase between candles creates organic complexity

**Shadow Behavior:**
- Direction: Radial outward from flame center
- Hardness: Hard shadows due to small source size
- Movement: Constant subtle shifting (living, breathing quality)
- Multiple Flames: Overlapping shadows with different directions
- Ceiling/Upper Shadows: Dark, minimal bounce (light falls downward)

**Warm Cast Properties:**
- Skin Rendering: Extremely warm, golden-amber, flattering to most skin tones
- White Balance: Daylight-balanced camera sees heavy orange; tungsten balance still warm
- Color Shift: All neutrals become warm; blues become muted or gray
- Bounce Light: Warm fill from surrounding surfaces (walls, ceiling)
- Falloff: Rapid inverse square due to low source intensity

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Intimate/period/atmospheric] scene lit by [candle/fireplace/campfire/torch], 
subject illuminated by [number] [source type] creating extreme warm [1800K–2800K] light, 
organic flicker casting dancing shadows on [surfaces], 
[hard/soft] shadows shifting with flame movement, 
rich amber-orange glow on skin and surroundings, 
deep warm shadows with [subtle/no] detail, 
background fading to darkness beyond flame reach, 
[smoke/heat haze/atmosphere] distorting air above flame, 
cinematic fire lighting, 
photorealistic flame behavior
```

**Negative Prompts:**
```
cool white light, even studio lighting, static light source, 
no shadow movement, fluorescent lighting, daylight balance, 
clean modern lighting, LED look, flat lighting, 
blue ambient light, overexposed flames losing detail
```

---

### ADVANCED TECHNIQUES

**1. Single Candle Intimacy**
- Source: One candle at 1–2 ft from subject
- Light: Extremely soft due to proximity (inverse square)
- Shadow: Single, shifting direction
- Eye Light: Catchlight from flame (small, warm)
- Emotional: Vulnerability, intimacy, historical authenticity
- Ratio: Key to ambient = extreme (near darkness beyond)

**2. Fireplace Multi-Layer**
- Base: Red glowing coals (constant, low, red-orange)
- Active: Dancing flames (variable, higher, yellow-orange)
- Bounce: Warm light from hearth surround (soft fill)
- Shadow: Complex — coals create sharp base shadows, flames add shifting overlay
- Emotional: Domestic warmth, safety, nostalgia

**3. Torch/Carrier Light**
- Source: Moving flame held by subject
- Light: Unstable, subject partially illuminated
- Shadow: Extreme movement, long shadows
- Flicker: Enhanced by walking movement + wind
- Emotional: Journey, danger, exploration, period drama

**4. Candlelit Group Scene**
- Multiple sources: 3–20 candles
- Each face illuminated by nearest candle
- Overlapping warm pools of light
- Background: Deep shadow between sources
- Emotional: Ritual, conspiracy, romance, historical

**5. Fire as Background/Rim**
- Subject between camera and fire
- Rim light from flames (warm, flickering)
- Face in shadow or minimal bounce fill
- Emotional: Danger, destruction, silhouette drama

---

### FLAME TYPE QUICK REFERENCE
| Source | Color Temp | Flicker | Shadow | Best For |
|--------|------------|---------|--------|----------|
| Single Candle | 1850K | Gentle, slow | Single, soft | Intimate portrait |
| Multiple Candles | 1900K | Complex, organic | Overlapping | Historical scene |
| Fireplace | 1500–3000K | Moderate | Layered | Domestic warmth |
| Campfire | 1800–2800K | Active, windy | Long, shifting | Outdoor night |
| Torch | 2000K | Very active | Extreme movement | Action, period |
| Gas Lamp | 2200K | Minimal | Stable | Victorian, street |

---

### EXAMPLE PROMPTS

**Intimate Portrait:**
> Intimate portrait lit by single candle, subject's face illuminated by warm 1900K flickering light at 18 inches distance, soft amber glow wrapping skin with golden highlights, hard shadows shifting subtly on wall behind as flame dances, deep brown shadows on non-illuminated side of face, catchlight from flame visible in eyes, background dissolving into pure darkness beyond candle reach, atmospheric heat haze above flame, romantic historical aesthetic, photorealistic skin texture in warm light, cinematic color science

**Campfire Scene:**
> Group gathered around crackling campfire at night, faces illuminated by warm 2500K firelight with orange-red glow, long shadows stretching behind subjects shifting with flame movement, sparks rising into dark sky, smoke catching backlight creating volumetric rays, background forest in deep shadow, realistic fire behavior with blue-white base and yellow-orange tips, documentary camping aesthetic, warm-cool contrast between fire and night blue

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify Kelvin temperature ("1900K", "2500K") to anchor warm cast
- Use "flickering" or "dancing shadows" to imply movement
- Mention "hard shadows" due to small source size
- Include "darkness beyond" or "fading to black" for falloff realism
- Use "blue-white at base" for accurate flame detail
- Specify number of sources for complexity (single vs multiple)
