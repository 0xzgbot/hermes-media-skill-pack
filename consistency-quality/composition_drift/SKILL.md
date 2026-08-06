# SKILL: Composition Drift
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of preventing and correcting compositional instability in AI-generated imagery and video. Composition drift occurs when the subject migrates from intended position (rule of thirds, center frame, etc.) toward the center or edge, when framing changes between generations, or when video subjects drift across the frame over time. This skill provides re-anchoring vocabulary and stability techniques [^84^].

### TRIGGER KEYWORDS
composition drift, framing drift, subject drift, position drift, framing instability, subject migration, composition instability, horizon drift, video drift, frame position, camera drift, framing consistency, composition lock

### CORE RULES
- Specify absolute subject position: "subject positioned at left rule-of-thirds intersection"
- Name the shot type explicitly: "medium close-up from chest to top of head"
- Horizon line must be specified in landscape shots: "horizon at lower-third"
- For video: "subject remains at [position] throughout clip" prevents temporal drift
- Avoid vague compositional language: "framed nicely" does nothing; "centered in frame, waist-up portrait" works
- Background anchor objects help stabilize video composition: name them
- Specify camera distance and angle: "camera at eye level, 3 feet from subject, slightly right of center"

---

### DETECTION SIGNALS

**Position Drift:**
- Subject starts at rule-of-thirds intersection but drifts toward center
- Subject placed at edge of frame without narrative reason
- Subject partially cut off by frame edge (unintentional)
- Eyes not on upper third line (too high or too low)
- Horizon line tilting or migrating up/down frame

**Framing Inconsistency:**
- Same character framed differently across series (medium shot → close-up without prompt change)
- Camera distance varying between generations
- Angle shifting (eye level → high angle) without instruction
- Background elements changing position relative to subject

**Video-Specific Drift:**
- Subject migrating from left third to center over 4–6 seconds [^84^]
- Camera "forgetting" the grid as clip progresses [^84^]
- Horizon tilting during panning shots
- Framing tightening or loosening without camera movement cue

---

### RE-ANCHORING VOCABULARY

**Rule of Thirds Anchors:**
```
rule of thirds composition, subject at left third intersection, subject at right third intersection, eyes on upper third line, horizon on lower third line, negative space in left two-thirds, negative space in right two-thirds
```

**Center Frame Anchors:**
```
subject centered in frame, symmetrical composition, subject in geometric center, balanced framing, centered portrait, direct center composition
```

**Edge Anchors:**
```
subject at left edge of frame, subject at right edge, subject entering from left, subject exiting right, frame edge cutting subject at waist, subject partially out of frame
```

**Headroom & Lead Room:**
```
generous headroom above subject, tight headroom, leading space in front of subject, subject looking into frame with space ahead, subject at frame edge with no lead room (tension)
```

**Horizon Anchors:**
```
horizon line at lower third, horizon line at center (drama), horizon line at upper third (ground emphasis), level horizon, straight horizon, diagonal horizon (dynamic)
```

**Depth Plane Anchors:**
```
foreground [element], midground subject, background [element], three-plane composition, layered depth, subject in midground with foreground interest and background context
```

---

### FIX STRATEGIES

**1. The Grid Lock**
- Explicitly state grid position:
  - `subject positioned at left third intersection`
  - `eyes aligned with upper horizontal third line`
  - `horizon placed on lower third`
- Most effective for static compositions

**2. The Negative Space Command**
- `generous negative space to left of subject`
- `empty space above subject creating headroom`
- Physical space anchors prevent migration

**3. The Environmental Persistence**
- Describe background elements as static anchors [^84^]:
  - `static background elements anchoring composition`
  - `heavy architectural elements fixed in frame`
- Environmental weight prevents subject drift

**4. The Shot Duration Limit**
- For video: keep clips 4–6 seconds for maximum stability [^84^]
- Longer clips = model "forgets" compositional grid
- Break long scenes into 4–6 second segments

**5. The Recursive Refinement**
- Use final frame of drifting clip as "Master Reference" for next segment [^84^]
- Chain segments with consistent end/start frames
- Prevents reset drift at clip boundaries

**6. The 3-Variation Rule**
- Generate 3 variations simultaneously [^84^]
- Probabilistic nature yields at least one stable clip
- Select stable version, discard drifters

**7. The Camera Movement Explicit**
- `static camera, locked tripod, no camera movement`
- `slow dolly push-in maintaining subject position`
- `steady pan keeping subject at left third`
- Explicit movement prevents unintended drift

**8. The Framing Verb**
- `medium shot framing subject from waist up`
- `close-up framing head and shoulders`
- `wide shot framing subject in environment`
- Shot type verbs lock framing scale

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Positive: `(rule of thirds:1.2), subject at left third, balanced composition`
- Negative: `centered subject, bad composition, cropped, cut off, out of frame`
- Use `centered` or `rule of thirds` explicitly; model defaults to center if unspecified

**Flux / Flux2:**
- Place composition instruction early (first 10–15 words)
- Use concrete positional language: `subject at left third`, `eyes on upper third line`
- No negative prompts; rely on positive anchoring

**LTX Video:**
- Compositional drift is primary video artifact [^84^]
- Subject migrates from rule of thirds toward center over time
- Guardrail: `stable subject position across frames, no compositional drift, locked framing`
- Use `static camera` or explicit movement path to prevent drift
- 4–6 second clip maximum for grid stability [^84^]

---

### EXAMPLE FIX PROMPTS

**Fix: Rule of Thirds Anchor (Flux):**
> `Rule of thirds composition, subject positioned at left third intersection, eyes aligned with upper horizontal third line, generous negative space to right of subject, horizon on lower third, static camera, photorealistic landscape portrait`

**Fix: Center Frame Lock (SDXL):**
> Positive: `Symmetrical centered composition, subject in geometric center of frame, balanced framing, equal negative space on all sides, direct center portrait`
> Negative: `off-center, asymmetric, bad composition, cut off, out of frame`

**Fix: Video Drift Prevention (LTX):**
> `Scene: City street. Subject: Man walking. Camera/Lens: Static tripod-locked, subject at left third. Style: Documentary. Motion: Walking left to right. Guardrails: Stable subject position across all frames, no migration toward center, locked framing, 4-second clip.`

---

### DETECTION CHECKLIST
- [ ] Subject at intended grid position?
- [ ] Eyes on upper third line (for portraits)?
- [ ] Horizon level and at intended height?
- [ ] Headroom appropriate (not too much/little)?
- [ ] Lead room in front of subject (if moving/looking)?
- [ ] Framing consistent across series (MS/MS/MS, not MS/CU/WS)?
- [ ] Video: Subject stable across frames, no migration?
- [ ] Video: Horizon stable during camera movement?
- [ ] No unintentional cropping of subject?

---

### TECHNICAL NOTES FOR AI GENERATION
- Models default to center-frame composition if not specified
- Rule of thirds must be explicitly requested; not automatic
- Video compositional drift worsens with clip length — 4–6 seconds is stability sweet spot [^84^]
- Environmental persistence (static background elements) anchors subject position [^84^]
- The 3-variation rule is essential for video — generate multiples and select stable [^84^]
- Recursive refinement (using final frame as next reference) maintains continuity [^84^]
- For commercial work, always specify shot type (MS, CU, WS) to lock framing scale
