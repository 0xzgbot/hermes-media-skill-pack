# SKILL: LTX 2.3 Prompt Engineering Master
## Version: 1.0 | Hermes Agent Universal LTX 2.3 Prompt Optimization Doctrine

---

### DESCRIPTION
The master reference for LTX 2.3 prompt engineering across all video generation modes (T2V, I2V, Audio-to-Video, V2V). This skill distills deep research on LTX 2.3's 22B asymmetric dual-stream DiT architecture, 4x larger text connector, Gemma3-12B text encoder behavior, and native audio-video generation into a single authoritative doctrine. Covers the single-paragraph flow requirement, present-tense mandate, temporal language strategies, prompt-length-to-duration matching, acting direction granularity, and the complete anti-pattern catalog specific to LTX 2.3's motion-aware conditioning.

---

### TECHNICAL PARAMETERS

**LTX 2.3 Architecture & What It Means for Prompting:**
- **Model:** 22B asymmetric dual-stream DiT (14B video + 5B audio + shared conditioning)
- **Text Encoder:** Gemma3-12B with multi-layer feature extraction — dramatically more responsive to prompt detail than LTX 2.0
- **Text Connector:** 4x larger than LTX 2.0 — complex spatial relationships and temporal sequences resolve accurately
- **VAE:** Rebuilt for sharper textures, cleaner edges, better fine detail preservation across frames
- **Modes:** T2V, I2V, Audio-to-Video, Video-to-Video, Extend, Retake
- **Output:** Up to 4K (2160p), 24/25/30/48/50 FPS, up to 20-second clips
- **Inference:** Fast Flow (8 steps, distilled, CFG 1.0) vs. Pro Flow (50+ steps, dev, CFG 3.0–7.0)

**The Single-Paragraph Mandate:**
LTX 2.3's Gemma3 encoder processes prompts as flowing narrative paragraphs far better than fragmented bullet points or keyword lists.

| Format | Result | Why |
|--------|--------|-----|
| **Single flowing paragraph** | ✅ Coherent motion, consistent style, natural pacing | Gemma3 processes narrative continuity as temporal sequence |
| **Bullet points** | ❌ Disjointed motion, jarring transitions, confused style | Breaks temporal flow; model treats each bullet as separate scene |
| **Keyword soup** | ❌ Arbitrary output, ignored details, generic results | LTX understands natural language, not tag lists |
| **Numbered steps** | ❌ Staccato pacing, mechanical motion | Creates artificial beat structure |

**The Present-Tense Requirement:**
Always use present tense for action and movement. Past/future tense confuses the temporal conditioning.

| Tense | Example | Result |
|-------|---------|--------|
| ✅ Present | "She walks toward the door, pauses, then turns back" | Clear temporal sequence, natural motion |
| ❌ Past | "She walked toward the door and paused" | Motion appears completed before clip starts |
| ❌ Future | "She will walk toward the door" | Motion deferred, static or absent frames |
| ❌ Imperative | "Walk toward the door" | No subject anchoring, ambiguous execution |

**Prompt-Length-to-Duration Matching (Critical):**
LTX 2.3's 4x larger text connector means longer prompts consistently outperform short ones — BUT the prompt must match the clip duration.

| Duration | Minimum Prompt Length | Recommended Length | Risk of Under-Prompting |
|----------|----------------------|-------------------|------------------------|
| **2–3 seconds** | 20 words | 30–50 words | Low — short duration needs less direction |
| **4–5 seconds** | 40 words | 60–80 words | Moderate — action may complete too quickly |
| **8–10 seconds** | 70 words | 90–120 words | **High** — short prompts = rushed/muddled action |
| **15–20 seconds** | 100 words | 130–180 words | **Critical** — insufficient direction = temporal drift |

**The Temporal Language Toolkit:**
Time words help LTX 2.3 plan motion chronologically across frames.

| Temporal Word | Effect | Example |
|--------------|--------|---------|
| **"slowly"** | Reduces motion speed, extends action duration | "The camera slowly pushes in" |
| **"gradually"** | Progressive change over time | "Gradually, the fog lifts" |
| **"suddenly"** | Abrupt transition, shock moment | "She suddenly turns toward the window" |
| **"continues"** | Sustains action across remaining frames | "He continues speaking as the camera tracks" |
| **"then"** | Sequential action chaining | "She looks down, then meets his gaze" |
| **"meanwhile"** | Parallel action streams | "Meanwhile, traffic flows beneath the bridge" |
| **"pause"** | Brief motion hold | "He pauses, breath visible in cold air" |
| **"finally"** | Closing action, narrative resolution | "Finally, the sun breaks through clouds" |

**The Six Essential Elements (In Order):**
Every strong LTX 2.3 prompt contains these six elements in this priority order:

1. **Establish the Shot** — shot scale, framing, camera position
2. **Set the Scene** — lighting, color palette, atmosphere, textures
3. **Describe the Action** — core motion as natural sequence, beginning to end
4. **Define the Character(s)** — age, clothing, distinguishing features, physical cues
5. **Identify Camera Movement** — explicit motion verbs, speed, direction
6. **Describe the Audio** — ambient sound, music, speech, acoustic environment

---

### PROMPT ARCHITECTURE

**Universal LTX 2.3 Template (Single Flowing Paragraph):**
```
[Shot type] of [subject], [subject description including age/clothing/features].
[Subject] [primary action in present tense], [environment description with lighting and atmosphere].
[Secondary action or environmental motion continues in parallel].
Camera [explicit motion verb] [direction/speed], [lens and aperture if specified].
[Lighting quality and color temperature], [specific atmospheric effects].
[Audio description: ambient sounds, music mood, or speech characteristics].
[Style reference or film stock if applicable].
```

**I2V Prompt Adaptation:**
When using Image-to-Video, the prompt structure changes — static elements are already locked in the anchor image.

```
[Motion focus]: What happens NEXT from the still frame — transition from stillness to motion.
[Camera motion]: How the camera moves relative to the anchored subject.
[Environmental motion]: What moves in the scene independently of the subject.
[Audio]: Sounds that emerge as motion begins.
[Guardrails]: Quality constraints, what to preserve from the anchor.
```

**I2V Critical Rule:** Do NOT describe static visual elements already visible in the anchor image. Focus exclusively on motion, transition, and temporal change.

**Audio-to-Video Prompt Structure:**
```
[Visual interpretation of audio]: What scenes and motion accompany the soundtrack.
[Subject]: Who/what performs or responds to the audio.
[Camera]: Movement synchronized to audio rhythm, energy, or beat.
[Lighting]: Visual mood matching audio emotional arc.
[Environment]: Acoustic space described visually (reverb = large space, dry = intimate).
```

**Guardrails (Positive-Only Quality Constraints):**
```
stable temporal coherence, consistent lighting across frames, natural motion blur,
no temporal jitter, no edge shimmer, stable framing, consistent character proportions,
realistic physics, smooth camera movement, coherent environmental motion
```

---

### ADVANCED TECHNIQUES

**1. The Acting Beat Breakdown**
- Principle: LTX 2.3's redesigned text connector enables granular acting direction.
- Technique: Break performance into micro-beats with physical cues between dialogue segments.
- Example: "A middle-aged man with greying hair speaks in a sad, slow-paced voice, 'I remember after you kids came along...' He pauses and looks to the side, then continues, 'your mom...' His eyes widen momentarily. He finishes with a cracking voice, 'said something to me I never quite understood.' The camera slowly zooms into his face."
- Why it works: Physical cues (looks to side, eyes widen) translate more reliably than emotional labels ("he feels sad").
- Best For: Dialogue scenes, emotional monologues, narrative storytelling

**2. The Motion Sequence Chronicle**
- Principle: Describe action as a chronological sequence from beginning to end, not a static scene.
- Technique: Use "then," "meanwhile," "finally" to structure temporal progression.
- Example: "A young woman in a red coat walks briskly through a rain-soaked Tokyo street at night. Neon signs reflect in puddles at her feet. She stops at a crosswalk, checks her phone, then continues walking as the light changes. The camera tracks her from behind at a steady pace."
- Why it works: LTX 2.3 plans motion across the full duration. A complete sequence prevents the model from repeating a single gesture.
- Best For: Walking sequences, procedural actions, narrative progression

**3. The Detail-to-Scale Matching**
- Principle: Close-ups need more detail than wide shots — match prompt granularity to shot scale.
- Technique: For close-ups, describe facial features, fabric texture, micro-expressions. For wide shots, describe environment, spatial relationships, atmospheric effects.
- Comparison:
  - Close-up: "Extreme close-up of her eyes. Tears well in the lower lid. Her gaze shifts slightly left. The catchlight from a window moves across her iris as she blinks slowly."
  - Wide shot: "Wide establishing shot of a coastal village at dawn. Fishing boats dot the harbor. Smoke rises from chimneys. Mountains loom in the background mist."
- Why it works: LTX 2.3 allocates detail budget across the frame. Directing detail to the appropriate scale prevents blur in critical areas.
- Best For: Shot-reverse-shot dialogue, product reveals, environmental storytelling

**4. The Environmental Motion Layer**
- Principle: Static subjects come alive when environmental elements move around them.
- Technique: Add parallel motion streams that don't depend on the primary subject.
- Example: "She stands motionless on the platform. Meanwhile, steam from the train swirls around her ankles. A newspaper page tumbles past. In the background, pigeons take flight."
- Why it works: Creates temporal depth and realism even when the primary subject is still. Prevents "frozen frame" feeling.
- Best For: Portraits, product shots, contemplative moments, interview framing

**5. The Audio Anchor Method**
- Principle: For audio-to-video, the audio drives temporal structure; the prompt provides visual interpretation.
- Technique: Describe the visual translation of sonic elements.
- Example (for upbeat electronic music): "A dancer moves with sharp, staccato energy matching the beat. Each kick drum hit coincides with a quick head movement. The lighting pulses in sync with the bass, alternating between cyan and magenta."
- Example (for spoken word): "A poet stands at a microphone in a dimly lit café. Their gestures are slow and deliberate, matching the measured pace of their speech. The audience is visible in soft focus, heads nodding gently."
- Why it works: LTX 2.3's dual-stream architecture processes audio and video together. Explicit audio-visual mapping improves synchronization.
- Best For: Music videos, lip-sync content, ASMR, spoken word, podcasts

**6. The I2V Motion Extension**
- Principle: The anchor image defines the starting state; the prompt must describe the transition FROM that state.
- Technique: Begin prompts with "From this still moment..." or "As motion begins..."
- Example: "From this still portrait, the subject begins to smile slowly. The smile reaches their eyes. They tilt their head slightly. Hair moves gently as if from a passing breeze."
- Why it works: Anchors the prompt to the image's frozen moment and defines the trajectory of change.
- Best For: Portrait animation, product reveals, landscape time-lapses from a single frame

**7. The Style Lock with Motion**
- Principle: Style references must be paired with motion-appropriate descriptors.
- Technique: Choose style references that include inherent motion qualities.
- Examples:
  - "Wes Anderson symmetry" → motion should be "precise, deliberate, dolly tracking at constant speed"
  - "Documentary handheld" → motion should be "organic breathing movement, slight reframing, authentic urgency"
  - "Noir cinematography" → motion should be "slow deliberate camera, deep shadows moving across faces"
- Why it works: Style and motion are inseparable in video. Mismatched style/motion pairs produce uncanny results.
- Best For: Genre-specific content, branded video styles, aesthetic consistency across campaigns

---

### EXAMPLE PROMPTS

**T2V — Cinematic Dialogue Scene:**
> A medium close-up of a middle-aged man with greying hair sitting in a modest kitchen. Soft morning light enters through lace curtains behind him. He speaks in a sad, slow-paced voice, "I remember after you kids came along..." He pauses and looks to the side, his eyes catching the light. Then he continues, "your mom..." His eyes widen momentarily, a flicker of memory crossing his face. He finishes with a cracking voice, "said something to me I never quite understood." The camera slowly zooms into his face as he speaks. The audio is crisp with faint room tone. 35mm film look with fine grain and soft highlight roll-off.

**I2V — Portrait Coming to Life:**
> From this still portrait, the woman begins to breathe slowly, her chest rising and falling with natural rhythm. Her eyes blink once, then focus softly on something beyond the camera. A gentle smile forms gradually, reaching the corners of her eyes. Her hair moves subtly as if from a soft breeze passing through the room. The camera remains static, locked on her face, while natural daylight from the window shifts slightly across her cheek. Preserve facial identity, natural skin texture, and eye color from the anchor frame.

**Audio-to-Video — Music Visualizer:**
> A lone dancer in an industrial warehouse moves with sharp, staccato energy that matches the driving electronic beat. Each kick drum hit coincides with a quick angular arm movement. The lighting pulses in sync with the bass, alternating between deep cyan and hot magenta. Dust particles in the air catch the light with each pulse. The camera orbits slowly around the dancer at constant speed, 24mm wide angle emphasizing the warehouse scale. Concrete walls reflect colored light. The dancer's silhouette is sharp against the pulsing background. Underground rave atmosphere, raw and unpolished.

---

### TECHNICAL NOTES FOR AI GENERATION
- **Always write as a single flowing paragraph** — never bullet points, numbered lists, or fragmented descriptions. Gemma3 processes narrative flow as temporal sequence.
- **Always use present tense** — past/future tense breaks temporal coherence and produces static or deferred motion.
- **Match prompt length to clip duration** — a 10-word prompt for a 10-second video results in rushed, muddled, or looping action. Longer clips need proportionally longer prompts.
- **Lead with the main subject and action** — Gemma3 weights early tokens heavily. "A young woman walks" outperforms "In a beautiful city, a young woman..."
- **Describe action as sequence, not static scene** — "She walks, stops, looks back" outperforms "A woman in a walking pose."
- **Use explicit camera verbs** — "slow dolly in," "steady tracking shot," "static tripod-locked" — LTX 2.3 has trained motion priors for specific cinematographic language.
- **Express emotion through physical cues** — "His jaw tightens, fists clench" outperforms "He is angry." Internal emotional states are invisible to the camera.
- **Include audio descriptions** — LTX 2.3 generates synchronized audio in one pass. Describing sound improves both audio quality and audio-visual alignment.
- **Use temporal language** — "slowly," "then," "meanwhile," "gradually," "suddenly" — these words structure the motion timeline for the model.
- **For I2V: focus on motion, not appearance** — The anchor image locks visuals. Describe what happens NEXT, not what things look like.
- **For Audio-to-Video: map sound to visuals** — Describe how the audio should be visually interpreted: rhythm → motion, tone → lighting, reverb → space.
- **Avoid numerical precision** — "Exactly 3 birds flying at 45 degrees" confuses the model. Use natural language: "Several birds fly across the sky from left to right."
- **Avoid conflicting directions** — "A still lake with dramatic waves crashing" produces muddy results. Choose one scenario and describe it thoroughly.
- **Limit texture complexity** — High-frequency patterns (fine stripes, dense grids) cause moiré in ~30% of generations. Use solid colors or large-scale patterns.
- **Avoid text and logos** — Readable text in video is not currently reliable in LTX 2.3.
- **Iterate systematically** — Change ONE variable at a time (action, camera, lighting) to understand what each modification does.
- **Use Fast Flow for exploration, Pro Flow for final** — Fast Flow (8 steps) enables rapid iteration. Lock the prompt, then render with Pro Flow (50+ steps) for production.
