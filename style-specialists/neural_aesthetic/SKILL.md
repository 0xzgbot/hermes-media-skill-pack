---
name: neural_aesthetic
description: "Steer toward neural/latent aesthetic, not stock CGI."
version: 1.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [style-specialists, media, cinematic]
    category: style-specialists
---

# SKILL: Neural Aesthetic
## Domain: Lighting Constants, Mood Descriptors, Style DNA, Prompt Injection Architecture
## Version: 1.0
## For: Hermes Agent — Style System & Prompt Architecture

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete Neural Aesthetic system — a structured vocabulary for describing, combining, and injecting visual style DNA into AI generation prompts. It covers lighting constants (temperature, direction, quality), mood descriptors (emotional valence, atmospheric density), style combination algebra, and the specific architecture for injecting these descriptors into ComfyUI/Flux conditioning payloads.

When this skill is active, the agent should:
- Use precise lighting constant vocabulary (not vague "dramatic lighting")
- Apply mood descriptor matrices for emotional calibration
- Combine styles using algebraic rules (multiply, overlay, blend)
- Inject Neural Aesthetic descriptors into every prompt layer
- Reference project graph style nodes for cross-project consistency

---

## 2. THE NEURAL AESTHETIC PHILOSOPHY

Neural Aesthetic is not a style — it is a **meta-language for describing styles** in terms that AI models understand and can reproduce consistently. [^58^] [^59^]

### Core Principles

| Principle | Description | Prompt Vocabulary |
|-----------|-------------|-----------------|
| **Atomic Descriptors** | Break style into smallest indivisible units (light temp, shadow hardness, color saturation) | "atomic descriptor", "indivisible style unit", "base aesthetic particle" |
| **Combinatorial Algebra** | Styles combine like colors — primary + secondary = tertiary | "style algebra", "aesthetic combination", "descriptor fusion" |
| **Emotional Valence** | Every visual choice carries emotional weight; map descriptor to feeling | "emotional valence", "mood mapping", "feeling calibration" |
| **Consistency Through Structure** | Same descriptors produce same results across models when structured identically | "structural consistency", "descriptor lock", "style DNA replication" |
| **Model-Agnostic** | Descriptors work across Flux, SDXL, LTX, DALL-E when properly formatted | "model-agnostic descriptor", "universal style atom", "cross-model vocabulary" |

---

## 3. LIGHTING CONSTANTS

Lighting is the most important visual descriptor. Neural Aesthetic breaks light into **measurable, reproducible constants**.

### Temperature Constants (Kelvin)

| Temperature | Color | Emotional Register | Prompt Term |
|-------------|-------|-------------------|-------------|
| **1850K** | Candle flame | Intimacy, danger, ancient | "candlelight warmth", "flame flicker" |
| **2700K** | Warm incandescent | Home, safety, nostalgia | "warm incandescent", "living room glow" |
| **3200K** | Tungsten studio | Professional, theatrical, golden | "tungsten key", "golden hour studio" |
| **4000K** | Neutral white | Office, clinical, neutral | "neutral white", "daylight balanced" |
| **5600K** | Daylight | Natural, honest, baseline | "daylight balanced", "natural sun" |
| **6500K** | Overcast daylight | Cool, flat, melancholic | "overcast cool", "grey day light" |
| **7500K** | Shade / north light | Cold, distant, blue | "north light cool", "shaded blue" |
| **9500K** | Deep shade / twilight | Night, mystery, sci-fi | "twilight blue", "deep shade cold" |

### Direction Constants

| Direction | Shadow Pattern | Emotional Effect | Prompt Term |
|-----------|---------------|------------------|-------------|
| **Frontal** | Minimal shadow, flat | Neutral, documentary, revealing | "frontal flat light", "documentary evenness" |
| **45° Side** | Classic Rembrandt, dimensional | Natural, flattering, dimensional | "45-degree key", "Rembrandt lighting" |
| **90° Side** | Split face, dramatic | Mystery, duality, tension | "split lighting", "90-degree side key" |
| **Backlight / Rim** | Silhouette, edge glow | Separation, ethereal, isolation | "rim light", "backlight silhouette", "edge separation" |
| **Top / Overhead** | Eye socket shadow, harsh | Vulnerability, interrogation, noon | "overhead harsh", "top-down key", "noon shadow" |
| **Underlight** | Monster light, unnatural | Horror, unease, supernatural | "underlight", "monster lighting", "unnatural uplight" |
| **Practical** | Motivated by visible source | Realism, grounded, lived-in | "practical motivation", "visible light source", "grounded illumination" |

### Quality Constants

| Quality | Description | Prompt Term |
|---------|-------------|-------------|
| **Hard** | Sharp shadow edge, small source, direct | "hard light", "sharp shadow", "small source direct" |
| **Soft** | Gradual shadow falloff, large source, diffused | "soft light", "gradual shadow", "large source diffused" |
| **Bounced** | Indirect, ambient, no visible source | "bounced fill", "indirect ambient", "invisible source" |
| **Volumetric** | Light visible in air (dust, fog, haze) | "volumetric light", "visible beam", "atmospheric light" |
| **Caustic** | Light patterns through water/glass | "caustic pattern", "water refraction light", "glass pattern" |
| **Subsurface** | Light entering and exiting translucent material | "subsurface glow", "translucent light", "internal scatter" |

### Complete Lighting Constant Template
```
lighting_constant:
  temperature: 3200
  direction: "45-degree camera-left"
  quality: "soft diffused through window"
  fill_level: -2
  rim: "9500K camera-right edge"
  practical_sources: ["table lamp visible in frame"]
  shadow_hardness: 0.3
  contrast_ratio: "3:1"
```

---

## 4. MOOD DESCRIPTOR MATRIX

Mood is not "sad" or "happy" — it is a **calibrated combination of atmospheric constants**.

| Mood | Light Temp | Light Quality | Color Shift | Atmosphere | Depth of Field | Grain |
|------|-----------|-------------|-------------|-----------|---------------|-------|
| **Melancholic** | 6500K | Soft overcast | Blue shadow tint | Light haze | Shallow | Fine |
| **Joyful** | 5600K | Hard sun | Warm highlight | Clear air | Deep | None |
| **Tense** | 3200K + 9500K contrast | Hard key, no fill | Magenta/cyan split | Heavy fog | Shallow | Medium |
| **Nostalgic** | 2700K | Bounced golden | Sepia warmth | Dust particles | Medium | Heavy |
| **Isolated** | 9500K | Single rim only | Cool monochrome | Volumetric fog | Very shallow | Fine |
| **Mysterious** | 1850K + 7500K | Underlight + rim | Purple shadow | Heavy haze | Shallow | Medium |
| **Clinical** | 4000K | Even LED | Neutral grey | Sterile clear | Deep | None |
| **Romantic** | 2700K | Soft diffused | Pink highlight | Rose petal particles | Very shallow | Fine |
| **Dystopian** | Mixed neon | Hard practical | Acid green + magenta | Toxic fog | Medium | Heavy |

---

## 5. STYLE DNA ARCHITECTURE

Style DNA is the **complete genetic code** of a visual style — every descriptor that defines it.

### Style DNA Structure

```yaml
style_id: "cybernoir_quiet_luxury"
name: "CyberNoir Quiet Luxury"
parent_styles: ["cyberpunk_base", "quiet_luxury"]
lighting:
  temperature: 3200
  direction: "45-degree side"
  quality: "soft through frosted glass"
  rim: "9500K subtle edge"
color:
  primary: {"hue": 220, "sat": 0.2, "lum": 0.15}
  secondary: {"hue": 30, "sat": 0.3, "lum": 0.4}
  accent: {"hue": 180, "sat": 0.8, "lum": 0.5}
mood:
  valence: -0.3
  arousal: 0.2
  atmosphere: "toxic elegance"
materials:
  - "brushed titanium"
  - "frosted plexiglass"
  - "oxidized copper"
camera:
  lens: "anamorphic 50mm"
  aperture: "f/1.4"
  movement: "slow dolly"
  aspect_ratio: "2.39:1"
negatives:
  - "no neon saturation"
  - "no chaotic clutter"
  - "no warm fill"
```

### Style Combination Algebra

| Operation | Symbol | Description | Example |
|-----------|--------|-------------|---------|
| **Multiply** | `*` | Both styles applied fully; may conflict | `cyberpunk * wes_anderson` = symmetrical neon |
| **Overlay** | `+` | Primary style dominant, secondary subtle accent | `cyberpunk + ghibli` = cyberpunk with soft painterly background |
| **Blend** | `~` | 50/50 mix of both styles | `pixar ~ giallo` = appealing characters in lurid lighting |
| **Mask** | `@` | Primary style with secondary applied only to specific regions | `wes_anderson@character` = Anderson composition with default character |
| **Subtract** | `-` | Remove descriptors from primary style | `cyberpunk - neon` = cyberpunk without neon |

---

## 6. PROMPT INJECTION ARCHITECTURE

Neural Aesthetic descriptors must be **injected into every layer** of the prompt pipeline.

### Layer 1: Subject Injection
```
[Subject] with [style DNA material properties], [style DNA lighting on subject]
```

### Layer 2: Environment Injection
```
[Environment] with [style DNA color primary] dominant, [style DNA atmosphere]
```

### Layer 3: Camera Injection
```
[style DNA lens], [style DNA aperture], [style DNA movement], [style DNA aspect ratio]
```

### Layer 4: Lighting Injection
```
[style DNA lighting temperature] key from [direction], [style DNA lighting quality],
[style DNA rim], [style DNA contrast ratio]
```

### Layer 5: Negative Injection
```
[style DNA negatives]
```

### Complete Injection Template
```
SUBJECT: A [character] with [style DNA materials], illuminated by [style DNA lighting].
ENVIRONMENT: [setting] dominated by [style DNA color primary] with [style DNA atmosphere].
CAMERA: [style DNA lens] at [style DNA aperture], [style DNA movement], [style DNA aspect ratio].
LIGHTING: [style DNA lighting full description].
MOOD: [style DNA mood valence/arousal description].
NEGATIVE: [style DNA negatives].
```

---

## 7. PROJECT GRAPH INTEGRATION

| Neural Aesthetic Element | project graph node |
|-------------------------|------------------|
| Style DNA definition | `Style` node with full YAML properties |
| Lighting constant | `Constant` node with `category: lighting` |
| Mood descriptor | `Style` → `HAS_MOOD` → `Mood` node |
| Color bible | `Scene` → `HAS_COLOR_BIBLE` → `ColorBible` node |
| Style combination | `Style` → `COMBINES_WITH` → `Style` edge with `operation` (multiply, overlay, blend) |
| Negative descriptors | `Style` → `HAS_NEGATIVE` → `Negative` node |

**MCP Tool Integration:**
- `graph_query` "styles with mood valence < -0.2" returns all melancholic styles
- `graph_context` on Style node returns full DNA, parent styles, and combination rules
- `graph_impact` on Style change shows all shots/workflows using that style

---

## 8. SKILL STACKING

```
BASE SKILL: Prompt Engineering Core
META SKILL: Neural Aesthetic (this file)
    └── VOCABULARY: lighting constants, mood matrices, style DNA, combination algebra
STYLE SKILL: [Any Style Specialist]
    └── VOCABULARY: domain-specific aesthetic (Pixar, Wes Anderson, etc.)
STRUCTURE SKILL: Cinematic Continuity
    └── GRAMMAR: shot lists, temporal coherence
TECH SKILL: ComfyUI/Flux Pipeline
    └── PARAMETERS: sampler, model, CFG
```

**Neural Aesthetic + Pixar Stack:**
> "Apply Pixar character design WITH Neural Aesthetic lighting constant 3200K soft key + 9500K rim, mood valence +0.6 (joyful), material subsurface scattering"

---

## 9. QUICK REFERENCE: LIGHTING CONSTANT MATRIX

| Scene Type | Temp | Direction | Quality | Fill | Rim | Contrast |
|------------|------|-----------|---------|------|-----|----------|
| Golden Hour Portrait | 3200K | 45° side | Soft | -2 stops | 9500K edge | 3:1 |
| Noir Alley | 2700K | Top overhead | Hard | None | 9500K back | 8:1 |
| Sci-Fi Medbay | 4000K | Even overhead | LED panel | -1 stop | None | 2:1 |
| Romantic Dinner | 2700K | Practical | Candle + soft | -3 stops | None | 4:1 |
| Dystopian Street | Mixed | Practical neon | Hard | None | Mixed | 10:1 |
| Documentary | 5600K | Frontal | Bounced | -1 stop | None | 2:1 |

---

## 10. SOURCES

- AI Image Prompt Engineering Guide [^58^]
- AI Image Prompt Engineering Guide (Advanced) [^59^]

---

## 11. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering lighting constants (temperature, direction, quality), mood descriptor matrices, style DNA architecture, combination algebra, and prompt injection templates.
