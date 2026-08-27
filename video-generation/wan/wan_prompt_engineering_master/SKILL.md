---
name: wan_prompt_engineering_master
description: "Prompt Wan 2.2, 2.7, and 3.0 with control."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [wan, wan-3.0, wan-2.2, prompting, umt5]
    category: video-generation
    related_skills: [wan, wan_camera_motion_control, wan_audio_direction, wan_reference_control, minimax_h3_prompt_engineering_master]
---

# SKILL: Wan Prompt Engineering Master
## Hermes Agent — Wan 2.2 (local) · 2.7 Thinking · 3.0 / 3.0 Prime (new)

### DESCRIPTION

Prompting control for the **Wan family**. Three dialects share a subject, but **tokenizers, audio defaults, and flags differ**:

- **2.2 local (UMT5-XXL, Comfy native / WanVideoWrapper):** cinematic English paragraph, **motion-first on I2V**, dual **high-noise / low-noise** MoE experts. Apache weights. This is what you run on 3090s.
- **2.7 Thinking Mode:** same family, plus a **plan-before-denoise** pass. Structured sequential language (`first` / `then`). ~15 s class. Speed penalty ~30–60%.
- **3.0 / 3.0 Prime (the new Wan, hosted, public Aug 2026):** up to **30 s**, **20 references**, **native audio**. Alibaba formula: subject+place+movement, then `@Image1` jobs, numbered shots with `[0-6s]`, voice / SFX / music as **three layers**. Prompt expansion and thinking are **API flags**, not prompt poetry. **No 3.0 open drop** — last Apache flagship is 2.2.

Never assume 2.2 negatives work at CFG 1 (Lightning). Never assume 3.0 stays silent if you omit sound. Never paste H3 `<d>` / `At 00:03.500` into Wan 3.0.

Camera nodes / FLF / Animate → `wan_camera_motion_control`. 3.0 soundtrack → `wan_audio_direction`. `@` refs / docs → `wan_reference_control`.

---

### WAN 2.2 — LOCAL COMFY (MoE)

**Architecture that changes prompts:**

- Mixture-of-Experts: **high-noise expert** (structure / motion) + **low-noise expert** (detail). Comfy 14B templates load **two** diffusion files. Both must match the task (T2V vs I2V).
- Text encoder: **UMT5-XXL** (often `umt5_xxl_fp8_e4m3fn_scaled`). Natural sentences beat tag soup. Official example prompts are **one dense paragraph**, present tense, appearance + space + implied motion.
- VAE: `wan_2.1_vae` still used under 2.2 graphs.
- Tasks: `T2V-A14B`, `I2V-A14B` (480p & 720p), `TI2V-5B` (hybrid, 720p@24 on 4090-class), `FLF2V`, `Animate-14B` (Mix / Move), `S2V-14B` (speech-to-video).
- Practical start: **832×480, 81 frames**, then step to 720p.
- Lightning / LightX2V distill LoRAs often run **CFG ≈ 1** → classic negative prompts **die**. Use **NAG / ConDelta** nodes, or put constraints in the **positive** ("fixed camera, no extra people").

**2.2 T2V template (order):**

```
[Style / era in a few words]. [Subject + distinctive traits]. [Present-tense action through the clip].
[Environment, light, weather]. [Camera: one move, speed, lens if it matters].
[What must not change: identity, count of people, locked-off vs moving].
```

Sweet spot **~80–120 words** for a 5 s 480p. Under ~20 words: MoE invents extra people and camera.

**2.2 I2V (critical):** The start image owns look. Prompt **only** what happens next + camera + environment motion.

```
From this still, the subject [action]. Camera [one verb + speed]. [Wind / cloth / steam]. Preserve face, wardrobe, and lighting from the image. No new characters.
```

Official long visual paragraphs (cat/surf examples) are **T2V**. On I2V they fight the still — subtract appearance.

**2.2 FLF2V:** Start and end images own the endpoints. Prompt the **transition** (path, speed, whether the camera is allowed to move). Optional positives: `smooth interpolation, consistent lighting`. Optional negatives **only if CFG > 1**.

**2.2 prompt extend:** Official `generate.py --use_prompt_extend` (DashScope) rewrites from the image. Local shop: **off** once the prompt is locked, or you lose I2V subtraction.

---

### WAN 2.7 — THINKING MODE

- Flag: `enable_thinking` / Comfy toggle. Default often **off**.
- Helps: multi-object interaction, cloth/water/hair, camera that must stay legal for the whole clip.
- Prompt: short **structured** beats (`First … Then … Finally …`), spatial anchors (left of frame, sitting on the ledge). Keep thinking prompts tight (~under 75 words of plan); put detail in sequential clauses, not adjective piles.
- Do not enable thinking on a 4-word prompt — nothing to plan.
- Duration class: **15 s**, not 3.0's 30 s. Instruction-style localized edits exist here and carry into 3.0.

---

### WAN 3.0 / 3.0 PRIME — NEW HOSTED LINE

Live on fal (`alibaba/wan-3.0/*` and `wan-3.0-prime/*`) and Alibaba Cloud Model Studio (`wan3.0-video`). Weights **closed**.

**Caps (verify live schema — fal Prime / Model Studio as of Aug 2026):**

| | 3.0 / Prime |
| --- | --- |
| Duration | **2–30 s** (null / omit = **smart duration** from prompt+refs) |
| Resolution | 480p / 720p / 1080p. **No 4K tier** despite random spec tables. fal Prime T2V default often 1080p |
| Aspect | explicit or **adaptive** |
| References | up to **10 images, 5 videos, 5 audios** (20 files); video refs sum **≤ 15 s** (16 fps+ on some hosts); audio refs **≤ 15 s**; optional **one document or public web URL** |
| Address refs | `Image 1` / `Video 1` / `Audio 1` (array order) or `@Image1` / `@Video1` / `@Audio1` |
| Audio | Native; **default on**. Invents VO and BGM if unspecified. fal `audio: false` = silent clip |
| Prompt length | up to **~20,000 characters** |
| Flags | `enable_prompt_expansion` / Auto Polish (default **true**, +20–60 s, **breaks seed lock**); `enable_thinking` (default **false**; **required** for `file_url` / `web_url`) |
| Keyframes vs refs | First/last frames can coexist with other refs on some UIs; Runware: `frameImages` (up to 2) **do not combine** with `referenceImages` — check the host |

**Standard vs Prime:** fal price rails (~1.4×). Lock the prompt on Standard (cheaper), then Prime. There is no published quality table — treat Prime as the finish pass.

**Alibaba starter formula (add one layer at a time):**

1. Subject + place + movement: `A red fox walks across a snowy field at sunrise.`
2. Then look / camera, style, sound.

SPACE checklist (Morphic / Alibaba-style): **Subject → Performance → Ambience → Camera (shot type + one move) → Extra cues (audio, pacing, cut policy).**

**3.0 shot list (anything longer than one beat):**

```
A short story about a girl who finds a stray cat.

Shot 1 [0-5s]: She walks home in the rain and stops under a doorway.
Shot 2 [5-12s]: Close up on a small wet cat looking up at her.
Shot 3 [12-20s]: She kneels down and holds out her hand.
```

Short summary first, then numbered shots with **time ranges**. One clear job per range. If a beat is rushed, **widen that range only**.

**Three things 3.0 decides if you stay silent:**

| Unspecified | Model invents | Kill / force |
| --- | --- | --- |
| Voice lines | Made-up dialogue | `no voice lines in the whole video.` |
| Music | BGM from topic | `no background music.` |
| Number of shots | Cuts when it wants | `one continuous take` / `fixed shot` |
| Duration / aspect | Smart pick 2–30 s + ratio | Set them |

**I2V on 3.0:** like 2.2 — **what moves + camera only**. `She turns toward the window and smiles. Slow push in.` Repeat appearance = fights the still. Unspecified camera **moves anyway** → say `fixed shot`.

**Localized edit (plain instructions, from 2.7):** `Remove the sunglasses. Her movement and everything else in the video stays the same.`

**Auto Polish / `enable_prompt_expansion`:** ON for a messy one-liner. **OFF** once `@` labels and `[0-6s]` ranges are exact — expansion **rewrites control syntax** and the same seed will not reproduce.

**`enable_thinking`:** off unless the plan is multi-object / legal camera for 30 s, **or** you attached a document/web page (then it is required).

**Model Studio curl shape:** `prompt` + `media[]` typed `reference_image` / `reference_video` / `reference_audio`, `parameters.resolution`, `ratio`, `duration`, `enable_thinking`. Example: `Video 1 holds Image 1 and plays a country ballad on the chair in Image 2.`

---

### CROSS-VERSION ANTI-PATTERNS

| Mistake | 2.2 local | 3.0 hosted |
| --- | --- | --- |
| Appearance dump on I2V | Fights the still | Same |
| Unlabeled refs | N/A / weak | Identity scramble |
| Stacked camera verbs | MoE wobble | Fighting moves |
| Keyword soup | UMT5 shrugs | Expansion may "help" then drift |
| Empty audio | Usually silent (good) | **Invented VO + BGM** |
| Negatives at CFG 1 | Ignored | Use spoken constraints; or `audio: false` |
| H3 `At 00:03.500` / `<d>` | Wrong dialect | Prefer `Shot N [0-5s]` and quoted speech |
| LTX "single paragraph only" | 2.2 **likes** paragraphs; 3.0 wants **numbered shots** for long clips | |
| Expansion ON + exact `@` | N/A | Labels get rewritten |
| Assuming 4K | No | No 4K tier |
| Combining frameImages + referenceImages | Host-specific | Some APIs **forbid** mixing — check schema |

---

### ROUTING FOR THIS SHOP

- Dual 3090: Wan **2.2 I2V/FLF** on the video GPU; Flux/Z-Image stills on Spark. Do not load 14B high+low + LTX + H3-Base on one 24 GB card.
- 3.0 Prime: fal/API. Expansion ON for briefs; OFF for production prompts with `@` and times.
- Isolated Hermes: install this pack in `$HERMES_HOME/skills`.

### VERIFICATION

- Version named in the shot log (2.2 vs 2.7 vs 3.0 / Prime)
- I2V prompt has no wardrobe novel
- 3.0: every ref labeled; music/VO either specified or explicitly forbidden; cut policy stated if you need one take
- 2.2: both MoE weights loaded for 14B
- Expansion/thinking flags match intent (lock vs explore); thinking ON if doc/web
- Duration in-band: 2.2 ~5 s iterate; 3.0 2–30 s
