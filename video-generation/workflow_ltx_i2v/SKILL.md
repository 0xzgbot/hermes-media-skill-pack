# SKILL: LTX 2.3 Image-to-Video Workflow Master
## Version: 1.0 | Hermes Agent LTX I2V Pipeline & Anchor Strategy Specialist

---

### DESCRIPTION
Comprehensive workflow doctrine for LTX 2.3 Image-to-Video (I2V) generation — the most reliable method for visual consistency in AI video production. This skill encodes the anchor image requirements, prompt adaptation rules for I2V mode, the motion-from-still transition grammar, ComfyUI node architecture, and multi-shot continuity strategies required to transform FLUX 2 still frames into temporally coherent video sequences. Covers anchor quality thresholds, the I2V prompt subtraction principle, latent injection mechanics, and the shot-to-shot handoff protocol for narrative sequences.

---

### TECHNICAL PARAMETERS

**Why I2V Beats T2V for Consistency:**
- **T2V Limitation:** LTX 2.3 generates the first frame from text. Visual identity can vary significantly from the intended look.
- **I2V Advantage:** The first frame is locked to a high-quality reference image. The model animates FROM that exact visual state rather than generating it.
- **Consistency Spectrum:** T2V character drift: 40–60% across frames. I2V with good anchor: 85–92% across frames. I2V + ID-LoRA: 95%+.
- **Temporal Degradation:** Even I2V consistency weakens toward the end of longer clips. Plan shorter takes (under 5 seconds) for critical identity shots.

**The Anchor Image Quality Threshold:**

| Quality Level | Source | Resolution | Detail | I2V Result |
|--------------|--------|-----------|--------|------------|
| **Maximum** | FLUX 2 Pro/Max | 1536×1536+ | Full skin texture, fabric weave, environmental clarity | Best possible fidelity and consistency |
| **High** | FLUX 2 Dev | 1024×1024 | Good detail, slight softness acceptable | Excellent results for most productions |
| **Medium** | SDXL / Other | 1024×1024 | Adequate detail, some texture loss | Acceptable for background/environment shots |
| **Low** | Compressed JPEG / Small | < 1024 | Blurry, artifacted, low detail | Poor — model amplifies artifacts in motion |
| **Unacceptable** | Upscaled from thumbnail | Any | Artificial sharpening, block artifacts | Do not use — produces unstable, warped motion |

**Anchor Composition Rules:**
- **Resolution:** Match or exceed target video resolution. Downscaling preserves detail; upscaling introduces artifacts.
- **Composition:** Leave negative space in the direction of intended camera motion. If camera pushes in, subject should not fill frame. If camera tracks left, leave space on left edge.
- **Focus:** Sharp focus on primary subject. Slight background blur is acceptable and can enhance motion separation.
- **Lighting:** Even, modeled lighting with clear direction. Flat lighting reduces dimensional cues for motion.
- **No Text/Logos:** Anchor images with text often produce warped text in motion. Remove or avoid text in anchor frames.

**The I2V Prompt Subtraction Principle:**
Unlike T2V, I2V prompts must NOT describe static visual elements already present in the anchor image.

| Element | T2V Prompt | I2V Prompt (Correct) | I2V Prompt (Wrong) |
|---------|-----------|---------------------|-------------------|
| Subject appearance | "Woman with red hair in a leather jacket" | (Omitted — locked by image) | "Woman with red hair in a leather jacket" |
| Environment | "Rainy Tokyo street at night" | (Omitted — locked by image) | "Rainy Tokyo street at night" |
| Lighting | "Neon reflections in puddles" | (Omitted — locked by image) | "Neon reflections in puddles" |
| Motion | — | "She walks forward, hair moving with breeze" | — |
| Camera | — | "Camera tracks behind at steady pace" | — |
| Transition | — | "From stillness, motion begins gradually" | — |
| Audio | — | "Footsteps on wet pavement, distant traffic" | — |

**I2V ComfyUI Node Architecture:**

| Node | Function | Critical Settings |
|------|----------|-------------------|
| **LoadImage** | Loads anchor image | Must be RGB, no alpha channel issues |
| **LTXVImgToVideoInplace** | Injects anchor into video latent | Toggle ON for I2V; OFF for T2V pass-through |
| **LTXVConditioning** | Encodes positive/negative text + frame rate | Frame rate MUST match output fps |
| **Empty Latent** | Allocates video latent dimensions | Width/Height divisible by 32; frames divisible by 8+1 |
| **KSampler + ManualSigmas** | Noise schedule and sampling | Higher early sigma = more motion; lower = less |
| **LTXVLatentUpsampler** | x2 spatial upscale in latent | Apply between low-res and high-res passes |
| **VAEDecodeTiled** | Decodes latent to frames | Mandatory above 1536px; prevents OOM |
| **CreateVideo** | Muxes frames + audio to MP4 | FPS must match conditioning frame rate |

---

### PROMPT ARCHITECTURE

**Core I2V Prompt Template (What Changes, Not What Is):**
```
From this still moment, [subject] begins to [primary action].
[Secondary motion — environmental or subject detail].
The camera [explicit motion verb] [direction/speed/quality].
[Environmental elements that activate — wind, light shift, particles].
[Audio that emerges as motion begins].
[Motion quality — speed, shutter, blur characteristics].
[Guardrails — what to preserve, what to avoid].
```

**The Motion Activation Phrases:**
These phrases help LTX 2.3 transition from the frozen anchor state into natural motion:

| Phrase | Effect | Best For |
|--------|--------|----------|
| "From this still moment..." | Gentle activation, gradual motion onset | Portraits, contemplative scenes |
| "As motion begins..." | Clear transition point | Product reveals, dramatic entrances |
| "Gradually coming to life..." | Slow build, organic activation | Nature, environmental time-lapses |
| "Frozen frame animates..." | Direct instruction to model | Technical demonstrations |
| "The scene awakens..." | Environmental motion emphasis | Landscapes, cityscapes, atmospheric |
| "Stillness gives way to..." | Narrative transition | Story sequences, emotional arcs |

**Multi-Shot I2V Continuity Protocol:**
For sequences requiring multiple shots with the same subject:

```
Shot 1:
- Anchor: FLUX 2 generated still (Subject in Opening Pose A)
- I2V: Motion A (e.g., "slow push-in as subject begins to speak")
- Output: Video segment A, final frame captured

Shot 2:
- Anchor: Final frame of Shot 1 (Subject in End Pose A = Opening Pose B)
- I2V: Motion B (e.g., "subject continues speaking, slight head turn")
- Output: Video segment B

Shot N:
- Anchor: Final frame of Shot N-1
- I2V: Motion N
- Output: Final segment

Assembly: Concatenate segments in edit; transitions are seamless because end frame = start frame
```

**Guardrails (I2V-Specific):**
```
preserve exact facial identity from anchor, maintain consistent skin texture,
no morphing of anchor features, stable color palette from source image,
natural motion onset from still state, no sudden jumps or warps,
consistent lighting direction from anchor, preserve anchor composition proportions
```

---

### ADVANCED TECHNIQUES

**1. The Portrait Animation Anchor**
- Setup: FLUX 2 portrait → subtle life animation
- Anchor Requirements: High-detail face, neutral or near-neutral expression, good catchlights in eyes, shoulders visible
- I2V Prompt: "From this still portrait, the subject begins to breathe slowly, chest rising and falling with natural rhythm. Their eyes blink once, then focus softly. A gentle smile forms gradually. Hair moves subtly as if from a passing breeze. The camera remains static, locked on their face."
- Key: Minimal motion preserves identity best. Extreme motion causes drift.
- Best For: Portrait social content, memorial videos, "living photo" effects

**2. The Product Reveal From Still**
- Setup: FLUX 2 product hero shot → camera motion reveal
- Anchor Requirements: Product centered, clean background, sharp detail, room for camera approach
- I2V Prompt: "As motion begins from this product shot, the camera slowly pushes in toward the product, shallow depth of field tightening on surface detail. A subtle light sweep crosses the product from left to right, highlighting texture. Steam or mist rises gently in the background."
- Key: Camera motion does the work; product stays locked in place.
- Best For: E-commerce videos, product launches, commercial hero shots

**3. The Landscape Time-Lapse From Frame**
- Setup: FLUX 2 landscape still → environmental motion
- Anchor Requirements: Wide composition, clear sky area, visible landscape elements
- I2V Prompt: "From this frozen landscape, clouds begin to drift slowly across the sky. Light shifts gradually as the sun moves, casting longer shadows across the terrain. Mist in the valley begins to lift and swirl. The camera remains static, capturing the passage of time."
- Key: Environmental motion (clouds, light, mist) is highly reliable in I2V.
- Best For: Nature documentaries, travel content, meditation videos

**4. The Character Walk Cycle From Pose**
- Setup: FLUX 2 character in mid-stride → continuous walking
- Anchor Requirements: Full body visible, one foot forward (clear gait pose), arms in natural position
- I2V Prompt: "From this walking pose, the subject continues forward with a steady, confident stride. Arms swing naturally with each step. Hair moves with the rhythm of the gait. The camera tracks smoothly from the side, maintaining the subject in the same frame position."
- Key: Starting from an active pose (not standing still) creates more natural motion continuation.
- Best For: Fashion lookbooks, character introductions, game cinematics

**5. The Talking Head With Lip Sync**
- Setup: FLUX 2 portrait → speaking animation with audio
- Anchor Requirements: Face filling 30–40% of frame, mouth in neutral closed position, good lighting on face
- Additional: Reference audio clip (5 sec, clean voice) + ID-LoRA for identity
- I2V Prompt: "[VISUAL] From this portrait, the subject begins to speak. Natural lip movement synchronized to voice. Subtle head movements and micro-expressions accompany the speech. Eyes blink at natural intervals. [SPEECH] 'Exact dialogue words in quotes.' [SOUNDS] Voice quality description."
- Key: Neutral mouth position in anchor produces best lip-sync results.
- Best For: Spokesperson videos, educational content, personalized messages

**6. The Multi-Angle Character Study**
- Setup: Single FLUX 2 portrait → 360° orbit reveal
- Anchor Requirements: Centered subject, full body or 3/4 visible, neutral background preferred
- I2V Prompt: "From this static pose, the camera begins a slow orbit around the subject at constant angular speed. The subject remains in the same pose as the perspective shifts, revealing their silhouette from all angles. Lighting remains consistent, wrapping around the form as the camera moves."
- Key: Subject stays frozen while camera moves — highest consistency method.
- Best For: Character design presentations, fashion turntables, product 360°

**7. The Narrative Shot Handoff**
- Setup: Multiple I2V shots sequenced into a narrative
- Shot 1 Anchor: FLUX 2 still of Subject A at Window, looking out
- Shot 1 Motion: "Subject A turns from window, walks toward door"
- Shot 2 Anchor: Final frame of Shot 1 (Subject A at door, hand on handle)
- Shot 2 Motion: "Subject A opens door, steps through, door closes behind"
- Shot 3 Anchor: Final frame of Shot 2 (closed door, empty room)
- Shot 3 Motion: "Camera holds on empty room, dust particles in light, silence"
- Assembly: Simple cuts between segments; continuity guaranteed by frame matching
- Key: Each shot's motion should end at a natural pause point for clean handoff.
- Best For: Short films, narrative sequences, scripted content

---

### EXAMPLE PROMPTS

**Portrait Coming to Life (I2V):**
> From this still portrait, the woman begins to breathe slowly, her chest rising and falling with natural rhythm. Her eyes flutter open, then focus softly on something beyond the camera. A gentle, genuine smile forms gradually, reaching the corners of her eyes. Her hair moves subtly as if from a soft breeze passing through the room. The camera remains static, locked on her face, while natural daylight from the window shifts slightly across her cheek. Preserve exact facial identity, natural skin texture, and eye color from the anchor frame.

**Product Hero Reveal (I2V):**
> As motion begins from this product shot, the camera slowly pushes in toward the matte black headphones, shallow depth of field tightening on the ear cup surface detail. A subtle warm light sweep crosses the product from left to right, highlighting the brushed titanium finish. A wisp of steam rises gently in the dark background. The product rotates slowly on its invisible axis, revealing the cushioned headband. The camera movement is smooth and deliberate, luxury commercial cinematography.

**Landscape Time-Lapse (I2V):**
> From this frozen mountain landscape at dawn, clouds begin to drift slowly across the pink and orange sky. Light shifts gradually as the sun rises higher, casting longer shadows across the snow-covered peaks. Mist in the valley below begins to lift and swirl in gentle eddies. Pine trees in the foreground sway slightly with a passing breeze. The camera remains static on a tripod, capturing the serene passage of time, documentary nature cinematography.

**Multi-Shot Narrative Handoff (Shot 1 of 3):**
> From this still frame of the woman standing at the rain-streaked window, she slowly turns away from the glass. Her reflection fades from the window surface. She walks with measured steps across the wooden floor toward the door. Her coat sways slightly with each step. The camera tracks her movement from a static position, maintaining medium framing. She reaches the door and places her hand on the handle, pausing for a moment before the scene ends.

---

### TECHNICAL NOTES FOR AI GENERATION
- **The anchor image is 60% of the I2V result quality** — invest maximum effort in FLUX 2 anchor generation. A mediocre anchor cannot be saved by good motion prompting.
- **Never redescribe static elements in I2V prompts** — "She has red hair" when the anchor already shows red hair wastes tokens and can confuse the model.
- **Focus exclusively on motion, transition, and temporal change** — What happens NEXT from the still frame.
- **Motion activation phrases improve results:** "From this still moment," "As motion begins," "Gradually coming to life" — these signal the model to animate rather than reinterpret.
- **Shorter clips = higher consistency:** Under 5 seconds (65–81 frames) preserves anchor identity best. Beyond 10 seconds, drift increases.
- **Use Extend for longer sequences:** Generate 5-second segments, use the final frame as next anchor, rather than pushing single generation past 121 frames.
- **Final frame capture for multi-shot:** Always save the last frame of each I2V segment — it becomes the anchor for the next shot.
- **Camera motion in I2V is highly reliable:** Orbit, push-in, and tracking all work well because the subject stays locked.
- **Subject motion in I2V requires careful prompting:** "Subject walks" from a standing pose can produce awkward first steps. Starting from an active pose (mid-stride) produces better continuation.
- **Neutral expression anchors work best for dialogue:** A closed-mouth neutral face gives the model maximum range for lip-sync animation.
- **Environmental motion is the safest I2V application:** Clouds, light shifts, water, particles — these animate beautifully from still frames with minimal drift.
- **For ComfyUI:** LTXVImgToVideoInplace must be toggled ON. The node injects the image into the latent at timestep zero. Without it, the workflow runs as T2V.
- **ID-LoRA + I2V + Reference Audio = maximum talking head quality** — this triple-stack produces the most consistent speaking characters in open-source video generation.
- **Color consistency across shots:** When using final-frame handoff, monitor for color temperature drift. If drift occurs, apply a color correction node between segments.
