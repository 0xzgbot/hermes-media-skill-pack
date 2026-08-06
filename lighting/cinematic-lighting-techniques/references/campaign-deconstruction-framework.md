# Campaign Deconstruction Framework

Structured approach for analyzing world-class ad campaigns and translating creative strategy into AI prompt specifications.

## Analysis Steps

### 1. Identify Campaign Source
Select recent Cannes Lions winner, Apple product film, or luxury fashion campaign. Document:
- Creative agency
- Core insight / narrative hook
- Target audience and cultural context

### 2. Extract Lighting Language
Document the lighting approach:
- Dominant light sources (natural, artificial, mixed)
- Color temperatures used (warm/cool balance)
- HDR or computational photography techniques
- Shadow treatment and highlight roll-off

### 3. Map Composition Patterns
Identify recurring compositional choices:
- Rule of thirds usage frequency
- Leading line placement and direction
- Foreground-background depth layering approach
- Subject positioning relative to frame geometry

### 4. Decode Color Grading Signature
Note the grading characteristics:
- Highlight treatment (warm roll-off, cool lift)
- Shadow behavior (lifted, crushed, detailed)
- Saturation ceiling and color harmony strategy
- Teal-orange or other cinematic contrast ratios

### 5. Map Emotional Arc
Document pacing and emotional progression:
- Opening hook technique
- Tension building method
- Climax/resolution timing
- Audio-visual synchronization patterns

## Case Study: Apple "Shot on iPhone" (2025-2026)

**Core Insight:** Democratize cinematic quality by proving professional-grade imagery is accessible through smartphone technology.

**Lighting Language:** Natural light dominance (70% of campaign), computational HDR for extended dynamic range, night mode shadow detail preservation, warm golden tones (#FFD700) for day / cool blues (#4682B4) for night.

**Composition Patterns:** Rule of thirds on primary subjects (85%), leading lines to emotional focal point, portrait mode bokeh depth layering, environmental context always present.

**Color Grading Signature:** Warm highlight roll-off preserving skin tone naturalism, shadow lifting without flat appearance, slight teal-orange cinematic contrast in video, consistent saturation ceiling preventing oversaturation.

## Improved Prompt Translation Template

When translating campaign analysis into Flux.2 prompts:
1. Add computational photography simulation language (Night Mode, HDR descriptors)
2. Specify native device color science characteristics in grading descriptions
3. Enhance environmental storytelling with cultural specificity
4. Improve temporal pacing for video templates using signature camera movements

### Example — Night Street Photography (Flux.2)
"Hyper-detailed urban night photography capturing authentic street life, lone figure walking through rain-slicked Tokyo alleyway with neon signs reflecting on wet asphalt as hero, computational HDR combining multiple exposures revealing shadow detail in narrow passage while preserving specular highlights from red (#FF0040) and cyan (#00FFFF) neon signage, iPhone 15 Pro Night Mode simulation with natural noise texture, color grading: warm skin tones preserved against cool blue shadows (#1E3A5F) with neon accent reflections, composition: leading lines of alley walls converging behind subject at rule of thirds intersection creating depth and mystery, --ar 4:5 --style raw --stylize 125 --v 5.2 --q 2 --h 1024"

### Example — Golden Hour Portrait (LTX 2.3)
"Video scene: slow push-in on young woman's face illuminated by golden hour sunlight filtering through tree canopy, camera movement: gentle dolly forward with subtle handheld micro-movement creating organic documentary feel, motion strength: 0.25, timing: 0-4s establishing medium shot showing subject in natural park environment with dappled light patterns shifting across skin, 4-8s slow push to close-up capturing eye catchlight from warm sunlight (#FFB347) and natural micro-expressions of peaceful contentment, 8-12s extreme close-up on eyes reflecting golden tree canopy with shallow depth of field blurring background to painterly bokeh, audio: gentle wind through leaves, distant birdsong and soft ambient nature sounds creating meditative atmosphere, color grading: warm golden hour tones (#FFD700) preserving natural skin tones with subtle teal shadow contrast (#5F8A8B), --lxt 2.5 --duration 12s --fps 30"
