---
name: wan_audio_direction
description: "Direct Wan 3.0 voice, SFX, and music."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wan, wan-3.0, audio, dialogue, foley]
    category: video-generation
    related_skills: [wan_prompt_engineering_master, minimax_h3_audio_direction, sound_design]
---

# Wan Audio Direction

Wan **2.2** local T2V/I2V is usually **silent picture** (S2V is the speech graph). Wan **3.0 / 3.0 Prime** generates **voice + SFX + music in the same pass**, **on by default**. This skill is the 3.0 soundtrack contract. Do not use MiniMax `<d>` tags or `overall_soundscape:` fields here.

## When to Use

- Any Wan 3.0 / Prime generate
- Clip invented VO or BGM you never asked for
- Dialogue timing across a 10–30 s shot list

Don't use for: H3 (`minimax_h3_audio_direction`); LTX (`ltx23_audio_visual_sync`); 2.2 Lightning graphs unless you are on S2V.

## Alibaba's three separate things

Write each as its own sentence. Mixing them into one "cinematic audio" clause is how 3.0 picks a random ballad and a random line.

### 1. Voice

Exact line + delivery + language/accent.

```
She says, 'I told you this would happen.' Fast, a little annoyed, American English.
```

Unspecified → model **invents** lines. Kill: `no voice lines in the whole video.`

Quoted speech is kept more faithfully than paraphrased intent ("she tells him off").

### 2. Sound effects

Object + action + space.

```
A glass falls off the table and shatters on the wood floor, quiet room.
Rain bed under it, tires on wet asphalt, one distant horn.
```

### 3. Music

Named style, not a mood adjective alone.

```
Slow piano under the whole scene.
```

Kill: `no background music.`

Host silent-clip switch (fal `audio: false` / OpenArt Audio off) is faster than arguing with invented score when you will replace audio in post.

## Shot-list audio

Put the line on the shot that owns the mouth.

```
Shot 1 [0-5s]: She walks home in the rain. No dialogue. Rain on jacket, cars in the next street. No background music.
Shot 2 [5-12s]: Close-up. She says, 'You're soaking.' Soft, tired, British English. Cat mew. No background music.
```

If music should cover the whole piece, say so **once** after the shot list, not differently in every shot.

## 2.2 / S2V notes

- S2V-14B: the **audio file** owns timing; prompt is visual performance. Do not write a second lyric.
- Lightning CFG 1: "no music" in a negative box does nothing. Put `no extra people, silent` in the **positive** if you must, or accept silence as the 2.2 default.

## Anti-patterns

| Bad | What happens | Fix |
| --- | --- | --- |
| No audio paragraph on 3.0 | Invented VO + BGM | Specify three layers or explicit bans |
| H3 `non_diegetic_music:` | Ignored / parsed as prose junk | Plain English layers |
| Unquoted "she explains the product" | Paraphrased, often wrong | Exact quoted line |
| Music named as a commercial track | Wrong mix + rights | Genre + instruments |
| Audio on + `no background music` fighting a host default | Sometimes still bleeds | `audio: false` if you will score in post |

## Verification

- 3.0: voice, SFX, music each either specified or explicitly forbidden
- Quoted lines sit on the correct `[t0-t1]` shot
- Silent intent uses host audio toggle **or** both kill phrases
- No `<d>` / `overall_soundscape` H3 fields in the Wan prompt
