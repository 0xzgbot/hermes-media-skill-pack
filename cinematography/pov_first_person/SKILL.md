# SKILL: POV & First-Person
## Version: 1.0 | Hermes Agent Camera & Lens Language

---

### DESCRIPTION
Mastery of subjective camera positioning that places the audience inside a character's perceptual experience. POV (Point of View) and first-person framing create visceral immersion through sightline alignment, hand presence, physiological movement (breathing, head bob), and restricted field of view. Essential for horror, action, VR adaptation, and intense psychological identification.

### TRIGGER KEYWORDS
POV, point of view, first person, subjective camera, character POV, looking through eyes, immersive, first-person perspective, hand visible, character view, through character eyes, found footage, bodycam aesthetic, helmet cam

### CORE RULES
- Camera height matches character eye level exactly — never cheat height for composition
- Hands may appear in lower frame: adds embodied physicality and confirms POV
- Physiological movement optional: breathing sway, head bob for immersion vs. static for calm
- Field of view matches intended focal length: wide for disorientation, normal for everyday
- Sound design is crucial for POV: internal sounds (heartbeat, breathing) mix with external
- Avoid impossible POV framings that would require the character to move their neck unnaturally
- Horror POV: restrict what viewer can see; create dread through limited field of view

---

### TECHNICAL PARAMETERS

**Sightline Framing:**
- Height: Matched to character's eye level (varies by character stature)
- Alignment: Camera looks where character looks; head turns = camera pans
- Peripheral Restriction: Human FOV ~180° horizontal; camera FOV typically 60–120° for cinematic POV
- Focus Behavior: Mimics human attention — sharp on subject, peripheral blur
- Blink Simulation: Occasional momentary blackout (controversial; use sparingly)

**Hand Presence Mechanics:**
- Visibility: Character's hands/tools enter lower frame (bottom 15–25%)
- Perspective: Arms appear elongated, distorted at frame edges (wide-angle effect)
- Interaction: Hands reach toward objects, grasp doorknobs, hold weapons
- Shadow: Body shadow visible on ground/walls in bright conditions
- Weapon/Tool Framing: Held object dominates center-lower frame

**Physiological Camera Movement:**
- Breathing: Subtle vertical rhythm (1–2 pixel shift at 12–20 cycles/minute)
- Heartbeat: Micro-tremor during stress (rapid, subtle vibration)
- Head Bob: Natural oscillation during walking (sinusoidal, 2Hz)
- Saccades: Rapid eye-movement jumps between points of interest
- Dizziness: Uncontrolled spin/tilt during disorientation
- Shock: Sudden violent movement (whip pan, drop, shake)

**Field of View & Lens Choice:**
- Realistic Human: 50mm equivalent (central sharp vision)
- Peripheral Simulation: 24–35mm for wider immersive feel
- VR/Extreme: 16mm+ for full peripheral (causes distortion)
- Aperture: f/2.8–f/4 for shallow depth mimicking human attention
- Focus Pull: Eye naturally shifts focus between distances

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
First-person POV shot, [character type] perspective, 
camera at [eye height] looking [direction/action], 
[hands/arms/weapon] visible in lower frame reaching toward [object], 
subtle [breathing rhythm/head bob/heartbeat tremor] in camera motion, 
[sightline] following [point of interest], 
natural human field of view [60°/90°/120°], 
shallow depth of field mimicking eye focus on [subject], 
peripheral blur outside central attention zone, 
[emotional state: calm/tense/terrified/excited] affecting camera stability, 
immersive subjective cinematography, 
photorealistic environment from human perspective
```

**Negative Prompts:**
```
third person perspective, objective camera, stable tripod shot, 
no hand presence, clean camera movement, 
wide establishing shot, omniscient view, 
overhead angle, static framing, 
disembodied floating camera, video game HUD
```

---

### ADVANCED TECHNIQUES

**1. Walking POV (Journey/Exploration)**
- Movement: Forward walking with natural head bob
- FOV: 24–35mm for environmental awareness
- Hands: Slight swing at frame edges
- Sound: Footsteps, breathing, fabric rustle (implied in visual pacing)
- Emotional: Discovery, journey, mundane realism
- Best For: Entering new spaces, exploration sequences, travel

**2. Weapon/Tool POV (Action/Horror)**
- Frame Bottom: Weapon (gun, knife, flashlight) dominates
- Movement: Weapon sways with breathing; snaps to target
- Focus: Sharp on target; weapon slightly soft (eye focuses beyond gun)
- Recoil: Violent upward jerk (for firearms)
- Emotional: Agency, danger, competence, violence
- Best For: Action sequences, horror survival, tactical scenarios

**3. Vulnerable POV (Restrained/Injured)**
- Movement: Limited — character bound, lying down, or incapacitated
- Angle: Low to ground or tilted unnaturally
- Vision: Blur, double vision, or tunnel vision effects
- Breathing: Labored, irregular
- Emotional: Helplessness, vulnerability, disorientation
- Best For: Horror, thriller, medical drama, aftermath

**4. Height Difference POV (Child/Creature)**
- Height: 2–4 ft for child; 1–2 ft for animal; 6–7 ft for giant
- Perspective: Adult world towers above or shrinks below
- Movement: Scampering (child/animal); heavy, slow (giant)
- Emotional: Innocence, fear, power, alienation
- Best For: Horror (child's room), fantasy, creature features

**5. Memory/Flashback POV**
- Quality: Slight diffusion, desaturation, or color shift
- Movement: Floating, less grounded than present-tense POV
- Focus: Soft overall, sharp only on emotional trigger objects
- Sound: Muffled, distant (implied in visual rhythm)
- Emotional: Nostalgia, trauma, dreamlike unreality
- Best For: Character backstory, psychological depth

**6. VR/Immersive 360 POV**
- FOV: Extreme wide (16mm+) for peripheral coverage
- Distortion: Barrel distortion acceptable for immersion
- Movement: Smooth (VR doesn't tolerate shake well)
- Interactivity: Gaze-directed focus (look = sharp)
- Emotional: Presence, embodiment, simulation
- Best For: VR content, immersive experiences, experimental

---

### POV EMOTIONAL STATE MATRIX
| State | Camera Stability | Breathing | Focus Behavior | Hand Presence |
|-------|------------------|-----------|----------------|---------------|
| Calm | Stable, smooth | Slow, deep | Normal shifts | Relaxed |
| Tense | Slight tremor | Quick, shallow | Rapid saccades | Gripped, ready |
| Terrified | Violent shake | Panicked, irregular | Tunnel vision | Clenched, defensive |
| Excited | Energetic bob | Fast, energetic | Wide, scanning | Active, reaching |
| Injured | Drifting, unstable | Labored | Blurred, drifting | Weak, limp |
| Stealth | Minimal movement | Held, controlled | Slow, deliberate | Cautious, precise |

---

### EXAMPLE PROMPTS

**Horror Exploration POV:**
> First-person POV shot, character exploring dark abandoned house at night, camera at 5'8" eye height with subtle breathing rhythm and cautious head movements, flashlight beam cutting through darkness creating narrow cone of visibility, hand holding flashlight visible in lower right frame with realistic arm length distortion, shallow depth of field beyond flashlight beam, peripheral darkness creating claustrophobic tunnel vision, sudden whip pan as character reacts to floorboard creak, immersive horror cinematography, photorealistic environment, subjective tension

**Child's Perspective POV:**
> First-person POV from child's height (3.5 feet), looking up at towering adult figures in kitchen, camera tilted upward revealing ceiling and looming faces from below, small hands visible at bottom of frame reaching toward table edge, wide 28mm field of view creating slight distortion at edges, natural head bob and slight unsteadiness of child movement, warm kitchen light from low perspective making adults appear monumental, immersive subjective childhood perspective, photorealistic scale distortion, emotional vulnerability

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify "first-person POV" or "POV shot" explicitly to trigger subjective framing
- Include "hands visible" or "arms in frame" for embodiment
- Mention "breathing motion" or "subtle camera shake" for physiological realism
- Use "shallow depth of field" to mimic human eye focus behavior
- Specify height ("3 feet tall", "eye level") for perspective accuracy
- Include "flashlight beam" or "narrow field of view" for restricted vision scenarios
- Use "whip pan" or "sudden movement" for reactive moments
