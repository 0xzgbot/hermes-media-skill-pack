# SKILL: Resolution & Aspect Ratio Language
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Mastery of dimensional control in AI image generation. Aspect ratio is not merely a crop — it is a compositional command that dictates spatial logic, subject framing, and environmental scope [^63^]. Resolution determines pixel budget and native detail. Each model has specific sweet spots, increment constraints, and optimal ranges [^58^].

---

### ASPECT RATIO AS COMPOSITIONAL COMMAND

**The Hidden Impact:**
When you specify an aspect ratio, the AI optimizes composition for that exact frame shape. Generating square and cropping later removes context the AI specifically included [^58^]. Match ratio to subject matter from the start [^63^].

**Vertical Subjects (People, Trees, Towers):**
- Ratios: 9:16, 2:3, 3:4, 4:5
- Why: Provides vertical pixels for full body, height, upward gaze
- Risk in wide ratios: Head cut off, body warped to fit sideways [^63^]

**Horizontal Subjects (Landscapes, Cars, Rooms):**
- Ratios: 16:9, 2:1, 21:9, 3:2
- Why: Horizontal space for horizons, vehicles, architectural sweep
- Risk in tall ratios: Cramped composition, subject stacked unnaturally [^63^]

**Square Subjects (Portraits, Products, Instagram):**
- Ratio: 1:1
- Why: Balanced, versatile, social-native
- Risk: Neither vertical nor horizontal emphasis; safe default

---

### STANDARD ASPECT RATIOS & USE CASES

| Ratio | Dimensions (Common) | Best For | Model Notes |
|-------|---------------------|----------|-------------|
| 1:1 | 1024×1024, 1080×1080 | Instagram, product, portrait | Universal default |
| 4:5 | 1080×1350 | Instagram portrait, editorial | Vertical but not extreme |
| 2:3 | 1024×1536, 1080×1620 | Portrait, full body, phone wallpaper | Classic vertical photo |
| 9:16 | 1080×1920 | TikTok/Reels, stories, phone full | Native vertical video |
| 3:2 | 1536×1024 | Landscape photography, print | Classic photo ratio |
| 16:9 | 1920×1080, 1280×720 | Video, desktop, cinematic | Widescreen standard |
| 21:9 | 2560×1080 | Cinematic ultra-wide, anamorphic | Movie scope |
| 2.39:1 | ~1920×804 | CinemaScope, anamorphic | True film ratio |
| 2:1 | 2048×1024 | Panoramic, landscape, banner | Wide but not cinematic |

---

### MODEL-SPECIFIC RESOLUTION RULES

**Flux / Flux2:**
- Flux 1.1 Pro Ultra: Up to 4MP native (2000×2000, ~4 megapixels) [^58^]
- Flux Dev/Schnell: Flexible ratio parameter; exact pixels determined internally [^58^]
- Optimal: 1024×1024 to 2000×2000
- No increment constraints; ratio-based input
- Prompt language: Specify ratio directly — `16:9 aspect ratio`, `vertical 9:16`, `cinematic 2.39:1 widescreen`

**SDXL / z_image:**
- Native sweet spot: ~1024×1024 (1MP) [^58^]
- Maximum before quality degradation: 1536×1536 (2.25MP)
- Increment rule: Width and height must be multiples of 8 [^58^]
- Wrong multiples cause errors or silent rounding [^58^]
- Prompt language: Less reliable ratio parsing; set exact dimensions in UI
- Common SDXL sizes:
  - 1024×1024 (1:1)
  - 1024×576 (16:9)
  - 768×1344 (9:16)
  - 1216×832 (3:2)

**SD 1.5:**
- Native: 512×512
- Upscaling required for higher resolution
- Increment: Multiples of 64
- Prompt language: Ratio rarely parsed from prompt; set in UI

**LTX Video:**
- Default resolution: 1216 × 704 at 30 FPS [^67^]
- Other resolutions supported but 1216×704 is optimized
- Aspect ratio: 16:9 native (1216:704 = 1.73:1)
- Prompt language: `16:9 cinematic video`, `horizontal landscape format`
- Frame rate: Specify `30fps` for native; other rates supported

**GPT-image / DALL-E 3:**
- Fixed presets: 1024×1024, 1792×1024 (16:9), 1024×1792 (9:16) [^58^]
- gpt-image-2: Any resolution with constraints [^74^]
- Prompt language: `square 1:1`, `landscape 16:9`, `portrait 9:16`

---

### PROMPT LANGUAGE FOR ASPECT RATIO

**Direct Ratio Commands:**
```
--ar 16:9          # Midjourney syntax
aspect ratio 16:9  # Universal
16:9 widescreen    # Descriptive
vertical 9:16      # Vertical
square 1:1         # Square
cinematic 2.39:1   # Anamorphic
panoramic 21:9     # Ultra-wide
```

**Compositional Cues (When Model Ignores Ratio Parameter):**
```
full body portrait        # Signals need for vertical space
landscape vista           # Signals need for horizontal space
close-up headshot         # Signals square or 4:5
panoramic mountain range  # Signals 2:1 or 21:9
Instagram story format    # Signals 9:16
cinematic widescreen shot # Signals 16:9 or 2.39:1
```

**Resolution Language:**
```
8k uhd              # Quality signal, not literal pixels
4k resolution       # Quality signal
high resolution     # Generic
highly detailed     # Better than resolution claims
sharp at 100% zoom    # Specific quality claim
pixel-perfect detail  # Technical precision
```

---

### RESOLUTION VS. ASPECT RATIO

**Resolution = Total Pixels:**
- 1920×1080 = 2.07MP (16:9)
- 1024×1024 = 1.05MP (1:1)
- 3840×2160 = 8.29MP (16:9)
- Two images can share aspect ratio but have very different resolutions [^58^]

**Upscale Strategy:**
1. Generate at model's native sweet spot
2. Upscale using Real-ESRGAN, Topaz Gigapixel, or model-native upscale
3. Never generate far above native resolution — quality degrades [^58^]

**Platform-Specific Upscale:**
- Flux 1.1 Pro Ultra: Generate up to 4MP natively when possible [^58^]
- SDXL: Generate at 1024×1024, then upscale 2× to 2048×2048
- LTX: Generate at 1216×704, upscale for final delivery

---

### EXAMPLE PROMPTS BY RATIO

**1:1 Square (Product):**
> `Square 1:1 product photography, titanium watch centered on pure black background, symmetric composition, 8k detail, sharp focus, studio lighting`

**9:16 Vertical (Portrait):**
> `Vertical 9:16 portrait, full body fashion model in flowing red gown, standing in marble corridor, shot from low angle, 8k, sharp focus, editorial photography`

**16:9 Horizontal (Landscape):**
> `Cinematic 16:9 landscape, panoramic mountain range at sunrise, golden light on snow peaks, mist in valleys, 8k uhd, National Geographic photography`

**21:9 Ultra-Wide (Cinematic):**
> `Cinematic 21:9 ultra-wide, anamorphic film still of astronaut on Mars ridge, Earth as small blue dot, 2.39:1 aspect ratio, Kodak Vision3, film grain, dramatic side-light`

**4:5 Vertical (Instagram):**
> `4:5 portrait editorial, close-up beauty shot with soft window light, warm tones, shallow depth of field, Instagram-ready composition, sharp skin detail`

**2:1 Panoramic (Banner):**
> `Panoramic 2:1 banner, city skyline at blue hour with light trails on highway, wide horizontal composition, website header format, crisp architectural detail`

---

### TECHNICAL NOTES FOR AI GENERATION
- Always generate at target aspect ratio natively — never crop after [^58^]
- Match ratio to subject: vertical subjects = vertical ratios, horizontal subjects = horizontal ratios [^63^]
- SDXL: Stay within 1MP–2MP native; use multiples of 8 [^58^]
- Flux: Use ratio parameter or specify in prompt; supports up to 4MP [^58^]
- LTX: Default 1216×704 at 30fps; other ratios supported but may need testing [^67^]
- GPT-image: Specify ratio in prompt even with reference images [^59^]
- Resolution claims ("8k") in prompts act as quality signals, not literal pixel counts
