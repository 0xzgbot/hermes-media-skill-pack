# Changelog

## 2026-08-27 (H3 + Wan prompting clusters)

- **MiniMax H3 / Hailuo 3.** Cluster `video-generation/minimax_h3`: Base vs Full-Reference dialects from MiniMax's official prompt guides (shot blocks, `<d>` dialogue, I2VA/FL2VA/L2VA alignment lines, six-section Ref2VA). Specialists: camera (type + amplitude + speed), stereo audio, omni-reference, technical (IR vs Base vs 2K, FL2VA vs ref2va).
- **Wan 2.2 / 2.7 / 3.0 Prime.** Cluster `video-generation/wan`: UMT5 + MoE local 2.2 vs Thinking Mode vs the **new Wan 3.0** (up to 30 s, 20 refs, native audio, Auto Polish / thinking flags). Specialists: camera/FLF/Animate, three-layer sound, Omni-Reference `@` labels.
- Pack size: **138** top-level skills, **153** `SKILL.md` (was 136 / 142).

## 2026-08-27

- **Indexable in current Hermes.** All 142 `SKILL.md` files now start with YAML frontmatter (`name` + `description` ≤ 60 chars). Previously 107 skills had no frontmatter, so `skills_list()` / slash commands never saw them.
- **Install into Cinesmith without touching your Hermes.** Documented `HERMES_HOME=<repo>/hermes_home` vs `~/.hermes`. New skill: `isolated-hermes-home`.
- **Local multi-GPU runtime.** New skills: `multi-comfy-orchestration` (DGX Spark + dual RTX 3090s, one Comfy per GPU), `local-cinematic-pipeline`, `z_image_turbo`, `workflow_ltx_first_last_frame`, `ltx25_beat_scripting`, `vision_audit_remediation`.
- Pack size: **136** top-level skills (was 129).
