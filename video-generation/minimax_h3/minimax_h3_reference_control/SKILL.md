---
name: minimax_h3_reference_control
description: "Bind H3 subjects, pictures, video, audio."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, h3, reference, identity, editing]
    category: video-generation
    related_skills: [minimax_h3_prompt_engineering_master, character_consistency, workflow_ltx_first_last_frame]
---

# MiniMax H3 Reference Control

Highest-leverage H3 habit: **every attached file has a role**, and Full-Reference is a **different format** from Base I2VA/FL2VA.

Source of record: MiniMax `VIDEO_PROMPT_WRITING_GUIDE_ref_en.md`.

## When to Use

- Identity lock, product lock, style/texture from a still
- Motion / camera / edit rhythm from a clip
- Voice from a recording
- Localized edits (swap subject, sign, line, light)
- Continuation from an existing clip

Don't use for: pure T2VA with no assets (master only). Don't use I2VA when the still is a **character sheet**, not frame 0.00.

## Caps

| Input | Max | Duration |
| --- | --- | --- |
| Images | 9 | — |
| Video clips | 3 | each 2–15 s; **sum ≤ 15 s** |
| Audio clips | 3 | each 2–15 s; **sum ≤ 15 s** |
| Total files | 12 | — |

Ref2VA needs **at least one image or video**. Audio alone is rejected. Order is semantic: **reordering the same files is a different request**.

fal T2V aspects: 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. First & last follows the **uploaded image** aspect.

## Frame-anchor vs Full-Reference

| Still's job | Format |
| --- | --- |
| Literal first frame | Base **I2VA** + official alignment sentence |
| Literal first and last | Base **FL2VA** |
| Literal last only | Base **L2VA** — still belongs to **final** `[Shot N]` |
| Character / product / style / motion / voice / edit source | **Full-Reference** six sections |

Mixing "this is my actor" into I2VA fights the contract that Picture 1 **is** frame 0.000.

## Four labels (keep them stable across all six sections)

| Label | Meaning | Standalone line? |
| --- | --- | --- |
| `<Subject N>` | Reusable visible unit: person, animal, object, scene, wardrobe, style, action, pose | Yes — one line per unit |
| `<Picture N>` | Image used as **concrete frame**, keyframe, last frame, or storyboard anchor | Only then. If the still only defines a character, cite it **inside** the Subject line |
| `<Video N>` | Edit source, continuation start, or whole-video camera/cut/rhythm structure | Yes for those jobs. A person taken from the clip is still a Subject |
| `<Audio N>` | Copied or referenced audio signal | Yes |

`<Video>` and `<Audio>` indices are **independent**. The same file may be `<Video 1>` and `<Audio 2>`. A video does **not** auto-create `<Audio>` just because the file has sound.

Examples:

```
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue cardigan, and a thin silver necklace.
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.
<Picture 2> is the first frame of [Shot 1], showing a woman seated beside a café window.
<Picture 3> is a storyboard reference for [Shot 1] and [Shot 2], defining their viewpoint, subject placement, and shot order.
<Video 1> is the source video for the target video edit.
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

## Six sections (fixed order)

### 1. `subject_definitions`

One item per line. Role + features to follow. If a Picture/Video only names the source of a Subject and will not be analyzed separately, cite it inside that Subject — do not add a spare line.

### 2. `summary`

One short paragraph. **Starts with a square-bracketed task-type prefix.** Combine with `+`, do not repeat a type.

| Task type | When |
| --- | --- |
| `keyframe completion` | Image is a concrete first/last/key frame |
| `reference generation` | Guidance for character/scene/style/action/camera/storyboard — **not** a frame and **not** the clip being edited |
| `video editing` | Existing source video is directly modified |
| `video continuation` | New content continues from an existing clip |
| `audio reuse` | Same audio signal copied in full or in part |
| `audio reference` | Timbre/style/beat only; signal not copied |

A video used **only** for camera language is `reference generation`, not `video editing`.

Editing opener after the prefix: `The target video is an edited version of <Video 1>.`

Examples: `[reference generation + audio reference]`, `[video continuation + keyframe completion]`, `[video editing + audio reuse]`.

### 3. `retention_analysis`

One line per label. Do **not** write `(S1)` here.

**Visual** (`Subject` / `Picture` / `Video`): `fully_preserved` | `partially_preserved` | `attribute_transfer` | `weak_reference`

```
<Subject 1> (appears in [Shot 1], [Shot 3]): fully_preserved - ...
<Picture 2> ([Shot 1] first frame): fully_preserved - ...
<Video 1> (cut and pacing structure): weak_reference - ...
```

**Audio:** `fully_copy` | `partially_copy` | `reference` | `weak_reference`

```
<Audio 1>: reference - the target speaker follows <Audio 1>'s voice timbre without copying the original signal.
```

New plot events in the target video are **not** a loss of fidelity.

### 4. `detailed_description`

- Style in **one or two sentences before `[Shot 1]`** (unlike Base, where style opens Shot 1).
- Same shot/camera/`<d>` grammar as Base.
- Insert labels at first appearance and wherever they apply.
- Frame phrasing: `the shot begins from <Picture 1>` / `the shot's keyframe corresponds to <Picture 2>` / `the shot ends on <Picture 3>`.
- Speaking subject: `<Subject 2> (S1) turns … says, <d>[English] …</d>`
- Generation tasks: **350–500 English words**. Dialogue-dense: fit the spoken timeline even if that bends the count. Edits: scale with source complexity.
- Never reduce a shot to a plot summary or a list of reference relationships.

### 5–6. Sound fields

Same as Base. If reference audio is used, state copy vs reference **in the field that matches the audible layer** (ambience in soundscape, audience score in music). Do not repeat `<d>` lyrics there.

## Informal job sentences (API / lazy hosted)

When Context-IR is in the path, informal jobs still help:

```
Use Image 1 for overall mood, location, and film texture.
Use Image 2 for the talent identity (face, hair, wardrobe).
Match Video 1 for shot rhythm, transition language, and music.
Match Audio 1 for the singing voice; the subject in Image 2 performs it.
```

If the same prompt is weaker locally, expand to the six sections.

## Identity preserve list

When a character must survive, enumerate locks (hair, crown, ribbon, layered garments, fasteners, tassels). Same pattern for products and **on-screen type** (exact quoted string).

Wide shots: back / rear three-quarter if you must hide a distant frontal face. Close-up for the face.

## Localized edits

Name the change **and** the freeze:

```
Replace the cat in the video with a dog.
Replace the newspaper with a green hardcover book; everything not listed stays.
In Video 1, replace the woman's line — "<old>" — with Audio 1: "<new>". Adjust performance subtly.
Relight Video 1 from daytime to night. Blocking and lens stay.
```

Edits are instruction lists, not new trailers. Task type: `[video editing + …]`.

## Comfy / Diffusers pitfalls

- **fl2va vs ref2va** checkpoints. R2V graph + FL2VA weights = most-reported silent fail.
- Shipped R2V template may only wire **two** image slots; model accepts nine — extend the graph.
- `ref_image_size`: `match` is faster; `max` preserves up to 2048 short edge and costs time.
- Hosted R2V: overlapping jobs can **429** — queue sequentially.
- Diffusers: no `negative_prompt`, no `guidance_scale`. Reference order is part of the request.

## Verification

- Format is Full-Reference when assets are not literal first/last frames
- Six sections present, labels stable, summary has `[task types]`
- Each Subject/Picture/Video/Audio has a retention line
- `detailed_description` is a timeline, not a relationship list
- Start-frame stills use I2VA/FL2VA alignment **or** a `<Picture>` first-frame definition
- Correct checkpoint for the graph
