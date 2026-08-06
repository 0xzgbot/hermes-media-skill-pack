# SKILL: Non-Human & Creature
## Version: 1.0 | Hermes Agent Character & Direction System

---

### DESCRIPTION
Mastery of cinematographic techniques for non-human subjects — animals, creatures, robots, monsters, and hybrids. Balances scale reference for comprehension, navigates the uncanny valley between human and non-human, and develops distinct motion languages that communicate character without dialogue. Essential for nature documentary, creature features, sci-fi, horror, and fantasy [^34^][^41^].

### TRIGGER KEYWORDS
creature, monster, animal, robot, beast, non-human, fantasy creature, alien, dragon, wolf, horse, mechanical creature, hybrid creature, mythical creature, wildlife, creature design, creature feature

### CORE RULES
- Scale reference is essential: always include familiar object or human to establish creature's size
- Camera height at creature's eye level signals connection; overhead signals vulnerability
- Reveal in stages: partial views before full reveal build dread or wonder
- Motion language defines character: predators are fluid and deliberate; prey are quick and reactive
- Uncanny valley management: the more human-like, the more critical precise anatomy becomes
- Texture of skin/fur/scales carries emotion — rough vs. smooth signals threat vs. gentleness
- Eyes are the emotional window even for creatures: front-on eye contact = connection, avoidance = mystery

---

### TECHNICAL PARAMETERS

**Scale Reference:**
- Human Presence: Include human figure, hand, or familiar object for size context
- Environmental Scale: Trees, buildings, furniture provide relative measurement
- Extreme Close-Up: Macro shots of creature features without context create scale ambiguity
- Miniaturization: Small creatures shot from their eye level make them heroic/relatable
- Monumentalization: Large creatures framed from below emphasize dominance
- Ratio Preservation: Maintain realistic proportions between creature and environment

**Uncanny Valley Navigation:**
- Definition: The unsettling effect when human-like entities are almost but not quite human [^41^]
- Safe Zone 1: Clearly non-human (robot with metal face, animal, monster) = appealing
- Danger Zone: Near-human with slight wrongness (dead eyes, wrong skin texture, odd movement) = revulsion [^34^][^41^]
- Safe Zone 2: Fully human = normal appeal
- Avoidance Strategy: Either commit to full non-human or full human; don't linger in valley
- Intentional Use: Some horror deliberately uses uncanny valley for creepiness (Ava in Ex Machina, Michael Myers mask) [^34^]
- Correction Factors: Slightly exaggerated non-human features push entity out of danger zone

**Motion Language:**
- Animal Motion: Non-constant movement — pause, burst, pause; head movements before body
- Robot Motion: Linear, precise, mechanical; occasional glitch or stutter for character
- Creature Motion: Weight-based — heavy creatures move slow with momentum; light creatures dart
- Hybrid Motion: Mix of human and non-human gaits (bipedal wolf, crawling humanoid)
- Eye Movement: Animals track differently than humans (head turns with eyes, saccades differ)
- Breathing: Visible in creatures; chest movement, gill flutter, steam venting
- Tail/Appendage: Continuous secondary motion even when body still

**Eye Contact & Gaze:**
- Direct Gaze: Predator eyes on camera = confrontation, threat, intimacy
- Averted Gaze: Prey animal avoiding lens = fear, submission, wildness
- Reflected Gaze: Creature sees itself in water/mirror = self-awareness, uncanny moment
- No Eyes: Creatures without visible eyes (insects, worms, deep-sea) = alien, otherworldly
- Eye Glow: Bioluminescence or reflective tapetum = supernatural, night hunting

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Shot type] of [creature type], 
[scale reference: human hand/familiar object/environmental element] establishing size, 
[creature] positioned [eye level/low angle/high angle] for [relatability/dominance/vulnerability], 
[motion language: paused predator/linear robot/heavy lumber/darting prey], 
[eye treatment: direct gaze/averted/reflected/glowing/absent] signaling [psychological state], 
[texture detail: fur/scales/metal/chitin/skin] in [lighting quality], 
[uncanny position: clearly non-human/intentionally near-human/full alien], 
cinematic creature cinematography, 
photorealistic [animal/robot/monster] behavior
```

**Negative Prompts:**
```
uncanny valley unintentional, human eyes on non-human face, 
wrong scale without reference, cartoonish movement, 
smooth human gait on animal body, static pose without life, 
flat lighting hiding texture, human smile on creature face, 
incorrect anatomy proportions, cute anthropomorphism without intent
```

---

### ADVANCED TECHNIQUES

**1. The Predator Pause**
- Setup: Large predator frozen mid-motion, about to strike
- Camera: Low angle at predator eye level or below
- Eyes: Direct gaze locked on prey (or camera)
- Motion: Completely still except for subtle tail twitch or ear rotation
- Background: Environment frames predator; prey visible but small
- Emotional: Coiled energy, inevitability, apex dominance
- Best For: Nature doc, thriller, monster reveal

**2. The Miniature Hero**
- Setup: Small creature (insect, rodent, bird) shot from its eye level
- Camera: On ground or at creature height; world towers above
- Scale: Grass blades become forest; pebbles become boulders
- Motion: Quick, darting, precise — hyperactive compared to human scale
- Emotional: Underdog, resilience, hidden world, empathy
- Best For: Nature documentary, children's content, macro cinematography

**3. The Uncanny Android**
- Setup: Humanoid robot with deliberate near-human features
- Design: Beautiful but slightly wrong — perfect skin, dead eyes, too-symmetric face [^34^]
- Motion: Smooth but with micro-stutters or too-perfect posture
- Gaze: Direct but without true comprehension behind eyes
- Light: Clinical, even; or warm but unconvincing
- Emotional: Discomfort, beauty, existential questioning
- Best For: Sci-fi, horror, philosophical drama [^41^]

**4. The Monumental Beast**
- Setup: Massive creature (dragon, kaiju, whale) framed from extreme low angle
- Scale: Human figures tiny in foreground or on creature itself
- Motion: Slow, weight-driven, earth-shaking impact
- Environment: Creature interacts with architecture/nature; scale readable through destruction
- Eyes: Either glowing from height or invisible due to scale
- Emotional: Awe, terror, sublime, nature's power
- Best For: Fantasy, disaster, myth, action

**5. The Sympathetic Creature**
- Setup: Non-human subject framed with human emotional cues
- Eyes: Large, forward-facing, with catchlights (mammalian empathy triggers)
- Scale: Medium shot with human nearby or hands interacting
- Motion: Gentle, seeking, vulnerable
- Light: Soft, warm, protective
- Emotional: Love, care, interspecies bond, innocence
- Best For: Family, pet content, conservation, emotional narrative

**6. The Alien Other**
- Setup: Completely non-terrestrial biology
- Anatomy: No bilateral symmetry or radically different body plan
- Eyes: Multiple, compound, absent, or distributed
- Motion: No recognizable terrestrial gait — sliding, floating, pulsating
- Scale: Ambiguous; no human reference or distorted reference
- Emotional: True alienness, cosmic horror, wonder, incomprehension
- Best For: Hard sci-fi, horror, experimental, cosmic narrative

---

### CREATURE TYPE MOTION MATRIX
| Creature | Primary Motion | Secondary Motion | Eye Behavior | Scale Cue |
|----------|----------------|------------------|--------------|-----------|
| Feline | Pause-burst-pause | Tail tip twitch | Direct, slit pupil | Human leg/tall grass |
| Canine | Constant trot | Panting, ear rotation | Friendly, tracking | Human waist/furniture |
| Bird | Head darting | Feather ruffle | Side-placed, quick | Hand/perch |
| Insect | Jerky, mechanical | Antennae wave | Compound, no gaze | Finger/blade of grass |
| Robot | Linear, precise | LED status blink | Camera-like, steady | Human/human hand |
| Monster | Heavy, weighty | Drool, steam, spore | Variable by design | Building/vehicle |
| Deep Sea | Drift, pulse | Bioluminescence flash | Absent or huge | Submersible/human |

---

### EXAMPLE PROMPTS

**Predator Pause:**
> Low angle shot at tiger eye level, massive predator frozen in tall grass with only ears and eyes visible above golden savanna grass, direct predatory gaze locked on camera with vertical slit pupils catching sunlight, completely motionless body with only subtle tail tip twitch visible, background acacia tree providing African scale reference, warm golden hour side-light creating rim on fur texture, shallow depth of field isolating eyes from grass foreground, cinematic wildlife cinematography, coiled kinetic energy, photorealistic predator behavior, National Geographic quality

**Uncanny Android:**
> Medium close-up of humanoid android, face perfectly symmetrical with flawless synthetic skin but eyes lacking true human warmth and micro-movement, direct gaze at camera with slight unnerving stillness between blinks, smooth neck and jawline transitioning to visible mechanical seam at collarbone, cool 5000K clinical lighting emphasizing artificial perfection, background minimal white laboratory space, subtle uncanny valley effect — beautiful but wrong [^41^], slight motion stutter in finger movement at frame edge, cinematic sci-fi aesthetic, photorealistic synthetic skin texture, existential discomfort

---

### TECHNICAL NOTES FOR AI GENERATION
- Always include scale reference ("human hand nearby", "building in background") unless scale ambiguity is intentional
- Use "uncanny valley" or "near-human but wrong" only when intentional horror/sci-fi effect desired
- Specify motion style explicitly ("jerky insect movement", "heavy dinosaur gait")
- Include "eye level with creature" or "low angle looking up" for perspective control
- Use "bioluminescence" or "reflective eyes" for night creature effects
- Mention "fur texture", "scale detail", "mechanical joints" for material specificity
- For sympathetic creatures, specify "large forward eyes" and "catchlights" for mammalian empathy triggers
