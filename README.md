# Hermes Media Skill Pack

**138 media-production skills for [Hermes Agent](https://hermes-agent.nousresearch.com):** a prompting and production system for AI-generated still images, video, and audio (153 SKILL.md documents total; the `ltx23`, `minimax_h3`, and `wan` clusters each nest several specialist skills).

The pack distills professional cinematography, lighting design, art direction, character consistency, and video-generation workflow knowledge into markdown skills that any Hermes Agent instance can load and apply. It covers the production pipeline end to end: story structure and shot planning, prompt engineering and style direction, LTX 2.3/2.5 and FLUX 2 generation, local multi-Comfy routing, and post-production.

[![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

---

## What's inside

```
hermes-media-skill-pack/
├── README.md                    ← this file
├── LICENSE                      ← MIT
├── MANIFEST.md                  ← complete skill inventory (138 skills)
├── CHANGELOG.md                 ← release history
├── audio/                       ← 5 skills  · sound design & music
├── cinematography/              ← 17 skills · lens, framing, camera motion
├── consistency-quality/         ← 15 skills · drift, artifacts, audit & coherence
├── genre-libraries/             ← 15 skills · industry/topic prompt libraries
├── lighting/                    ← 13 skills · lighting design & atmosphere
├── media-tools/                 ← 7 skills  · ComfyUI, isolated Hermes, multi-GPU
├── narrative-formats/           ← 21 skills · story structures & content formats
├── post-production/             ← 3 skills  · color, VFX, editing
├── prompt-engineering/          ← 9 skills  · prompt craft & token discipline
├── style-specialists/           ← 15 skills · director/artist style emulation
├── video-generation/            ← 18 skills · LTX 2.3/2.5, MiniMax H3, Wan 2.2/3.0, FLUX 2, Z-Image, local pipeline
└── scripts/                     ← inject_frontmatter.py (frontmatter tooling)
```

Every skill is a folder containing `SKILL.md`, and where relevant `references/`, `scripts/`, or `assets/`.

**What it is not:** not a GUI, plugin, or application; not a set of LoRA/embedding weights; not tied to any commercial service. ComfyUI, FAL, and Tenor integrations are optional and configured by you.

---

## What a skill encodes

Each skill is a standalone `SKILL.md` document that teaches the agent one piece of production knowledge:

- **Language.** The vocabulary of lenses, lighting, camera motion, and color that separates generic AI output from intentional, art-directed output.
- **Structure.** Repeatable formats (15-second social clips, 60-second brand films, documentary interviews, hero's-journey narratives) with beats, timings, and shot lists.
- **Failure patterns.** Documented generation artifacts (anatomy errors, character drift, color bleed, scale distortion) and how to fix them.
- **Workflows.** End-to-end generation pipelines for LTX 2.3/2.5 and FLUX 2, including JSON schema payloads, anchor-frame strategy, multi-Comfy routing, and ComfyUI execution.
- **Local runtime.** An isolated Hermes home that does not touch `~/.hermes`, DGX Spark + dual-3090 Comfy instances, and a vision audit before you ship a render.

The skills were built through real production use with Hermes Agent, ComfyUI, LTX 2.3, FLUX 2, MiniMax H3, Wan 2.2/3.0, and FAL image/video generation. They are model-agnostic where possible (prompt language and art direction apply to any generator) and specific where it matters (LTX / FLUX / H3 / Wan workflows include exact dialects, nodes, and payload flags).

---

## Requirements

| Component | Required? | Notes |
|---|---|---|
| [Hermes Agent](https://hermes-agent.nousresearch.com) | Yes | Current Hermes indexes YAML frontmatter (`name` + `description` ≤ 60 chars). Skills load from `~/.hermes/skills/` or a project `HERMES_HOME`. |
| ComfyUI | Optional | Needed for `media-tools/comfyui` and most `video-generation/*` workflow skills. Multiple instances (DGX Spark + dual 3090s) → `multi-comfy-orchestration`. |
| LTX 2.3 / 2.5 / FLUX 2 / Z-Image / Wan 2.2 / MiniMax H3-Base | Optional | For the `video-generation/` skills specifically. Wan 3.0 and Hailuo H3 2K are hosted. |
| FAL account | Optional | Fallback only in `workflow_flux2_text_to_image`; skip for a fully local pipeline. |
| Tenor API key | Optional | Only for `media-tools/gif-search`. |
| Spotify / audio tools | Optional | Only for `audio/spotify`, `audio/heartmula`, `audio/songsee`. |
| ffmpeg | Optional | Recommended for `post-production/video-editing-workflow`. |

The prompt-language, art-direction, and consistency skills (the majority of the pack) work with any image or video generator and have no external dependencies at all.

---

## Installation

Modern Hermes discovers skills via `skills_list()` (frontmatter only) then `skill_view(name)`. After install, start a new session (`/reset` or `--now`) so the index refreshes.

### Option A: daily-driver Hermes (`~/.hermes`)

```bash
cd hermes-media-skill-pack
cp -r audio cinematography consistency-quality genre-libraries lighting \
      media-tools narrative-formats post-production prompt-engineering \
      style-specialists video-generation ~/.hermes/skills/
```

### Option B: Cinesmith / project Hermes (does not modify your global install)

Cinesmith sets `HERMES_HOME=<repo>/hermes_home` and will not use `~/.hermes` unless you set `CINESMITH_ALLOW_GLOBAL_HERMES=1`. Install the pack into that home:

```bash
export HERMES_HOME=/path/to/cinesmith/hermes_home
mkdir -p "$HERMES_HOME/skills"
cp -r audio cinematography consistency-quality genre-libraries lighting \
      media-tools narrative-formats post-production prompt-engineering \
      style-specialists video-generation "$HERMES_HOME/skills/"
```

See `media-tools/isolated-hermes-home` and `media-tools/multi-comfy-orchestration`.

### Option C: partial installs

```bash
# A category
cp -r cinematography lighting ~/.hermes/skills/

# A single skill
cp -r style-specialists/pixar_specialist ~/.hermes/skills/
```

After copying, restart Hermes (or reload skills) so the index picks them up. Skills are then available automatically when a task matches a skill's description, or on demand via the skill viewer / slash commands.

> **Note:** category subfolders are just organization; Hermes scans skill folders recursively, so nested placement works fine. If your Hermes version only indexes top-level skill folders, copy the category contents directly into `~/.hermes/skills/` instead.

---

## How a skill is structured

Each skill is a consistent markdown document:

```markdown
# SKILL: <Name>
## Domain: <disciplines covered>
## Version: 1.0

### DESCRIPTION
What the skill does and when to use it.

### KEY PRINCIPLES / CORE DOCTRINE
The underlying knowledge (the physics of a lens, the logic of a lighting setup).

### PROMPT STRUCTURE / RECIPES
Ready-to-use prompt templates, token blocks, and negative-prompt guidance.

### WORKFLOW / APPLICATION
Step-by-step procedures, including ComfyUI nodes or payloads where relevant.

### VERIFICATION / PITFALLS
How to check the output and what commonly goes wrong.
```

Every skill now starts with YAML frontmatter so current Hermes can index it:

```yaml
---
name: anamorphic_lens_signature
description: "Prompt anamorphic squeeze, oval bokeh, and streak flares."
version: 1.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [cinematography, media, cinematic]
    category: cinematography
---
```

The agent loads a skill's content into context when a task matches its scope, then applies the doctrine, templates, and workflow. Because the skills are plain markdown, they also work as reference documents you can read directly, paste into other AI tools, or use as the basis for your own skills.

---

## Using the pack

A typical production flow:

1. **Define the format** → `narrative-formats/` (e.g. `30_second_tv_spot`, `90_second_short`, `product_launch_hero_shot`).
2. **Build the story** → `story_spine_narrative`, `hero_journey_narrative_structure`, `ghost_machine_narrative`.
3. **Plan the look** → `style-specialists/` for art direction, plus `lighting/` and `cinematography/` for the technical look.
4. **Write the prompts** → `prompt-engineering/` (`positive_prompt_structure`, `negative_prompt_library`, `quality_token_sets`, `seed_strategy`).
5. **Generate** → `video-generation/` (LTX 2.3, MiniMax H3, Wan 2.2/3.0, FLUX 2) or `media-tools/comfyui`.
6. **Check consistency** → `consistency-quality/` (drift, artifacts).
7. **Finish** → `post-production/` (color grading, VFX, editing).

### Recipe: 30-second cinematic brand spot

1. Load `narrative-formats/30_second_tv_spot` for the beat structure, timing map, and shot list.
2. Load `genre-libraries/luxury_premium` (or the matching genre) for the brand voice, palette, and visual vocabulary.
3. Load a style specialist (`wes_anderson_specialist`, `film_noir_classic_specialist`, etc.) for art direction.
4. Load `cinematography/anamorphic_lens_signature` and `lighting/golden_hour_mastery` for the technical look.
5. Generate hero stills with `prompt-engineering/positive_prompt_structure`, using `quality_token_sets` to keep prompts disciplined.
6. Animate with `video-generation/workflow_ltx_i2v` (anchor-first I2V), `wan` (2.2 local or 3.0 hosted), or `minimax_h3` (shot-block + stereo).
7. Grade with `post-production/color_grading_film_emulation`.

### Recipe: fixing character drift

1. Load `consistency-quality/character_consistency` (the four-layer anti-drift architecture: Character DNA → Character Pack → Shot Keyframes → Animation, plus IP-Adapter/LoRA guidance).
2. Diagnose the specific failure with `anatomical_errors`, `skin_tone_inconsistency`, `eye_color_mismatch`, `clothing_detail_loss`, or `character_age_drift`.
3. Fix scene-level drift with `composition_drift`, `scale_distortion`, `background_bleed`, `motion_blur_artifacts`, or `photometric_overexposure`.
4. Apply the five-axes verification from `cinematic_consistency_protocol` before re-generating.

### Recipe: emulating a director's style

1. Load the specialist (`pixar_specialist`, `studio_ghibli_specialist`, `wes_anderson_specialist`, `film_noir_classic_specialist`, `surrealism_dali_specialist`, `monet_specialist`, and more).
2. Load `prompt-engineering/style_suffix_library` for consistent suffixes and `artist_reference_vocabulary` for the reference language.
3. Pair with lighting (`dramatic_chiaroscuro` with Film Noir; `soft_pastel_animation_lighting` with Ghibli/Pixar) and lens skills (`anamorphic_lens_signature`, `telephoto_compression`, `macro_intimacy`).
4. Tighten the match with `iterative_prompt_refinement`.

### Recipe: image-to-video (anchor-first pipeline)

1. Generate the anchor still: `video-generation/flux2dev_cinematic_still_mastery` or `workflow_flux2_text_to_image`.
2. Lock the anchor with `workflow_ltx_i2v` (anchor quality thresholds, prompt-subtraction rules for I2V, multi-shot continuity).
3. Keep the anchor's palette and lighting locked via `consistency-quality/color_palette_injection`.
4. Generate motion with `ltx23` (camera-movement language) or `ltx25_beat_scripting` on the 2.5 graph.
5. Sync audio with `audio/sound_design` and `audio/music_scoring_cinematic`.
6. Gate with `consistency-quality/vision_audit_remediation` before calling it done.

### Recipe: fully local (Spark + 3090s, isolated Hermes)

1. Load `media-tools/isolated-hermes-home` (project `HERMES_HOME`, not `~/.hermes`).
2. Load `media-tools/multi-comfy-orchestration` (DGX Spark + dual 3090s, one Comfy per GPU).
3. Load `video-generation/local-cinematic-pipeline`: plan → Z-Image/Flux still → LTX I2V or first/last → audit.
4. Local video alternative: Wan 2.2 I2V/FLF on the video 3090 (`wan_prompt_engineering_master`). Do not try to load 14B MoE + LTX + H3-Base on one 24 GB card.

### Recipe: MiniMax H3 (Hailuo 3) prompting control

1. Load `video-generation/minimax_h3` and pick Base (T2VA / I2VA / FL2VA / L2VA) vs Full-Reference before writing.
2. Load `minimax_h3_prompt_engineering_master` (official three fields or six Ref2VA sections). Local H3-Base has no Context-IR; write the IR yourself.
3. Camera: `minimax_h3_camera_movement_language` (type + amplitude + speed). Audio: `minimax_h3_audio_direction` (`<d>` dialogue, soundscape, score; stereo is always on).
4. Assets: `minimax_h3_reference_control`. Graphs, duration, and license: `minimax_h3_technical_configuration`.
5. First green local run is an MP4 with stereo at 768p. 2K is hosted H3-Regenerate-2K, not a missing node.

### Recipe: Wan 2.2 local / Wan 3.0 hosted

1. Load `video-generation/wan` and name the line in the shot log: 2.2 (Apache, Comfy) vs 3.0 / Prime (hosted, up to 30 s).
2. Load `wan_prompt_engineering_master`. I2V takes motion and camera only. For 3.0, use `@Image1` jobs and `Shot N [0-5s]`, turning Auto Polish off once labels are exact.
3. Camera, FLF, and Animate: `wan_camera_motion_control`. 3.0 sound: `wan_audio_direction` (voice, SFX, music as three layers, or explicit `no voice lines` / `no background music`). References: `wan_reference_control`.
4. 2.2 runs on dual 3090s; 3.0 Prime on fal/Model Studio. Turn Thinking on if you attached a document or URL.

---

## Category reference

| Category | Skills | Covers |
|---|---|---|
| `audio/` | 5 | Sound design, cinematic scoring, music generation (HeartMuLa), spectrograms, Spotify control |
| `cinematography/` | 17 | Lens signature, framing, camera motion (anamorphic, vertical zoom, drone, dolly zoom, steadicam, telephoto, macro, rack focus, POV), travel and sci-fi language, action/interior/car/documentary language |
| `consistency-quality/` | 15 | Anti-drift architecture, five-axes verification, palette injection, vision audit, and targeted failure fixes (anatomy, skin tone, eye color, clothing, drift, bleed, distortion) |
| `genre-libraries/` | 15 | Industry and topic prompt libraries (automotive, beauty, food, lifestyle, luxury, sports, streetwear, tech, travel) plus genre cinematography variants |
| `lighting/` | 13 | Lighting design and atmosphere (golden hour, blue hour, chiaroscuro, neon, overcast, softbox, volumetric rays, candlelight, window light) |
| `media-tools/` | 7 | ComfyUI workflows, isolated Hermes home, multi-Comfy orchestration, GIF search, YouTube content, media and image pipelines |
| `narrative-formats/` | 21 | Duration formats (15s, 30s, 60s, 90s), story structures, character direction, and platform formats |
| `post-production/` | 3 | Color grading, green-screen VFX, video editing workflow |
| `prompt-engineering/` | 9 | Positive/negative structure, quality token sets, seed strategy, style suffixes, artist vocabulary, resolution, texture layering, iterative refinement |
| `style-specialists/` | 15 | Director and artist style emulation across film, animation, and painting movements |
| `video-generation/` | 18 | LTX 2.3/2.5 clusters, MiniMax H3, Wan 2.2/3.0, FLUX 2, Z-Image, first/last frame, and the fully local pipeline |

The full per-skill inventory lives in [`MANIFEST.md`](MANIFEST.md).

---

## Compatibility notes

- **Hermes Agent:** YAML frontmatter is required for `skills_list()` / slash commands. Category folders are optional; the skills themselves are self-contained. Default install is `~/.hermes/skills/`. Cinesmith uses a repo `hermes_home/` and does not modify your global Hermes unless you opt in.
- **Generation backends:** ComfyUI is referenced by the workflow skills (`comfy run`, `run_workflow.py`, JSON payloads). Video skills cover LTX 2.3/2.5, MiniMax H3-Base, Wan 2.2 (local), and Wan 3.0 / Hailuo H3 (hosted); check your ComfyUI version for exact node names. Multi-instance shops run one Comfy process per GPU.
- **API keys:** skills reference environment variables (e.g. `TENOR_API_KEY`, `COMFY_CLOUD_API_KEY`). No keys are embedded in the pack; configure your own.
- **Server addresses:** workflow examples use `127.0.0.1` / generic hosts. Point them at your own ComfyUI instance.
- **Models referenced:** LTX 2.3 / 2.5 (Lightricks), FLUX 2 and Z-Image Turbo (Black Forest Labs / Spark graphs), MiniMax H3 / Hailuo 3, Wan 2.2 (Apache, last open flagship) and Wan 3.0 / 3.0 Prime (hosted). The prompt-language skills are model-agnostic; H3 and Wan dialects are not interchangeable.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Skills don't appear after copying | New Hermes session (`/reset` or `--now`). Every `SKILL.md` must start with YAML `name` + `description`. Under Cinesmith, install into `$HERMES_HOME/skills`, not `~/.hermes`. |
| ComfyUI workflow skills fail | Confirm ComfyUI is running (`comfy run` / your launcher); check node names against your ComfyUI version; verify `COMFY_CLOUD_API_KEY` or the local endpoint. |
| Character still drifts | Work the `consistency-quality/` skills in order: `character_consistency` → five-axes check in `cinematic_consistency_protocol` → targeted fix (skin tone, clothing detail, …). |
| Style doesn't match the reference | Combine the specialist with `style_suffix_library` + `artist_reference_vocabulary`, then iterate with `iterative_prompt_refinement`. |
| Video looks static / flat | Revisit `workflow_ltx_i2v` / `ltx23` camera language or the matching H3 / Wan camera skill. Do not mix dialects. |
| "Don't touch my Hermes" / Cinesmith | Use `isolated-hermes-home`. Never `cp` the pack into `~/.hermes` when `HERMES_HOME` is a project tree. |
| H3 local looks worse than Hailuo | H3 Context-IR is hosted-only. Convert the brief to official Base or Full-Reference (`minimax_h3_prompt_engineering_master`). |
| Wan 3.0 invented VO / BGM | Specify voice, SFX, and music as three layers, or `no voice lines` / `no background music` (`wan_audio_direction`). Turn Auto Polish off once `@` labels are exact. |

---

## Status

**Currently ships:** 138 top-level skills (153 `SKILL.md` documents) across 11 categories, covering the full cinematic pipeline from narrative structure and art direction through LTX 2.3/2.5, MiniMax H3, Wan 2.2/3.0, FLUX 2, and Z-Image generation to post-production. All skills are indexable in current Hermes via YAML frontmatter.

**Latest changes:** MiniMax H3 and Wan 3.0 prompting-control clusters (Base vs Full-Reference dialects, camera/audio/technical specialists), plus frontmatter on every skill and an isolated `HERMES_HOME` install path. See [`CHANGELOG.md`](CHANGELOG.md).

**Held / out of scope:** no weights or model files; integrations (ComfyUI, FAL, Tenor, Spotify) require your own accounts and endpoints.

---

## Contributing

Skills are plain markdown with YAML frontmatter (`name`, `description` ≤ 60 chars, `platforms`, `metadata.hermes`). Keep personal/private data out. Add new skills under the matching category folder and update [`MANIFEST.md`](MANIFEST.md) when adding or removing skills.

---

## License

MIT. See [LICENSE](LICENSE). Use freely; attribution optional.
