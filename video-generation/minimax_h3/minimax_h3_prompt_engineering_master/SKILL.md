---
name: minimax_h3_prompt_engineering_master
description: "Write MiniMax H3 Base and Ref2VA prompts."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, hailuo, h3, prompting, video]
    category: video-generation
    related_skills: [minimax_h3, minimax_h3_camera_movement_language, minimax_h3_audio_direction, minimax_h3_reference_control, minimax_h3_technical_configuration]
---

# SKILL: MiniMax H3 Prompt Engineering Master
## Hermes Agent — Hailuo 3 / MiniMax-H3 prompting doctrine

### DESCRIPTION

Authoritative prompting control for **MiniMax H3**. H3 is a joint audio-video DiT that always emits **32 kHz stereo**. It was trained on a **structured intermediate representation** that hosted **H3-Context-IR** normally writes for you. Open **H3-Base** does not include that compiler — you write the IR yourself, or quality collapses.

This skill is the dialect. Camera vocabulary → `minimax_h3_camera_movement_language`. Soundtrack → `minimax_h3_audio_direction`. Omni-reference / six-section rewrite → `minimax_h3_reference_control`. Graphs, duration grid, license → `minimax_h3_technical_configuration`.

Do **not** paste an LTX single paragraph. Do **not** paste Wan `@Image1` / `Shot 1 [0-5s]`. Do **not** assume Hailuo/fal quality from a local Comfy run of the same words.

Sources of record: MiniMax `VIDEO_PROMPT_WRITING_GUIDE_base_en.md` and `VIDEO_PROMPT_WRITING_GUIDE_ref_en.md` (Hugging Face `MiniMaxAI/MiniMax-H3`).

---

### TECHNICAL PARAMETERS (prompting consequences)

| Fact | Value |
| --- | --- |
| Family | MiniMax H3 / Hailuo 3 |
| Open piece | H3-Base ~33B, **community license** (not Apache) |
| Encoder | Qwen3-VL-32B hidden states (layer 50) — dense English, not tag soup |
| Local canvas | **768 px short edge** (e.g. ~1344×768 16:9) |
| Hosted finish | **2K** via H3-Regenerate-2K only |
| Duration | **4–15 s** at **24 fps**. Requested length snaps to a **17k+5 frame grid** (~5.17 s for a 5 s ask) |
| Audio | **Always generated**, 32 kHz stereo. Unspecified = garbage or invented room tone |
| Prompt budget (fal / API) | up to **~7,000 characters** |
| Negative prompt | **Not supported.** Guidance is distilled into the weights. No `guidance_scale`. |
| Dialogue languages | Stable: AR, ZH, EN, FR, DE, IT, JA, KO, PT, RU, ES |
| Official IR length | Context-IR `integrated_multimodal_description` / `detailed_description` typically **350–500 English words** for generation tasks |

**Three modules:**

| Module | Where | What it does to your prompt |
| --- | --- | --- |
| H3-Context-IR | Hosted only | Compiles messy briefs into Base or Full-Reference IR |
| H3-Base | Open weights / Comfy | Executes **exactly** what you wrote |
| H3-Regenerate-2K | Hosted only | 768p → 2K |

Local H3 **cannot** fix a lazy brief.

---

### CHOOSE THE FORMAT BEFORE YOU WRITE

The uploaded asset does not decide the task. **Role** does.

| Task | When | Prompt shape |
| --- | --- | --- |
| **T2VA** | No frame anchors | Three core fields. No alignment line. |
| **I2VA** | One still = **literal first frame** | Official first-frame instruction + three fields. |
| **FL2VA** | Two stills = first **and** last frames | Alignment line + path between them. Prefer **one shot**. |
| **L2VA** | One still = **literal last frame** | Alignment line. Image belongs to **final** `[Shot N]`, not Shot 1. |
| **Ref2VA / Full-Reference** | Identity, style, motion, voice, edit source, continuation | **Six sections.** Not a longer Base prompt. |

If the still is mood/identity and **not** a frame at 0.00 or end time → Full-Reference, not I2VA.

---

### BASE FORMAT (T2VA / I2VA / FL2VA / L2VA)

#### Alignment instruction (Part One) — image tasks only

Must be the **first line**, then one blank line, then the three fields.

**I2VA** (always this sentence):

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

**FL2VA** (`N` = actual last shot index; `S.SS` = duration to two decimals):

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.
```

**L2VA**:

```
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.
```

#### Three core fields (Part Two)

```
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

| Field | Contains | Does not contain |
| --- | --- | --- |
| `integrated_multimodal_description` | Style, composition, subjects, actions, cuts, speakers, `<d>` dialogue/singing, diegetic music, shot-synced foley | Plot summary with no visible/audible events |
| `overall_soundscape` | 1–4 sentences: ambience, physical action, non-verbal human sound | Dialogue, singing, diegetic music (those stay in the body) |
| `non_diegetic_music` | 1–3 sentences: instrumentation, tempo, rhythm, dynamics. Characters cannot hear this. | Abstract mood words ("sad cinematic"), artist/track names |

`N/A` is legal: soundscape **only** when the user wants **complete silence**; music whenever there is **no audience-only score**.

#### Shot grammar (hard rules)

- **No timestamp on `[Shot 1]`.** Open with style + initial composition.
- Later shots: `[Shot 2] At 00:03.500, the camera cuts to…` — **absolute** time, strictly increasing, inside duration. Format `MM:SS.mmm`.
- Ordinary cut verbs: `the camera cuts to` / `the shot cuts to` / `the shot transitions to` / `the shot changes to` / `the shot switches to`.
- Cross-dissolve, fade, wipe: **only if explicitly requested**.
- A cut must introduce new **subject, space, state, viewpoint, or time**. Distance or slight angle change → **camera motion**, not a cut.
- Style tokens at Shot 1: `Cinematic`, `live-action`, `2D-animated`, `3D CG`, `claymation`, `watercolor`, `vintage film`. Keyframe tasks: derive style from the still.

#### Keyframe path logic

| Task | Structure |
| --- | --- |
| I2VA | first-frame anchor → action onset → continuous development → result. Preserve identity, clothing, colors, key objects, spatial relationships. Do not novelize wardrobe already in the still. |
| FL2VA | first-frame state → observable intermediate changes → narrowing differences → last-frame state. **Single shot preferred.** Last frame is reached by the **final** `[Shot N]`. Do not re-describe two stills; describe the **path**. |
| L2VA | plausible preceding state → action/transition → gradual convergence in the final shot → last-frame landing. The still is **not** Shot 1's picture. |

#### Camera (summary — full table in camera skill)

Write **natural English** inside the shot: **motion type + amplitude + speed**. Not `camera: dolly-in, slow`.

```
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera holds a static shot as the runner exits the frame.
```

One move per shot. Amplitude/speed omitted when medium/normal.

#### Speakers and dialogue (summary — full rules in audio skill)

- Stable IDs `(S1)`, `(S2)`, joint `(S1,S2)`. Silent characters get **no** ID.
- First appearance: age/gender/timbre/accent/on-screen, **outside** `<d>`.
- Inside `<d>`: **only** `[Language]` + verbatim words and punctuation. Do not translate or paraphrase.
- Voiceover: exact phrase `says in an off-screen voiceover`, then **lips remain completely closed**.
- Line across a cut: `<scenetrans>` + continuity sentence. Truncated by clip end: `<cutoff>`.
- On-screen type: English double quotes, original language preserved: `A red neon sign reading "营业中"`.

---

### FULL-REFERENCE FORMAT (Ref2VA)

Not Base-plus-jobs. Six English sections **in this order**:

1. `subject_definitions` — `<Subject N>`, standalone `<Picture N>` only if it is a **frame/storyboard anchor**, `<Video N>` for edit/continue/structure, `<Audio N>` for copy/timbre/BGM.
2. `summary` — one paragraph starting with `[task types]`. Combine with `+`, no repeats. Types: `keyframe completion`, `reference generation`, `video editing`, `video continuation`, `audio reuse`, `audio reference`.
3. `retention_analysis` — one line per label. Visual: `fully_preserved` / `partially_preserved` / `attribute_transfer` / `weak_reference`. Audio: `fully_copy` / `partially_copy` / `reference` / `weak_reference`.
4. `detailed_description` — style in **1–2 sentences before `[Shot 1]`**. Insert labels where they apply. Generation tasks: **350–500 words**. Editing tasks: scale with source complexity.
5. `overall_soundscape`
6. `non_diegetic_music`

Do **not** put a standalone `<Picture>` line for a still that only defines a character — cite it inside `<Subject>`. `<Video>` is structure/edit source; a person pulled from that clip is still a `<Subject>`. See `minimax_h3_reference_control`.

---

### API / FAL VARIANT (Context-IR in the path)

On Hailuo / fal, timed blocks also work because IR rewrites them:

```
[0 to 2 seconds] High-angle overhead …
[2 to 4 seconds] Smoothly push in to her right arm …
```

Use this **only** when you know Context-IR is in the path. If the same prompt is weaker in Comfy, convert to official Base or Full-Reference.

Hosted extras that work on API and are **not** the Base spec: explicit "do not" constraints (`No soft dissolves`, `Do not introduce extra people`). Keep Base prompts closer to official sections.

---

### SIX ELEMENTS (ORDER) — BASE PATH

1. Alignment instruction (I2VA / FL2VA / L2VA only)
2. Shot 1 — style, composition, subject, first action, one camera move
3. Shot 2…N — absolute cut times; one job per shot; cut only if new information
4. Speakers + `<d>` lines inside the body (budget: 1–2 sentences per ~5 s)
5. `overall_soundscape` — diegetic, or `N/A`
6. `non_diegetic_music` — concrete instruments, or `N/A`

---

### ANTI-PATTERNS

| Anti-pattern | What happens | Fix |
| --- | --- | --- |
| Twelve-word T2VA, no audio fields | Weird speech-like noise, random room tone | Write both audio fields or explicit `N/A` |
| LTX single paragraph | Weak structure on Base | Convert to `[Shot N]` + three fields |
| Wan `Shot 1 [0-5s]` / `@Image1` | Wrong dialect | Base timestamps or Full-Reference labels |
| Timestamp on Shot 1 | Guide violation | Drop it |
| Restating the line in soundscape | Double dialogue | Soundscape = foley/ambience only |
| Artist-named songs | License + wrong mix | Genre, tempo, instruments |
| Overlong spoken lines | Rushed delivery, audio past last frame | Cut the line |
| Mood-board stills on I2VA | Fights the "this IS frame 0" contract | Switch to Full-Reference |
| FL2VA with many cuts | Interpolation smears | One continuous shot |
| L2VA treating the still as Shot 1 | Ending never lands | Align still to **end** time, infer the opening |
| Stacked camera moves | Fighting motion | One move per shot |
| Abstract "sad cinematic score" | Weak music | Concrete instruments and hits |
| HUD / readable text without quotes | Glyph noise | Exact string in `"..."` |
| Negative prompt / CFG | Ignored; no guider | Put constraints in the positive body (API "do not" only on hosted) |
| FL2VA checkpoint on R2V graph | Silent fail / garbage | Switch to ref2va |

---

### EXAMPLE — T2VA (official shape)

```
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters of a small street bakery before sunrise. The camera pushes in with small amplitude at slow speed as the middle-aged baker with a calm, slightly raspy voice (S1) places a fresh loaf on the wooden counter and says: <d>[English] First batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a close-up of steam rising from the sliced bread while the baker's final words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as trays clink softly inside the bakery. The doorbell rings once, followed by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo, joined by sparse upright-bass notes and a gentle fade at the end.
```

---

### EXAMPLE — I2VA

```
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, the young woman shown in <Picture 1> remains beside the rain-covered train window, preserving her appearance, clothing, seat position, and the carriage layout. The camera trucks right with small amplitude at slow speed as she lifts her gaze from the folded letter toward the passing city lights. The quiet, breathy young woman (S1) says: <d>[English] I get off at the next station.</d> She folds the letter along its existing crease.

overall_soundscape: The train wheels produce a steady metallic rhythm beneath a low ventilation hum. Rain ticks against the window while paper rustles softly in her hands.

non_diegetic_music: Sustained cello notes at a slow tempo with widely spaced piano tones, gradually decreasing in volume.
```

---

### EXAMPLE — FL2VA (8 s, single shot, no score)

```
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a rain-soaked cyclist begins in the position and framing established by Picture 1, holding a closed black umbrella beside a silver bicycle. The camera pulls out with small amplitude at slow speed as she releases the bicycle handle, raises the umbrella above her shoulder, and presses the runner upward until the canopy opens. Water rolls from the expanding fabric while she steps beneath it, rotates the handle into the final angle, and settles into the pose, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: Rain falls steadily on the pavement, followed by the metallic click of the umbrella runner and the soft snap of the canopy opening. Water drips from the bicycle frame as distant traffic passes.

non_diegetic_music: N/A
```

---

### EXAMPLE — API timed brand beat (Context-IR path only)

```
Use Image 1 for mood and film texture; Image 2 for the talent.

[0 to 3 seconds] Wide, desert highway, vintage car. Slow push toward the woman from Image 2.
[3 to 8 seconds] She opens the trunk and lifts the bag. Fine grain, restrained color.
[8 to 12 seconds] Shared look with the man; then she walks away carrying the bag.

Audio: cloth, trunk latch, light wind, no vocals.
Do not add logos or extra people.
```

---

### LOCAL vs HOSTED CHECKLIST

- Comfy first success = **MP4 containing stereo**, not a pretty frame. Silent file → audio VAE not wired.
- Iterate 768p locally; 2K is a **purchase**, not a missing node.
- If hosted looks good and local does not: you skipped IR. Convert to official Base/Full-Reference.
- Weights: community license (territory, attribution, no distillation). API is a different contract.

### VERIFICATION

- Format named: T2VA / I2VA / FL2VA / L2VA / Full-Reference
- Shot 1 has no timestamp (Base and Full-Reference bodies)
- Every later shot has a strictly increasing `At MM:SS.mmm`
- Image tasks include the official alignment sentence
- FL2VA is one shot unless cuts were requested
- Dialogue is inside `<d>[Language] …</d>` verbatim
- Soundscape has no copied dialogue; music is instruments or `N/A`
- Each attached file has a job (Base informal) or a Full-Reference label
- One camera move per shot
- Duration in the 4–15 s band
