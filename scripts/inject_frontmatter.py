#!/usr/bin/env python3
"""Add or shorten YAML frontmatter so modern Hermes can index every skill.

Hermes skills_list() only reads name + description from YAML at byte 0.
Description hardline is 60 characters (index truncates at 57).
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ≤60 chars, one sentence, ends with period. Trigger must fit in 57.
DESCS: dict[str, str] = {
    # audio
    "music_scoring_cinematic": "Write cinematic score cues and picture-sync music maps.",
    "sound_design": "Layer foley, diegetic, and non-diegetic soundscapes.",
    "heartmula": "Generate full songs from lyrics with HeartMuLa.",
    "songsee": "Render spectrograms and audio-feature visualizations.",
    "spotify": "Control Spotify playback, search, and playlists.",
    # cinematography
    "anamorphic_lens_signature": "Prompt anamorphic squeeze, oval bokeh, and streak flares.",
    "dolly_zoom_vertigo_effect": "Build Vertigo/dolly-zoom tension in stills and video.",
    "drone_aerial_framing": "Direct aerial altitude, path, and landscape scale.",
    "dutch_angle_tension": "Use canted angles for unease without cheap tilt.",
    "macro_intimacy": "Shoot macro close-ups with shallow-depth storytelling.",
    "pov_first_person": "Frame first-person POV shots and eyeline motion.",
    "rack_focus_technique": "Pull focus between planes to shift story attention.",
    "steadicam_handheld_camera": "Choose steadicam float vs handheld shake language.",
    "telephoto_compression": "Compress space with long-lens stacking and isolation.",
    "time_lapse_hyper_lapse": "Plan time-lapse and hyper-lapse camera paths.",
    "wide_angle_environmental": "Tell environment stories with wide-angle coverage.",
    "action-sequence-cinematography": "Cover fights, chases, and impact beats for action.",
    "architectural-interior-cinematography": "Film interiors with true verticals and material light.",
    "car-commercial-cinematography": "Direct vehicle hero shots, chrome, and road motion.",
    "documentary-realism-cinematography": "Shoot observational, available-light documentary coverage.",
    "sci-fi-futurism-cinematography": "Build speculative worlds, neon, and future surfaces.",
    "sunlit_travel_cinematography": "Frame warm travel and destination wanderlust stills.",
    # consistency
    "anatomical_errors": "Diagnose and fix AI anatomy failures in people.",
    "background_bleed": "Stop background textures crawling across shots.",
    "character_age_drift": "Lock apparent age across a character series.",
    "character_consistency": "Lock identity via DNA, packs, adapters, and anchors.",
    "cinematic_consistency_protocol": "Run five-axis continuity checks before re-rendering.",
    "cinematic_continuity": "Hold camera geography, keys, and prop state.",
    "clothing_detail_loss": "Preserve wardrobe details across generations.",
    "color_palette_injection": "Lock and inject a palette across stills and clips.",
    "composition_drift": "Stop framing and grid drift across a sequence.",
    "eye_color_mismatch": "Keep eye color stable across character shots.",
    "motion_blur_artifacts": "Fix bogus motion blur and smear artifacts.",
    "photometric_overexposure": "Recover blown highlights and exposure mismatches.",
    "scale_distortion": "Fix relative-size errors between subjects.",
    "skin_tone_inconsistency": "Match skin tone across lighting and shots.",
    # genre
    "automotive": "Prompt automotive product and brand-film language.",
    "beauty_skincare": "Prompt beauty, skin, and cosmetics product language.",
    "food_hospitality": "Prompt food, kitchen, and hospitality visuals.",
    "health_wellness": "Prompt health, wellness, and care visuals.",
    "lifestyle_aspiration": "Prompt lifestyle and aspirational living scenes.",
    "luxury_premium": "Prompt luxury materials, restraint, and finish.",
    "sports_performance": "Prompt athletic effort, sweat, and peak action.",
    "streetwear_youth_culture": "Prompt streetwear, youth culture, and attitude.",
    "tech_innovation": "Prompt product-tech and innovation visuals.",
    "travel_tourism_wanderlust": "Prompt travel, place, and wanderlust campaigns.",
    "beauty-cosmetics-cinematography": "Film cosmetics, skin texture, and bottle beauty.",
    "fashion-editorial-cinematography": "Direct fashion editorials, lookbooks, and drape.",
    "food-beverage-cinematography": "Film food and drink with appetite and steam.",
    "landscape-environment-cinematography": "Film landscape, weather, and environmental scale.",
    "sports-athleticism-cinematography": "Film sport peaks, exertion, and crowd energy.",
    # lighting
    "blue_hour_silhouette_lighting": "Light blue-hour silhouettes and dusk rims.",
    "cinematic-lighting-techniques": "Pick cinematic keys, ratios, and grade strategies.",
    "dramatic_chiaroscuro": "Build high-contrast chiaroscuro and falloff.",
    "fire_candlelight": "Light with fire, candle, and warm practicals.",
    "golden_hour_mastery": "Use golden-hour sun angle, color, and length.",
    "natural_window_light": "Shape interiors with window key and bounce.",
    "neon_night_city": "Light night cities with neon and wet streets.",
    "neon_practical_lighting": "Use neon practicals as motivated color keys.",
    "overcast_diffusion": "Light with overcast, soft, shadowless daylight.",
    "soft_pastel_animation_lighting": "Light animated-feature pastels, warm and safe.",
    "studio_softbox_setups": "Build studio softbox ratios for people and product.",
    "underwater_aquatic_light": "Light underwater caustics, murk, and shafts.",
    "volumetric_god_rays_lighting": "Add volumetric shafts and god-ray atmosphere.",
    # narrative
    "15_second_social_content": "Structure a 15-second social clip beat map.",
    "30_second_tv_spot": "Structure a 30-second TV/brand spot beat map.",
    "60_second_brand_film": "Structure a 60-second brand film beat map.",
    "90_second_short": "Structure a 90-second short with three acts.",
    "child_youth_direction": "Direct child and youth performance safely.",
    "documentary_interview_format": "Plan interview coverage, eyelines, and cutaways.",
    "elder_authority": "Direct elder presence, dignity, and authority.",
    "ensemble_group_dynamics": "Stage ensemble blocking and group eyelines.",
    "entertainment_gaming": "Format entertainment and gaming trailer beats.",
    "explainer_educational": "Structure explainer beats, diagrams, and VO.",
    "female_protagonist_framing": "Frame a female lead with agency, not ornament.",
    "ghost_machine_narrative": "Build ghost-in-the-machine sci-fi story spines.",
    "hero_journey_narrative_structure": "Map a hero's-journey beat sheet to shots.",
    "male_antagonist_presence": "Stage antagonist weight, stillness, and threat.",
    "non_human_creature": "Direct creature performance and non-human body.",
    "performance_direction_micro_expression": "Direct micro-expressions and eye-acting beats.",
    "product_launch_hero_shot": "Plan a product-launch hero still and motion.",
    "story_spine_narrative": "Compress story to a spine of irreversible beats.",
    "girl_next_door_realism": "Cast approachable, unstyled recurring realism.",
    "heartwarming_storytelling": "Write wholesome micro-arcs for family-safe spots.",
    "tiktok_vertical_platform": "Fit shots to TikTok vertical timing and safe areas.",
    # post
    "chroma_key_green_screen_vfx": "Key green screen cleanly and composite plates.",
    "color_grading_film_emulation": "Grade toward film stocks and print emulation.",
    "video-editing-workflow": "Edit, pace, and structure picture for delivery.",
    # prompt
    "artist_reference_vocabulary": "Name artist/era references without dumping lists.",
    "iterative_prompt_refinement": "Tighten prompts across passes with a change log.",
    "negative_prompt_library": "Apply targeted negatives, not kitchen-sink bans.",
    "positive_prompt_structure": "Order positives: subject, light, lens, grade.",
    "quality_token_sets": "Use short quality tokens; drop empty superlatives.",
    "resolution_aspect_ratio": "Pick aspect, resolution, and delivery crop.",
    "seed_strategy": "Lock, fork, and document seeds for series work.",
    "style_suffix_library": "Append consistent style suffixes per look.",
    "sensory-texture-layering-technique": "Swap static adjectives for kinetic sensory verbs.",
    # style
    "art_nouveau_deco_specialist": "Emulate Art Nouveau and Art Deco ornament.",
    "baroque_caravaggio_specialist": "Emulate Caravaggio tenebrism and Baroque mass.",
    "cyberpunk_neon_noir_specialist": "Emulate cyberpunk neon-noir city and wet chrome.",
    "film_noir_classic_specialist": "Emulate classic noir shafts, venetian, and rain.",
    "impressionism_monet_specialist": "Emulate Impressionist broken color and atmosphere.",
    "italian_giallo_specialist": "Emulate giallo color, gloves, and set-piece kills.",
    "neural_aesthetic": "Steer toward neural/latent aesthetic, not stock CGI.",
    "pixar_specialist": "Emulate Pixar volume, appeal, and story lighting.",
    "soviet_constructivist_brutalist_specialist": "Emulate Constructivist graphic and Brutalist mass.",
    "stop_motion_claymation_aesthetic": "Emulate stop-motion and claymation surface.",
    "studio_ghibli_specialist": "Emulate Ghibli weather, food, and hand-painted air.",
    "surrealism_dali_specialist": "Emulate Dalí-like surreal objects and dream logic.",
    "synthwave_retrowave_specialist": "Emulate synthwave grids, suns, and chrome nights.",
    "ukiyo_e_specialist": "Emulate ukiyo-e line, flat color, and wave.",
    "wes_anderson_specialist": "Emulate Anderson symmetry, pastels, and tableau.",
    # video
    "flux2_json_schema": "Build type-safe Flux.2 JSON payloads for ComfyUI.",
    "flux2dev_architectural_environment": "Generate Flux.2 architectural and environment stills.",
    "flux2dev_cinematic_still_mastery": "Generate Flux.2 cinematic stills as video anchors.",
    "flux2dev_fashion_beauty_editorial": "Generate Flux.2 fashion and beauty editorials.",
    "flux2dev_macro_texture_surface": "Generate Flux.2 macro texture and surface stills.",
    "flux2dev_photorealistic_portraiture": "Generate Flux.2 photoreal portraits with locked DNA.",
    "flux2dev_product_hero_photography": "Generate Flux.2 product hero stills for campaigns.",
    "flux2dev_prompt_engineering_master": "Write Flux.2 prompts: structure, tokens, and locks.",
    "ltx23": "Index LTX 2.3/2.5 video skills: prompt, motion, sync.",
    "ltx23-prompt-engineering-master": "Write LTX present-tense motion prompts that actually move.",
    "ltx23_audio_visual_sync": "Sync LTX native audio, lips, and score to picture.",
    "ltx23_camera_movement_language": "Prompt LTX pans, tracks, cranes, and locked-off holds.",
    "ltx23_character_consistency": "Hold LTX character identity across V2V and I2V.",
    "ltx23_subject_motion_performance": "Direct LTX body acting, gait, and facial performance.",
    "ltx23_technical_configuration": "Set LTX sampler, frames, distilled vs full, LoRAs.",
    "motion_graphics_kinetic_type": "Design kinetic type and motion-graphics beats.",
    "workflow_ltx_i2v": "Run LTX image-to-video from a locked anchor frame.",
    "workflow_flux2_text_to_image": "Run Flux.2 text-to-image on ComfyUI, FAL as fallback.",
    # media-tools already short enough mostly
    "comfyui": "Generate images, video, and audio via ComfyUI workflows.",
    "gif-search": "Search and download Tenor GIFs with curl and jq.",
    "image-generation-workflow": "Generate or refine stills with a repeatable AI loop.",
    "media-pipeline-workflow": "Build and debug multi-stage AI media pipelines.",
    "youtube-content": "Turn a YouTube URL into transcript, chapters, posts.",
}


def skill_name(folder: str) -> str:
    return folder


def category_of(path: Path) -> str:
    rel = path.relative_to(ROOT)
    return rel.parts[0]


def extract_fm(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text
    m = re.search(r"\n---\s*\n", text[3:])
    if not m:
        return None, text
    end = 3 + m.end()
    return text[:end], text[end:]


def replace_description(fm: str, desc: str) -> str:
    quoted = desc.replace('"', '\\"')
    new_line = f'description: "{quoted}"'
    # multiline description: > ... until next unindented key or closing ---
    fm2, n = re.subn(
        r"^description:\s*>[^\n]*\n(?:[ \t].*\n)*",
        new_line + "\n",
        fm,
        count=1,
        flags=re.M,
    )
    if n:
        return fm2
    fm2, n = re.subn(
        r'^description:\s*".*?"\s*$',
        new_line,
        fm,
        count=1,
        flags=re.M,
    )
    if n:
        return fm2
    fm2, n = re.subn(
        r"^description:\s*.*$",
        new_line,
        fm,
        count=1,
        flags=re.M,
    )
    if n:
        return fm2
    # insert after name
    return re.sub(r"^(name:.*)$", r"\1\n" + new_line, fm, count=1, flags=re.M)


def make_frontmatter(name: str, desc: str, category: str) -> str:
    tags = [category.replace("_", "-"), "media", "cinematic"]
    return (
        "---\n"
        f"name: {name}\n"
        f'description: "{desc}"\n'
        "version: 1.1.0\n"
        "author: 0xzgbot, Hermes Agent\n"
        "license: MIT\n"
        "platforms: [linux, macos, windows]\n"
        "metadata:\n"
        "  hermes:\n"
        f"    tags: [{', '.join(tags)}]\n"
        f"    category: {category}\n"
        "---\n\n"
    )


def main() -> None:
    too_long = []
    missing_desc = []
    changed = 0
    for path in sorted(ROOT.rglob("SKILL.md")):
        folder = path.parent.name
        desc = DESCS.get(folder)
        if desc and len(desc) > 60:
            too_long.append((folder, len(desc), desc))
        text = path.read_text(encoding="utf-8")
        fm, body = extract_fm(text)
        if fm is None:
            if not desc:
                missing_desc.append(str(path))
                continue
            new = make_frontmatter(skill_name(folder), desc, category_of(path)) + text.lstrip()
            path.write_text(new, encoding="utf-8")
            changed += 1
            continue
        if not desc:
            # keep existing; check length
            m = re.search(r'^description:\s*["\']?(.*)$', fm, re.M)
            continue
        new_fm = replace_description(fm, desc)
        if new_fm != fm:
            path.write_text(new_fm + body, encoding="utf-8")
            changed += 1
    print(f"updated {changed} skills")
    if too_long:
        print("TOO LONG:")
        for n, L, d in too_long:
            print(f"  {L:3d} {n}: {d}")
    if missing_desc:
        print("NO DESC MAPPING:")
        for p in missing_desc:
            print(" ", p)


if __name__ == "__main__":
    main()
