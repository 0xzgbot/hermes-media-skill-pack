# Changelog

## 2026-08-27

- **Indexable in current Hermes.** All 142 `SKILL.md` files now start with YAML frontmatter (`name` + `description` ≤ 60 chars). Previously 107 skills had no frontmatter, so `skills_list()` / slash commands never saw them.
- **Install into Cinesmith without touching your Hermes.** Documented `HERMES_HOME=<repo>/hermes_home` vs `~/.hermes`. New skill: `isolated-hermes-home`.
- **Local multi-GPU runtime.** New skills: `multi-comfy-orchestration` (DGX Spark + dual RTX 3090s, one Comfy per GPU), `local-cinematic-pipeline`, `z_image_turbo`, `workflow_ltx_first_last_frame`, `ltx25_beat_scripting`, `vision_audit_remediation`.
- Pack size: **136** top-level skills (was 129).
