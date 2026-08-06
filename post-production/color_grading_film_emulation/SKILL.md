# SKILL: Color Grading & Film Emulation
## Version: 1.0 | Hermes Agent Post-Production & Look Development

---

### DESCRIPTION
Mastery of cinematic color science and analog film emulation for AI-generated imagery. This skill bridges the gap between raw render output and finished cinematic look by encoding the vocabulary of professional color grading: LUT-based looks, film stock characteristics, tonal curves, and the emotional grammar of color. Essential for ensuring that every frame in a campaign shares a unified, intentional color identity.

---

### TECHNICAL PARAMETERS

**The 5-Pillar Color System:**
- **Primary Palette:** 60% of frame — sets emotional temperature
- **Secondary Palette:** 30% of frame — provides contrast and depth
- **Accent Color:** 10% of frame — draws eye, punctuates story
- **Shadow Tint:** Color cast in blacks (cool = mystery, warm = nostalgia)
- **Highlight Roll-Off:** How bright areas transition to white (hard = digital, soft = film)

**Film Stock Emulation Lookup:**

| Film Stock | Color Character | Shadow Tint | Highlight Roll-Off | Best For |
|------------|----------------|-------------|-------------------|----------|
| **Kodak Vision3 500T** | Warm highlights, cool shadows, wide latitude | Cool blue-black | Soft, creamy | Night interiors, moody drama |
| **Kodak Vision3 250D** | Neutral daylight, high saturation, tight grain | Neutral black | Moderate | Day exteriors, commercial |
| **Fujifilm Eterna 500** | Creamy highlights, pastel shadows, organic grain | Warm brown-black | Very soft | Romance, nostalgia, golden age |
| **Kodak Ektachrome 100** | Saturated, punchy reds and greens, high contrast | Cool neutral | Hard clip | Fashion, pop, 1970s throwback |
| **Ilford Delta 3200** | Aggressive grain, high contrast, pushed B&W | Pure black | Hard | Documentary, gritty realism |
| **CineStill 800T** | Tungsten balanced, halation bloom in highlights | Warm black | Blooming / soft | Neon nights, music videos |

**Tonal Curve Descriptors:**
- **S-Curve:** Increased contrast, cinematic punch, crushed blacks
- **Linear:** Flat, log-like, maximum latitude for grading
- **Lifted Blacks:** Filmic shadow detail, reduced contrast, vintage feel
- **Crushed Blacks:** Deep shadows, high contrast, modern digital look
- **Soft Highlights:** Gentle roll-off, film-like, forgiving brights
- **Hard Clip:** Digital precision, clinical, sharp edge at white point

**Color Temperature Grading:**
- **Day-for-Night (American):** Desaturate blues, crush shadows, cool overall
- **Teal & Orange:** Push shadows toward cyan, highlights toward amber — skin separation
- **Bleach Bypass:** Desaturated, high contrast, metallic sheen — war, dystopia
- **Cross-Process:** Unnatural color shifts, magenta shadows, green highlights — experimental
- **Daylight Balance:** 5600K neutral, clean, documentary truth
- **Tungsten Warmth:** 3200K golden, nostalgic, interior intimacy

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Cinematic color grading, [film stock emulation] color science,
[shadow tint] in dark areas, [highlight roll-off] in bright areas,
[tonal curve] contrast profile, [color temperature] overall cast,
[saturation level] color intensity, [specific look: teal-orange / bleach-bypass / cross-process],
unified color identity across sequence, professional post-production look,
[grain level] film grain texture
```

**Negative Prompts (SDXL/z_image):**
```
uncorrected color, inconsistent white balance, oversaturated neon, flat log look,
clipped highlights, crushed blacks with no detail, color banding, posterization,
multiple color temperatures in one frame, digital sharpening artifacts, video look
```

---

### ADVANCED TECHNIQUES

**1. The Teal & Orange Blockbuster**
- Shadows: Push toward cyan/teal (#0A4F5C)
- Skin Tones: Pull toward warm amber (#D4A373)
- Saturation: Reduce overall, boost skin
- Contrast: Moderate S-curve
- Emotional: Heroic, commercial, universally pleasing
- Best For: Action, brand films, aspirational content

**2. The Bleach Bypass War Look**
- Saturation: -30% to -50%
- Contrast: Aggressive S-curve
- Shadows: Crushed, metallic
- Highlights: Hard clip with slight halation
- Grain: Heavy, pushed 35mm
- Emotional: Trauma, grit, survival, documentary
- Best For: War films, dystopia, post-apocalyptic, social realism

**3. The Kodak Gold Nostalgia**
- Film Stock: Vision3 250D or Eterna 500
- Shadow Tint: Warm brown-black
- Highlight: Soft golden roll-off
- Saturation: Rich but not oversaturated
- Grain: Fine, organic, 35mm
- Emotional: Memory, childhood, lost time, romance
- Best For: Heritage brands, family stories, period pieces, travel

**4. The CineStill Night Bloom**
- Film Stock: CineStill 800T
- Key Feature: Halation bloom in practical lights
- Color Temp: Tungsten warm (3200K)
- Shadows: Deep blue-black
- Highlights: Red/orange bloom around bulbs
- Emotional: Nocturnal, intimate, music, youth
- Best For: Night city, concerts, bars, neon-adjacent storytelling

**5. The Desaturated Documentary**
- Saturation: -20% to -40%
- Contrast: Minimal, lifted blacks
- Skin Tones: Preserved naturally
- Grain: Fine 16mm texture
- Emotional: Truth, objectivity, observer distance
- Best For: Documentary, journalism, social issues, realism

---

### EXAMPLE PROMPTS

**Kodak Night Interior:**
> Cinematic color grading, Kodak Vision3 500T film emulation, cool blue-black shadow tint with warm creamy highlight roll-off, moderate S-curve contrast, tungsten 3200K overall warmth, rich saturated color intensity, soft film grain texture, professional post-production look, unified color identity

**Bleach Bypass Dystopia:**
> Bleach bypass color treatment, desaturated metallic palette, aggressive contrast with crushed shadows and hard highlight clip, cool shadow tint, minimal color saturation, heavy pushed 35mm grain, post-apocalyptic color science, gritty documentary aesthetic

**Teal & Orange Hero:**
> Teal and orange cinematic grading, cyan-teal shadows (#0A4F5C), warm amber skin tones (#D4A373), moderate S-curve contrast, reduced overall saturation with boosted skin, soft highlight roll-off, clean professional blockbuster look, subtle 35mm grain

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify film stock name explicitly to trigger emulation priors
- Use "shadow tint" and "highlight roll-off" for precise tonal control
- Mention grain type (fine/medium/heavy) and format (16mm/35mm/65mm)
- For FLUX: describe color in positive terms; no negative prompts
- For LTX: specify "consistent color grading across frames" as guardrail
- For SDXL: use "cinematic color grading" and film stock names as quality tokens
- Color temperature in Kelvin helps anchor white balance: 3200K warm, 5600K neutral, 9000K cool
