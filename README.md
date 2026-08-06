# Hermes Media Skill Pack

**129 media-production skills for [Hermes Agent](https://hermes-agent.nousresearch.com)** — a complete prompting and production system for AI-generated **still images, video, and audio** (135 SKILL.md documents total; the `ltx23` cluster bundles 6 sub-skills).

This pack distills professional cinematography, lighting design, art direction, character consistency, and video-generation workflow knowledge into skills that any Hermes Agent instance can load and apply. It covers the entire production pipeline — from story structure and shot planning, through prompt engineering and style direction, to LTX 2.3 / FLUX 2 generation, consistency enforcement, and post-production.

---

## Table of Contents

- [What this pack is](#what-this-pack-is)
- [What's inside](#whats-inside)
- [Requirements](#requirements)
- [Installation](#installation)
- [How the skills work](#how-the-skills-work)
- [Using the skills](#using-the-skills)
  - [Starting a project](#starting-a-project)
  - [Recipe: 30-second cinematic brand spot](#recipe-30-second-cinematic-brand-spot)
  - [Recipe: fixing character drift](#recipe-fixing-character-drift)
  - [Recipe: emulating a director's style](#recipe-emulating-a-directors-style)
  - [Recipe: image-to-video (anchor-first pipeline)](#recipe-image-to-video-anchor-first-pipeline)
- [Category reference](#category-reference)
- [Skill format](#skill-format)
- [Compatibility notes](#compatibility-notes)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Contributing](#contributing)

---

## What this pack is

The Media Skill Pack is a **curated skill library** — a set of standalone `SKILL.md` documents, organized by production discipline, that teach a Hermes Agent how to think about visual media production.

Each skill encodes a specific piece of professional knowledge:

- **Language** — the vocabulary of lenses, lighting, camera motion, and color that separates generic AI output from intentional, art-directed output.
- **Structure** — repeatable formats (15-second social clips, 60-second brand films, documentary interviews, hero's-journey narratives) with beats, timings, and shot lists.
- **Failure patterns** — documented generation artifacts (anatomy errors, character drift, color bleed, scale distortion) and how to fix them.
- **Workflows** — end-to-end generation pipelines for LTX 2.3 and FLUX 2, including JSON schema payloads, anchor-frame strategy, and ComfyUI execution.

The skills were built through real production use with Hermes Agent, ComfyUI, LTX 2.3, FLUX 2, and FAL image/video generation. They are **model-agnostic where possible** (prompt language and art direction apply to any generator) and **specific where it matters** (LTX/FLUX workflows include exact node and payload guidance).

### What it is not

- Not a GUI, plugin, or application — it's a set of markdown skill documents for Hermes Agent.
- Not a LoRA/embedding/model pack — no weights, no checkpoints.
- Not tied to any commercial service — ComfyUI, FAL, and Tenor integrations are optional and configured by you.

---

## What's inside

```
hermes-media-skill-pack/
├── README.md                    ← this file
├── LICENSE                      ← MIT
├── MANIFEST.md                  ← complete skill inventory (129 skills)
├── audio/                       ← 5 skills  — sound design & music
├── cinematography/              ← 17 skills — lens, framing, camera motion
├── consistency-quality/         ← 14 skills — drift, artifacts & coherence fixes
├── genre-libraries/             ← 15 skills — industry/topic prompt libraries
├── lighting/                    ← 13 skills — lighting design & atmosphere
├── media-tools/                 ← 5 skills  — ComfyUI, GIF, YouTube, pipelines
├── narrative-formats/           ← 21 skills — story structures & content formats
├── post-production/             ← 3 skills  — color, VFX, editing
├── prompt-engineering/          ← 9 skills  — prompt craft & token discipline
├── style-specialists/           ← 15 skills — director/artist style emulation
└── video-generation/            ← 12 skills — LTX 2.3 & FLUX 2 workflows
```

Every skill is a folder containing `SKILL.md` (and, where relevant, `references/`, `scripts/`, or `assets/`).

---

## Requirements

| Component | Required? | Notes |
|---|---|---|
| [Hermes Agent](https://hermes-agent.nousresearch.com) | ✅ Yes | Any recent release; skills load from `~/.hermes/skills/` |
| ComfyUI | 🟡 Optional | Needed for `media-tools/comfyui` and most `video-generation/*` workflow skills |
| LTX 2.3 / FLUX 2 models | 🟡 Optional | For the `video-generation/` skills specifically |
| FAL account | 🟡 Optional | Referenced as a fallback path in `workflow_flux2_text_to_image` |
| Tenor API key | 🟡 Optional | Only for `media-tools/gif-search` |
| Spotify / audio tools | 🟡 Optional | Only for `audio/spotify`, `audio/heartmula`, `audio/songsee` |
| ffmpeg | 🟡 Optional | Recommended for `post-production/video-editing-workflow` |

The **prompt-language, art-direction, and consistency skills** (the majority of the pack) work with any image or video generator — no external dependencies at all.

---

## Installation

### Option A — install the whole pack

```bash
cd hermes-media-skill-pack
cp -r audio cinematography consistency-quality genre-libraries lighting \
      media-tools narrative-formats post-production prompt-engineering \
      style-specialists video-generation ~/.hermes/skills/
```

### Option B — install specific categories

```bash
cp -r cinematography lighting ~/.hermes/skills/
```

### Option C — install individual skills

```bash
cp -r style-specialists/pixar_specialist ~/.hermes/skills/
```

After copying, **restart Hermes** (or reload skills) so the skill index picks them up. Skills are then available:

- **Automatically**, when the agent's task matches a skill's description (skills are injected as context when relevant).
- **On demand**, via the skill viewer / slash commands (e.g. `/skills` in the CLI), or by asking the agent to "use the <skill> skill".

> **Note:** category subfolders (`cinematography/`, `lighting/`, …) are just organization. Hermes scans skill folders recursively, so nested placement works fine. If your Hermes version only indexes top-level skill folders, copy the category contents directly into `~/.hermes/skills/` instead of the category folders.

---

## How the skills work

Each skill is a markdown document with a consistent internal structure:

```markdown
# SKILL: <Name>
## Domain: <disciplines covered>
## Version: 1.0

### DESCRIPTION
What the skill does and when to use it.

### KEY PRINCIPLES / CORE DOCTRINE
The underlying knowledge — e.g. the physics of a lens, the logic of a lighting setup.

### PROMPT STRUCTURE / RECIPES
Ready-to-use prompt templates, token blocks, and negative-prompt guidance.

### WORKFLOW / APPLICATION
Step-by-step procedures, including ComfyUI nodes or payloads where relevant.

### VERIFICATION / PITFALLS
How to check the output and what commonly goes wrong.
```

The agent loads the skill's content into context when the task matches the skill's scope, then applies the doctrine, templates, and workflow to your request. Because the skills are **plain markdown**, they also work as reference documents you can read directly, paste into other AI tools, or use as the basis for your own skills.

---

## Using the skills

### Starting a project

A typical production flow through the pack:

1. **Define the format** → `narrative-formats/` (e.g. `30_second_tv_spot`, `90_second_short`, `product_launch_hero_shot`)
2. **Build the story** → `story_spine_narrative`, `hero_journey_narrative_structure`, `ghost_machine_narrative`
3. **Plan the look** → `style-specialists/` for art direction + `lighting/` + `cinematography/` for the technical look
4. **Write the prompts** → `prompt-engineering/` (`positive_prompt_structure`, `negative_prompt_library`, `quality_token_sets`, `seed_strategy`)
5. **Generate** → `video-generation/` (LTX 2.3 / FLUX 2) or `media-tools/comfyui`
6. **Check consistency** → `consistency-quality/` (drift, artifacts)
7. **Finish** → `post-production/` (color grading, VFX, editing)

### Recipe: 30-second cinematic brand spot

1. Load `narrative-formats/30_second_tv_spot` — get the beat structure, timing map, and shot list for a 30s spot.
2. Load `genre-libraries/luxury_premium` (or the genre matching the brand) — get the brand voice, palette, and visual vocabulary.
3. Load a style specialist (`style-specialists/wes_anderson_specialist`, `film_noir_classic_specialist`, etc.) for the art direction.
4. Load `cinematography/anamorphic_lens_signature` + `lighting/golden_hour_mastery` for the technical look of each shot.
5. Generate hero stills with `prompt-engineering/positive_prompt_structure`, using `quality_token_sets` to keep prompts disciplined.
6. Animate with `video-generation/workflow_ltx_i2v` (anchor-first I2V) or `workflow_flux2_text_to_image` → video.
7. Grade with `post-production/color_grading_film_emulation`.

### Recipe: fixing character drift

When a character changes appearance across generations:

1. Load `consistency-quality/character_consistency` — the four-layer anti-drift architecture (Character DNA → Character Pack → Shot Keyframes → Animation) plus IP-Adapter/LoRA guidance.
2. Diagnose the specific failure with `anatomical_errors`, `skin_tone_inconsistency`, `eye_color_mismatch`, `clothing_detail_loss`, or `character_age_drift`.
3. Fix scene-level drift with `composition_drift`, `scale_distortion`, `background_bleed`, `motion_blur_artifacts`, or `photometric_overexposure`.
4. Apply the five-axes verification from `cinematic_consistency_protocol` before re-generating.

### Recipe: emulating a director's style

1. Load the specialist: `pixar_specialist`, `studio_ghibli_specialist`, `wes_anderson_specialist`, `film_noir_classic_specialist`, `cyberpunk_neon_noir_specialist`, `ukiyo_e_specialist`, `surrealism_dali_specialist`, `italian_giallo_specialist`, `synthwave_retrowave_specialist`, `soviet_constructivist_brutalist_specialist`, `baroque_caravaggio_specialist`, `impressionism_monet_specialist`, `art_nouveau_deco_specialist`, or `stop_motion_claymation_aesthetic`.
2. Load `prompt-engineering/style_suffix_library` for consistent style suffixes, and `artist_reference_vocabulary` for the reference language.
3. Combine with lighting (`dramatic_chiaroscuro` pairs naturally with Film Noir; `soft_pastel_animation_lighting` with Ghibli/Pixar) and lens skills (`anamorphic_lens_signature`, `telephoto_compression`, `macro_intimacy`).
4. Iterate with `iterative_prompt_refinement` — each pass tightens the style match.

### Recipe: image-to-video (anchor-first pipeline)

The most reliable consistency path for AI video:

1. Generate a hero still (the **anchor frame**) — `video-generation/flux2dev_cinematic_still_mastery` or `workflow_flux2_text_to_image`.
2. Lock the anchor with `video-generation/workflow_ltx_i2v` — it encodes anchor quality thresholds, prompt-subtraction rules for I2V, and multi-shot continuity.
3. Keep the anchor's palette/lighting locked via `consistency-quality/color_palette_injection`.
4. Generate motion with `video-generation/ltx23` (the umbrella cluster — prompt engineering master, camera movement language, audio-visual sync, subject motion performance, technical configuration).
5. Sync audio with `audio/sound_design` + `audio/music_scoring_cinematic`.

---

## Category reference

### `audio/` — Sound design & music (5)
| Skill | Covers |
|---|---|
| `sound_design` | Foley, diegetic/non-diegetic audio, 8-layer soundscape model, music cues, audio-visual synchronization |
| `music_scoring_cinematic` | Cinematic music scoring and cue architecture |
| `heartmula` | HeartMuLa open-source music generation |
| `songsee` | Spectrograms and audio-feature visualizations |
| `spotify` | Control Spotify via the Hermes Spotify toolset |

### `cinematography/` — Lens, framing & camera (17)
| Skill | Covers |
|---|---|
| `anamorphic_lens_signature` | Anamorphic lens characteristics: flares, bokeh, squeeze, oval highlights |
| `dolly_zoom_vertigo_effect` | The Vertigo/dolly-zoom effect and when to use it |
| `drone_aerial_framing` | Aerial framing, altitude grammar, flight-path composition |
| `dutch_angle_tension` | Canted angles and psychological disorientation |
| `macro_intimacy` | Macro lens language and close-up storytelling |
| `pov_first_person` | First-person POV framing |
| `rack_focus_technique` | Focus-pull technique and depth storytelling |
| `steadicam_handheld_camera` | Steadicam vs. handheld language |
| `sunlit_travel_cinematography` | Daylight travel and location cinematography |
| `telephoto_compression` | Telephoto compression and background stacking |
| `time_lapse_hyper_lapse` | Time-lapse and hyper-lapse techniques |
| `wide_angle_environmental` | Wide-angle environmental storytelling |
| `action-sequence-cinematography` | Action choreography and coverage |
| `architectural-interior-cinematography` | Interior and architectural space |
| `car-commercial-cinematography` | Automotive commercial language |
| `documentary-realism-cinematography` | Observational / documentary modes |
| `sci-fi-futurism-cinematography` | Sci-fi and futuristic environments |

### `consistency-quality/` — Coherence & failure fixes (14)
| Skill | Covers |
|---|---|
| `character_consistency` | Anti-drift architecture: DNA → pack → keyframes → animation; IP-Adapter/LoRA/DreamBooth |
| `cinematic_consistency_protocol` | Five-axes consistency verification and the anchor-to-video pipeline |
| `cinematic_continuity` | Scene-level continuity: camera geography, lighting keys, prop state |
| `anatomical_errors` | Anatomy failure patterns and fixes |
| `character_age_drift` | Age drift across generations |
| `skin_tone_inconsistency` | Skin-tone matching |
| `eye_color_mismatch` | Eye-color consistency |
| `clothing_detail_loss` | Wardrobe detail preservation |
| `composition_drift` | Compositional grid drift across clips |
| `color_palette_injection` | Palette locking and injection |
| `scale_distortion` | Scale/relative-size failures |
| `background_bleed` | Background contamination across frames |
| `motion_blur_artifacts` | Motion-blur artifacts and fixes |
| `photometric_overexposure` | Exposure and highlight failures |

### `genre-libraries/` — Industry/topic libraries (15)
`automotive`, `beauty_skincare`, `food_hospitality`, `health_wellness`, `lifestyle_aspiration`, `luxury_premium`, `sports_performance`, `streetwear_youth_culture`, `tech_innovation`, `travel_tourism_wanderlust`, plus genre cinematography variants: `beauty-cosmetics-cinematography`, `fashion-editorial-cinematography`, `food-beverage-cinematography`, `landscape-environment-cinematography`, `sports-athleticism-cinematography`.

### `lighting/` — Lighting design (13)
`blue_hour_silhouette_lighting`, `cinematic-lighting-techniques`, `dramatic_chiaroscuro`, `fire_candlelight`, `golden_hour_mastery`, `natural_window_light`, `neon_night_city`, `neon_practical_lighting`, `overcast_diffusion`, `soft_pastel_animation_lighting`, `studio_softbox_setups`, `underwater_aquatic_light`, `volumetric_god_rays_lighting`.

### `media-tools/` — Tooling (5)
`comfyui` (diffusion workflows; scripts, tests, and workflow references included), `gif-search` (Tenor GIF search via curl), `youtube-content` (fetch transcripts and transform to content), `image-generation-workflow` (AI image gen/refine workflow), `media-pipeline-workflow` (build/debug AI media pipelines).

### `narrative-formats/` — Story & formats (21)
Duration formats: `15_second_social_content`, `30_second_tv_spot`, `60_second_brand_film`, `90_second_short`.
Story: `story_spine_narrative`, `hero_journey_narrative_structure`, `ghost_machine_narrative`, `heartwarming_storytelling`.
Character direction: `child_youth_direction`, `elder_authority`, `female_protagonist_framing`, `male_antagonist_presence`, `non_human_creature`, `ensemble_group_dynamics`, `performance_direction_micro_expression`.
Formats: `documentary_interview_format`, `explainer_educational`, `entertainment_gaming`, `girl_next_door_realism`, `product_launch_hero_shot`, `tiktok_vertical_platform`.

### `post-production/` — Finishing (3)
`color_grading_film_emulation`, `chroma_key_green_screen_vfx`, `video-editing-workflow`.

### `prompt-engineering/` — Prompt craft (9)
`positive_prompt_structure`, `negative_prompt_library`, `quality_token_sets`, `seed_strategy`, `style_suffix_library`, `artist_reference_vocabulary`, `resolution_aspect_ratio`, `sensory-texture-layering-technique`, `iterative_prompt_refinement`.

### `style-specialists/` — Art direction (15)
`pixar_specialist`, `studio_ghibli_specialist`, `wes_anderson_specialist`, `film_noir_classic_specialist`, `cyberpunk_neon_noir_specialist`, `italian_giallo_specialist`, `ukiyo_e_specialist`, `surrealism_dali_specialist`, `synthwave_retrowave_specialist`, `soviet_constructivist_brutalist_specialist`, `baroque_caravaggio_specialist`, `impressionism_monet_specialist`, `art_nouveau_deco_specialist`, `neural_aesthetic`, `stop_motion_claymation_aesthetic`.

### `video-generation/` — LTX 2.3 & FLUX 2 (12)
| Skill | Covers |
|---|---|
| `ltx23` | Umbrella cluster: prompt-engineering master, camera movement language, character consistency, audio-visual sync, subject motion performance, technical configuration |
| `workflow_ltx_i2v` | LTX 2.3 image-to-video: anchor requirements, prompt subtraction, multi-shot continuity, ComfyUI node architecture |
| `workflow_flux2_text_to_image` | FLUX 2 text-to-image via ComfyUI with FAL fallback |
| `flux2_json_schema` | Type-safe JSON payload schemas mapped to ComfyUI nodes |
| `flux2dev_prompt_engineering_master` | FLUX 2 prompt engineering master reference |
| `flux2dev_cinematic_still_mastery` | FLUX 2 cinematic still generation |
| `flux2dev_photorealistic_portraiture` | FLUX 2 photorealism & portraiture |
| `flux2dev_product_hero_photography` | FLUX 2 product hero shots |
| `flux2dev_fashion_beauty_editorial` | FLUX 2 fashion/beauty editorial |
| `flux2dev_architectural_environment` | FLUX 2 architecture & environments |
| `flux2dev_macro_texture_surface` | FLUX 2 macro texture & surface detail |
| `motion_graphics_kinetic_type` | Motion graphics and kinetic typography |

---

## Skill format

Skills in this pack use the classic Hermes skill layout:

```markdown
# SKILL: <Name>
## Domain: <disciplines>
## Version: 1.0

### DESCRIPTION
### [doctrine / principles]
### [prompt structure / recipes]
### [workflow / application]
### [verification / pitfalls]
```

Newer skills (e.g. `ltx23`, `comfyui`, `media-tools/*`) use YAML frontmatter:

```yaml
---
name: ltx23
description: "..."
version: 1.0
---
```

Both formats load identically in Hermes. The descriptive `# SKILL:` header format is intentionally human-readable so the documents double as standalone reference material.

---

## Compatibility notes

- **Hermes Agent:** the pack targets the standard skills directory (`~/.hermes/skills/`). Category folders are optional; the skills themselves are self-contained.
- **Generation backends:** ComfyUI is referenced by the workflow skills (`comfy run`, `run_workflow.py`, JSON payloads). The `video-generation` skills describe LTX 2.3 and FLUX 2 node parameters; check your ComfyUI version for exact node names.
- **API keys:** skills reference environment variables (e.g. `TENOR_API_KEY`, `COMFY_CLOUD_API_KEY`). No keys are embedded in the pack — configure your own.
- **Server addresses:** workflow examples use `127.0.0.1` / generic hosts. Point them at your own ComfyUI instance.
- **Models referenced:** LTX 2.3 (Lightricks), FLUX 2 (Black Forest Labs), Wan 2.1. The prompt-language skills are model-agnostic.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Skills don't appear after copying | Restart Hermes; verify `SKILL.md` exists at each skill's top level; if using category folders and they're not indexed, flatten them into `~/.hermes/skills/` |
| ComfyUI workflow skills fail | Confirm ComfyUI is running (`comfy run` / your launcher); check node names against your ComfyUI version; verify `COMFY_CLOUD_API_KEY` or local endpoint |
| Character still drifts | Work the `consistency-quality/` skills in order: `character_consistency` → five-axes check in `cinematic_consistency_protocol` → targeted fix (`skin_tone_inconsistency`, `clothing_detail_loss`, …) |
| Style doesn't match the reference | Combine the specialist with `style_suffix_library` + `artist_reference_vocabulary`, then iterate with `iterative_prompt_refinement` |
| Video looks static / flat | Revisit `video-generation/workflow_ltx_i2v` motion guidance and `ltx23` camera-movement language; add `music_scoring_cinematic` for pacing |

---

## License

MIT — see [LICENSE](LICENSE). Use freely, attribute if you like.

## Contributing

Skills are plain markdown — improvements are welcome. Keep the structure consistent (`# SKILL:` header, `### DESCRIPTION`, doctrine, recipes, workflow, pitfalls), keep personal/private data out, and add new skills under the matching category folder. Update `MANIFEST.md` when adding or removing skills.
