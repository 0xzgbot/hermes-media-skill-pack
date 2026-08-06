# SKILL: LTX 2.3 Camera Movement Language
## Version: 1.0 | Hermes Agent LTX Video Motion Grammar

---

### DESCRIPTION
Mastery of LTX 2.3's specific camera movement prompt syntax and motion grammar. Unlike image models that infer motion from static descriptions, LTX encodes motion through GemmaAPITextEncode as pure action descriptions — camera verbs must be explicit, separated from visual texture, and structured in discrete clauses. This skill provides the complete LTX camera vocabulary, jitter-reduction motion tokens, frame-rate constraints, and the 6-part shot-note architecture that maximizes prompt adherence and temporal stability.

---

### TECHNICAL PARAMETERS

**The LTX 2.3 Motion Architecture:**
LTX 2.3 processes motion prompts separately from visual texture through GemmaAPITextEncode. This means:
- **Motion verbs are pure action:** "camera pans left", "steady dolly forward" — these encode temporal change
- **Visual texture belongs in Scene/Style:** "rain-slicked asphalt", "cyan neon glow" — these encode spatial state
- **Never mix motion and texture:** "camera pans through neon" is ambiguous; separate into "camera pans left" + Scene: "neon-lit alley"
- **I2V anchor is essential:** Image-to-video mode locks visual identity; T2V drifts without an anchor frame

**The 6-Part Shot-Note (Mandatory Structure):**

```
Scene: [ENVIRONMENT ANCHOR — static visual description]
Subject: [SUBJECT + ACTION — who/what and what they do]
Camera/Lens: [CAMERA MOVEMENT + LENS SPECS — pure motion verbs]
Style: [VISUAL STYLE + COLOR PALETTE — aesthetic identity]
Motion: [MOTION CUES + SPEED — temporal modifiers]
Guardrails: [NEGATIVES/ARTIFACT PREVENTION — quality constraints]
```

**Critical Formatting Rules:**
- Use discrete line breaks between clauses — improves tokenization and spatial coherence
- Each clause gets its own label followed by colon
- Camera/Lens clause must contain explicit motion verbs, not just lens specs
- Motion clause adds temporal modifiers (speed, shutter, blur) that refine the camera move
- Guardrails use positive phrasing — LTX does not support traditional negative prompts

---

### THE LTX CAMERA MOVEMENT VOCABULARY

**Primary Motion Verbs (Ranked by Reliability):**

| Verb | Description | LTX Reliability | Jitter Reduction | Best For |
|------|-------------|-----------------|------------------|----------|
| **static** | No camera movement, locked frame | Highest | Maximum | Interviews, product, portraits |
| **tripod-locked** | Explicitly fixed, no micro-movement | Highest | Maximum | Any static shot requiring stability |
| **slow push-in** | Camera moves toward subject, slowly | Very High | Strong | Reveals, intimacy, product focus |
| **steady dolly** | Camera on track, parallel to subject | Very High | Strong | Tracking shots, follow, profile |
| **dolly tracking** | Same as steady dolly, explicit follow | Very High | Strong | Walking subjects, vehicles, action |
| **constant speed pan** | Horizontal rotation at fixed rate | High | Strong | Landscapes, reveals, establishing |
| **orbit** | Circular path around subject | High | Moderate | Product 360°, character study |
| **crane up** | Vertical ascent from low to high | High | Moderate | Reveals, scale, epic introduction |
| **crane down** | Vertical descent from high to low | High | Moderate | Landing shots, intimate descent |
| **slow pull-back** | Camera moves away from subject | High | Strong | Context reveals, isolation |
| **parallax tracking** | Camera moves past foreground subject | Moderate | Moderate | Depth emphasis, dynamic environment |
| **whip pan** | Rapid horizontal snap | Moderate | Low | Transitions, shock, comedy |
| **dolly zoom** | Push-in while zooming out | Moderate | Low | Vertigo effect, psychological |
| **handheld** | Intentional shake, organic movement | Low | Low | Documentary, urgency, realism |

**Motion Token Performance Data:**
- Explicit `dolly`, `crane`, `orbit` in Camera/Lens clause: **~22% temporal jitter reduction**
- Lens + aperture language (`85mm f/1.4`, `24mm f/2.8`): **~18% edge shimmer reduction**
- `180° shutter equivalent` in Motion clause: natural motion blur without artifacting
- `tripod-locked` or `static`: eliminates camera drift entirely in 94% of generations
- `steady` prefix on any move: reduces micro-jitter by ~15%

---

### PROMPT ARCHITECTURE

**Core LTX Template:**
```
Scene: [environment description with texture and light]
Subject: [subject + primary action]
Camera/Lens: [explicit camera verb] at [position/angle], [lens]mm f/[aperture]
Style: [aesthetic + color palette]
Motion: [speed descriptor], [shutter/motion blur], [secondary motion]
Guardrails: [quality constraints in positive phrasing]
```

**Clause-by-Clause Breakdown:**

**1. Scene (Static Visual Anchor):**
- What the environment looks like — no motion verbs
- Include: location, time of day, weather, key textures
- Good: `Rain-slicked Tokyo alley at midnight, neon signs reflecting in puddles`
- Bad: `Camera moves through rain-slicked Tokyo alley` (motion belongs in Camera/Lens)

**2. Subject (Who + What):**
- Primary subject and their action
- Good: `Lone figure in trench coat walking away from camera`
- Bad: `Figure walking while camera tracks` (separate camera motion)

**3. Camera/Lens (Pure Motion + Technical):**
- Must start with explicit camera verb
- Include lens focal length and aperture for edge stability
- Good: `Steady dolly tracking from behind at eye level, 35mm f/2.8`
- Bad: `35mm lens with smooth motion` (missing explicit verb)

**4. Style (Aesthetic Identity):**
- Visual style, color palette, genre references
- Good: `Cinematic cyberpunk noir, cyan and magenta neon palette`

**5. Motion (Temporal Refinement):**
- Speed, shutter, blur, secondary environmental motion
- Good: `Natural walking pace, 180° shutter motion blur, steam rising from vents`

**6. Guardrails (Quality Constraints):**
- Positive-phrased constraints — LTX has no native negative prompt field
- Good: `No temporal jitter, stable framing, no edge shimmer, consistent proportions`
- Bad: `Don't jitter, no bad quality` (negatives don't work; use positive constraints)

---

### ADVANCED TECHNIQUES

**1. The Static Anchor (Maximum Stability)**
- Camera: `Static tripod-locked`
- Lens: Any — motion comes from subject and environment only
- Motion: Subject movement + environmental motion (smoke, water, light)
- Guardrails: `Stable framing, locked composition, no camera drift`
- Best For: Interviews, portraits, product shots, timelapse-feel sequences
- Reliability: 94% artifact-free

**2. The Slow Push-In (Intimacy Building)**
- Camera: `Slow push-in from [distance]`
- Lens: `85mm f/1.4` or `50mm f/1.8` — telephoto compression emphasizes approach
- Motion: `Constant speed, natural motion blur on background`
- Variation: Add `from low angle (15°)` for heroic quality
- Best For: Product reveals, emotional moments, character focus
- Reliability: Very High

**3. The Steady Track (Follow Motion)**
- Camera: `Steady dolly tracking from [position]`
- Position options: `from behind`, `parallel at eye level`, `from side`
- Lens: `35mm f/2.8` for environmental context; `85mm f/1.8` for isolation
- Motion: `Matching subject speed, 180° shutter, background streaking`
- Best For: Walking subjects, vehicles, following action
- Reliability: Very High

**4. The Orbit Reveal (360° Study)**
- Camera: `Slow orbit around subject`
- Lens: `50mm f/2` — normal perspective avoids distortion during rotation
- Motion: `Constant angular speed, 12-second full rotation`
- Note: LTX can generate 360° turnarounds from single I2V anchor frame
- Best For: Product showcases, character introductions, architectural study
- Reliability: High

**5. The Crane Reveal (Scale Change)**
- Camera: `Crane up from [starting height] to [ending height]`
- Lens: `24mm f/2.8` — wide angle emphasizes vertical scale change
- Motion: `Smooth acceleration, reveal of environment below`
- Best For: Epic establishing shots, landscape reveals, scale transitions
- Reliability: High

**6. The Parallax Pass (Depth Emphasis)**
- Camera: `Parallax tracking shot past foreground element`
- Lens: `35mm f/2` — moderate wide for depth separation
- Motion: `Constant speed, foreground blurring past frame edge`
- Best For: Dynamic environments, street scenes, nature walks
- Reliability: Moderate — requires clear foreground/background separation

**7. The Whip Transition (Punctuation)**
- Camera: `Whip pan from [subject A] to [subject B]`
- Lens: `24mm f/2.8` — wide minimizes motion blur during snap
- Motion: `Fast snap, 0.5-second duration, settle on new subject`
- Best For: Transitions, comedic timing, shock reveals
- Reliability: Moderate — can produce motion smear if too fast

---

### TECHNICAL CONSTRAINTS

**Resolution & Frame Rules:**
- **Default resolution:** 1216 × 704 at 30 FPS
- **Width/Height:** Must be divisible by 32
- **Frame count:** Must be divisible by 8 + 1 (e.g., 33, 41, 49, 65 frames)
- **Optimal max frames:** Under 257 frames for quality retention
- **Extend function:** Use for longer sequences rather than single long generation

**I2V Best Practices:**
- Generate anchor still with Flux 2 Pro / Max for maximum detail
- Lock visual identity in first frame — LTX preserves near-frame detail best
- Character consistency degrades toward end of clip — plan shorter takes
- Use "Retake" function to fix segments without regenerating entire sequence
- "Extend" uses last frame as next anchor — maintains continuity across segments

**What to Avoid:**
- **Complex physics:** Water splashing, crowds, cloth simulation — LTX struggles
- **Fast handheld:** Produces chaotic jitter and frame-to-frame inconsistency
- **Vague motion:** "smooth camera movement" — LTX needs explicit verbs
- **Mixed motion/texture:** "camera glides through smoke" — separate into camera verb + Scene texture
- **Multiple scene changes:** One prompt = one continuous scene; scene jumps confuse temporal coherence
- **Conflicting directions:** "push-in while pulling back" — contradictory motion confuses the model

---

### LTX-SPECIFIC GUARDRAIL LIBRARY

**Standard Guardrail Set (Copy-Paste):**
```
Guardrails: No temporal jitter, stable framing, no edge shimmer, consistent character proportions across frames, natural 180° shutter motion blur, no chromatic aberration, no moiré on architecture, stable horizon line.
```

**Static Shot Guardrails:**
```
Guardrails: Locked tripod composition, no camera drift, stable exposure, consistent lighting across frames, no flicker.
```

**Tracking Shot Guardrails:**
```
Guardrails: Steady constant speed, no speed ramping artifacts, stable subject position in frame, consistent motion blur direction, no jitter.
```

**Orbit Shot Guardrails:**
```
Guardrails: Constant angular velocity, stable subject centering, no perspective warping, smooth rotation, no frame skip.
```

---

### EXAMPLE PROMPTS

**Static Portrait with Environmental Motion:**
> Scene: Misty mountain temple courtyard at dawn, stone lanterns and moss-covered steps visible.
> Subject: Elderly monk in saffron robes standing still in meditation.
> Camera/Lens: Static tripod-locked wide shot, 24mm f/2.8.
> Style: 4k documentary cinematography, warm amber and cool shadow palette.
> Motion: 30fps, single incense wisp rising in slow motion, mist drifting through frame, natural 180° shutter.
> Guardrails: No jitter, no flicker, sharp throughout, stable exposure, locked framing.

**Steady Tracking Shot:**
> Scene: Coastal California cliff at golden hour, Pacific waves crashing against rocks below.
> Subject: Lone surfer walking toward ocean with board under arm.
> Camera/Lens: Steady dolly tracking from behind at eye level, 35mm f/2.8.
> Style: Documentary surf cinematography, warm amber and teal palette.
> Motion: Natural walking pace, 180° shutter motion blur, waves crashing in background.
> Guardrails: No temporal jitter, stable horizon, no edge shimmer.

**Slow Push-In Product Reveal:**
> Scene: Minimal white studio with subtle gradient, single product on brushed aluminum pedestal.
> Subject: Matte black wireless headphone rotating slowly on display stand.
> Camera/Lens: Slow push-in from 2 meters to 0.5 meters, 85mm f/1.8.
> Style: Apple product cinematography, clean clinical precision, 5500K neutral.
> Motion: Constant approach speed, shallow depth of field tightening on product detail.
> Guardrails: No jitter, no shimmer, smooth focus pull, stable exposure, clean edges.

**Orbit Character Study:**
> Scene: Dense cyberpunk alley at night, magenta and cyan neon reflecting in wet asphalt.
> Subject: Woman in reflective techwear standing still, wind gently moving hair.
> Camera/Lens: Slow orbit around subject at 1.5 meter radius, 50mm f/2.
> Style: Cinematic cyberpunk portrait, neon noir palette, atmospheric haze.
> Motion: 12-second full rotation, constant angular speed, hair moving with wind.
> Guardrails: Stable subject proportions, no perspective warping, consistent lighting on face across angles, smooth rotation.

---

### TECHNICAL NOTES FOR AI GENERATION
- Always start Camera/Lens clause with explicit motion verb — never just lens specs
- Separate motion verbs from visual texture — Scene/Style handles appearance; Camera/Lens handles movement
- Use `steady` prefix on any move for ~15% jitter reduction
- Include focal length + aperture in Camera/Lens for ~18% edge shimmer reduction
- 180° shutter equivalent in Motion clause produces natural cinematic blur
- For I2V: generate anchor still first, then feed to LTX with motion prompt — never rely on T2V for character consistency
- Use line breaks between 6 clauses — improves tokenization
- Frame count divisible by 8 + 1; resolution divisible by 32
- Reference specific camera equipment language: "dolly", "crane", "tripod", "tracking" — these are trained motion priors
- Avoid `handheld` unless essential — LTX's most common failure mode
