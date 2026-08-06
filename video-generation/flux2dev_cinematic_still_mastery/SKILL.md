# SKILL: FLUX.2 Dev Cinematic Still Mastery
## Version: 1.0 | Hermes Agent Flux2 Film Frame & Storyboard Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for generating production-quality cinematic still frames with FLUX.2 Dev. This skill encodes the precise film stock emulation vocabulary, aspect-ratio-aware composition language, color-temperature-to-mood mapping, and temporal-freeze techniques required to produce frames that read as extracted from motion pictures rather than static photographs. Covers anamorphic vs spherical optics, film grain architectures, aspect ratio psychology, and the specific positive-only constraint system for cinematic artifact prevention.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Cinematic Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled)
- **Token Priority:** First 10–15 tokens must establish the shot type and subject. "Wide establishing shot of..." or "Intimate extreme close-up of..." must lead.
- **Prompt Length:** 50–90 words for complex cinematic scenes. Complex scenes with multiple light sources benefit from longer prompts up to 120 words.
- **Guidance Scale:** 3.5–4.0 for cinematic work (higher = overly contrasty, saturated; lower = muddy mid-tones)
- **Steps:** 30–40 for film grain fidelity and subtle halation. 28 minimum for acceptable texture.
- **Resolution:** Generate at target aspect ratio: 1920×816 for 2.39:1, 1920×1080 for 16:9, 1440×1080 for 4:3. Avoid generating square and cropping.
- **No Prompt Weights:** Avoid `(word:1.2)` syntax. Use natural emphasis: "prominently featuring," "with particular attention to."

**Film Stock Emulation Matrix:**

| Film Stock | Color Character | Grain Structure | Halation | Best Genre |
|-----------|----------------|----------------|----------|------------|
| **Kodak Vision3 500T** | Warm shadows, rich skin, slight magenta in blacks | Fine, even, pushed one stop | Moderate red halation around highlights | Drama, intimacy, night interiors |
| **Kodak Vision3 250D** | Neutral-warm, excellent latitude, naturalistic | Very fine, clean | Minimal | Documentary, natural light, realism |
| **Kodak Vision3 50D** | Saturated, crisp, vibrant primaries | Ultra-fine, virtually invisible | None | Day exteriors, nature, vibrant fiction |
| **Kodak EASTMAN Double-X 5222** | High contrast, silvery blacks, punchy | Coarse, prominent, classic | Strong | Noir, period drama, gritty realism |
| **Fujifilm Eterna 500T** | Cool shadows, green-tinted blacks, creamy highlights | Fine, organic | Subtle green | Sci-fi, melancholy, Asian cinema |
| **Fujifilm Velvia 50 (still)** | Hyper-saturated, contrasty, jewel-like | Fine, saturated grain | None | Fantasy, heightened reality, memory |
| **CineStill 800T** | Tungsten-balanced, extreme halation, sodium vapor glow | Moderate, pushed look | Extreme red/orange around highlights | Neon noir, night city, music video |
| **Ilford HP5 Plus (B&W)** | Rich tonal range, creamy mid-tones, deep blacks | Prominent, organic, classic | N/A (B&W) | Documentary, classic cinema, mood |

**Aspect Ratio Psychology & Composition:**

| Ratio | Emotional Register | Composition Strategy | Classic Association |
|-------|-------------------|---------------------|---------------------|
| **2.39:1 Anamorphic** | Epic, expansive, isolation in landscape | Subject at thirds, vast negative space | Lawrence of Arabia, Blade Runner |
| **1.85:1 Flat** | Naturalistic, contemporary, intimate | Balanced framing, moderate headroom | Modern American indie, comedy |
| **16:9 (1.78:1)** | Digital, immediate, broadcast | Center-weighted or rule of thirds | TV, streaming, documentary |
| **4:3 (1.33:1)** | Nostalgic, contained, formal | Symmetrical, centered, classical | Classic Hollywood, The Grand Budapest Hotel |
| **1:1 Square** | Instagram, constrained, focused | Centered, minimal, graphic | Social, Wes Anderson inserts |
| **9:16 Vertical** | Mobile-native, intimate, urgent | Subject-centered, minimal background | TikTok, mobile-first content |

**Lens & Optical Signature Library:**

| Lens / System | Optical Character | Bokeh | Distortion | Best For |
|--------------|-------------------|-------|------------|----------|
| **Cooke S4/i** | Warm, creamy, "Cooke look," slight veiling | Cat-eye, smooth | Minimal barrel | Period drama, warm intimacy |
| **Cooke S7/i** | Modern Cooke, sharp but warm | Smooth oval | Very low | Contemporary narrative |
| **Arri/Zeiss Master Prime** | Clinical, sharp, high contrast | Geometric, defined | Near-zero | Sci-fi, precision, cold drama |
| **Leica Summilux-C** | Romantic, slightly glowing, beautiful falloff | Creamy, swirling | Subtle | Romance, beauty, luxury |
| **Hawk V-Lite Anamorphic** | Vintage anamorphic, heavy character | Oval, horizontal streak | Strong barrel + squeeze | Retro sci-fi, music video |
| **Atlas Orion Anamorphic** | Modern anamorphic, controlled flare | Oval, clean | Moderate squeeze | Contemporary anamorphic |
| **Kowa Prominar** | Vintage Japanese, warm, low contrast | Bubble, swirly | Strong character | 70s nostalgia, indie |
| **Canon K35** | Vintage spherical, glowing highlights | Creamy, warm | Moderate barrel | 70s-80s American cinema |
| **Lomo Round Front** | Russian anamorphic, unpredictable, wild | Weird oval, chaotic | Extreme character | Experimental, aggressive |
| **iPhone 16 Pro (computational)** | Deep DoF, natural, candid, slight HDR | Minimal, deep focus | Zero | Found footage, realism, documentary |

**Color Temperature-to-Mood Mapping:**

| Kelvin | Light Source | Emotional Association | Genre Match |
|--------|-------------|----------------------|-------------|
| 1700K | Match flame | Primitive, dangerous, intimate | Horror, cave, survival |
| 2400K | Candle, fireplace | Romance, nostalgia, warmth | Period drama, Christmas, intimacy |
| 3200K | Tungsten, incandescent | Domestic, theatrical, artificial | Stage, interior night, studio |
| 4200K | Fluorescent, overcast morning | Clinical, institutional, unease | Hospital, office, thriller |
| 5600K | Daylight, noon sun | Neutral, documentary, real | News, documentary, verité |
| 6500K | Overcast, north light | Melancholy, flat, contemplative | Nordic drama, grief, winter |
| 9000K–10000K | Deep twilight, heavy overcast | Mystery, liminality, transition | Noir, thriller, blue hour |

---

### PROMPT ARCHITECTURE

**Core Cinematic Still Template (FLUX.2 Dev):**
```
[Shot type + scale]: [Wide establishing / Medium shot / Close-up / Extreme close-up / Insert] of [subject]
[Subject + action]: [Who/what] [doing what] [emotional state]
[Environment]: [Where, time of day, weather, atmosphere]
[Camera + lens]: Shot on [camera system], [lens], f/[aperture]
[Lighting]: [Key light direction + quality + color temp K], [fill description], [practical sources]
[Film stock]: [Specific stock emulation], [grain level], [halation if applicable]
[Color grade]: [Color palette / HEX codes], [contrast level], [shadow tint]
[Composition]: [Aspect ratio], [subject placement], [negative space usage]
[Atmosphere]: [Haze, dust, rain, lens effects, chromatic aberration]
[Mood]: [Single emotional word or phrase]
```

**Guardrails (Positive-Only Cinematic Safety):**
```
coherent spatial logic, consistent perspective, natural light falloff,
photographic film grain, organic lens character, no artificial sharpening artifacts,
stable horizon line, believable depth of field, realistic shadow casting,
natural color relationships, no posterization in gradients, smooth tonal transitions
```

**Temporal Freeze Anchors (For Storyboard Consistency):**
When generating multiple frames from the same scene, lock these parameters:
- **Camera system** (never change between shots in same scene)
- **Film stock** (maintains grain/color continuity)
- **Color temperature** (±200K max drift between shots)
- **Lens focal length** (or document intentional changes)
- **Atmospheric density** (haze/fog consistent across sequence)

---

### ADVANCED TECHNIQUES

**1. The Anamorphic Wide Shot**
- Setup: Epic landscape or vast interior, subject small within frame
- Camera: "Shot on ARRI Alexa 65 with Hawk V-Lite anamorphic 40mm, 2.39:1 aspect ratio composition"
- Lens Character: "Oval bokeh in background lights, subtle horizontal lens flare from bright sources, 2x anamorphic squeeze rendering"
- Light: "Golden hour sun low on horizon, long shadows stretching across frame, warm 3000K key with cool 8000K fill from sky"
- Film: "Kodak Vision3 250D, fine grain, natural color rendition"
- Composition: "Subject positioned at left third, vast negative space to right, low horizon line emphasizing sky"
- Emotional: Awe, insignificance, grandeur, human vs. nature
- Best For: Epic opening shots, westerns, sci-fi establishing, travel

**2. The Intimate Two-Shot**
- Setup: Two characters in close proximity, emotional exchange
- Camera: "Shot on Cooke S4/i 50mm at f/2.0, medium two-shot, eye-level camera"
- Light: "Soft key from practical lamp between characters, warm 2800K tungsten, both faces modeled with gentle shadows, subtle edge light separating from background"
- Film: "Kodak Vision3 500T, fine grain, warm shadows with slight magenta in blacks"
- Focus: "Shallow depth of field, background softly out of focus, both subjects in acceptable sharpness"
- Composition: "Characters framed with equal weight, negative space above suggesting emotional weight"
- Emotional: Intimacy, tension, connection, unspoken communication
- Best For: Relationship drama, dialogue scenes, emotional reveals

**3. The Noir High-Contrast Single**
- Setup: Single figure in darkness, dramatic chiaroscuro
- Camera: "Shot on ARRI/Zeiss Master Prime 85mm at f/1.4, close-up, slight low angle"
- Light: "Hard single source from above-left creating deep shadows, 3200K tungsten, no fill — pure black shadow on right side of face, catchlight in one eye only"
- Film: "Kodak EASTMAN Double-X 5222, high contrast, silvery blacks, coarse grain"
- Atmosphere: "Cigarette smoke catching light beam, dust particles visible in harsh source"
- Color: "Monochrome with warm selenium tone, deep blacks, bright highlights with slight halation"
- Emotional: Danger, mystery, moral ambiguity, isolation
- Best For: Crime, noir, thriller, psychological drama

**4. The Magic Hour Long Lens**
- Setup: Compressed exterior, golden hour, telephoto compression
- Camera: "Shot on Canon C500 Mark III with 200mm telephoto at f/2.8, extreme background compression"
- Light: "Final five minutes of sunset, 2800K golden light, long shadows, warm glow on skin and surfaces, cool blue sky in background"
- Film: "Kodak Vision3 50D, ultra-fine grain, saturated warm tones, vibrant primaries"
- Bokeh: "Creamy circular bokeh from distant city lights or foliage, smooth transition zones"
- Emotional: Bittersweet, fleeting beauty, nostalgia, romantic finality
- Best For: Romance, endings, memory sequences, emotional peaks

**5. The Sci-Fi Clinical Wide**
- Setup: Futuristic interior, cold, precise, designed
- Camera: "Shot on ARRI/Zeiss Master Prime 21mm at f/5.6, wide shot, centered symmetrical composition"
- Light: "Cool 6500K LED panels from ceiling, even clinical distribution, no warm sources, slight cyan cast in shadows"
- Film: "Fujifilm Eterna 500T, cool shadows, green-tinted blacks, fine grain"
- Color: "Desaturated palette, whites and grays dominant, single accent color (#00D4AA cyan) on interface or clothing"
- Atmosphere: "Sterile air, no dust, no haze, sharp reflections on polished surfaces"
- Emotional: Cold, controlled, artificial, dystopian perfection
- Best For: Sci-fi, medical, corporate dystopia, space stations

**6. The Handheld Documentary Freeze**
- Setup: Candid moment captured, imperfect framing
- Camera: "Shot on Sony FX6 with 35mm at f/4, handheld slight tilt, documentary framing with excess headroom"
- Light: "Available light only, mixed sources — window daylight 5600K from left, warm practical 2700K from right, natural inconsistency"
- Film: "Kodak Vision3 250D, naturalistic, no stylization, fine clean grain"
- Imperfections: "Slight motion blur on moving hand, natural breathing composition shift, authentic documentary aesthetic"
- Emotional: Real, unfiltered, present-moment, journalistic truth
- Best For: Documentary, social realism, journalism, found footage

**7. The CineStill Neon Night**
- Setup: Urban night with practical neon/tungsten mix
- Camera: "Shot on Sony A7S III with 35mm f/1.4 at f/1.8, low light native ISO"
- Light: "Mixed tungsten streetlamps 3200K and sodium vapor 2200K, neon signs in magenta and cyan, extreme color contrast"
- Film: "CineStill 800T, extreme red/orange halation around bright highlights, pushed grain, tungsten color cast"
- Atmosphere: "Light rain creating reflections on asphalt, atmospheric haze catching colored light, wet surfaces mirroring neon"
- Emotional: Urban loneliness, nocturnal energy, cyber-romantic, edgy
- Best For: Music videos, neon noir, nightlife, contemporary thrillers

---

### EXAMPLE PROMPTS

**Epic Western Establishing:**
> Wide establishing shot of a lone rider on horseback crossing vast desert plain at golden hour, shot on ARRI Alexa 65 with Hawk V-Lite anamorphic 40mm at f/5.6, 2.39:1 aspect ratio composition, low horizon line with massive amber sky above, long shadows stretching from horse and rider across cracked earth, Kodak Vision3 250D film stock with fine grain and natural warm color rendition, dust particles visible in slanted sunlight, heat shimmer on distant horizon, epic scope with human figure small against landscape, awe-inspiring grandeur, cinematic western atmosphere

**Intimate Noir Close-Up:**
> Close-up of a middle-aged man in a darkened room, single hard light source from above-left creating deep chiaroscuro shadows, shot on ARRI/Zeiss Master Prime 85mm at f/1.4, Kodak EASTMAN Double-X 5222 high-contrast black and white with silvery blacks and coarse grain, one eye illuminated with sharp catchlight, other eye in pure black shadow, cigarette smoke curling through light beam, dust motes dancing in harsh source, slight low angle suggesting power, monochrome with warm selenium tone, cigarette cherry glowing red as only color accent, moral ambiguity, noir mystery atmosphere

**Sci-Fi Clinical Corridor:**
> Symmetrical wide shot of a sterile white corridor in a space station, shot on ARRI/Zeiss Master Prime 21mm at f/5.6, centered composition with vanishing point perspective, cool 6500K LED panels from ceiling creating even clinical light, Fujifilm Eterna 500T film stock with cool shadows and subtle green tint in blacks, polished reflective floor mirroring ceiling lights, single figure in white uniform walking away from camera at corridor end, interface screens with cyan accent color #00D4AA on walls, no dust no haze completely sterile atmosphere, desaturated palette whites and grays dominant, cold controlled dystopian perfection

---

### TECHNICAL NOTES FOR AI GENERATION
- **Shot type MUST be first 3–5 words:** "Wide establishing shot of..." establishes scale before FLUX.2 defaults to medium shot.
- **Film stock names are powerful tokens:** "Kodak Vision3 500T" triggers an entire color science more reliably than "warm cinematic look."
- **Aspect ratio in prompt:** Include "2.39:1 composition" or "16:9 framing" — FLUX.2 interprets compositional intent from ratio language even if generating at different resolution.
- **Anamorphic requires explicit mention:** "Anamorphic lens," "oval bokeh," "horizontal flare," "2x squeeze" — all needed to trigger anamorphic character.
- **Light direction via clock face:** "Key light from 10:30 position" gives precise directional control more reliably than "side lighting."
- **Color temperature in Kelvin:** "5600K daylight" or "3200K tungsten" prevents FLUX.2 from averaging mixed sources into muddy neutrals.
- **Grain as desired quality:** "Fine 35mm grain" or "coarse pushed grain" — never "no grain" (triggers plastic smoothing).
- **Guidance 3.5–4.0 for cinematic:** Higher guidance produces over-contrasty, posterized results. Lower produces flat, unmotivated lighting.
- **Avoid "cinematic" as standalone:** Too vague. Replace with specific film stock + lens + aspect ratio.
- **For storyboard sequences:** Use identical camera/lens/film stock across all frames. Vary only shot scale, subject position, and action.
- **Temporal consistency hack:** When generating a sequence, include the scene slug in every prompt: "Scene 7A — Interior Night" to maintain contextual continuity.
