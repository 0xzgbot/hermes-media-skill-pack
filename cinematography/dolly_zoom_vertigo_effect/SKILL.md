# SKILL: Dolly Zoom / Vertigo Effect
## Version: 1.0 | Hermes Agent Cinematic Camera Movement

---

### DESCRIPTION
Mastery of the dolly zoom (Vertigo effect, contra-zoom, trombone shot) — one of cinema's most psychologically disorienting camera techniques. This skill encodes the precise mathematical relationship between camera movement and focal length adjustment that creates the illusion of the background compressing or expanding while the subject remains constant in frame. Essential for moments of psychological shock, realization, dread, or spatial impossibility.

---

### TECHNICAL PARAMETERS

**The Mathematical Principle:**
The dolly zoom maintains constant subject size while changing perspective compression through the inverse relationship of:
- **Camera Distance (d)** — how far camera is from subject
- **Focal Length (f)** — zoom setting of lens

As the camera dollies forward (decreasing d), the lens zooms out (decreasing f) proportionally to keep subject framing identical. The background appears to stretch and expand away from subject.

As the camera dollies backward (increasing d), the lens zooms in (increasing f) proportionally. The background appears to compress and crash toward subject.

**The Formula:**
```
Subject Size = Constant
Background Compression ∝ f / d

Dolly In + Zoom Out = Background expands away (Vertigo effect)
Dolly Out + Zoom In = Background compresses inward (Reverse Vertigo)
```

**Movement Speed Ratios:**
- **Slow Dolly + Slow Zoom:** Creeping dread, gradual realization, psychological unease
- **Fast Dolly + Fast Zoom:** Sudden shock, panic attack, violent spatial distortion
- **Dolly Only (with post zoom):** Smoother but less visceral; common in digital workflows

**Focal Length Pairings:**

| Starting Lens | Ending Lens | Movement | Effect Strength | Best For |
|--------------|-------------|----------|-----------------|----------|
| **100mm** | **24mm** | Dolly in 3m → 1m | Extreme — background violently expands | Horror, shock, madness |
| **85mm** | **35mm** | Dolly in 4m → 2m | Strong — noticeable spatial warping | Realization, dread, awe |
| **50mm** | **24mm** | Dolly in 3m → 1.5m | Moderate — subtle unease | Suspense, subtle wrongness |
| **24mm** | **100mm** | Dolly out 1m → 4m | Reverse — background crushes inward | Isolation, entrapment, paranoia |
| **35mm** | **85mm** | Dolly out 2m → 4m | Reverse moderate | Vulnerability, exposure |

---

### PROMPT ARCHITECTURE

**Core Prompt Template (Standard Vertigo — Background Expands):**
```
Dolly zoom cinematography, camera dollying forward while simultaneously zooming out,
subject maintaining constant size in frame,
background appearing to stretch and expand away from subject,
[starting lens: 100mm / 85mm / 50mm] compressing to [ending lens: 24mm / 35mm],
[movement speed: slow creeping / fast sudden],
[subject reaction: shock / realization / horror / awe],
spatial distortion effect, perspective warping,
cinematic psychological disorientation
```

**Core Prompt Template (Reverse Vertigo — Background Compresses):**
```
Reverse dolly zoom cinematography, camera dollying backward while zooming in,
subject maintaining constant size in frame,
background appearing to compress and crash inward toward subject,
[starting lens: 24mm / 35mm] expanding to [ending lens: 100mm / 85mm],
[movement speed: slow creeping / fast sudden],
[subject emotion: isolation / paranoia / vulnerability],
claustrophobic spatial compression, perspective crushing,
cinematic psychological entrapment
```

**Negative Prompts:**
```
static camera, normal perspective, no spatial distortion, locked framing,
standard zoom only, dolly only without zoom, unmotivated movement,
smooth gimbal float, drone aerial, stable composition
```

---

### ADVANCED TECHNIQUES

**1. The Classic Vertigo (Hitchcock, 1958)**
- Movement: Dolly in + zoom out
- Subject: Character looking down from height, realization of danger
- Background: Tall tower stairs appear to stretch impossibly
- Speed: Moderate — 3–4 seconds for full effect
- Emotional: Acrophobia, loss of spatial reference, existential dread
- Best For: Heights, depths, psychological breaks, impossible spaces

**2. The Jaws Shock (Spielberg, 1975)**
- Movement: Dolly in + zoom out
- Subject: Character on beach, realizing shark attack
- Background: Beach and ocean stretch away violently
- Speed: Fast — sudden shock over 2 seconds
- Emotional: Sudden mortal terror, world distorting with realization
- Best For: Sudden danger, bad news, horrifying discovery

**3. The Reverse Entrapment**
- Movement: Dolly out + zoom in
- Subject: Character in room, walls appearing to close in
- Background: Room compresses, ceiling lowers, space becomes claustrophobic
- Speed: Slow — creeping paranoia over 5–6 seconds
- Emotional: Isolation, walls closing in, agoraphobia becoming claustrophobia
- Best For: Panic attacks, imprisonment, psychological horror, entrapment

**4. The Conversational Realization**
- Movement: Slow dolly in + zoom out during dialogue
- Subject: Character receiving devastating information
- Background: Room subtly warps, furniture seems to recede
- Speed: Very slow — almost subliminal over 8–10 seconds
- Emotional: Worldview shattering, subtle wrongness, uncanny valley of space
- Best For: Dramatic revelations, betrayals, tragic news, plot twists

**5. The Impossible Space**
- Movement: Dolly zoom on architecture or landscape
- Subject: Building, corridor, or road maintaining size while environment warps
- Background: Escher-like spatial impossibility
- Speed: Variable — can pulse or reverse mid-shot
- Emotional: Surrealism, madness, dream logic, spatial horror
- Best For: Surrealist sequences, nightmares, drug sequences, psychological horror

---

### TECHNICAL IMPLEMENTATION FOR AI GENERATION

**Describing the Effect to Image Models:**
Since AI image generators produce single frames, describe the dolly zoom as a "key frame" from the middle of the movement:
- "Wide-angle frame from dolly zoom sequence showing spatial distortion"
- "Background stretched and expanded due to contra-zoom effect"
- "Subject constant size but environment warped around them"
- "Perspective lines converging unnaturally due to simultaneous dolly and zoom"

**Describing the Effect to Video Models:**
For LTX or Wan video generation, describe the full motion:
- "Camera pushes forward while zooming out, background expands away"
- "Spatial distortion as perspective compresses while subject stays same size"
- "Vertigo effect — world stretching behind character"

**Common Pitfalls:**
- AI often renders the subject changing size instead of background — specify "subject constant size"
- Background expansion can look like simple wide-angle distortion — mention "unnatural spatial warping"
- The effect requires clear perspective lines to read — include "architectural lines", "road", "corridor", or "receding space"

---

### EXAMPLE PROMPTS

**Classic Vertigo Tower:**
> Dolly zoom cinematography key frame, subject standing at edge of high tower looking down with expression of existential dread, camera having pushed forward while zooming out from 100mm to 24mm, subject maintaining constant frame size but spiral staircase below appearing to stretch and expand impossibly away, spatial distortion making vertical space seem infinite, perspective lines warping unnaturally, Hitchcock Vertigo effect, cinematic psychological disorientation, dramatic low-angle on subject

**Jaws Beach Realization:**
> Dolly zoom cinematography, medium shot of woman on beach suddenly realizing danger, camera pushing forward while zooming out from 85mm to 35mm over 2 seconds, subject face constant size but beach and ocean horizon violently stretching away behind her, background expanding with spatial distortion, sudden mortal terror expression, summer afternoon light becoming sickly, cinematic shock effect, Spielberg Jaws reference

**Reverse Room Compression:**
> Reverse dolly zoom cinematography, man sitting alone in sparse apartment, camera pulling back while zooming in from 35mm to 85mm, subject maintaining constant frame size but walls and ceiling appearing to compress and crash inward, room becoming claustrophobically small, perspective crushing effect, creeping paranoia, isolation spatial distortion, slow psychological horror, cinematic entrapment aesthetic

---

### TECHNICAL NOTES FOR AI GENERATION
- Always specify "subject maintains constant size" to prevent AI from simply zooming
- Include clear perspective lines (roads, corridors, architectural edges) for the distortion to read
- Reference "Vertigo effect" or "dolly zoom" explicitly as style signal
- For FLUX: describe as "frame from dolly zoom sequence showing spatial warping"
- For LTX: describe the full camera motion — "camera pushes in while zooming out"
- The effect works best with subjects at medium distance from camera
- Background depth is essential — flat backgrounds show no distortion
- Combine with character expression of shock/dread/realization for maximum impact
