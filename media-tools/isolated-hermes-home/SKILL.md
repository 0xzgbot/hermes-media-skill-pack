---
name: isolated-hermes-home
description: "Run a project Hermes that does not touch yours."
version: 0.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, isolation, cinesmith, local-ai]
    category: media-tools
    related_skills: [multi-comfy-orchestration, local-cinematic-pipeline]
---

# Isolated Hermes Home

Use a **project-local** Hermes (`HERMES_HOME=<repo>/hermes_home`) so media production does not modify the Hermes you already run for coding, chat, or other boards.

This skill does **not** install a second copy of the Hermes binary. It points the existing CLI at a separate home directory: skills, profiles, memory, and kanban live beside the project, not in `~/.hermes`.

## When to Use

- Launching Cinesmith / Forge NPS / a media pipeline next to a daily-driver Hermes
- The user says "don't touch my Hermes" or "isolated hermes_home"
- Installing this media skill pack into a production runtime, not the global agent

Don't use for: editing `~/.hermes/skills` on purpose; one-off `/skills install` into the default home.

## Prerequisites

- Hermes CLI on `PATH`
- A project with `hermes_home/` (Cinesmith ships this) **or** willingness to create one
- Optional escape hatch only if the user explicitly wants the global home: `CINESMITH_ALLOW_GLOBAL_HERMES=1`

## Procedure

1. Confirm the intended home. Completion: `echo $HERMES_HOME` is empty or already the project path, never a surprise `~/.hermes` rewrite.
2. Export isolation **before** any Hermes subprocess:
   ```bash
   export HERMES_HOME="/path/to/project/hermes_home"
   mkdir -p "$HERMES_HOME/skills" "$HERMES_HOME/profiles"
   ```
   Completion: the directory exists and is writable.
3. Re-assert after sourcing `.env`. Cinesmith's `launch_cinesmith.sh` does this so a mistaken `HERMES_HOME` in `.env` cannot stick. Completion: launcher logs show `HERMES_HOME=<repo>/hermes_home`.
4. Install this pack **into that home**, not `~/.hermes`:
   ```bash
   cp -R audio cinematography consistency-quality genre-libraries lighting \
     media-tools narrative-formats post-production prompt-engineering \
     style-specialists video-generation "$HERMES_HOME/skills/"
   ```
   Completion: `ls "$HERMES_HOME/skills/cinematography"` lists skills.
5. Leave the user's global install alone. Completion: `ls ~/.hermes/skills` is unchanged from before the session (no new copies, no deleted skills).

## Pitfalls

- Copying the pack to `~/.hermes/skills` **is** modifying the Hermes they use. Don't.
- `CINESMITH_ALLOW_GLOBAL_HERMES=1` is an explicit opt-in, not a default.
- Isolation is the **home directory**, not a second GPU. ComfyUI URLs stay in `.env` (`COMFYUI_PRIMARY`, extra instances).
- Current session skill cache will not see new files until a new Hermes session.

## Verification

- `test "$HERMES_HOME" != "$HOME/.hermes"`
- Project skills resolve under `$HERMES_HOME/skills`
- Global `~/.hermes` mtime/skill list unchanged unless the user opted in
