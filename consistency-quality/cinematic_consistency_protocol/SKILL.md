---
name: cinematic_consistency_protocol
description: "Run five-axis continuity checks before re-rendering."
version: 1.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [consistency-quality, media, cinematic]
    category: consistency-quality
---

# The Cinematic Consistency Protocol (CCP v1.0)
## A Technical Manifesto for Cross-Model Visual Continuity in Multi-Modal Diffusion Pipelines

---

### Preamble: The Problem of Cross-Model Visual Drift

In high-end cinematic production, visual continuity is non-negotiable. When anchoring a sequence with **FLUX 2** (still generation) and extending into motion via **LTX 2.3** or **Wan 2.1** (video generation), we face a fundamental architectural mismatch: image diffusion models optimize for spatial fidelity, while video diffusion models optimize for temporal coherence. Without a standardized translation layer, "visual soul"—the specific quality of light, lens, and grain—dissolves between modalities.

This protocol defines the **Anchor → Translate → Verify** pipeline for maintaining cinematic identity across model boundaries.

---

## 1. The Anchor Protocol: Extracting & Encoding Visual Essence

### 1.1 FLUX 2 Anchor Generation (The "Still Bible")

FLUX 2 demonstrates superior adherence to structured, technical prompting and supports JSON-structured inputs that function like micro-APIs for cinematography . The anchor image must be generated with **extractable parameters**.

**Mandatory FLUX 2 Prompt Architecture:**
```
{
  "scene": "[Environment description]",
  "subject": "[Primary focus, pose, action]",
  "style": "[Photographic approach]",
  "colors": {
    "palette": ["#HEX1", "#HEX2", "#HEX3"],
    "dominant_hue": "[descriptive]",
    "color_temperature": "[Kelvin value]K"
  },
  "lighting": {
    "key_light": "[Source, direction, quality]",
    "fill_ratio": "[Key:Fill ratio, e.g., 4:1]",
    "color_temp_k": "[Number]K",
    "practical_sources": "[Visible lights in scene]"
  },
  "camera": {
    "lens": "[e.g., 85mm, 35mm, 24mm anamorphic]",
    "aperture": "[f-stop]",
    "iso": "[Number]",
    "shot_type": "[e.g., medium close-up, wide establishing]",
    "angle": "[eye-level, low-angle, Dutch]",
    "focus": "[e.g., shallow depth of field, deep focus]",
    "film_stock": "[e.g., Kodak Vision3 500T, Fujifilm Eterna]"
  },
  "atmosphere": {
    "haze": "[None/volumetric/light fog]",
    "grain": "[Fine/medium/heavy, push-processed]",
    "lens_effects": "[flare, chromatic aberration, vignette]"
  },
  "mood": "[Emotional tone]"
}
```

**Key Constraint:** FLUX 2 does not support negative prompts . Describe exactly what you want present; never describe what you want excluded.

### 1.2 The Visual Essence Extraction Matrix (VEEM)

From every FLUX 2 anchor, extract these **12 immutable parameters** before translation:

| Parameter | Extraction Method | Video Model Translation |
|-----------|------------------|------------------------|
| **Color Temperature (K)** | Parse from `lighting.color_temp_k` or infer from palette | Inject as explicit Kelvin value in prompt header |
| **Key:Fill Ratio** | Parse from `lighting.fill_ratio` | Describe as "harsh contrast" (>4:1), "soft wrap" (2:1), or "flat" (1:1) |
| **Lens Focal Length** | Parse from `camera.lens` | Critical for LTX 2.3; Wan 2.1 respects focal length in I2V but requires explicit restatement |
| **Aperture/DoF** | Parse from `camera.aperture` + `camera.focus` | Translate to "shallow focus," "deep focus," or "bokeh at [distance]" |
| **Film Stock Emulation** | Parse from `camera.film_stock` | Convert to grain structure + color cast descriptors |
| **ISO/Grain Profile** | Parse from `camera.iso` + `atmosphere.grain` | Map to "clean digital," "fine 35mm grain," or "pushed 16mm grain" |
| **Light Quality** | Parse from `lighting.key_light` | Use precise modifiers: "hard specular," "diffused softbox," "book light through muslin" |
| **Light Direction** | Parse from `lighting.key_light` | Use clock-face system: "10:30 key, 4:30 rim, 7:00 bounce fill" |
| **Color Palette (HEX)** | Extract from `colors.palette` | Restate as dominant color relationships; Wan 2.1 does not parse HEX but respects color names |
| **Atmospheric Density** | Parse from `atmosphere.haze` | Translate to "volumetric haze," "clean dry air," or "ground fog" |
| **Lens Character** | Parse from `camera.lens` + `atmosphere.lens_effects` | Specify anamorphic squeeze, spherical aberration, or vintage lens artifacts |
| **Composition** | Parse from `camera.shot_type` + `camera.angle` | Lock with "static [shot type]" or specify camera movement for video |

### 1.3 Cross-Model Prompt Translation Rules

#### FLUX 2 → LTX 2.3 Translation
LTX 2.3 supports **Image-to-Video (I2V)** with vastly improved consistency over prior versions, including "Extend" and "Retake" functions for multi-shot workflows . 

**Translation Formula:**
```
[LTX 2.3 I2V Prompt] = 
  "Cinematic motion continuation of reference frame. " +
  "[Subject action/motion description]. " +
  "Camera: [movement or static lock]. " +
  "Lighting: [Restate key light quality and direction]. " +
  "Color temperature: [X]K. " +
  "Atmosphere: [haze/grain]. " +
  "Maintain exact focal length of [Y]mm, [aperture] aperture look. " +
  "No style drift. Strict visual continuity."
```

**LTX 2.3 Specific Constraints:**
- Resolution must be divisible by 32; frame count divisible by 8 + 1 
- Use I2V as foundation, then "Extend" with optional prompt guidance to evolve the scene while locking the last frame as the next anchor 
- For motion, LTX 2.3 handles camera movement instructions better than earlier versions, but avoid complex physics (water, crowds) in edge cases 

#### FLUX 2 → Wan 2.1 Translation
Wan 2.1 utilizes a **spatio-temporal VAE** for temporal coherence and performs best when the visual identity is locked via image-to-video rather than text-to-video .

**Translation Formula:**
```
[Wan 2.1 I2V Prompt] = 
  "[Subject] [continuous action]. " +
  "[Camera movement or static composition]. " +
  "Lighting remains [quality]: [direction] at [X]K. " +
  "[Film stock] grain, [aperture] depth of field, [lens] lens characteristics. " +
  "[Atmosphere]. " +
  "Seamless temporal continuity."
```

**Wan 2.1 Specific Constraints:**
- **Guidance Scale:** Maintain 5–7. Higher values cause flicker and over-correction per frame; lower values allow drift 
- **One Scene = One Prompt:** Never change environment or lighting mid-prompt. Wan 2.1 confuses sudden prompt switches with scene jumps 
- **Camera Movement:** Use structured syntax: `[Opening shot] + [Camera movement] + [Details revealed]` 
- **Resolution:** Generate at 480p/720p (training sweet spot) and upscale externally for final delivery 

---

## 2. Descriptor Standardization: The Cinematic Lexicon

To ensure universal parseability across FLUX 2, LTX 2.3, and Wan 2.1, replace ambiguous aesthetic terms with the following **standardized technical vocabulary**.

### 2.1 Lighting Taxonomy (Kelvin & Quality)

| Common Term | Banned | CCP Standard Replacement | Technical Meaning |
|-------------|--------|-------------------------|-------------------|
| "Warm light" | ✅ | "Tungsten key, 3200K, hard specular" | Incandescent household/studio lamp temperature  |
| "Golden hour" | ✅ | "Magic hour, 3000K, horizontal raking light" | Post-sunrise/pre-sunset sun position  |
| "Cool light" | ✅ | "Daylight balance, 5600K, clean top light" | Natural noon sun color temp  |
| "Cinematic lighting" | ✅ | "Rembrandt key, 4:1 contrast, 3200K, negative fill camera-right" | Specific pattern: key at 45° high, shadow triangle on opposite cheek |
| "Moody" | ✅ | "Low-key, 8:1 contrast, practical sources only, 2400K" | High contrast, minimal fill, warm tungsten practicals |
| "Soft light" | ✅ | "Diffused through 8x8 Ultrabounce, 2:1 wrap, 4200K" | Large source relative to subject, fluorescent or LED through diffusion |
| "Neon look" | ✅ | "Practical magenta (#FF00FF) and cyan (#00FFFF) tubes, 4200K ambient" | Specific color channels from practical sources |

**Kelvin Reference Scale for Prompting:**
- **1700K:** Match flame 
- **1900K:** Candlelight 
- **2400K–3000K:** Warm tungsten, golden hour 
- **3200K:** Standard tungsten / photoflood 
- **4200K:** White fluorescent 
- **5600K:** Daylight 
- **6500K:** Overcast / open shade 
- **9000K–10000K:** Heavy overcast / skylight 

### 2.2 Lens & Optical Taxonomy

| Common Term | Banned | CCP Standard Replacement |
|-------------|--------|-------------------------|
| "Blurry background" | ✅ | "85mm lens, f/1.4, subject at 1.5m, background at 10m, circular bokeh" |
| "Wide shot" | ✅ | "18mm lens, deep focus, f/8, hyperfocal distance" |
| "Zoomed in" | ✅ | "135mm telephoto compression, f/2.8, shallow DoF" |
| "Vintage look" | ✅ | "Cooke Speed Panchro 50mm, spherical aberration, warm flare, 1970s negative" |
| "Anamorphic" | ✅ | "40mm anamorphic 2x squeeze, horizontal flare, oval bokeh, 2.39:1 extraction" |

### 2.3 Film Stock & Grain Taxonomy

| Grain Descriptor | Visual Characteristic | Use Case |
|-----------------|----------------------|----------|
| "Kodak Vision3 500T" | Fine grain, cool shadows, warm highlights, wide latitude | Night interiors, moody drama |
| "Kodak Vision3 250D" | Tight grain, neutral daylight balance, high saturation | Day exteriors, commercial work |
| "Fujifilm Eterna 500" | Creamy highlights, pastel shadows, organic grain | Romantic/nostalgic tones |
| "Ilford Delta 3200" | Aggressive grain, high contrast, pushed B&W | Documentary, gritty realism |
| "16mm reversal" | Heavy grain, saturated, limited latitude | Retro/vintage aesthetic |
| "Clean digital" | No grain, perfect color separation, clinical | Sci-fi, product, futuristic |

---

## 3. The Consistency Check: Semantic Verification Parameters

After video generation, run the following **five-axis verification** against the original FLUX 2 anchor. This is the "drift detection" layer.

### 3.1 The Five Axes of Continuity

| Axis | Verification Method | Acceptable Drift Threshold |
|------|--------------------|---------------------------|
| **Luminosity Continuity** | Compare histogram mean/luminance of anchor vs. sampled video frames | ±8% luminance variance |
| **Chromatic Continuity** | Compare dominant HEX palette of anchor vs. video frames using color clustering | 3 of 5 dominant colors must match within ΔE < 10 |
| **Atmospheric Continuity** | Visual inspection for haze density, volumetric quality, and particulate consistency | No change in atmospheric density class (e.g., "light fog" cannot become "clear") |
| **Optical Continuity** | Verify DoF, bokeh character, and lens distortion match | Focal length must read as equivalent; bokeh shape must not change |
| **Temporal Coherence** | Evaluate frame-to-frame consistency using cross-frame attention metrics | No object identity morphing; no texture flicker > 2% of frame area |

### 3.2 Technical Implementation of Consistency Checks

Based on temporal consistency research in video diffusion , enforce these architectural safeguards in your pipeline:

**Frame Conditioning (Primary Defense)**
Condition each generated video frame on the FLUX 2 anchor image and the immediately preceding frame. This creates a chain of visual dependencies that reduces object drift and texture mutations .

**Latent Noise Reuse (Secondary Defense)**
In diffusion-based video pipelines, reuse latent noise or conditioning vectors across frames. This reduces flicker and maintains cohesive style and structure when extending from the anchor still .

**Cross-Frame Attention (Tertiary Defense)**
Enable the video model to reference multiple previous frames simultaneously during generation. This "looks back" at earlier frames to determine how the current frame should render, preserving texture and identity as objects move .

**Optical Flow Guidance (Motion Defense)**
Use optical flow estimates between anchor and generated frames as soft guidance rather than hard constraints. When flow estimation is imperfect, spatial conditions (depth maps, edge maps) provide corrective positional information .

### 3.3 The "Retake" Trigger Conditions

If any of the following occur during generation, halt the pipeline and regenerate with tightened parameters:

1. **Color Temperature Drift:** Video frames shift >500K from anchor Kelvin value
2. **Focal Length Drift:** Perspective compression changes (e.g., 85mm look shifts to 24mm look)
3. **Lighting Logic Break:** Shadows fall in contradictory directions relative to anchor key light
4. **Grain Structure Mutation:** Film stock emulation changes mid-sequence (e.g., from fine 35mm to video noise)
5. **Subject Morphing:** Character or object identity shifts beyond acceptable threshold (use face consistency or structural similarity metrics) 

---

## 4. Production Workflow: Anchor-to-Video Pipeline Example

### Step 1: Anchor Lock (FLUX 2)
Generate hero still using JSON-structured prompt with full VEEM parameters. Export HEX palette, Kelvin value, and lens specification to a `.yaml` sidecar file.

### Step 2: Essence Translation
Run the VEEM parser to auto-generate LTX 2.3 and Wan 2.1 compliant prompt strings. The parser enforces:
- Kelvin restatement in first sentence
- Lens focal length lock
- Film stock grain restatement
- Static or specified camera movement only

### Step 3: Video Generation (LTX 2.3 or Wan 2.1)
- **For LTX 2.3:** Use I2V with the FLUX anchor as first frame. Generate primary motion clip. Use "Extend" with the last frame as the new anchor for sequence continuation .
- **For Wan 2.1:** Use I2V mode with anchor frame. Keep guidance at 6.0. Generate in 720p maximum, then upscale .

### Step 4: Consistency Verification
Run the Five Axes check. If drift exceeds thresholds, adjust:
- **LTX 2.3:** Use "Retake" on failed segment with stronger prompt adherence 
- **Wan 2.1:** Lower guidance scale by 0.5 to reduce flicker, or regenerate with more explicit lighting descriptors 

### Step 5: Post-Integration
Apply film grain, color grading, and lens effects in post using the original FLUX 2 anchor as the reference still in the color suite. This final "grain lock" step ensures that even if subtle drift occurred, the sequence is optically married to the anchor.

---

## 5. Model-Specific Quick Reference

| Feature | FLUX 2 (Anchor) | LTX 2.3 (Video) | Wan 2.1 (Video) |
|---------|----------------|-----------------|-----------------|
| **Best Input** | Text (JSON structured) | Image-to-Video | Image-to-Video |
| **Prompt Length** | 80+ words ideal  | Medium length, motion-focused | Short-medium, single scene  |
| **Color Control** | HEX codes supported  | Inherited from image + text | Color names only, no HEX |
| **Negative Prompts** | Not supported  | Supported | Supported |
| **Guidance Scale** | 4.5 (Flex) / fixed (Pro) | Model-dependent | 5–7 optimal  |
| **Max Generation** | 4MP still | 4K video, 50 FPS  | 480p/720p native  |
| **Consistency Tools** | Multi-reference (up to 8-10 imgs)  | Extend, Retake, Keyframe  | Spatio-temporal VAE  |
| **Camera Motion** | N/A (still) | Respects camera instructions  | Requires specific syntax  |

---

## Appendix A: The Forbidden Terms List

The following terms are **banned** from CCP-compliant prompts due to model-specific interpretation variance:

- "Cinematic" (use specific lighting pattern)
- "Beautiful" (use technical color/texture descriptors)
- "Professional" (use camera/lens specification)
- "High quality" (use resolution, codec, or film stock)
- "Moody" (use contrast ratio and color temperature)
- "Natural light" (use time of day + Kelvin value + window direction)
- "Soft focus" (use specific lens + diffusion filter)

---

**Protocol Version:** CCP v1.0  
**Effective Date:** 2026-04-20  
**Models Covered:** FLUX 2 (Pro/Max/Flex), LTX 2.3, Wan 2.1  
**Next Review:** Upon release of FLUX 3, LTX 3.0, or Wan 3.0

*This document is a living standard. As diffusion architectures evolve, the translation matrices and forbidden terms list will require updating to maintain optical truth across model boundaries.*