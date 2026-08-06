# SKILL: Cinematic Continuity
## Domain: Multi-Shot Sequences, Visual Coherence, Character Consistency, Pipeline Continuity
## Version: 1.0
## For: Hermes Agent — Scene Planning, Shot Lists, Character Locking

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete language of cinematic continuity — both traditional film grammar and AI-specific workflow discipline. It covers the 180-degree rule, eyeline matching, match cuts, shot-reverse-shot, lighting continuity, color grading coherence, and the AI-native techniques required to maintain character identity across frames, shots, and scenes.

When this skill is active, the agent should:
- Plan shots using traditional continuity editing grammar
- Enforce spatial coherence (axis of action, eyeline consistency)
- Maintain lighting, color, and prop continuity across sequences
- Apply AI-specific locking techniques (anchor frames, IP adapters, frame-to-frame chaining)
- Build shot lists that prevent character drift and visual discontinuity
- Understand how project graph graph relationships enforce continuity automatically

---

## 2. THE CONTINUITY EDITING GRAMMAR

Traditional continuity editing creates invisible cuts that preserve spatial geography, temporal flow, and viewer immersion. [^46^] These principles are non-negotiable when planning multi-shot AI-generated sequences.

### Core Continuity Principles

| Principle | What It Means | Prompt/Planning Vocabulary |
|-----------|---------------|--------------------------|
| **180-Degree Rule** | Invisible axis between characters; camera stays on one side to maintain left/right geography [^46^] | "axis of action", "180-degree line", "camera side consistency", "screen direction locked" |
| **Eyeline Match** | Character looks in direction consistent with their spatial position; next shot shows what they see [^46^] | "eyeline match", "looking left 15 degrees", "gaze direction consistent", "POV continuity" |
| **Match Cut** | Cut between shots where composition, movement, or shape aligns seamlessly [^46^] | "match cut transition", "graphic match", "motion match", "shape-to-shape cut" |
| **Shot-Reverse-Shot** | Alternating over-shoulder or clean singles between two characters in dialogue [^46^] | "shot-reverse-shot", "clean single", "over-shoulder framing", "dialogue coverage" |
| **Eye Trace** | Guiding viewer attention from one point in frame to the next cut point [^46^] | "eye trace guide", "attention handoff", "focal point continuity" |
| **Action Match** | Movement continues across cut without jump (e.g., door opening) | "action match cut", "motion continuity across cut", "continuous gesture" |

### The Axis of Action (180-Degree Rule Deep Dive)

Imagine a line connecting two characters. The camera must stay on ONE side of this line for the entire scene. Crossing the line reverses screen direction and disorients the viewer. [^46^]

**Application:**
- When generating a multi-shot scene, the agent must record which side of the axis each shot was generated from.
- If Shot 1 has Character A on the left and Character B on the right, Shot 2 (reverse angle) must maintain this left/right relationship.
- **Graph enforcement:** In the project graph, the `axis_side` property on Scene nodes locks camera geography.

**Prompt Translation:**
> "180-degree axis locked, Character A screen-left, Character B screen-right, over-shoulder reverse angle maintaining spatial geography"

### Eyeline Matching in AI Workflows

Eyeline matching ensures that when Character A looks at Character B, the next shot of Character B shows them from the correct angle. [^46^]

**The Math:**
- If Character A looks 30° to their right, the reverse shot of Character B must show them looking 30° to their left (mirror).
- If Character A looks upward, Character B must be positioned higher in frame.

**AI Prompt Template:**
> "Character A looking 20 degrees up and 15 degrees right, eyeline match to Character B positioned upper-right of frame, spatial relationship consistent with previous shot"

---

## 3. SHOT PLANNING & STORYBOARDING

Before generating any frames, the agent must build a shot list that enforces continuity at the planning stage.

### The production Shot List Schema

| Field | Purpose | Example |
|-------|---------|---------|
| **Shot ID** | Unique identifier | S01A, S01B, S02A |
| **Duration** | Length in seconds | 4.5s |
| **Framing** | Shot type | Wide / Medium / Close-Up / ECU |
| **Camera** | Movement and position | Static / Dolly-in / Orbit-left / Whip-pan |
| **Axis Side** | 180-degree rule compliance | Left / Right / Neutral (on axis) |
| **Character Action** | One verb + one object | "picks up key" |
| **Character Expression** | Emotional state | Neutral → Concerned |
| **Lighting Key** | Light direction, temperature | "Window-left 3200K, rim-right 5600K" |
| **Background Plate** | Environment consistency | "alley_night_v2" |
| **Prop State** | Object continuity | "Key in right hand, coffee cup on table" |
| **Anchor Frame** | Reference image for generation | `asset_elena_S01A.png` |
| **Previous Shot** | Chain reference | S01A |
| **Next Shot** | Chain reference | S01C |

### Shot Types & Continuity Implications

| Shot Type | Abbreviation | Continuity Role | Best For |
|-----------|-------------|-----------------|----------|
| **Extreme Wide / Establishing** | EW / EST | Sets geography, time, mood | Scene openers, location lock |
| **Wide / Long Shot** | WS / LS | Full body + environment | Action, movement, spatial context |
| **Medium Shot** | MS | Waist up, social distance | Dialogue, two-shots, interaction |
| **Medium Close-Up** | MCU | Chest up, intimate | Emotional beats, reactions |
| **Close-Up** | CU | Face / object detail | Revelation, prop emphasis, tension |
| **Extreme Close-Up** | ECU | Eye / mouth / object detail | Intense emotion, texture, micro-action |
| **Over-Shoulder** | OTS | Dialogue coverage | Shot-reverse-shot, spatial relationship |
| **Point of View** | POV | Character's literal view | Immersion, revelation, subjectivity |
| **Insert** | INS | Cutaway detail | Prop continuity, time passage, emphasis |
| **Cutaway** | CA | Non-POV detail | Reaction shots, environment texture |

### The Coverage Principle

For any scene with dialogue or interaction, generate coverage in this order:
1. **Master shot (Wide)** — Establishes geography, actor positions, lighting baseline
2. **Medium two-shot** — Social framing for interaction beats
3. **Singles (MCU/CU)** — Emotional coverage, one per character
4. **Inserts / Cutaways** — Prop detail, hands, reactions, environment texture
5. **POV shots** — Optional, for subjective moments

**AI Workflow Note:** Generate the master shot FIRST. Extract its lighting, color, and character state as the anchor for all subsequent shots. [^44^]

---

## 4. VISUAL CONTINUITY: LIGHTING, COLOR & PROPS

Continuity is not just editing — it is every department maintaining consistency across time and space. [^48^]

### Lighting Continuity

Lighting continuity ensures viewers remain immersed by maintaining consistent intensity, color balance, shadow placement, and light direction across shots. [^48^]

**The Lighting Continuity Checklist:**
- [ ] Key light direction matches across all shots in scene
- [ ] Color temperature consistent (±200K tolerance)
- [ ] Shadow placement matches time of day / motivated sources
- [ ] Rim/hair light intensity consistent for character separation
- [ ] Fill level maintains contrast ratio (key:fill = 2:1 to 4:1 typically)
- [ ] Practical lights (lamps, screens, fire) maintain consistent glow

**Application:**
In the project graph, each Scene node stores a `lighting_key` object. All shots linked to that scene inherit the lighting key automatically. Changing the scene's lighting key triggers `graph_impact` to show all affected shots.

**Prompt Translation:**
> "lighting continuity locked: 3200K key from window-left, 5600K rim from practical lamp-right, 2:1 contrast ratio, shadow direction 45 degrees camera-left, fill level -2 stops, consistent across all shots in sequence"

### Color Continuity & Grading

Color grading maintains visual coherence across scenes shot under different conditions or generated by different models. [^47^]

**Color Continuity Rules:**
- **Scene-to-scene:** Gradual shifts only. Abrupt color changes must be motivated (entering a club, waking from dream).
- **Character-to-character:** Skin tones must match across shots. Use the same reference seed/model for character skin.
- **Prop-to-prop:** Object colors must not drift. A red coffee cup stays the same red.
- **Temporal color arcs:** Warm → neutral → cool can track emotional journey across a sequence.

**The Color Bible (Per Scene):**
```json
{
  "scene_id": "scene_alley_night",
  "color_grade": {
    "primary": {"hue": 220, "sat": 0.3, "lum": 0.2},
    "skin_tone_reference": "#E8C4A0",
    "shadow_tint": {"hue": 240, "sat": 0.4},
    "highlight_roll-off": "warm",
    "film_emulation": "Kodak_5219",
    "grain_intensity": 0.15
  }
}
```

**Prompt Translation:**
> "color continuity locked to scene bible: cool blue-primary at 30% saturation, skin tone reference #E8C4A0, shadow tint blue-purple, warm highlight roll-off, Kodak 5219 film emulation, 15% grain intensity, consistent across all shots"

### Prop & Costume Continuity

The smallest prop inconsistency breaks immersion. [^44^]

**Prop Continuity Rules:**
- **Handedness lock:** If a character holds a gun in their right hand in Shot 1, they hold it in their right hand in Shot 7.
- **State lock:** A broken window stays broken. A lit cigarette burns down progressively.
- **Position lock:** A coffee cup on the table stays in the same relative position unless a character moves it (and then the new position becomes the locked state).
- **Costume lock:** Every outfit gets its own anchor pack. [^44^] Changing outfits requires a new character reference set.

**Application:**
In the project graph, Prop nodes have `state` and `position` properties. Edges track `HELD_BY` (which hand) and `LOCATED_AT` (which set position). `graph_detect_changes` flags any prop state drift between shots.

---

## 5. AI-NATIVE CONTINUITY TECHNIQUES

Traditional continuity assumes a physical set with real actors. AI generation has unique challenges: every frame is independently generated from noise, and models have no memory of previous outputs. [^43^] [^44^]

### The Character Drift Problem

AI models process each generation independently without memory of previous outputs. [^43^] Small variations accumulate across frames, causing gradual changes in facial features, proportions, lighting, and style.

**Symptoms of Drift:**
- Face shape changes between shots
- Eye color shifts subtly
- Outfit details mutate (buttons appear/disappear)
- Lighting direction flips inexplicably
- Background texture crawls

### The 4-Layer Anti-Drift Workflow [^44^]

| Layer | What It Is | Why It Matters |
|-------|-----------|----------------|
| **1. Character DNA (Spec)** | Written definition of every visual feature | Creates constraints that prevent AI creativity from ruining consistency |
| **2. Character Pack (Visual Ground Truth)** | Reference images: front, 3/4, profile, expressions | Gives AI a visual anchor to maintain identity |
| **3. Shot Keyframes (Camera Views)** | Static images defining each shot's composition | Locks composition before motion is added |
| **4. Animation + Edit (Motion + Continuity)** | Video generation and post-production polish | Brings everything to life while preserving layers 1-3 |

### Anchor Frame Chaining [^44^] [^45^]

The most reliable technique for shot-to-shot continuity:

1. **Generate Shot 1** from text prompt + character pack.
2. **Extract the best frame** from Shot 1.
3. **Use that frame as the reference image** for Shot 2.
4. **Repeat** for every subsequent shot.

This creates a "visual chain" where each shot inherits the previous shot's state. [^45^]

**production Integration:**
project graph stores the `anchor_frame` property on each Shot node. The graph automatically chains `PRECEDES` edges so the agent knows which frame to use as reference for the next shot.

**Prompt Template for Chained Generation:**
```
Subtle motion, keep character identity and outfit unchanged.
[Action in 1 verb phrase].
Camera: [one move].
Style: keep same animation style, same lighting, no flicker.
Background: keep environment consistent.
Reference: [previous shot best frame].
```

### IP Adapters & Identity Locking [^43^]

IP (Image Prompt) Adapters extract identity features from reference images and inject them into the generation process, creating a persistent "identity embedding" that carries across generations.

**How to Use:**
1. Upload 3-5 reference images (front, 3/4, profile, expressions).
2. The system extracts facial features, proportions, and identifying characteristics.
3. These features are encoded into a reusable identity embedding.
4. All subsequent generations reference this embedding for consistency.

**Best Practice:** Provide 3-5 angles with consistent lighting. [^43^] Mixed lighting in references causes the model to average incorrectly.

### Multi-Frame Aware Generation [^43^]

Advanced video models (LTX, Sora, Veo) understand frames as connected parts of a larger sequence rather than independent images. [^43^]

**Benefits:**
- Automatic identity persistence across frames
- Consistent lighting direction and intensity
- Smooth transitions between poses and expressions
- Environment continuity as scenes progress

**Application:**
When using multi-frame aware models, the agent should generate entire sequences (not individual shots) and use project graph to verify that the generated sequence matches the planned graph structure.

---

## 6. THE CONTINUITY BIBLE

A Continuity Bible is the single source of truth for all visual consistency across a project. [^44^] Every department — and every AI generation — references this document.

### Continuity Bible Structure

```yaml
project: "The production Short"
version: 1.0

characters:
  elena:
    face_embedding: "assets/embeddings/elena_v1.pkl"
    skin_tone: "#E8C4A0"
    eye_color: "hazel"
    hair: "dark brown, shoulder length, slight wave"
    default_expression: "neutral with slight curiosity"
    outfits:
      casual:
        anchor_pack: "characters/elena_casual_pack/"
        description: "blue denim jacket, white t-shirt, silver pendant"
        handedness: "right"
      cyber_suit:
        anchor_pack: "characters/elena_cyber_pack/"
        description: "black tactical suit, neon cyan accents"
        handedness: "right"
    distinguishing_marks:
      - "scar above left eyebrow"
      - "freckles on right cheek"

scenes:
  alley_night:
    lighting_key:
      key_direction: "window-left"
      key_temp: 3200
      fill_level: -2
      rim_temp: 5600
      rim_direction: "practical-right"
    color_bible:
      primary: {"hue": 220, "sat": 0.3}
      skin_ref: "#E8C4A0"
      shadow_tint: {"hue": 240, "sat": 0.4}
    props:
      coffee_cup:
        initial_position: "table center"
        state: "full, steaming"
        color: "white ceramic, red logo"
      alley_door:
        state: "closed, slightly ajar"
        hinge_side: "left"
    axis_of_action:
      line: "elena-to-door"
      camera_side: "left"

shots:
  S01A:
    scene: "alley_night"
    framing: "Wide"
    camera: "Static"
    axis_side: "left"
    characters: ["elena"]
    props: ["coffee_cup", "alley_door"]
    anchor_frame: "assets/keyframes/S01A_elena_wide.png"
    lighting_lock: true
    color_lock: true
```

### Continuity Checklist (Per Shot)

Before approving any generated shot, verify:
- [ ] Character face matches anchor pack (eye spacing, nose shape, jawline)
- [ ] Outfit details match continuity bible (buttons, logos, accessories)
- [ ] Handedness matches previous shots
- [ ] Prop state matches previous shots (position, condition, quantity)
- [ ] Lighting direction matches scene lighting key
- [ ] Color temperature matches scene bible (±200K)
- [ ] Background environment matches established geography
- [ ] Axis side matches 180-degree rule
- [ ] Eyeline direction matches spatial relationship
- [ ] Camera movement matches shot list specification

---

## 7. PROMPT ENGINEERING FOR CONTINUITY

When generating multi-shot sequences, the prompt structure must encode continuity constraints explicitly.

### Layer 1: Identity Lock
```
Character identity locked to reference image [anchor_path].
Face: [specific features from continuity bible].
Outfit: [exact description from continuity bible].
Handedness: [left/right].
Distinguishing marks: [scars, freckles, tattoos].
```

### Layer 2: Spatial Lock
```
180-degree axis locked to [axis_description].
Camera side: [left/right/neutral].
Character position: [screen-left/screen-right/center].
Background plate: [environment_reference].
Prop positions: [prop_name at position].
```

### Layer 3: Lighting Lock
```
Lighting continuity locked to scene [scene_id].
Key light: [direction, temperature, intensity].
Fill level: [stops below key].
Rim light: [direction, temperature].
Shadow direction: [angle].
Contrast ratio: [key:fill].
```

### Layer 4: Motion Lock
```
Action: [one verb phrase].
Camera: [single movement instruction].
Style: keep same animation style, same lighting, no flicker.
Background: keep environment consistent.
Motion intensity: [subtle/moderate/dynamic].
```

### Layer 5: Temporal Lock (For Video)
```
Frame-to-frame chaining enabled.
Reference previous frame: [frame_path].
Temporal coherence: high.
No flicker, no texture crawl, no lighting pop.
```

### Complete Continuity Prompt Template
```
CHARACTER LOCK: Character Elena locked to reference assets/elena_casual_front.png.
Face: oval shape, hazel eyes, dark brown shoulder-length hair with slight wave,
      scar above left eyebrow, freckles on right cheek.
Outfit: blue denim jacket, white t-shirt, silver pendant necklace.
Handedness: right.

SPATIAL LOCK: 180-degree axis locked (Elena screen-left, door screen-right).
Camera side: left. Background plate: alley_night_v2.
Prop state: coffee cup full on table center, white ceramic with red logo.

LIGHTING LOCK: Scene alley_night lighting key.
Key: 3200K window-left, rim: 5600K practical-right,
fill -2 stops, shadow direction 45 degrees camera-left, 2:1 contrast ratio.

MOTION LOCK: Action: slowly turns head to look at door.
Camera: static, slight dolly-in 10%.
Style: keep same cinematic style, no flicker, no lighting change.
Background: alley environment remains stable.

TEMPORAL LOCK: Reference previous shot S01A frame 48.
Frame-to-frame chaining active. Temporal coherence high.
```

---

## 8. NEGATIVE PROMPTS (What Breaks Continuity)

| Avoid | Why It Breaks Continuity | Replace With |
|-------|-------------------------|--------------|
| "dramatic lighting change" | Abrupt unmotivated shifts disorient viewer | "lighting continuity locked", "gradual motivated shift" |
| "different outfit" | Unless scene transition is established, costume must match | "same outfit as previous shot", "continuity costume locked" |
| "new hairstyle" | Hair state must match unless time passage is established | "same hairstyle as anchor", "hair continuity maintained" |
| "dynamic camera movement" | Complex motion increases drift probability in AI | "subtle camera movement", "locked-off with slight dolly" |
| "different background" | Environment must match established geography | "same background plate", "environment continuity locked" |
| "multiple actions" | Too many simultaneous changes increase failure rate [^44^] | "one action at a time", "single gesture per shot" |
| "ignore previous frame" | Breaks frame-to-frame chaining | "reference previous frame", "frame-to-frame chaining active" |
| "change eye color" | Facial feature drift destroys character recognition | "eye color locked to hazel", "facial features anchored" |
| "different hand holding object" | Handedness errors are classic continuity mistakes | "right hand holding object", "handedness continuity locked" |

---

## 9. SKILL STACKING: HOW THIS COMPOSES WITH OTHER SKILLS

### Stacking Architecture

```
BASE SKILL: Prompt Engineering Core
    └── GRAMMAR: syntax, structure, negative prompts, weighting

STYLE SKILL: Pixar Specialist
    └── VOCABULARY: animation principles, shape language, SSS, appeal

STYLE SKILL: Wes Anderson Specialist
    └── VOCABULARY: symmetry, color discipline, typography, deadpan

STRUCTURE SKILL: Cinematic Continuity (this file)
    └── GRAMMAR: shot lists, 180-degree rule, eyeline match, lighting lock,
                frame-to-frame chaining, continuity bible

TECHNICAL SKILL: ComfyUI/Flux/LTX Pipeline
    └── PARAMETERS: sampler, steps, CFG, model selection, IP adapter, conditioning

OUTPUT: Multi-shot sequences with perfect visual continuity,
        character consistency, and spatial coherence
```

### How Continuity Stacks With Style Skills

| Style Skill Brings | Continuity Skill Brings | Result |
|-------------------|------------------------|--------|
| Pixar: appealing character design | Continuity: anchor frame locking | "Appealing character that stays identical across 20 shots" |
| Pixar: warm emotional lighting | Continuity: lighting key lock | "Warm lighting that doesn't drift between shots" |
| Wes Anderson: 60-30-10 color | Continuity: color bible | "Pastel palette that stays consistent across the sequence" |
| Wes Anderson: symmetrical framing | Continuity: axis lock | "Perfect symmetry maintained in shot-reverse-shot" |

### Skill Priority Rules

When skills conflict:
1. **Continuity skill wins on spatial grammar** (axis, eyeline, shot order)
2. **Style skill wins on aesthetic vocabulary** (color, lighting mood, composition)
3. **Technical skill wins on generation parameters** (model, sampler, IP adapter)
4. **Base skill wins on syntax** (prompt structure, formatting)
5. **User override wins always**
6. **When continuity and style conflict:** Continuity takes precedence for multi-shot sequences. A beautiful but discontinuous sequence is a failure. A consistent but less stylized sequence is salvageable.

---

## 10. PROJECT GRAPH INTEGRATION

Cinematic Continuity is where project graph becomes essential. The graph database enforces continuity automatically.

### Graph Enforcement Points

| Continuity Rule | project graph node/Edge | How It Enforces |
|-----------------|----------------------|-----------------|
| Character identity | `Character` node + `HAS_EMBEDDING` edge | All shots linked to character must use same face embedding |
| Costume state | `Character` → `WEARS` → `Outfit` edge | Outfit changes trigger `graph_impact` on all dependent shots |
| Lighting key | `Scene` → `HAS_LIGHTING_KEY` → `LightingKey` node | All shots in scene inherit lighting parameters |
| Axis of action | `Scene` → `HAS_AXIS` → `Axis` node | Camera side locked; crossing axis flags warning |
| Prop state | `Prop` node + `LOCATED_AT` / `HELD_BY` edges | Position and state tracked across shots |
| Shot order | `Shot` → `PRECEDES` → `Shot` edge | Anchor frame chaining follows graph edges |
| Color bible | `Scene` → `HAS_COLOR_BIBLE` → `ColorBible` node | Color grade parameters locked per scene |

### MCP Tool Integration

When the agent calls `graph_context` on a Scene node, it receives:
```json
{
  "scene": "alley_night",
  "lighting_key": {...},
  "color_bible": {...},
  "axis_of_action": {"line": "elena-to-door", "camera_side": "left"},
  "shots": ["S01A", "S01B", "S01C"],
  "props": [
    {"name": "coffee_cup", "state": "full", "position": "table center"}
  ],
  "continuity_warnings": [
    "S01B crosses axis of action",
    "S01C lighting temp shifted 400K from scene key"
  ]
}
```

When the agent calls `graph_detect_changes` after modifying a prop:
```json
{
  "changed": ["coffee_cup"],
  "affected_shots": ["S01A", "S01B", "S01C"],
  "risk_level": "MEDIUM",
  "warning": "Prop state change affects 3 shots. Regenerate with new state."
}
```

---

## 11. QUICK REFERENCE: CONTINUITY DESCRIPTOR MATRIX

Use this matrix to rapidly build continuity constraints by selecting one item from each column.

| Shot Type | Axis Side | Lighting Key | Camera | Motion | Anchor Strategy |
|-----------|-----------|--------------|--------|--------|---------------|
| Wide (EST) | Neutral | Scene master key | Static | None | Master anchor frame |
| Medium (MS) | Left | Scene key + fill | Dolly-in | Subtle | Chain from wide |
| Close-Up (CU) | Left | Scene key + softer fill | Static | Blink/breathe | Chain from MS |
| Over-Shoulder | Right | Scene key + rim | Static | Head turn | Chain from MS |
| POV | Subject | Scene key + lens distortion | Handheld subtle | Gaze movement | Chain from CU |
| Insert | Neutral | Practical light only | Static | None | Independent |

---

## 12. ADVANCED TECHNIQUES

### The Transition Shot Arsenal

Use these shots to hide generation seams and reset viewer perception between character-heavy scenes: [^44^]

| Transition Type | Description | When to Use |
|---------------|-------------|-------------|
| **Prop Close-Up** | Detail shot of object, no face visible | Hide facial drift between emotional beats |
| **Silhouette Walk** | Character passes camera as dark shape | Hide outfit detail drift |
| **Environment Insert** | Background-only establishing shot | Reset geography, hide character inconsistency |
| **POV Cutaway** | Character's view of environment | Shift perspective without showing character |
| **Reaction Shot** | Secondary character reaction | Bridge dialogue without showing primary |
| **Empty Frame** | No characters, just environment | Hard reset, allows lighting/color adjustment |

### The "Continuity Pass" Workflow

After generating all shots for a scene:
1. **Frame scrub:** Review every frame for facial drift, prop state, lighting pop.
2. **Side-by-side:** Compare Shot N and Shot N+1 on screen simultaneously.
3. **Drift log:** Document inconsistencies in `.project-graph/continuity_log.json`.
4. **Regenerate list:** Use `graph_impact` to identify minimum shots to regenerate.
5. **Color match:** Apply scene color bible as LUT across all shots in post.

### Temporal Coherence for Video Models

When using LTX 2.3 or similar video models:
- **Generate in short bursts:** 5–8 seconds maximum per clip. [^44^]
- **Use keyframes:** Define start frame + end frame, let model interpolate. [^44^]
- **Motion prompt discipline:** One action per prompt. Don't ask for "running while smiling while camera orbiting." [^44^]
- **Deflicker in post:** Apply temporal smoothing filters (EbSynth, frame interpolation).

---

## 13. SOURCES & REFERENCES

- Adobe, "What is continuity editing in film?" [^46^]
- Beverly Boy Productions, "Why is Lighting Continuity Important in Film?" [^48^]
- Renderfire, "Character Consistency in AI Video: Techniques That Actually Work" [^43^]
- Neolemon, "How to Create Consistent Characters in AI Videos" [^44^]
- Artlist, "Consistent Character AI: Pro Tips & Workflow" [^45^]
- Tella, "Color Grading Definition" [^47^]
- Reddit r/StableDiffusion, "AI-generated video visual continuity" [^49^]

---

## 14. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering traditional continuity editing (180-degree rule, eyeline match, match cuts), shot planning, lighting/color/prop continuity, AI-native anti-drift workflows (anchor frames, IP adapters, frame-to-frame chaining), continuity bible structure, and project graph graph enforcement.
