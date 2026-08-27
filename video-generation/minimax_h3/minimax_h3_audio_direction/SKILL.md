---
name: minimax_h3_audio_direction
description: "Direct H3 stereo: foley, dialogue, score."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [minimax, h3, audio, foley, dialogue]
    category: video-generation
    related_skills: [minimax_h3_prompt_engineering_master, sound_design, ltx23_audio_visual_sync]
---

# MiniMax H3 Audio Direction

H3 **always** generates **32 kHz stereo** in the same pass as picture. There is no silent default. Unspecified audio is the #1 first-week failure (speech-like garbage, unrequested room tone, invented VO).

Picture dialect lives in `minimax_h3_prompt_engineering_master`. This file is the soundtrack contract from the official Base + Full-Reference guides.

## When to Use

- Any H3 T2VA / I2VA / FL2VA / L2VA / Ref2VA
- Lip-sync, VO, music-video, product foley
- User says the clip "sounds weird" or "talking over nothing"

Don't use for: Flux stills; LTX audio (`ltx23_audio_visual_sync`); Wan 3.0 three-layer prose (`wan_audio_direction`).

## Three disjoint layers

Keep them **separate**. Do not copy a spoken line into the soundscape.

| Layer | Official home | What to write |
| --- | --- | --- |
| **Shot-synced diegetic** | Inside `integrated_multimodal_description` / `detailed_description` | Door slam on the cut, radio in the room, on-screen instrument, `<d>` dialogue/singing |
| **Ambience + physical + non-verbal** | `overall_soundscape` (1–4 English sentences, one paragraph) | Wind, rain, traffic, footsteps, fabric, impacts, breathing, laughter, panting |
| **Audience-only score** | `non_diegetic_music` (1–3 sentences) | Instrumentation, speed, rhythm, dynamic change. Characters cannot hear this. |

**`N/A` rules:**

- Soundscape: `N/A` **only** when the user wants **complete silence** for the whole video.
- Music: `N/A` whenever there is **no** non-diegetic score (FL2VA product paths often want this).

Do **not** use abstract mood words ("uneasy drone", "sad cinematic") in the music field. Name instruments and tempo.

```
overall_soundscape: Steady rain taps against the café windows while low room ambience continues underneath. The entrance bell rings once, followed by wet footsteps and the soft scrape of a chair.

non_diegetic_music: Sparse piano notes at a slow tempo, joined by sustained low strings that gradually increase in volume before fading out.
```

## Dialogue and singing

Official wrapper:

```
The young woman with a quiet, breathy voice (S1) says: <d>[English] I get off at the next station.</d>
The two children (S1,S2) shout together, <d>[English] Wait for us!</d>
```

Hard rules:

- Speakers who vocalize get stable IDs `(S1)`, `(S2)`, joint `(S1,S2)`. Silent characters get **no** ID. Reuse the same ID across shots.
- First appearance: character type, age, gender, on-screen vs off, pitch, timbre, rate, accent — **outside** `<d>`.
- Inside `<d>`: language tag + **verbatim** user words and punctuation. Do not translate, paraphrase, or "improve" the line.
- Delivery notes (clearly / warmly / flatly) stay outside `<d>`. Fancy acting novels degrade sync.
- **Budget:** one or two spoken sentences per ~5 s. Longer → rushed, overrun, lips past last frame.
- Stable languages: Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish.

**Voiceover — exact official phrasing:**

```
The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.
```

**Across a cut / truncated by end:**

- Same line crosses a cut: `<scenetrans>` at both connecting points + `continues seamlessly across the cut` / `carries over from the previous shot`.
- Speech chopped by duration: `<cutoff>`.

Do **not** repeat dialogue, singing, or on-screen music inside `overall_soundscape`.

## Foley that works

H3 is strong on **physical, visible** sound; weak on abstract atmosphere with nothing on screen to own it.

Good: `a cork pop exactly as the cork flies`; `ice tapping crystal as the glass is set down`.

Bad: `sound: a pop`; `uneasy drone` with empty frame.

Layer ambience in **one clause** in the soundscape: rain on glass, low murmur, occasional cup clink.

## Music

- Instrumentation + structure over time (`low drone 0–2 s, pizzicato at 3 s, brass sting at 10 s, freeze last 2 s`).
- Original cue language only. Do not name commercial tracks or artists.
- Singing, radio, TV, phone music the **characters can hear** belong in the multimodal body (diegetic), not `non_diegetic_music`.
- Social-ready ≠ broadcast mix. Plan to replace score for paid ads.

## Reference audio (Full-Reference)

| Marker | Meaning |
| --- | --- |
| `fully_copy` | Entire source is the complete final track |
| `partially_copy` | Part of the timeline / selected layers; other sounds added or removed |
| `reference` | Timbre / rhythm / style only — do **not** carry original dialogue unless asked |
| `weak_reference` | Broad category similarity |

Bind: `<Audio 1> is the voice-timbre reference for <Subject 1> (S1).`

Clone line: match timbre from Audio 1, write the **new** `<d>` words. Clip 2–15 s; **sum of audio refs ≤ 15 s**.

Unintelligible source lyrics: write `[unclear]` — do not guess.

Replace a line in an edit: quote **both** old and new; "adjust performance subtly to match."

## Hosted "do not" (API/IR only)

On Hailuo/fal: `no vocals`, `no speech-like noise`, `no unrequested room tone` can help. On Base, **fill the two fields** with what you want, including `room tone only: refrigeration hum, no voices` or `N/A`.

There is **no negative-prompt slot**.

## Pitfalls

- Silent MP4 = **wiring** (audio VAE), not "H3 refused sound."
- Restating the lyric in soundscape → doubled vocal.
- Multi-speaker order often needs an edit pass.
- Pronunciation varies — test a throwaway before locking a campaign language.
- Inventing `(S1)` for a BGM vocal that no on-screen person produces — use `<Audio N>` as the source instead.

## Verification

- Soundscape contains zero copied `<d>` text
- Every foley event is tied to something visible
- Spoken duration fits the clip
- VO uses `off-screen voiceover` + closed lips
- Music is instruments/tempo or `N/A`
- Stereo present in the file
