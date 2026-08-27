---
name: wan_reference_control
description: "Bind Wan 3.0 Image, Video, Audio refs."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wan, wan-3.0, reference, identity, omni]
    category: video-generation
    related_skills: [wan_prompt_engineering_master, minimax_h3_reference_control, character_consistency]
---

# Wan Reference Control

Wan **2.2** references are mostly **one start image** (I2V) or **start+end** (FLF2V). Wan **3.0 Omni-Reference** is a different machine: up to **20 files**, plus optional **document / web**, addressed **by order** in the prompt.

Do not use MiniMax `<Subject 1>` / six-section Full-Reference here.

## When to Use

- 3.0 character + product + location + voice in one generate
- Unlabeled uploads scrambling identity
- Doc/PPT/PDF/web → video (thinking required)
- Mixing first/last frames with extra refs

Don't use for: pure 2.2 T2V; H3 Ref2VA (`minimax_h3_reference_control`).

## Caps (3.0 / Prime — verify host)

| Input | Max | Notes |
| --- | --- | --- |
| Images | 10 | Array order = `Image 1` |
| Videos | 5 | Each usable as motion/camera/edit; **sum ≤ 15 s**; some hosts want 16 fps+ |
| Audios | 5 | **Sum ≤ 15 s** |
| Total media | 20 | |
| Document **or** public web URL | 1 | fal `file_url` / `web_url`; **requires `enable_thinking=true`**. Login-walled pages fail. Mutually exclusive on some APIs |

**Keyframe vs reference arrays:** OpenArt allows start frame + end frame **plus** extra refs if you **label which is which**. Runware documents `frameImages` (≤2) **not combining** with `referenceImages`. If the host rejects the payload, split the job: FLF-only **or** omni-ref, not both.

2.2 local: one I2V still, or two FLF stills, matching aspect. No `@` parser.

## Label every file

3.0 will **not** guess that picture 3 is the shop and picture 4 is the jacket.

**Alibaba / OpenArt `@` style:**

```
@Image1 is the woman. @Image2 is the coffee shop. @Audio1 is her voice.
The woman from @Image1 sits by the window in @Image2 and orders a coffee.
```

**fal positional style (same meaning):**

```
the subject in Image 1 walks past Video 1
Video 1 holds Image 1 and plays a country ballad on the chair in Image 2.
```

Reuse the same label wherever it applies. One primary job per file: **identity**, **location**, **product**, **motion plate**, **camera language**, **voice**, **opening frame**, **closing frame**.

## Jobs that work

```
@Image1 is the talent identity (face, hair, wardrobe). Keep it across every shot.
@Image2 is the product. It stays the same object; do not restyle it.
@Video1 is camera language and cut rhythm only — not a new location.
@Audio1 is her speaking voice for the line in Shot 2.
```

I2V subtraction still applies: if `@Image1` is also the start frame, do **not** re-describe wardrobe.

## Documents and URLs

Turn a PPT/PDF/DOC/XLS/MD or a public page into a clip:

- Attach `file_url` **or** `web_url`
- **Must** set `enable_thinking=true`
- Prompt: what the video should **do** with the doc (`explain slide 3 as a 12s product walkthrough, no extra claims`)
- Expansion ON is reasonable here (messy source); still label any extra `@` media

## Identity across 30 s

3.0 advertises multi-dimensional feature alignment (face, prop, scene). Prompt still has to **name** the lock:

```
The courier in @Image1 keeps the same yellow jacket and face in every shot. @Image2 is the alley. Do not add a second courier.
```

Save a character pack in the host's character store when you will reuse them; do not re-upload six near-duplicates unlabeled.

## Localized edits

```
Remove the sunglasses. Her movement and everything else in the video stays the same.
```

Name the change **and** the freeze. Same pattern for light, style, or swapping a voice line.

## Auto Polish vs labels

`enable_prompt_expansion` default **true** rewrites `@Image1` and `[0-5s]` when it "helps." **Off** for production prompts with exact labels. Same seed will not reproduce while expansion is on.

## Anti-patterns

| Bad | Fix |
| --- | --- |
| Six uploads, no labels | Job sentence per file |
| H3 `subject_definitions:` | Wan `@` / `Image 1` prose |
| Doc attached, thinking off | `enable_thinking=true` |
| Mixing frameImages + refs on a host that forbids it | Split jobs |
| Video refs totalling >15 s | Trim or drop clips |
| Re-describing the I2V still | Motion + camera only |

## Verification

- Every attached file appears in the prompt with a job
- `@` index matches upload order (Image 1 = first image slot)
- Doc/web ⇒ thinking on
- Start/end stills named if used
- Expansion off once labels are exact
- 2.2 jobs are I2V/FLF only — no fake 20-ref claims
