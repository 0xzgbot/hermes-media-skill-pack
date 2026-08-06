# SKILL: Pixar Specialist
## Domain: Animation, Character Design, Lighting, Rendering, Storytelling
## Version: 1.0
## For: Hermes Agent — Prompt Engineering & Scene Planning

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete technical and artistic vocabulary of Pixar Animation Studios. It covers the 12 principles of animation, character design shape language, RenderMan lighting/rendering techniques, the Pixar Story Spine, color scripting, and the specific visual signatures of Pixar shorts vs. features.

When this skill is active, the agent should:
- Use Pixar-specific terminology in prompts (subsurface scattering, color script, shape language)
- Apply the 12 animation principles as motion descriptors
- Reference Pixar lighting models (DomeLight, DiscLight, point-based GI)
- Build scenes using the Pixar Story Spine structure
- Understand character archetypes through shape language (circle=friendly, square=strong, triangle=dangerous)

---

## 2. THE 12 PRINCIPLES OF ANIMATION (Pixar/Disney Foundation)

These principles, codified by Disney animators Frank Thomas and Ollie Johnston in *The Illusion of Life* (1981), form the bedrock of all Pixar animation. [^6^] [^7^] When writing motion prompts, reference these principles explicitly.

| Principle | What It Means | Prompt Vocabulary |
|-----------|---------------|-----------------|
| **Squash & Stretch** | Gives illusion of weight/volume. Volume must be conserved. [^10^] | "squash and stretch physics", "weight-driven deformation", "elastic motion with volume preservation" |
| **Anticipation** | Small preparatory action before major action. [^10^] | "anticipation pose", "wind-up motion", "pre-action telegraph" |
| **Staging** | Clear presentation of idea. Composition, lighting, camera angle direct attention. [^10^] | "strong staging", "focal point isolation", "theatrical composition" |
| **Straight Ahead vs. Pose-to-Pose** | Sequential drawing vs. keyframe-first. [^7^] | "pose-to-pose blocking", "straight-ahead fluid motion", "keyframe holds" |
| **Follow Through & Overlapping** | Parts of body move independently. Hair/clothes continue after body stops. [^7^] | "follow-through motion", "overlapping action", "secondary motion lag" |
| **Slow In / Slow Out** | Acceleration/deceleration curves. Nothing starts/stops instantly. [^7^] | "ease-in ease-out", "slow-in slow-out curves", "weighted acceleration" |
| **Arcs** | Natural motion follows curved paths, not straight lines. [^6^] | "arc-based motion", "circular trajectory", "organic path curves" |
| **Secondary Action** | Additional motion reinforcing main action. [^7^] | "secondary motion", "ambient life", "breathing life into background" |
| **Timing** | Frame spacing controls speed perception. More frames = slower. [^7^] | "snappy timing", "broad timing", "on-ones vs on-twos" |
| **Exaggeration** | Push reality for appeal/energy without breaking believability. [^7^] | "exaggerated posing", "pushed expressions", "stylized physics" |
| **Solid Drawing** | 3D form, weight, balance. Volume awareness in space. [^7^] | "solid posing", "grounded weight", "dimensional form" |
| **Appeal** | Interesting, compelling, charismatic. Not necessarily beautiful. [^17^] | "appealing design", "charismatic silhouette", "engaging presence" |

### Short vs. Feature Application
- **Shorts:** Broader squash/stretch, more exaggerated timing, snappier poses. [^14^]
- **Features:** Subtler principles, grounded physics, emotional realism over cartooniness.

---

## 3. CHARACTER DESIGN: SHAPE LANGUAGE

Pixar characters are designed using geometric psychology before any detail is added. [^18^] [^19^] [^31^] The silhouette alone communicates personality.

### The Three Primary Shapes

| Shape | Psychology | Pixar Examples | Prompt Use |
|-------|-----------|----------------|------------|
| **Circle** | Soft, friendly, approachable, harmless, cute, changeable | Dug (Up), Bing Bong (Inside Out), Baymax-style | "circular silhouette", "round friendly forms", "soft approachable geometry" |
| **Square** | Strong, reliable, sturdy, grounded, stubborn, inflexible | Carl (Up), Mr. Incredible, WALL-E | "square build", "blocky sturdy form", "grounded rectangular silhouette" |
| **Triangle** | Sharp, dangerous, dynamic, cunning, aggressive, intelligent | Muntz (Up), Alpha (Up), Randall (Monsters Inc) | "angular silhouette", "triangular sharp edges", "pointed aggressive geometry" |

### Shape Mixing Rules
- **Heroes:** Circle-dominant with square secondary (friendly + capable)
- **Villains:** Triangle-dominant with sharp accents
- **Mentors:** Square-dominant with rounded edges (reliable + warm)
- **Comic Relief:** Pure circle or exaggerated proportions

### Pixar-Specific Character Traits
- **Eyes:** Large, expressive, asymmetrical for life. Pupil size conveys emotion.
- **Silhouette:** Must be readable in black. Test: can you identify the character from silhouette alone?
- **Proportions:** Baby schema (big head, big eyes) for cute. Elongated limbs for elegant.
- **Texture:** Subsurface scattering on skin. Fuzz on surfaces. Micro-detail in pores.

---

## 4. LIGHTING & CINEMATOGRAPHY

Pixar lighting is not illumination—it is storytelling. Light shows you where to look and enhances emotional feel. [^3^] [^28^]

### The Color Script
A **color script** is a visual roadmap: painted frames representing key moments that define how light, color, and mood shift across the film. [^28^] It ensures emotional consistency before animation begins.

**Prompt Translation:**
- "color script progression from warm amber to cold blue"
- "emotional color arc: joy → tension → resolution"
- "lighting key painted in gouache style"

### Pixar Light Types (RenderMan/Technical)

| Light Type | Description | Visual Effect | Prompt Vocabulary |
|------------|-------------|---------------|-------------------|
| **DomeLight** | Hemisphere environment light, HDRI-based | Soft ambient fill, natural sky | "dome light ambient fill", "HDRI sky dome", "soft environmental bounce" |
| **DiscLight** | Circular area light | Soft directional with falloff | "disc light key", "soft circular source", "gentle area illumination" |
| **DistantLight** | Infinite directional (sun) | Hard shadows, parallel rays | "distant sun light", "parallel shadow rays", "hard directional key" |
| **RectLight** | Rectangular area light | Studio softbox look | "rectangular softbox", "studio key light", "controlled rectangular falloff" |
| **SpotLight** | Cone-based spot | Focused pool of light | "spotlight isolation", "theatrical cone light", "focused dramatic pool" |

### Lighting Temperature & Mood
- **Warm (2700K–4000K):** Safety, home, nostalgia, joy. Golden hour.
- **Neutral (5500K):** Clinical, neutral, daylight baseline.
- **Cool (7000K–9500K):** Danger, isolation, sci-fi, sadness. Moonlight.
- **Complementary contrast:** Warm key + cool fill = cinematic depth. [^30^]

**Prompt Example:**
> "warm 3200K key light from window left, cool 9500K rim light from behind, volumetric dust particles in beam, shallow depth of field, cinematic Pixar lighting key"

### Volumetric & Atmospheric Effects
- **Volumetric fog/haze:** Defines light beams, adds depth layers.
- **Dust/pollen in air:** Catches light, adds texture to negative space.
- **Subsurface glow:** Skin, wax, leaves, coral—light enters, scatters, exits. [^24^]
- **Caustics:** Light patterns through water/glass onto surfaces.

---

## 5. RENDERING & MATERIALS (RenderMan Technical)

Pixar's RenderMan is an Academy Award-winning renderer built on physically-based shading. [^4^] [^16^] Understanding these technical terms elevates prompt precision.

### Core RenderMan Concepts

| Technique | What It Does | Prompt Translation |
|-----------|-------------|-------------------|
| **Subsurface Scattering (SSS)** | Light enters material, scatters internally, exits. Skin, wax, milk, fruit. [^5^] [^24^] [^27^] | "subsurface scattering skin", "translucent wax material", "internal light bounce" |
| **Global Illumination (GI)** | Indirect light bounce. Color bleeding between surfaces. [^21^] | "global illumination bounce", "color bleeding", "indirect light fill" |
| **Path Tracing** | Simulates actual light ray paths. Physically accurate. [^5^] | "path traced lighting", "physically accurate light transport", "ray-traced shadows" |
| **Point-Based Color Bleeding** | Fast GI approximation using surfel clouds. [^21^] | "soft color bleeding", "ambient occlusion contact shadows" |
| **Multi-Bounce GI** | Light bounces 2–4+ times. Rich, realistic interiors. [^23^] | "multi-bounce indirect light", "rich interior bounce", "complex light transport" |
| **Denoising** | ML-based noise reduction (trained on Pixar datasets). [^4^] | "clean render", "production denoised", "smooth final gather" |

### Material Types

| Material | Properties | Pixar Use | Prompt Terms |
|----------|-----------|-----------|--------------|
| **Pixar Surface** | Layered material: diffuse + specular + subsurface + fuzz | Default character skin | "Pixar Surface shader", "layered skin material", "fuzz-enhanced surface" |
| **Subsurface Skin** | DMFP (diffuse mean free path) controls scatter depth | Human characters | "skin subsurface", "DMFP-scattered light", "translucent epidermis" |
| **Glass/Transmission** | Refraction + reflection + caustics | Gems, water, bottles | "transmission glass", "refractive caustics", "physically accurate refraction" |
| **Hair/Fur** | Anisotropic specular, multiple scattering | Merida, Sulley | "anisotropic hair", "fur multiple scatter", "Marschner hair model" |
| **Cloth/Fabric** | Sheen, velvet, weave pattern | Costumes, upholstery | "fabric sheen", "velvet BRDF", "woven cloth texture" |

### The "Piper" Aesthetic (Short Film Benchmark)
*Piper* (2016) represents Pixar's photorealistic short film peak: [^22^] [^29^]
- **Macro photography style:** Shallow depth of field, long lenses
- **Doc-style cinematography:** Naturalistic, observational
- **7 million feathers** on the bird, regionally controlled
- **Water as personality:** Shaped waves with exact timing, not pure physics
- **Sand as geometry:** Micro-detail via geometric sculpting
- **Norman Rockwell color touchstone:** Warm, textured, nostalgic palette

**Prompt Translation for Piper Style:**
> "macro photography shallow depth of field, Norman Rockwell color palette, naturalistic doc-style cinematography, water shaped as character personality, geometric micro-detail sand, warm nostalgic texture, feather-level detail"

---

## 6. THE PIXAR STORY SPINE

Pixar stories follow a causal, emotionally-driven structure. [^8^] Every beat must answer *"Because of that..."*

### The 7 Sentence Starters

1. **Once upon a time...** — Establish protagonist and world (normal)
2. **Every day...** — Routine / status quo
3. **But one day...** — Inciting incident disrupts normal
4. **Because of that...** — Rising action + consequences (causality!)
5. **Because of that...** — Escalation (repeat as needed)
6. **Until finally...** — Climax / turning point
7. **And ever since then...** — New normal / emotional resolution

### Emotional Beats (The Internal Spine)
The best Pixar films track parallel emotional arcs:
- **Toy Story:** Woody learns to share leadership (jealousy → acceptance)
- **Inside Out:** Joy learns sadness has value (denial → integration)
- **Up:** Carl learns to let go and live (grief → connection)
- **Soul:** Joe learns purpose is living, not achieving (obsession → presence)

### Prompt Application for Scene Narrative
When generating a sequence, structure the prompt as:
> "Scene 1: Once upon a time [establishing shot, warm golden light, safe world]. Scene 2: But one day [disruption, cool lighting intrusion, tension]. Scene 3: Because of that [consequence, saturated emotional color, rising action]."

---

## 7. SHORT FILMS VS. FEATURES: TECHNICAL DIFFERENCES

| Aspect | Short Films | Feature Films |
|--------|-------------|---------------|
| **Animation Timing** | Snappier, broader, on-2s or on-4s possible [^9^] | Smoother, on-1s, grounded physics |
| **Style Experimentation** | High. Mixed media, 2D/3D hybrid, stylized looks. [^22^] | Consistent within film universe |
| **Asset Reuse** | Heavy reuse from features, retextured/remodeled [^9^] | Original assets built from scratch |
| **Lighting Approach** | Often painted keys by director, real-time lookdev [^9^] | Full lighting department, multiple passes |
| **Rendering** | Lower complexity, faster iteration | Maximum quality, 10–24 hrs per frame |
| **Character Count** | Small cast, often 1–3 characters | Large ensemble |
| **Scope** | Single idea, one emotional beat | Multi-threaded, complex arcs |
| **Tech Incubation** | Shorts as R&D (Piper = water/sand tech) [^29^] | Proven tech deployed at scale |

### Notable Short Film Styles to Reference

| Short | Style Signature | Prompt Vocabulary |
|-------|-----------------|-------------------|
| *Piper* | Photorealistic macro, shallow DOF | "Piper macro aesthetic", "shallow DOF nature", "photorealistic bird" |
| *Purl* | 2D/3D hybrid, office satire, on-2s animation | "Purl hybrid 2D-3D", "snappy on-twos", "office satire styling" |
| *Bao* | Soft rounded forms, food texture, maternal warmth | "Bao soft rounded world", "food surface detail", "warm maternal glow" |
| *Sanjay's Super Team* | 2D Hindu mythology + 3D reality blend | "mythological 2D-3D blend", "stylized deity forms", "cultural pattern overlay" |
| *Kitbull* | 2D painterly, hand-drawn texture | "Kitbull painterly 2D", "hand-drawn texture overlay", "expressive line work" |
| *Wind* | Stylized, emotional, memory-like haze | "Wind stylized memory", "soft haze emotional", "ethereal light diffusion" |
| *Burrow* | Watercolor texture, storybook illustration | "Burrow watercolor", "storybook illustration texture", "whimsical hand-painted" |

---

## 8. PROMPT ENGINEERING: THE PIXAR VOCABULARY

When generating Pixar-style content, use this layered vocabulary structure:

### Layer 1: Animation Physics
```
squash and stretch with volume conservation, anticipation pose, 
arc-based motion path, follow-through hair motion, 
slow-in slow-out ease curves, solid grounded posing
```

### Layer 2: Character Design
```
circular friendly silhouette, large expressive asymmetrical eyes, 
appealing baby-schema proportions, subsurface scattering skin, 
Pixar Surface material, fuzz-enhanced surface texture
```

### Layer 3: Lighting & Atmosphere
```
warm 3200K key light from window, cool 9500K rim light, 
DomeLight environmental fill, volumetric dust particles, 
soft color bleeding between surfaces, shallow depth of field
```

### Layer 4: Rendering Quality
```
path traced global illumination, multi-bounce indirect light, 
physically based shading, production denoised, 
high-quality subsurface scattering, cinematic color script
```

### Layer 5: Story/Emotion
```
Pixar Story Spine structure, emotional color arc, 
character-driven composition, staging for clarity, 
appeal over pure realism
```

### Complete Prompt Template
```
A [character description using shape language], 
[animation physics descriptors], 
[lighting setup with temperatures and light types], 
[rendering quality descriptors], 
[emotional/story context].

Example:
"A circular-friendly young protagonist with large expressive asymmetrical eyes 
and soft rounded silhouette, squash-and-stretch physics with volume conservation, 
arc-based jump motion with follow-through hair, warm 3200K window key light 
with cool 9500K rim, DomeLight environmental fill, volumetric dust particles, 
path-traced global illumination with multi-bounce color bleeding, 
subsurface scattering skin, Pixar Surface material, production quality render, 
Pixar Story Spine 'once upon a time' establishing moment, 
joyful emotional color script, shallow depth of field, cinematic staging"
```

---

## 9. NEGATIVE PROMPTS (What to Avoid)

| Avoid | Why | Replace With |
|-------|-----|--------------|
| "hyperrealistic" | Pixar is stylized, not photoreal (except specific shorts like Piper) | "stylized 3D", "appealing cartoon realism", "Pixar Surface aesthetic" |
| "dark gritty" | Pixar is optimistic, even in sadness | "warm melancholy", "hopeful sadness", "emotional warmth" |
| "anime style" | Different shape language, eye proportions | "Western 3D animation", "Pixar proportions", "CGI feature film" |
| "flat lighting" | Pixar uses complex motivated lighting | "motivated key light", "environmental bounce", "volumetric atmosphere" |
| "perfect symmetry" | Pixar characters are asymmetrical for life | "appealing asymmetry", "organic imperfection", "hand-crafted feel" |
| "motion blur" | Pixar uses smear frames, not blur | "smear frame motion", "pose-to-pose clarity", "stylized motion" |

---

## 10. SKILL STACKING: HOW THIS COMPOSES WITH OTHER SKILLS

### Yes, Skills Can Be Stacked

Skills are **compositional**, not mutually exclusive. When the Hermes agent loads multiple skills, it should merge their vocabularies hierarchically.

### Stacking Architecture

```
BASE SKILL: Prompt Engineering Core
    └── GRAMMAR: syntax, structure, negative prompts, weighting

STYLE SKILL: Pixar Specialist (this file)
    └── VOCABULARY: animation principles, shape language, lighting, rendering

TECHNICAL SKILL: ComfyUI/Flux Pipeline
    └── PARAMETERS: sampler, steps, CFG, model selection, conditioning

OUTPUT: Pixar-style prompts optimized for the production pipeline
```

### Example Stack Execution

**User Request:** *"Generate a Pixar-style scene of a cute robot in a sunny workshop"*

**Skill 1 (Pixar Specialist) provides:**
- Shape language: "square build with rounded edges" (friendly + sturdy)
- Animation: "solid grounded posing, slight anticipation in head tilt"
- Lighting: "warm 4000K window key, DomeLight fill, dust particles"
- Rendering: "subsurface scattering on painted metal, Pixar Surface material"

**Skill 2 (Prompt Engineering Core) provides:**
- Structure: subject + environment + lighting + quality + style
- Syntax: comma-separated descriptors, weighting with parentheses
- Negatives: "avoid flat lighting, avoid perfect symmetry"

**Skill 3 (ComfyUI Pipeline) provides:**
- Model: "flux2dev_fp8 for character detail"
- Sampler: "dpmpp_2m for smooth gradients"
- CFG: "3.5 for natural color bleeding"
- Conditioning: "CLIPTextEncode with Pixar vocabulary injection"

**Composed Output Prompt:**
```
A cute square-built robot with rounded edge accents and large expressive 
asymmetrical eyes, friendly circular silhouette mixed with square sturdy form, 
solid grounded posing with slight head-tilt anticipation, warm 4000K sunlight 
streaming through workshop window, DomeLight environmental fill, volumetric 
dust particles in light beams, painted metal surface with subsurface scattering 
wear marks, Pixar Surface material, path-traced global illumination, 
multi-bounce indirect light, soft color bleeding, production quality render, 
Pixar feature film aesthetic, shallow depth of field, cinematic staging, 
appealing asymmetry, hand-crafted workshop environment
```

### Skill Priority Rules

When skills conflict:
1. **Technical skill wins on parameters** (sampler, model, resolution)
2. **Style skill wins on vocabulary** (lighting terms, animation descriptors)
3. **Base skill wins on syntax** (prompt structure, formatting)
4. **User override wins always** (explicit instructions beat skill defaults)

---

## 11. QUICK REFERENCE: PIXAR DESCRIPTOR MATRIX

Use this matrix to rapidly build prompts by selecting one item from each column.

| Character | Shape | Eyes | Material | Lighting | Mood | Quality |
|-----------|-------|------|----------|----------|------|---------|
| Protagonist | Circle | Large, asymmetrical | Subsurface skin | Warm key + cool rim | Joyful, curious | Path traced |
| Villain | Triangle | Narrow, sharp | Glossy hard surface | Hard spotlight | Menacing, cunning | Multi-bounce GI |
| Mentor | Square + round edges | Soft, kind | Weathered matte | Soft golden hour | Wise, nostalgic | Volumetric fog |
| Sidekick | Exaggerated circle | Huge, innocent | Fuzzy/fluffy | Bounce light only | Goofy, loyal | SSS + fuzz |
| Creature | Organic mix | Beady/glowing | Wet/slimy | Underwater caustics | Mysterious | Caustic refraction |

---

## 12. SOURCES & REFERENCES

- Frank Thomas & Ollie Johnston, *The Illusion of Life: Disney Animation* (1981)
- Pixar RenderMan Documentation [^4^] [^16^]
- Per H. Christensen, "Point-Based Global Illumination for Movie Production" [^21^]
- Christophe Hery, Pixar SSS Research [^24^] [^27^]
- Pixar Color Script methodology [^28^]
- Pixar Short Film production notes: *Piper* [^29^], *Purl* [^9^]
- Shape Language in Character Design [^18^] [^19^] [^31^]
- Pixar Story Spine structure [^8^]

---

## 13. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering animation principles, shape language, lighting, rendering, storytelling, short film techniques, and prompt engineering templates.
