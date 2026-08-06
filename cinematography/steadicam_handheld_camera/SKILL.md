# SKILL: Steadicam & Handheld Camera
## Version: 1.0 | Hermes Agent Camera Movement Language

---

### DESCRIPTION
Mastery of fluid and organic camera movement through steadicam and handheld techniques for AI-generated cinematic content. This skill encodes the physics and emotional grammar of moving cameras: the weightless grace of steadicam, the kinetic urgency of handheld, the psychological tension of intentional shake, and the narrative purpose behind every camera motion decision.

---

### TECHNICAL PARAMETERS

**Steadicam Characteristics:**
- **Weightless Float:** Camera hovers smoothly, eliminating vertical bounce and footsteps
- **Inertia:** Momentum carries through turns; starts and stops have gentle ramp
- **Z-Axis Stability:** Horizon remains level regardless of operator movement
- **Proximity:** Can move within inches of actors at walking speed
- **Emotional Register: Dreamlike, omniscient, seamless immersion**

**Handheld Characteristics:**
- **Human Breath:** Subtle vertical float matching operator's breathing
- **Micro-Jitters:** High-frequency shake from muscle tension
- **Weight Shift:** Frame tilts and sways with body movement
- **Immediacy:** Creates sense of being present in the moment
- **Emotional Register: Urgency, intimacy, documentary truth, chaos**

**Movement Vocabulary:**

| Movement | Steadicam Version | Handheld Version | Emotional Effect |
|----------|------------------|------------------|------------------|
| **Push-In** | Slow, inevitable approach | Nervous, hesitant advance | Revelation, confrontation |
| **Pull-Back** | Graceful withdrawal | Stumbling retreat | Discovery of scale, escape |
| **Orbit** | Perfect circular path | Elliptical, uneven loop | Observation, unease, worship |
| **Follow** | Smooth tracking parallel | Bumpy, breath-matched pursuit | Determination, chase, companionship |
| **Reveal** | Arc around obstacle | Peer around corner | Anticipation, surprise |
| **Spiral** | Descending/ascending helix | Unsteady circling | Disorientation, obsession |
| **Whip Pan** | Controlled fast swivel | Accidental snap to subject | Shock, discovery, comedic timing |

**The Fluidity Spectrum:**
```
LOCKED TRIPOD → SLIDER → STABILIZED GIMBAL → STEADICAM → HANDHELD INTENTIONAL → HANDHELD CHAOTIC
Objectivity        Precision      Smooth motion      Dreamlike      Intimacy           Panic
```

---

### PROMPT ARCHITECTURE

**Core Prompt Template (Steadicam):**
```
Steadicam cinematography, [movement type: push-in / orbit / follow / reveal],
weightless floating camera motion, smooth inertia-based movement,
level horizon, no footstep vibration, [speed: slow / walking pace / dynamic],
[proximity: intimate close / medium / wide environmental],
seamless immersive motion, professional fluid camera work,
[emotional register: dreamlike / omniscient / inevitable]
```

**Core Prompt Template (Handheld):**
```
Handheld cinematography, [movement type: follow / push-in / run / reveal],
organic human camera motion, subtle breathing float,
[micro-jitter intensity: gentle / moderate / chaotic],
[weight: light DSLR / heavy cinema camera],
[operator energy: calm / urgent / panicked],
immediate documentary presence, kinetic camera work,
[emotional register: intimate / urgent / raw / chaotic]
```

**Negative Prompts:**
```
locked static tripod, robotic gimbal perfection, drone aerial only,
no camera movement, smooth slider only, mechanical motion,
cgi camera path, video game camera, unmotivated movement
```

---

### ADVANCED TECHNIQUES

**1. The Steadicam Reveal**
- Movement: Slow orbit around foreground object to reveal subject
- Speed: Walking pace, 180° arc over 8–12 seconds
- Framing: Tight on obstacle → wide on reveal
- Emotional: Inevitable discovery, fate unfolding, beauty revealed
- Best For: Product reveals, location introductions, dramatic entrances

**2. The Handheld Chase**
- Movement: Following subject through tight spaces at speed
- Shake: Moderate to heavy, breath-matched, occasional frame-edge clipping
- Focus: Slightly soft, catching up to subject movement
- Emotional: Urgency, danger, documentary immediacy
- Best For: Action sequences, protests, run-and-gun documentary, thrillers

**3. The Intimate Two-Shot Walk**
- Movement: Steadicam walking backward in front of two characters
- Speed: Natural walking pace
- Framing: Medium two-shot, background moving past
- Emotional: Partnership, journey, forward momentum in relationship
- Best For: Relationship stories, buddy films, walking conversations

**4. The Panic Documentary**
- Movement: Handheld, chaotic, reframing constantly
- Shake: Heavy, occasional whip pans, brief out-of-focus moments
- Framing: Reactive — finding subject, losing subject, finding again
- Emotional: Confusion, crisis, unfiltered reality breaking through
- Best For: War zones, disasters, breaking news, found footage horror

**5. The Steadicam Dream Sequence**
- Movement: Slow push-in through space, impossible smoothness
- Speed: Glacial, hypnotic
- Framing: Subject isolated in vast environment
- Emotional: Surreal, memory, death, transcendence
- Best For: Fantasy, memory sequences, near-death experiences, art films

---

### EXAMPLE PROMPTS

**Steadicam Orbit Reveal:**
> Steadicam cinematography, slow 180-degree orbit around foreground column revealing subject seated in grand library beyond, weightless floating camera motion with perfect level horizon, smooth inertia carrying through turn, walking pace movement, medium framing transitioning from obscured to fully revealed, dreamlike omniscient camera presence, creamy shallow depth of field, warm tungsten practical lighting, seamless immersive motion, cinematic steadicam aesthetic

**Handheld Documentary Follow:**
> Handheld cinematography, camera following subject through crowded market street, organic human motion with subtle breathing float and moderate micro-jitters, reactive reframing as subject navigates through people, occasional brief soft focus catching up to movement, urgent but not panicked operator energy, immediate documentary presence, environmental details visible in peripheral frame, raw kinetic camera work, vérité visual grammar

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "steadicam" explicitly for fluid motion; "handheld" for organic shake
- Specify "level horizon" for steadicam; "breathing float" for handheld
- For LTX video: describe camera movement in motion terms — "camera orbits subject"
- For FLUX: describe single frame with implied motion — "dynamic steadicam frame"
- Intensity matters: "gentle handheld" vs "chaotic handheld" produce very different results
- Mention weight: "light DSLR handheld" vs "heavy cinema camera handheld"
- Combine with lens specs: "steadicam with 24mm wide lens" vs "handheld 85mm telephoto"
