---
name: minimax_h3_camera_movement_language
description: "Write H3 camera as type, amplitude, speed."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, h3, camera, cinematography]
    category: video-generation
    related_skills: [minimax_h3_prompt_engineering_master, ltx23_camera_movement_language, wan_camera_motion_control]
---

# MiniMax H3 Camera Movement Language

Official H3 camera is **not** LTX (`camera pans left` as a labeled clause) and **not** Wan Fun Camera nodes. It is a **natural-English action** inside the shot: **motion type + amplitude + speed**.

Source of record: MiniMax `VIDEO_PROMPT_WRITING_GUIDE_base_en.md` §4.3.

## When to Use

- Any H3 T2VA / I2VA / FL2VA / L2VA / Ref2VA
- User stacked `dolly + crane + orbit` in one sentence
- Cuts appearing when they only wanted a closer framing

Don't use for: look/style (master), dialogue/foley (audio skill), identity jobs (reference skill).

## Three dimensions

A complete expression names how the camera moves, then adds range and pace **only when they matter**. Medium amplitude and normal speed are usually omitted.

```
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

Write it **inside** the shot paragraph. Do **not** stack labels at the end (`camera: dolly-in, slow, handheld, 35mm`).

## Official motion-type vocabulary

| Type | What actually changes |
| --- | --- |
| `Zoom In` / `Zoom Out` | Focal length changes; camera body stays put |
| `Push In` / `Pull Out` | Camera body moves toward / away |
| `Pan Left` / `Pan Right` | Body stays; lens pivots horizontally |
| `Truck Left` / `Truck Right` | Whole camera translates horizontally |
| `Tilt Up` / `Tilt Down` | Body stays; lens pivots vertically |
| `Pedestal Up` / `Pedestal Down` | Whole camera rises / lowers |
| `Arc Shot` | Camera travels an arc around the subject |
| `Tracking Shot` | Camera follows a moving subject |
| `Static Shot` | Position and lens stay still |
| `Shake Slightly` / `Shake Strongly` | Controlled instability |
| `POV` | Subject's viewpoint |
| `Roll Clockwise` / `Roll Counterclockwise` | Rotation around the lens axis |

Amplitude: `with small amplitude` (composition stays readable) or `with large amplitude` (reveals substantially more space).

Speed: `at slow speed` (inspect / product) or `at fast speed` (reveal still physically legible).

Prompt phrasing uses the English action (`pushes in`, `trucks right`), not the table's Title Case as a keyword dump.

## Cuts vs camera

| Situation | Do this |
| --- | --- |
| New subject, space, state, viewpoint, or time | Cut. `[Shot 2] At 00:03.500, the camera cuts to…` |
| Only distance or a slight angle change | Camera motion in the **same** shot |
| FL2VA path between two stills | **One continuous shot** unless the user asked for cuts |
| User asked for dissolve / fade / wipe | Name that transition; otherwise ordinary cut verbs only |

Ordinary cut verbs: `the camera cuts to`, `the shot cuts to`, `the shot transitions to`, `the shot changes to`, `the shot switches to`.

Do not timestamp Shot 1. Later cut times are strictly increasing `MM:SS.mmm` inside the clip duration.

## One move per shot

Stacked pan + zoom + orbit is the H3 wobble pattern. If you need a new geometry, **cut** and start a new shot with one move.

Handheld: `Shake Slightly` **or** a named move, not both fighting.

## Keyframe tasks

- **I2VA:** camera develops **forward** from Picture 1. Don't invent a new opening composition.
- **FL2VA:** camera is part of the **path**. Last frame is the landing composition, not a second mood board.
- **L2VA:** camera **converges** on the still at end time.

## Anti-patterns

| Bad | Why | Good |
| --- | --- | --- |
| `camera: dolly-in, slow` | Label stack; Base was trained on sentences | `The camera pushes in with small amplitude at slow speed.` |
| `cinematic camera` | No verb | Name type + (optional) amplitude/speed |
| Cut to a tighter shot of the same beat | Wasted cut; interpolation smear | Push in / zoom in in-shot |
| Three verbs in one shot | Fighting motion | One verb; cut if the geography changes |

## Verification

- Each shot has **one** camera verb (or explicit static)
- Amplitude/speed present only when they change the result
- Cuts introduce new information
- FL2VA is one shot unless cuts were requested
- No LTX labeled `Camera/Lens:` block, no Wan Fun Camera node language
