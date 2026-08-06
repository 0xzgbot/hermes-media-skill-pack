# SKILL: Wide Angle Environmental
## Version: 1.0 | Hermes Agent Camera & Lens Language

---

### DESCRIPTION
Mastery of wide-angle optics (14–35mm focal length) for environmental storytelling, spatial exaggeration, and compositional drama. Wide angles expand field of view beyond natural human vision, exaggerating depth, distorting perspective, and making subjects feel powerful in foreground or insignificant against vast backgrounds. Critical for establishing shots, interiors, action, and psychological distortion [^21^].

### TRIGGER KEYWORDS
wide angle, wide lens, 14mm, 24mm, 28mm, 35mm, environmental shot, establishing shot, vast landscape, interior wide, distorted perspective, fish eye adjacent, edge distortion, exaggerated depth, environmental storytelling, wide establishing

### CORE RULES
- Wide angle exaggerates spatial depth: near subjects loom large, far subjects appear tiny
- Subject in foreground feels powerful or threatening; background figures feel distant/irrelevant
- Edge distortion is a creative tool: faces at frame edges distort — avoid for portraiture
- Interiors: wide angles are essential for showing the full architectural space in one frame
- Converging verticals: pointing camera up makes tall buildings lean inward — intentional or corrected
- 24mm–28mm is the "environmental portrait" sweet spot: subject + context without extreme distortion
- Motion toward camera on wide angle feels fast and aggressive: use for action and approach

---

### TECHNICAL PARAMETERS

**Focal Length Categories:**
- Ultra-Wide: 14–24mm — Extreme distortion, vast scope, architectural drama
- Wide: 24–35mm — Substantial expansion with moderate distortion, general purpose
- Standard: 50mm — "Normal" human FOV reference point
- FOV Expansion: 14mm captures ~114° diagonal; 35mm captures ~63° diagonal

**Barrel Distortion Characteristics:**
- Optical Effect: Straight lines near frame edges curve outward
- Center: Minimal distortion; sharpest, most natural area
- Edge: Increasing distortion and chromatic aberration
- Correction: In-camera or post-correction available; often left uncorrected for style
- Creative Use: Exaggerates environment scale; makes rooms feel cavernous

**Perspective Exaggeration:**
- Near-Far Relationship: Objects close to camera appear disproportionately large
- Background Recession: Distant elements appear farther away than reality
- Depth Enhancement: Spatial distances between planes feel expanded
- Body Distortion: Limbs/hands near frame edges stretch unnaturally
- Facial Distortion: Close wide-angle portraits unflatter — nose enlarges, face widens

**Deep Focus Capability:**
- Natural Tendency: Wide angles inherently produce greater depth of field
- Aperture Flexibility: Can shoot f/5.6–f/11 and maintain foreground-to-background sharpness
- Layered Staging: Multiple focal planes in focus simultaneously
- Hyperfocal Distance: Shorter; easier to achieve zone focus

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Wide angle [14mm/24mm/35mm] [environmental/establishing/action] shot, 
[subject] positioned [close to camera/in environment], 
barrel distortion creating [spatial effect: expansive room/vast landscape/dynamic perspective], 
foreground [element] disproportionately large drawing eye into frame, 
background [element] stretching into deep distance, 
deep focus keeping [foreground] and [background] simultaneously sharp, 
[low/high] angle perspective adding [power/vulnerability], 
cinematic wide angle composition, 
environmental storytelling through spatial relationships
```

**Negative Prompts:**
```
telephoto compression, shallow depth of field isolating subject, 
flat perspective, normal human field of view, 
portrait lens compression, circular bokeh background, 
tight framing without environment, studio backdrop, 
neutral perspective, standard 50mm look
```

---

### ADVANCED TECHNIQUES

**1. Environmental Establishment (The Classic)**
- Lens: 24–35mm
- Purpose: Show location scope and spatial context
- Composition: Subject small in frame against vast environment
- Emotional: Isolation, awe, environmental hostility or grandeur
- Examples: Mad Max: Fury Road desert scope; Grand Budapest Hotel diorama frames [^21^]

**2. Foreground Dominance (Power/Intimacy)**
- Lens: 14–24mm ultra-wide
- Setup: Subject or object extremely close to lens (12–24 inches)
- Effect: Foreground element fills 30–50% of frame; background provides context
- Emotional: Power, aggression, claustrophobic intimacy
- Risk: Facial distortion if subject is person — use for hands, objects, or stylized effect

**3. Symmetrical Wide (Wes Anderson Style)**
- Lens: 24–30mm
- Composition: Centered subject, symmetrical environment
- Effect: Diorama-like, theatrical, artificial perfection
- Distortion: Barrel distortion must be corrected or minimized
- Emotional: Whimsical, controlled, storybook
- Example: The Grand Budapest Hotel [^21^]

**4. Psychological Horror Distortion**
- Lens: 14–20mm ultra-wide
- Setup: Low angle, close to subject in confined space
- Effect: Room feels simultaneously vast and claustrophobic
- Distortion: Uncorrected barrel distortion, converging verticals
- Emotional: Unease, wrongness, psychological instability
- Example: The Shining's Overlook Hotel corridors [^21^]

**5. Deep Focus Layered Staging (Citizen Kane Style)**
- Lens: 24–28mm
- Aperture: f/8–f/11 for maximum depth
- Composition: Foreground subject + midground action + background detail
- Effect: Multiple story layers in single frame
- Emotional: Complexity, power dynamics, narrative density
- Example: Citizen Kane pioneered this technique [^21^]

**6. Dynamic Action Coverage**
- Lens: 18–28mm
- Movement: Camera tracking rapid motion
- Effect: Expanded view prevents action from leaving frame
- Spatial Orientation: Audience maintains sense of geography during chaos
- Emotional: Kinetic energy, visceral immediacy
- Example: Children of Men long takes [^21^]

---

### FOCAL LENGTH BEHAVIOR CHART
| Focal Length | Distortion | Depth of Field | Best Use | Risk |
|--------------|------------|----------------|----------|------|
| 14–18mm | Extreme | Very deep | Architecture, vast landscapes | Heavy distortion |
| 20–24mm | Moderate | Deep | Environmental, action | Edge stretching |
| 28–35mm | Mild | Moderate-Deep | General wide, establishing | Slight perspective |
| 50mm | None | Moderate | Reference "normal" | None (boring for drama) |

---

### EXAMPLE PROMPTS

**Environmental Establishment:**
> Wide angle 24mm establishing shot, lone figure standing at edge of vast salt flat stretching to horizon, subject small in lower third of frame emphasizing environmental scale, deep focus keeping cracked earth foreground and distant mountains simultaneously sharp, barrel distortion minimal at center, pale blue sky dominating upper frame, cinematic environmental storytelling, isolation and awe, photorealistic landscape, natural color science

**Psychological Interior:**
> Ultra-wide 16mm interior shot, subject walking down long hotel corridor, low angle making ceiling converge dramatically, barrel distortion curving corridor walls toward edges, deep focus from patterned carpet foreground to distant figure, symmetrical composition twisted by wide-angle perspective, unsettling spatial exaggeration making hallway feel simultaneously endless and claustrophobic, cinematic horror aesthetic, photorealistic architecture, psychological tension through lens distortion

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify exact focal length ("24mm", "14mm") rather than just "wide angle" for precision
- Use "barrel distortion" explicitly when desired; "corrected distortion" for clean architecture
- Include "deep focus" or "foreground and background sharp" to trigger large depth of field
- Mention "low angle" or "high angle" for dramatic perspective shifts
- Use "foreground element large" to trigger perspective exaggeration
- For portraits, specify "environmental portrait" rather than "close-up" to avoid facial distortion
