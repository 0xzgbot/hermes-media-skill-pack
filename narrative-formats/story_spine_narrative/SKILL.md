# SKILL: Story Spine / Narrative
## Domain: Three-Act Structure, Emotional Beats, Scene Sequencing, Character Arcs
## Version: 1.0
## For: Hermes Agent — Plot Architecture & Scene Planning

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete narrative architecture system — from the three-act structure and 11 story beats to emotional character arcs, scene sequencing logic, and the specific translation of plot into visual shots. It covers the Pixar Story Spine, Save the Cat beat sheet, Hero's Journey, and the practical workflow for turning a story into a production shot list.

When this skill is active, the agent should:
- Build stories using proven structural templates (3-act, 11 beats, Hero's Journey)
- Map emotional arcs to visual color/lighting shifts
- Sequence scenes using cause-and-effect logic
- Translate plot beats into specific shot types and camera movements
- Use project graph to track story state across the project graph

---

## 2. THE THREE-ACT STRUCTURE

The foundation of all screen narrative. [^80^] [^82^]

### Act 1: Setup (25%)

| Beat | Purpose | Visual Translation |
|------|---------|-------------------|
| **Opening Image** | Establish world, tone, protagonist's "before" state | Wide establishing shot, warm/safe lighting, character in comfortable environment |
| **Theme Stated** | Hint at what the story is really about | Dialogue scene with subtle visual metaphor in background |
| **Setup** | Introduce characters, relationships, status quo | Series of medium shots showing daily routine |
| **Catalyst** | Event that disrupts normal life | Sudden lighting shift, unexpected camera movement, prop disruption |
| **Debate** | Protagonist hesitates; should they act? | Close-up on conflicted expression, static camera, internal space |

### Act 2A: Confrontation (25%)

| Beat | Purpose | Visual Translation |
|------|---------|-------------------|
| **Break into Two** | Protagonist commits to new world | Threshold shot (doorway, bridge, vehicle), lighting changes |
| **B Story** | Relationship/love story begins | Two-shot, warmer lighting, softer focus |
| **Fun and Games** | Promise of the premise; genre delights | Dynamic montage, varied shots, peak visual spectacle |
| **Midpoint** | False victory or false defeat | Dramatic lighting, camera movement, emotional close-up |

### Act 2B: Descent (25%)

| Beat | Purpose | Visual Translation |
|------|---------|-------------------|
| **Bad Guys Close In** | Antagonist gains strength; pressure mounts | Darker lighting, tighter framing, increased shadow |
| **All Is Lost** | Rock bottom; death of hope | Desaturated color, minimal light, extreme close-up or vast empty shot |
| **Dark Night of the Soul** | Protagonist processes defeat | Static long take, single light source, isolation framing |

### Act 3: Resolution (25%)

| Beat | Purpose | Visual Translation |
|------|---------|-------------------|
| **Break into Three** | New plan, new determination | Lighting returns, dynamic camera, forward movement |
| **Finale** | Confrontation and climax | Maximum visual intensity, rapid cuts, saturated color, extreme camera angles |
| **Final Image** | Mirror of opening; show change | Same location/type as opening image but transformed lighting/character state |

---

## 3. THE PIXAR STORY SPINE

Pixar's causal, emotionally-driven structure. [^8^]

### The 7 Sentence Starters

1. **Once upon a time...** — Establish protagonist and world (normal)
2. **Every day...** — Routine / status quo
3. **But one day...** — Inciting incident disrupts normal
4. **Because of that...** — Rising action + consequences (causality!)
5. **Because of that...** — Escalation (repeat as needed)
6. **Until finally...** — Climax / turning point
7. **And ever since then...** — New normal / emotional resolution

### Emotional Arcs (The Internal Spine)

| Film | External Plot | Internal Arc | Visual Color Arc |
|------|--------------|--------------|------------------|
| Toy Story | Toys compete for Andy's love | Woody learns to share | Warm → Tense → Warm |
| Inside Out | Joy tries to save Riley's happiness | Joy learns sadness has value | Bright → Dark → Balanced |
| Up | Carl flies house to Paradise Falls | Carl learns to let go and live | Muted → Dark → Bright |
| Soul | Joe tries to return to his body | Joe learns purpose is living, not achieving | Blue → Dark → Warm |

---

## 4. THE HERO'S JOURNEY (Campbell/Vogler)

| Stage | Description | Visual Translation |
|-------|-------------|-------------------|
| **Ordinary World** | Safe, familiar, limited | Warm, balanced, contained framing |
| **Call to Adventure** | Disruption, invitation | Unusual light, unexpected object, wider frame |
| **Refusal** | Fear, hesitation | Tight framing, shadows, retreating movement |
| **Mentor** | Wisdom, guidance | Soft light, elevated position, two-shot |
| **Crossing Threshold** | Commitment to journey | Threshold framing, lighting shift, forward movement |
| **Tests/Allies/Enemies** | Learning, conflict | Varied environments, dynamic lighting, action coverage |
| **Approach Inmost Cave** | Near the goal, maximum danger | Dark, tight, claustrophobic framing |
| **Ordeal** | Death and rebirth | Extreme contrast, minimal light, transformation moment |
| **Reward** | Seizing the prize | Bright, saturated, triumphant lighting |
| **Road Back** | Return with prize, chased | Dynamic movement, urgent lighting, pursuit framing |
| **Resurrection** | Final test, mastery | Maximum visual intensity, character glow, epic scale |
| **Return with Elixir** | Changed world, wisdom shared | Return to opening location but transformed |

---

## 5. EMOTIONAL BEAT TO VISUAL TRANSLATION

Every emotional beat has a **visual signature**:

| Emotion | Lighting | Color | Camera | Sound |
|---------|----------|-------|--------|-------|
| **Joy** | Bright, even, warm | Saturated primaries | Dynamic, upward movement | Major key, fast tempo |
| **Sadness** | Soft, diffused, cool | Desaturated blue-grey | Static, downward gaze | Minor key, slow tempo |
| **Fear** | Harsh, high-contrast | Cold blue + warm amber | Handheld shake, dutch angle | Dissonant, irregular rhythm |
| **Anger** | Hard, directional | Red dominance | Aggressive movement, push-in | Loud, percussive |
| **Love** | Soft, golden | Warm pink + amber | Slow dolly, two-shot | Romantic melody, strings |
| **Wonder** | Volumetric, glowing | Magenta + cyan | Slow orbit, wide lens | Ethereal, sustained tones |
| **Isolation** | Single source, rim only | Cool monochrome | Telephoto, vast space | Sparse, echoey |
| **Tension** | Strobing, shifting | Magenta/cyan split | Static with sudden movement | Pulsing, building |

---

## 6. SCENE SEQUENCING LOGIC

Scenes must follow **cause-and-effect** logic. Every scene must answer: "Because of the previous scene, therefore this scene."

### The Scene Chain

```
Scene A: Character wants X → tries to get X → fails
    ↓ (therefore)
Scene B: Character now wants Y (consequence of failure) → tries to get Y → partial success
    ↓ (therefore)
Scene C: Character now faces Z (consequence of partial success) → tries to solve Z → ...
```

### production Shot List Generation

For each scene, generate shots in this order:
1. **Establishing shot** — Where are we? What time? What mood?
2. **Master shot** — Who is present? What is their spatial relationship?
3. **Coverage shots** — Emotional beats, one shot per beat
4. **Insert shots** — Props, details, reactions
5. **Transition shot** — How do we leave this scene?

---

## 7. PROJECT GRAPH INTEGRATION

| Narrative Element | project graph node |
|-------------------|------------------|
| Story spine | `Project` → `HAS_STORY` → `Story` node with 7 beats |
| Character arc | `Character` → `HAS_ARC` → `Arc` node with emotional states |
| Scene | `Scene` node with `act`, `beat`, `emotional_state` |
| Shot | `Shot` node with `scene_ref`, `beat_ref`, `emotional_beat` |
| Color arc | `Story` → `HAS_COLOR_ARC` → `ColorArc` node |
| Transition | `Shot` → `PRECEDES` → `Shot` edge with `transition_type` |

**MCP Tool Integration:**
- `graph_context` on Story node returns full spine, color arc, and scene list
- `graph_trace` from Scene A to Scene Z shows the causal chain
- `graph_impact` on emotional beat change shows all affected shots

---

## 8. SKILL STACKING

```
BASE SKILL: Prompt Engineering Core
STRUCTURE SKILL: Story Spine / Narrative (this file)
    └── VOCABULARY: 3-act, 11 beats, Hero's Journey, emotional arc, scene chain
STYLE SKILL: [Any Style Specialist]
    └── VOCABULARY: aesthetic vocabulary
STRUCTURE SKILL: Cinematic Continuity
    └── GRAMMAR: shot lists, temporal coherence, anchor frames
TECH SKILL: ComfyUI/Flux Pipeline
    └── PARAMETERS: sampler, model, CFG
```

---

## 9. QUICK REFERENCE: EMOTION-TO-VISUAL MATRIX

| Emotion | Light Temp | Light Quality | Color | Camera | Depth | Grain |
|---------|-----------|-------------|-------|--------|-------|-------|
| Joy | 5600K | Bright even | Saturated primaries | Dynamic | Deep | None |
| Sadness | 6500K | Soft diffused | Desaturated blue | Static | Shallow | Fine |
| Fear | Mixed | Hard high-contrast | Cold blue + amber | Dutch/handheld | Shallow | Medium |
| Anger | 3200K | Hard directional | Red dominance | Aggressive | Medium | Heavy |
| Love | 2700K | Soft golden | Warm pink + amber | Slow dolly | Very shallow | Fine |
| Wonder | Mixed | Volumetric glowing | Magenta + cyan | Slow orbit | Deep | None |
| Isolation | 9500K | Single rim | Cool mono | Telephoto | Very shallow | Fine |
| Tension | Mixed | Strobing shifting | Magenta/cyan | Static/sudden | Medium | Medium |

---

## 10. SOURCES

- Mikel Murphy, "The Art of Storytelling — Part 3" [^80^]
- NoFilmSchool, "What Is Three Act Structure in Film and TV?" [^82^]
- Reddit r/Screenwriting, "What is the 3 act structure?" [^83^]

---

## 11. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering three-act structure, 11 beats, Pixar Story Spine, Hero's Journey, emotional beat visual translation, scene sequencing, and PROJECT GRAPH INTEGRATION.
