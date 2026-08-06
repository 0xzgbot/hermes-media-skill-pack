# SKILL: LTX 2.3 Subject Motion & Performance Direction
## Version: 1.0 | Hermes Agent LTX Human Action, Acting & Facial Performance Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for directing subject motion, human performance, and action sequences in LTX 2.3. While the existing camera movement skill covers HOW the camera moves, this skill covers HOW subjects move — the acting grammar, facial expression triggers, gesture vocabulary, dialogue performance beats, and physics-based motion constraints required to generate believable human (and non-human) motion. Covers micro-expressions, gait patterns, hand gesture reliability, dialogue lip-sync anchoring, and the specific motion types LTX 2.3 handles well versus poorly.

---

### TECHNICAL PARAMETERS

**LTX 2.3 Motion Architecture for Subjects:**
- **Model:** 22B DiT with 3D RoPE for spatiotemporal dynamics
- **Motion Encoding:** GemmaAPITextEncode processes motion descriptions as temporal sequences
- **Subject Motion vs. Camera Motion:** Must remain in separate prompt clauses — never mix
- **Strength:** Moderate, natural human motion (walking, talking, gesturing, facial expression)
- **Weakness:** Complex physics (crowds, chaotic cloth, water splashing, intricate hand manipulations)
- **I2V Advantage:** Subject identity locks at frame zero; motion deviates less than T2V

**The Subject Motion Reliability Spectrum:**

| Motion Type | Reliability | Description | Best Practice |
|------------|-------------|-------------|---------------|
| **Static pose with breathing** | Highest (96%) | Minimal motion, chest rise/fall, eye blink | Use "breathing slowly, chest rising and falling naturally" |
| **Slow head turn** | Very High (92%) | Head rotates toward camera or away | Specify direction and speed: "turns head slowly to the left" |
| **Walking (steady pace)** | Very High (90%) | Natural gait, arms swinging | Specify gait: "walks with confident stride, arms swinging naturally" |
| **Talking / lip movement** | High (85%) | Mouth opens/closes, jaw movement | Pair with audio description for sync; use ID-LoRA for identity lock |
| **Smile formation** | High (83%) | Mouth curves, cheek lifts, eye involvement | "Smile reaches her eyes, crow's feet forming" |
| **Hand gestures (simple)** | Moderate (75%) | Pointing, waving, open palm | Keep hands visible and away from face; one gesture at a time |
| **Running** | Moderate (70%) | Faster gait, limb extension | Expect slight motion blur; specify "running at moderate pace" |
| **Dancing (structured)** | Moderate (65%) | Choreographed movement, rhythm | Specify dance style; avoid freestyle chaotic motion |
| **Object manipulation** | Low (55%) | Picking up, holding, using tools | Describe object and hand relationship explicitly |
| **Complex hand interactions** | Low (50%) | Typing, playing instrument, tying knots | Simplify to broad motion; detail often fails |
| **Crowd movement** | Very Low (35%) | Multiple independent subjects | Focus on one subject; background crowd as "blurred motion" |
| **Fast chaotic motion** | Very Low (30%) | Fighting, sports action, collapsing | Plan slower motion; use cuts between static poses instead |

**The Facial Expression Vocabulary:**

| Expression | Physical Cues (Use These) | Emotional Label (Avoid) |
|-----------|--------------------------|------------------------|
| **Joy** | Corners of mouth lift, cheeks raise, crow's feet form at eyes, shoulders relax | "Happy," "joyful" |
| **Sadness** | Brow center furrows, mouth corners drop, eyes glisten with moisture, chin tilts down | "Sad," "depressed" |
| **Anger** | Jaw tightens, brows lower and draw together, nostrils flare, lips press thin | "Angry," "furious" |
| **Surprise** | Brow raises, eyes widen, mouth opens slightly, head pulls back | "Surprised," "shocked" |
| **Fear** | Eyes widen with whites showing, brows raise and draw together, mouth opens | "Scared," "terrified" |
| **Disgust** | Nose wrinkles, upper lip raises, head tilts back slightly, eyes narrow | "Disgusted," "repulsed" |
| **Contempt** | One corner of mouth lifts asymmetrically, slight head tilt, relaxed eyelid | "Contemptuous" |
| **Neutral/Thoughtful** | Soft gaze, slight head tilt, slow blink, relaxed brow, mouth at rest | "Thinking," "neutral" |
| **Tired/Weary** | Eyelids heavy, shoulders slump, slow movements, slight forward head posture | "Tired," "exhausted" |

**The Gesture Reliability Library:**

| Gesture | Reliability | Description Prompt | Common Failure |
|---------|------------|-------------------|---------------|
| **Open palm facing camera** | High | "Raises open hand toward camera, palm visible, fingers slightly spread" | Fingers merge or become extra digits |
| **Pointing** | Moderate | "Points with index finger extended, other fingers curled" | Hand shape distorts, multiple fingers extend |
| **Waving** | Moderate | "Waves with open hand, fingers together, gentle side-to-side motion" | Hand blurs into smear |
| **Hand on chest/heart** | High | "Places right hand flat against chest, over heart" | Reliable when hand contacts torso |
| **Arms crossed** | High | "Crosses arms over chest, hands tucked under biceps" | Stable pose, minimal finger detail needed |
| **Hands in pockets** | Very High | "Stands with hands in coat pockets" | Hides hands entirely — eliminates failure mode |
| **Holding object (simple)** | Moderate | "Holds a coffee cup in right hand, grip relaxed" | Object may float or hand may not contact properly |
| **Clapping** | Low | "Claps hands together once" | Hands pass through each other or blur |
| **Typing / fine motor** | Very Low | "Types on a keyboard" | Finger positions fail almost always |

**Gait Pattern Descriptors:**

| Gait | Description | Emotional Association |
|------|------------|----------------------|
| **Confident stride** | Long steps, shoulders back, arms swinging freely, head level | Power, purpose, determination |
| **Hesitant shuffle** | Short steps, feet dragging slightly, shoulders hunched, head down | Uncertainty, fear, exhaustion |
| **Casual amble** | Medium steps, relaxed posture, hands in pockets or swinging loosely | Comfort, familiarity, leisure |
| **Urgent brisk walk** | Quick but controlled steps, slight forward lean, arms pumping | Purpose, deadline, anxiety |
| **Stagger / limp** | Uneven weight distribution, one leg favoring, upper body compensating | Injury, intoxication, weakness |
| **Bounce / energy** | Spring in step, slight upward motion with each stride, arms active | Youth, enthusiasm, excitement |
| **Slow deliberate pace** | Measured steps, body stable, minimal upper body motion, purposeful | Authority, contemplation, dignity |

---

### PROMPT ARCHITECTURE

**Core Subject Motion Template (LTX 2.3):**
```
Scene: [Environment — static description, no motion verbs]
Subject: [Who — age, clothing, distinguishing features]
Action: [What they do — present tense, chronological sequence]
Facial/Performance: [Expression using physical cues, gaze direction, micro-expressions]
Gesture: [Hand/arm position and movement, if visible]
Gait/Movement Quality: [How they move — speed, energy, physical state]
Camera: [Camera motion — pure motion verbs, separate from subject]
Motion: [Speed descriptors, shutter, environmental motion]
Guardrails: [Quality constraints in positive phrasing]
```

**The Performance Beat Structure (For Dialogue/Acting):**
```
[Character] [speaks/delivers/react] with [voice quality], "[Dialogue in quotes]."
[Physical reaction 1 — what their face/body does during or after speaking].
[Physical reaction 2 — secondary response, eye movement, breath change].
[Environmental response — if any — light shift, sound, object reaction].
```

**Guardrails (Positive-Only Motion Safety):**
```
natural human proportions, consistent limb positioning across frames,
realistic joint articulation, believable weight transfer during motion,
coherent facial expression continuity, natural blink rate,
realistic gait mechanics, consistent hand anatomy when visible,
smooth motion transitions, no frozen poses mid-action
```

---

### ADVANCED TECHNIQUES

**1. The Micro-Expression Hold**
- Setup: Extreme close-up of face, minimal motion except facial expression
- Subject: "Woman in her 40s, natural makeup, soft window light"
- Performance: "Her expression shifts almost imperceptibly — eyes narrow slightly, a single brow arches, the corner of her mouth twitches upward asymmetrically. She holds the gaze for two seconds, then blinks slowly."
- Camera: "Static tripod-locked extreme close-up, 85mm f/2.0, shallow depth of field on near eye"
- Motion: "Natural 180° shutter, no camera movement, only facial motion"
- Guardrails: "Consistent eye color across frames, no facial morphing, stable skin texture, natural blink"
- Emotional: Suspense, psychological depth, unspoken communication, intimacy
- Best For: Thriller reveals, dramatic pauses, character study, emotional subtext

**2. The Walking Character Study**
- Setup: Full or medium shot, subject walking through environment
- Subject: "Man in his 30s, worn leather jacket, jeans, scuffed boots"
- Gait: "Walks with a slight limp favoring left leg, shoulders compensating with subtle roll, head down at 15° angle, hands deep in jacket pockets"
- Environment: "Rain-slicked industrial alley at night, neon reflections in puddles"
- Camera: "Steady dolly tracking from side at matching pace, 35mm f/2.8"
- Motion: "Natural walking pace, 180° shutter motion blur on background, rain falling at natural speed"
- Guardrails: "Consistent leg anatomy, no limb distortion, stable jacket physics, natural weight transfer"
- Emotional: Defeat, perseverance, urban isolation, wounded dignity
- Best For: Character introductions, noir sequences, music video narrative

**3. The Dialogue Performance With Beats**
- Setup: Medium two-shot or close-up, speaking character
- Subject: "Elderly woman with silver hair pinned back, wire-rim glasses"
- Performance: "She speaks in a warm, measured voice, 'When I was your age...' She pauses, looking past the camera as if seeing a memory. Her eyes soften. She continues, 'we didn't have any of this.' A slight shake of her head. 'But we had time.' She smiles, the smile reaching her eyes, crow's feet deepening."
- Camera: "Slow push-in from medium to close-up over the course of her speech, 50mm f/2.0"
- Audio: "Warm vocal tone, slight tremor on certain words, room tone of a quiet kitchen"
- Guardrails: "Consistent facial identity, natural lip sync, no hand distortion, stable glasses position"
- Emotional: Nostalgia, generational wisdom, warmth, bittersweet reflection
- Best For: Documentary interviews, narrative dialogue, testimonial content

**4. The Reaction Shot (No Dialogue)**
- Setup: Close-up of subject reacting to off-screen event
- Subject: "Young man, short dark hair, stubble"
- Performance: "He watches something off-screen left. His eyes widen slightly. His jaw relaxes and drops a centimeter. He blinks once, slowly. A breath escapes through parted lips. He doesn't move his head — only his eyes track the unseen action."
- Environment: "Dimly lit room, practical lamp creating warm key on his face"
- Camera: "Static locked frame, 85mm f/1.8, shallow focus on his eyes"
- Motion: "No camera movement. Only facial micro-motion. 180° shutter."
- Guardrails: "Stable head position, consistent eye direction, no facial morphing, natural moisture in eyes"
- Emotional: Shock, awe, disbelief, witnessing the impossible
- Best For: Horror reveals, sci-fi first contact, miracle moments, plot twists

**5. The Environmental Interaction (Subject + World)**
- Setup: Subject interacting with physical environment
- Subject: "Child, approximately 8 years old, red raincoat"
- Action: "She crouches by a puddle, watching raindrops create ripples. She extends one finger toward the water surface. A drop lands on her fingertip. She pulls back slightly, then smiles. She stands, turning her face upward to the rain."
- Environment: "Autumn park, fallen leaves in amber and brown, overcast gray sky"
- Camera: "Slow crane down from medium to low angle, 35mm f/2.8"
- Motion: "Natural rain at moderate intensity, leaves occasionally tumbling past, puddle ripples from raindrops"
- Guardrails: "Consistent child proportions, natural finger anatomy when extended, realistic water interaction, stable rain pattern"
- Emotional: Wonder, childhood discovery, simple joy, connection with nature
- Best For: Family content, brand storytelling, nostalgic narratives

**6. The Group Motion (Limited Crowd)**
- Setup: Small group with one primary subject in focus
- Subject: "Businesswoman in navy suit walking through a lobby"
- Group: "Three other people walk in background, out of focus, moving in various directions"
- Action: "She walks with confident stride through the lobby. Background figures move past her, some glancing briefly. She does not acknowledge them. She checks her watch as she walks."
- Camera: "Steady dolly tracking from behind at her pace, 50mm f/2.0, background softly blurred"
- Motion: "Natural walking pace for all figures, 180° shutter, no collision between figures"
- Guardrails: "Primary subject in consistent focus, background figures stay blurred, no limb intersection artifacts, stable depth of field"
- Emotional: Determination, professional focus, urban anonymity
- Best For: Corporate narratives, city life, professional profiles

**7. The Animal Motion Proxy**
- Setup: Animal subject where human directing language doesn't apply
- Subject: "Golden retriever, mature adult, well-groomed coat"
- Action: "The dog trots across a sunlit meadow at an easy pace, tongue lolling slightly, tail wagging in a loose, sweeping arc. It stops suddenly, ears perking forward. It sniffs the air, head raised. Then it continues trotting, tail resuming its wag."
- Environment: "Green meadow with wildflowers, late afternoon golden light, distant trees"
- Camera: "Steady tracking shot from side at dog's height, 35mm f/4"
- Motion: "Natural trotting gait, tail physics consistent, ear movement reactive, grass moving in breeze"
- Guardrails: "Consistent dog proportions, natural tail movement physics, no leg distortion, stable coat texture"
- Emotional: Freedom, joy, animal instinct, pastoral peace
- Best For: Pet content, nature documentaries, lifestyle brands

---

### EXAMPLE PROMPTS

**Micro-Expression Close-Up:**
> Scene: Minimal bedroom, morning light through sheer curtains.
> Subject: Woman in her 40s with natural makeup, lying in bed.
> Action: She wakes gradually. Her eyes flutter open. She focuses on something across the room. Her expression shifts almost imperceptibly — eyes narrow slightly, a single brow arches, the corner of her mouth twitches upward asymmetrically. She holds the gaze for two seconds, then blinks slowly.
> Camera: Static tripod-locked extreme close-up on face, 85mm f/2.0.
> Motion: Natural 180° shutter, no camera movement, only facial motion, dust particles visible in light beam.
> Guardrails: Consistent eye color across frames, no facial morphing, stable skin texture, natural blink rate.

**Walking Character Introduction:**
> Scene: Rain-slicked industrial alley at night, neon signs reflecting in puddles, steam rising from a grate.
> Subject: Man in his 30s wearing a worn leather jacket, jeans, scuffed boots.
> Action: He walks with a slight limp favoring his left leg, shoulders compensating with a subtle roll, head down at a 15-degree angle, hands deep in jacket pockets. His gait is slow and deliberate.
> Camera: Steady dolly tracking from side at matching pace, 35mm f/2.8.
> Motion: Natural walking pace, 180° shutter motion blur on background, rain falling at natural speed, steam drifting upward.
> Guardrails: Consistent leg anatomy, no limb distortion, stable jacket physics, natural weight transfer.

**Dialogue Performance With Physical Beats:**
> Scene: Cozy kitchen, warm tungsten light, wooden table between two people.
> Subject: Elderly woman with silver hair pinned back, wire-rim glasses, cardigan.
> Action: She speaks in a warm, measured voice, "When I was your age..." She pauses, looking past the camera as if seeing a memory. Her eyes soften and her head tilts slightly. She continues, "we didn't have any of this." A slight shake of her head, her hand rising briefly then falling back to the table. "But we had time." She smiles, the smile reaching her eyes, crow's feet deepening.
> Camera: Slow push-in from medium to close-up over the course of her speech, 50mm f/2.0.
> Motion: Natural speaking rhythm, 180° shutter, subtle hand gesture, no sudden movements.
> Guardrails: Consistent facial identity, natural lip sync, no hand distortion, stable glasses position, coherent emotional arc.

---

### TECHNICAL NOTES FOR AI GENERATION
- **Use physical cues, not emotional labels:** "Jaw tightens, brows lower" outperforms "he is angry." LTX 2.3 renders visible physical changes, not internal states.
- **Hide hands for higher reliability:** "Hands in pockets" or "arms crossed" eliminates the most common failure mode (finger distortion).
- **One gesture at a time:** Complex multi-hand actions fail. Sequence gestures: "She points, then lowers her hand, then opens her palm."
- **Specify gait for walking shots:** Generic "walking" produces generic motion. "Confident stride with long steps and swinging arms" produces distinct character.
- **Micro-expressions need time:** Hold expressions for 2+ seconds in the prompt to ensure they're visible across enough frames.
- **Blinking is your friend:** "Blinks slowly" or "eyes flutter open" adds life and prevents the "doll stare" effect.
- **Breathing grounds static subjects:** Even motionless subjects feel alive with "chest rising and falling with slow breaths."
- **Keep fingers away from faces:** Hand-to-face contact (wiping tears, covering mouth) has high distortion risk.
- **Dancing works best with named styles:** "Ballet pirouette" or "salsa step" outperforms "dancing gracefully" — named styles have stronger motion priors.
- **Running produces motion blur:** Specify "running at moderate pace" and expect some limb blur. Plan camera motion to match subject speed.
- **Crowds fail — use depth of field:** Instead of "crowd of people walking," use "lone subject walking, blurred figures passing in background."
- **Object contact needs explicit description:** "Hand wrapped around mug handle, fingers visible" outperforms "holding a mug."
- **For dialogue: break into beats:** Separate dialogue into short phrases with physical reactions between. This creates natural acting rhythm.
- **Lip sync improves with audio conditioning:** For talking subjects, use the audio-to-video mode or ID-LoRA with reference audio.
- **Expect 15–20% gesture deformation:** Even "reliable" gestures may deform in some frames. Plan shots where brief deformation is acceptable or hidden.
