# SKILL: LTX 2.3 Audio-Visual Integration & Sync
## Version: 1.0 | Hermes Agent LTX Native Audio-Video Synchronization Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for LTX 2.3's groundbreaking native audio-video generation capability — the first open-source model to produce synchronized audio and video in a single diffusion pass. This skill encodes the dual-stream architecture implications, audio conditioning strategies, lip-sync performance direction, sound design vocabulary, and music-to-visual mapping required to leverage LTX 2.3's 5B audio stream alongside its 14B video stream. Covers reference audio conditioning, vocal separation preprocessing, the [VISUAL]/[SPEECH]/[SOUNDS] prompt tag system for ID-LoRA, and ambient sound design for cinematic atmosphere.

---

### TECHNICAL PARAMETERS

**LTX 2.3 Audio-Video Architecture:**
- **Model:** 22B asymmetric dual-stream DiT — 14B video stream + 5B audio stream
- **Connection:** Bidirectional cross-attention layers with shared timestep conditioning
- **Audio Encoder:** Separate audio VAE decodes acoustic latents into waveform
- **Text Encoder:** Gemma3-12B processes text conditioning for both streams simultaneously
- **Vocoder:** Upgraded HiFi-GAN in 2.3 reduces audio artifacts and dropout
- **Audio Modes:** Generated audio from text, reference audio conditioning, audio-to-video sync
- **Key Distinction:** Audio is frame-locked to video via shared latent space — NOT dubbed on afterward

**Audio Generation Quality by Type:**

| Audio Type | Quality | Reliability | Best Practice |
|-----------|---------|------------|---------------|
| **Ambient environmental** | High | Very High | "Rain on pavement," "wind through trees," "distant traffic" |
| **Room tone / silence** | High | High | "Quiet room tone," "soft ambient hum" |
| **Footsteps / Foley** | Moderate | Moderate | "Footsteps on wood floor," "door closing" |
| **Music (atmospheric)** | Moderate | Moderate | "Soft piano melody," "ambient electronic pad" |
| **Speech / dialogue** | Moderate-High | Moderate | Use ID-LoRA + reference audio for best results |
| **Singing** | Moderate | Moderate | Specify vocal style and range; pair with reference audio |
| **Complex music (multi-instrument)** | Low | Low | Simplify to primary instrument or mood |
| **Sound effects (transient)** | Low | Low | "Glass breaking" — transient sounds are harder to sync |

**The Three Audio Prompting Domains:**

| Domain | When to Use | Prompt Location | Example |
|--------|------------|-----------------|---------|
| **Ambient Sound** | Always — grounds the scene in acoustic space | End of prompt, after visuals | "The audio is a quiet room tone with distant city rumble" |
| **Character Voice** | Dialogue, narration, singing | Integrated with character description | "She speaks in a soft, warm voice with a slight tremor" |
| **Music / Score** | Emotional anchoring, genre signaling | After action, before guardrails | "Soft melancholic piano underscores the scene" |

**Reference Audio Conditioning (ID-LoRA Workflow):**
- **Input:** 5-second clean audio clip (WAV or MP3)
- **Processing:** Mel-Band RoFormer vocal separation isolates clean voice from background
- **Function:** Extracts persistent vocal traits (timbre, resonance, speaking color) — does NOT replay the sample
- **Output:** Generated speech with matched vocal identity, synced to lip movement
- **Critical:** Clean audio required — background music or noise teaches the model bad associations

**The [VISUAL] / [SPEECH] / [SOUNDS] Tag System (ID-LoRA Prompts):**
For ID-LoRA + reference audio workflows, structure prompts with three explicit tags:

```
[VISUAL] Scene description, character appearance, lighting, camera movement
[SPEECH] Exact words to speak, in quotation marks, with pacing notes
[SOUNDS] Voice quality description, ambient sound, acoustic environment
```

---

### PROMPT ARCHITECTURE

**Core Audio-Visual Template (LTX 2.3):**
```
[Visual scene description — single flowing paragraph].
[Subject action in present tense, continuing visual narrative].
[Camera motion and lighting, maintaining visual flow].
[Character speaks/hears/react — voice quality and delivery].
The audio includes [primary ambient sound] with [secondary sound layer].
[Music or score description if applicable — instrument, mood, volume].
[Acoustic environment — reverb, space size, dampening].
```

**Audio-to-Video Specific Template:**
```
[Visual interpretation of the audio track — what should be seen].
[Subject performing or reacting to the audio — physical motion tied to rhythm/energy].
[Camera movement synchronized to audio structure — static for vocals, energetic for beats].
[Lighting that pulses or shifts with audio dynamics].
[Environmental elements that respond to sound — dust, water, light].
```

**ID-LoRA Talking Head Template:**
```
[VISUAL] Medium close-up of [character description] in [environment].
[Camera: static or subtle push-in, lighting description].
[SPEECH] "[Exact dialogue in quotes, broken into short phrases with pacing.]"
[SOUNDS] [Voice quality: warm/cold/aged/young, accent, speaking pace].
[Ambient: room tone, background noise level, acoustic space].
```

**Guardrails (Positive-Only Audio-Visual Safety):**
```
clean audio without distortion, synchronized lip movement,
natural vocal timbre, appropriate room reverb for space size,
coherent audio-visual timing, consistent voice across frames,
no audio dropouts, stable volume levels, clear speech articulation
```

---

### ADVANCED TECHNIQUES

**1. The Lip-Sync Anchor (ID-LoRA + Reference Audio)**
- Setup: Talking head with precise lip synchronization
- Visual: "[VISUAL] Medium close-up of a woman with shoulder-length brown hair, wearing a blue blouse, sitting at a desk in a home office. Soft natural window light from the left. Camera static at eye level, 85mm f/2.0."
- Speech: "[SPEECH] 'The most important thing,' she pauses, making eye contact with the camera, 'is to start before you're ready.' She smiles slightly. 'You'll never feel fully prepared.'"
- Sounds: "[SOUNDS] Warm, clear female voice with slight enthusiasm. Clean vocal recording with minimal room reverb. Soft keyboard clicks in background. Quiet home office ambiance."
- Audio Input: 5-second clean reference audio of the target voice
- Why it works: ID-LoRA locks facial identity; reference audio locks vocal timbre; [SPEECH] guides phoneme-level lip articulation.
- Best For: Personalized video messages, educational content, branded spokesperson, synthetic interviews

**2. The Music Visualizer (Audio-to-Video)**
- Setup: Abstract or representational visuals synchronized to music
- Audio Input: Upbeat electronic track with strong beat structure
- Visual: "A dancer in an industrial warehouse moves with sharp, staccato energy matching the driving beat. Each kick drum hit coincides with a quick angular arm movement. The lighting pulses in sync with the bass, alternating between deep cyan and hot magenta. Dust particles catch the light with each pulse."
- Camera: "Camera orbits slowly at constant speed, 24mm wide angle, while the dancer performs in center frame."
- Audio Mapping: "The visual energy directly mirrors the audio — quiet sections show slow fluid movement, drops trigger explosive motion, breakdowns show stillness with subtle breathing."
- Why it works: Explicit audio-to-visual mapping guides the dual-stream cross-attention to synchronize.
- Best For: Music videos, promotional content, DJ visuals, event openers

**3. The Environmental Soundscape**
- Setup: Scene where ambient audio creates atmosphere without drawing attention
- Visual: "Wide establishing shot of a coastal fishing village at dawn. Small boats bob in the harbor. Smoke rises from stone chimneys. A single figure walks along the pier."
- Audio Layers:
  - Primary: "Gentle waves lapping against wooden dock pilings, rhythmic and constant"
  - Secondary: "Distant seagulls calling, occasional and sparse"
  - Tertiary: "Soft wind through rigging lines, creating metallic chimes"
  - Deep: "Very faint diesel engine rumble from a boat preparing to depart"
- Why it works: Layered ambient sound creates depth and realism. Each layer reinforces the visual environment.
- Best For: Documentary, travel content, atmospheric narratives, ASMR-style content

**4. The Foley-Accented Action**
- Setup: Physical action where sound reinforces the motion
- Visual: "A carpenter swings a hammer, striking a nail into reclaimed wood. Sawdust particles scatter with each impact. He pauses to examine his work, brushes sawdust from the surface with a calloused hand."
- Audio: "The audio features sharp, resonant hammer strikes with realistic wood impact sounds. Between strikes, the ambient sound of a workshop — faint saw whine, wood creaking, distant radio. The brush of sawdust creates a soft scratching sound."
- Why it works: Syncing specific visual actions to named sounds improves both audio and motion quality.
- Best For: Craft content, ASMR, product demonstrations, artisan profiles

**5. The Narration-Driven Documentary**
- Setup: Voiceover narration accompanying B-roll visuals
- Audio Input: Narrator voice track (can be real recording or generated)
- Visual: "Aerial drone shot slowly pushing forward over a dense rainforest canopy at golden hour. Mist rises between the trees. A river winds through the green expanse, catching the sunlight."
- Narration: "The narrator speaks in a measured, authoritative baritone, describing the ancient ecosystem below. Their voice is warm and reverent."
- Audio Structure: "Voiceover is clear and front-present. Underneath, ambient rainforest sounds — insect chorus, distant bird calls, wind through canopy. No music."
- Why it works: Separating narration audio from visual generation ensures the voice drives pacing while visuals provide illustration.
- Best For: Documentary, nature content, educational series, explainer videos

**6. The Emotional Score Cue**
- Setup: Scene where music drives emotional arc
- Visual: "A young couple sits on a bench in an empty train station at night. They are not touching. She looks out at the tracks. He looks at his hands."
- Music: "A solo piano plays a sparse, melancholic melody — single notes with long sustains and silence between. The music is quiet, almost internal."
- Audio Dynamics: "As the camera slowly pulls back, the piano melody becomes slightly more present, filling the empty acoustic space of the station. A distant train whistle underscores the final note."
- Why it works: Describing music dynamics (sparse, building, fading) creates emotional trajectory that matches visual pacing.
- Best For: Drama, romantic content, music-driven narratives, brand films

**7. The Synced Sound Design Reveal**
- Setup: Product reveal where audio punctuates the visual moment
- Visual: "A luxury watch rests on black velvet. The camera pushes in slowly. At the moment the watch face fills the frame, the second hand begins to move."
- Audio: "Complete silence for the first three seconds. Then, a single precise mechanical click as the second hand advances. The tick continues, perfectly regular — one tick per second. The acoustic space is completely dry, no reverb, emphasizing precision."
- Why it works: The contrast between silence and precise sound creates focus and luxury association.
- Best For: Product launches, luxury goods, tech reveals, precision engineering

---

### EXAMPLE PROMPTS

**Talking Head With ID-LoRA (Tagged Format):**
> [VISUAL] Medium close-up of a professional woman in her 40s with shoulder-length auburn hair, wearing a charcoal blazer, sitting in a modern office with floor-to-ceiling windows showing a city skyline. Soft diffused natural light from the window. Camera static at eye level, 85mm f/2.0, shallow depth of field with city softly blurred behind her.
> [SPEECH] "The key to effective leadership," she pauses and makes direct eye contact with the camera, "isn't about having all the answers." She leans forward slightly. "It's about asking the right questions." She smiles, the expression warm and genuine.
> [SOUNDS] Warm, clear female voice with measured authority and slight warmth. Clean vocal recording with minimal room reverb appropriate for a modern office. Subtle keyboard and mouse clicks in the distant background. Quiet professional ambiance.

**Audio-to-Video Music Visualization:**
> A lone contemporary dancer in a dark concrete warehouse moves with sharp, staccato energy that matches the driving electronic beat. Each kick drum hit coincides with a quick angular arm movement or foot stomp. The lighting pulses in sync with the bass, alternating between deep cyan and hot magenta. Dust particles in the air catch the light with each pulse. The camera orbits slowly around the dancer at constant speed, 24mm wide angle emphasizing the warehouse scale. During breakdown sections, the dancer's movements become slow and fluid, matching the stripped-back audio. When the drop hits, explosive energy returns. Underground rave atmosphere, raw and unpolished.

**Environmental Soundscape Documentary:**
> Wide establishing shot of a coastal fishing village at dawn, small wooden boats bobbing in the harbor, smoke rising from stone chimneys, a single figure in a yellow raincoat walking along the pier. Gentle golden light breaking through morning mist. The audio features gentle waves lapping against wooden dock pilings with rhythmic consistency, distant seagulls calling occasionally, soft wind creating metallic chimes through boat rigging, and a very faint diesel engine rumble from a boat preparing to depart. No music. Natural documentary atmosphere, peaceful and authentic.

---

### TECHNICAL NOTES FOR AI GENERATION
- **Audio is generated in the same latent pass as video** — not post-processed. Describe audio in every prompt for best results.
- **Clean reference audio is essential for ID-LoRA** — 5 seconds of clean voice, no background music, no noise. Dirty audio teaches bad associations.
- **Use [VISUAL], [SPEECH], [SOUNDS] tags for ID-LoRA** — this structured format is what the subgraph expects.
- **Vocal separation preprocessing:** Use Mel-Band RoFormer to isolate clean vocals from reference audio before conditioning.
- **Match acoustic description to visual space:** "Large cathedral reverb" for cathedral visuals; "Dry intimate space" for close-ups.
- **Speech clarity improves with shorter phrases** — Break long sentences into short phrases with physical direction between.
- **Music description: name instrument + mood + dynamics** — "Sparse solo piano, melancholic, building gradually" outperforms "sad music."
- **Ambient layers create depth** — Primary (closest), secondary (mid-distance), tertiary (distant), deep (barely perceptible).
- **For lip-sync: the [SPEECH] tag guides phonemes** — Exact words in quotes help the model resolve mouth shapes.
- **Reference audio anchors vocal timbre** — The model extracts persistent voice characteristics, not the exact recording.
- **Audio dropouts happen in complex scenes** — Simplify audio description if video has many moving elements.
- **Transient sounds (breaks, impacts) are harder than sustained sounds** — Expect lower reliability for "glass shattering" than "continuous rain."
- **For talking videos: portrait orientation often works better** — 9:16 trained natively on vertical content; face fills more frame area.
- **Volume dynamics in prompt affect output** — "Faint whisper" vs. "Projected voice" vs. "Shouted" — describe amplitude explicitly.
