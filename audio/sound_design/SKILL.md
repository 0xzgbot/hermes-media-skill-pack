# SKILL: Sound Design
## Domain: Foley, Diegetic/Non-Diegetic Audio, Music Cues, Audio-Visual Correlation
## Version: 1.0
## For: Hermes Agent — Audio Planning & Visual-Audio Synchronization

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete language of cinematic sound design — from diegetic and non-diegetic sound theory to foley techniques, music cue architecture, and the specific correlation between visual elements and their sonic counterparts. It covers the 8-layer soundscape model, trans-diegetic transitions, audio-visual synchronization for AI-generated media, and the integration of sound planning into the visual pipeline.

When this skill is active, the agent should:
- Plan soundscapes using the 8-layer model (dialogue, foley, ambience, spot FX, music, stingers, reverb, silence)
- Distinguish diegetic from non-diegetic sources and exploit the grey area
- Map visual elements to specific sonic signatures
- Use sound as a narrative device, not just decoration
- Integrate audio planning into shot lists and scene bibles

---

## 2. THE SOUNDSCAPE LAYERS

Every scene contains 8 simultaneous layers of sound. [^77^] [^78^] [^79^]

| Layer | Description | Examples | Priority |
|-------|-------------|----------|--------|
| **1. Dialogue** | Spoken words, voiceover, narration | Character speech, internal monologue, phone call | Highest |
| **2. Foley** | Everyday sounds recorded in sync | Footsteps, cloth rustle, object handling, door creaks | High |
| **3. Ambience / Atmos** | Background texture of location | Rain, wind, city traffic, room tone, forest birds | Medium |
| **4. Spot Effects** | Specific non-sync sound events | Gunshot, explosion, glass break, magical sparkle | High |
| **5. Music / Score** | Emotional and thematic underscoring | Orchestral theme, synth pad, diegetic radio music | Variable |
| **6. Stingers** | Sudden musical/sound hits at reveals | Orchestral stab, bass drop, metallic clang | Event-based |
| **7. Reverb / Space** | Acoustic signature of environment | Cathedral echo, bathroom slap, outdoor openness | Always present |
| **8. Silence** | Strategic absence of sound | Tension before explosion, shock after violence | Event-based |

### The Mix Hierarchy
1. Dialogue must be intelligible above all else
2. Foley supports action clarity
3. Ambience creates space without competing
4. Music supports emotion without overwhelming
5. Spot effects punctuate without deafening
6. Silence is the most powerful tool — use it strategically

---

## 3. DIEGETIC VS. NON-DIEGETIC SOUND

The fundamental division in film sound theory. [^77^] [^78^] [^79^] [^81^]

| Type | Definition | Examples | Emotional Function |
|------|-----------|----------|-------------------|
| **Diegetic** | Sound that exists within the film's world; characters can hear it | Footsteps, dialogue, door slam, radio playing in car, rain | Grounds audience in reality, creates immersion |
| **Non-Diegetic** | Sound that exists outside the film's world; only audience hears it | Orchestral score, narrator voiceover, tension sting | Guides emotional response, creates subtext |
| **Trans-Diegetic** | Sound that crosses the boundary — starts diegetic, becomes non-diegetic (or vice versa) | Radio music that becomes score; score that character hums | Blurs reality/emotion boundary, creates fluidity |
| **Acousmatic** | Sound whose source is not yet visible; creates mystery | Off-screen footsteps, distant scream, approaching engine | Builds anticipation, creates unease |

### The Grey Area
Many sounds exist in the grey zone between diegetic and non-diegetic:
- **Amplified foley:** Footsteps louder than realistic = non-diegetic emphasis
- **Reverb manipulation:** Adding cathedral reverb to a small room = non-diegetic gravitas
- **Selective muting:** Pulling down ambience to highlight dialogue = non-diegetic focus
- **Stingers:** Impact sounds that don't match the visual action = non-diegetic punctuation

---

## 4. FOLEY: THE ART OF SYNCHRONIZED SOUND

Foley is the craft of recreating everyday sounds in a studio to match on-screen action. [^79^] [^84^]

### Foley Categories

| Category | Description | Common Props | Examples |
|----------|-------------|--------------|----------|
| **Feet** | Footsteps on various surfaces | Different shoes, gravel box, wood planks, tile | Walking on gravel, running on wood, high heels on marble |
| **Movement** | Cloth, body movement, weight shifts | Various fabrics, leather, chains | Coat rustle, leather creak, chain jingle |
| **Specifics** | Object interactions unique to scene | Anything — coconuts for horse hooves, celery for bones | Door handle, glass clink, sword draw, bone break |

### Foley Techniques

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Sweetening** | Enhancing existing production sound with foley | When production audio is thin or muddy |
| **Replacement** | Completely replacing production sound | When production audio is unusable (wind, noise) |
| **Exaggeration** | Making sounds louder/more present than realistic | For emphasis, comedy, or genre effect |
| **Worldizing** | Playing sounds in real space and re-recording | For authentic reverb and spatial placement |

---

## 5. MUSIC & SCORE ARCHITECTURE

Music in film is not decoration — it is **emotional architecture**.

### Score Types

| Type | Description | Function | Examples |
|------|-------------|----------|----------|
| **Thematic / Leitmotif** | Recurring musical theme associated with character/idea | Recognition, emotional association | Darth Vader's Imperial March, Jaws theme |
| **Mood Underscoring** | Atmospheric pad or texture beneath scene | Sustains emotional tone | Synth drone under tense scene, strings under romance |
| **Mickey Mousing** | Music exactly mirrors action rhythm | Comedy, animation, emphasis | Cartoon bounce, sneaky tiptoe |
| **Source Music** | Diegetic music from within the world | Establishes time/place, character taste | Radio playing 80s hits, character playing piano |
| **Stinger** | Sudden musical hit at reveal or cut | Shock, punctuation, emphasis | Orchestral stab at jump scare |
| **Trans-Diegetic Bridge** | Music crosses diegetic/non-diegetic boundary | Fluid reality, memory, dream | Character hums the score; radio becomes orchestral |

### Music Cue Planning

For each scene, plan:
- **Entry point:** Exact frame where music begins
- **Instrumentation:** Specific instruments for emotional color
- **Tempo / Rhythm:** BPM and rhythmic feel
- **Key / Mode:** Major (happy/bright), minor (sad/tense), modal (mysterious)
- **Dynamics:** Volume arc across scene (pp → ff → pp)
- **Exit point:** How music ends (fade, cut, reverb tail)

---

## 6. AUDIO-VISUAL CORRELATION

Sound and image are not separate — they are **locked in a dance of meaning**.

### Correlation Types

| Type | Description | Example |
|------|-------------|---------|
| **Synchronous** | Sound matches image exactly | Footstep heard as foot hits ground |
| **Asynchronous** | Sound contradicts or diverges from image | Happy music over violent scene (irony) |
| **Counterpoint** | Sound and image work in opposition to create meaning | Cheerful scene with ominous score (dread) |
| **Empathetic** | Sound reinforces image emotion | Sad music over funeral scene |
| **Anempathetic** | Sound is indifferent to image emotion | Neutral ambience over tragedy (alienation) |

### Visual-to-Sound Mapping

| Visual Element | Sonic Signature | Prompt/Planning Term |
|----------------|----------------|---------------------|
| **Rain** | Low-frequency rumble, high-frequency patter, reverb wash | "rain soundscape: low rumble + high patter + reverb wash" |
| **Fire** | Crackle, low roar, wood pop, warm frequency spectrum | "fire sound: crackle + low roar + wood pop" |
| **Neon Sign** | Electrical hum, slight buzz, transformer whine | "neon electrical hum", "transformer buzz" |
| **Crowd** | Indistinct murmur, individual voices emerging | "crowd murmur", "indistinct chatter", "individual voice emergence" |
| **Empty Room** | Room tone, air conditioning, distant traffic, silence | "room tone", "empty space ambience", "distant traffic through wall" |
| **Forest** | Bird calls, wind through leaves, insect drone, twig snap | "forest soundscape", "leaf rustle", "insect drone" |
| **City Night** | Distant siren, car pass-by, dog bark, neon hum | "urban night ambience", "distant siren", "intermittent car pass" |
| **Ocean** | Wave crash, seagull, wind, sand texture | "ocean soundscape", "wave rhythm", "seagull cry" |

---

## 7. SILENCE AS SOUND DESIGN

Silence is not the absence of sound — it is **the most powerful sound**. [^77^]

### Types of Silence

| Type | Description | Effect | When to Use |
|------|-------------|--------|-------------|
| **Dead Silence** | Complete absence of sound | Shock, alienation, supernatural | After loud explosion, supernatural presence |
| **Near-Silence** | Only barely audible sounds remain | Tension, intimacy, focus | Before revelation, intimate moment |
| **Selective Muting** | Specific sounds removed while others remain | Subjectivity, disorientation | Character deafened, shock state |
| **Anticipatory Silence** | Music builds then cuts to silence | Maximum tension, breath-holding | Before jump scare, before important line |

---

## 8. SOUND DESIGN FOR AI-GENERATED MEDIA

AI video generation currently produces silent output. Sound design must be **planned in parallel** and added in post.

### The production Sound Pipeline

```
Visual Generation (ComfyUI/Flux/LTX)
    ↓
Shot List with Sound Notes (per shot)
    ↓
Audio Generation / Library Assembly
    ↓
Synchronization & Mix
    ↓
Final Output
```

### Per-Shot Sound Bible

```yaml
shot: S01A
sound_layers:
  dialogue:
    source: "recorded / AI-generated"
    content: "Elena: 'We need to leave. Now.'"
    treatment: "close mic, slight reverb for alley"
  foley:
    - action: "footsteps on wet asphalt"
      surface: "wet pavement"
      shoes: "boots"
    - action: "jacket rustle"
      material: "leather"
  ambience:
    location: "alley night"
    elements: ["distant traffic", "neon hum", "dripping water"]
  spot_effects:
    - trigger: "door slam"
      sound: "metal door heavy close"
  music:
    cue: "tension_build_01"
    entry: 2.5s into shot
    instrumentation: "synth bass + string drone"
    key: "D minor"
    dynamics: "pp → mp"
    exit: "hard cut at door slam"
  reverb:
    space: "narrow alley, brick walls"
    decay: "1.2 seconds"
    pre-delay: "15ms"
```

---

## 9. PROJECT GRAPH INTEGRATION

| Sound Element | project graph node |
|---------------|------------------|
| Sound bible | `Scene` → `HAS_SOUND_BIBLE` → `SoundBible` node |
| Music cue | `Shot` → `HAS_MUSIC_CUE` → `MusicCue` node |
| Foley list | `Shot` → `HAS_FOLEYS` → `Foley` nodes |
| Ambience | `Scene` → `HAS_AMBIENCE` → `Ambience` node |
| Sound transition | `Shot` → `PRECEDES` → `Shot` edge with `sound_transition` |

**MCP Tool Integration:**
- `graph_context` on Scene returns full sound bible
- `graph_trace` from Shot A to Shot B includes sound continuity check
- `graph_detect_changes` on sound layer changes flags affected shots

---

## 10. SKILL STACKING

```
BASE SKILL: Prompt Engineering Core
AUDIO SKILL: Sound Design (this file)
    └── VOCABULARY: diegetic, non-diegetic, foley, ambience, stinger, silence
STRUCTURE SKILL: Story Spine / Narrative
    └── VOCABULARY: 3-act, emotional beats, scene chain
STYLE SKILL: [Any Style Specialist]
    └── VOCABULARY: aesthetic vocabulary
STRUCTURE SKILL: Cinematic Continuity
    └── GRAMMAR: shot lists, temporal coherence
TECH SKILL: ComfyUI/Flux/LTX Pipeline
    └── PARAMETERS: sampler, model, CFG
```

---

## 11. QUICK REFERENCE: SOUND DESCRIPTOR MATRIX

| Scene Type | Dialogue | Foley | Ambience | Music | Key | Dynamics |
|------------|----------|-------|----------|-------|-----|----------|
| Intimate Conversation | Close mic | Minimal | Room tone | None or sparse | — | pp |
| Action Chase | Shouted | Heavy footsteps, impacts | City traffic | Fast tempo, percussion | Minor | ff |
| Horror Reveal | Scream | None (sudden absence) | Dead silence | Stinger + drone | Atonal | fff |
| Romantic Moment | Whispered | None | Soft wind | Strings, slow tempo | Major | mp |
| Sci-Fi Interior | Radio comm | Mechanical, tech | Ship hum | Synth pad | Modal | p |
| Nature Documentary | Voiceover | Animal movement | Biophony | Minimal piano | Major | pp |

---

## 12. SOURCES

- B2W TV, "Diegetic vs Non-Diegetic Sound | Simple Guide for Creators" [^77^]
- Jan Krzysztof Nosal (IADT), "Diegetic and Non-Diegetic Sound Effects in Film" [^78^]
- Studio 11 Chicago, "Film Sound Design" [^79^]
- WeVideo, "Diegetic vs Non-Diegetic Sound: Differences, Examples" [^81^]
- Gear4Music, "A Guide to Foley Sound and Recording" [^84^]

---

## 13. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering 8-layer soundscape, diegetic/non-diegetic theory, foley techniques, music cue architecture, audio-visual correlation, silence as design, and AI pipeline integration.
