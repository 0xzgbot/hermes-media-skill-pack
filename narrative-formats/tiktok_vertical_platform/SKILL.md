---
name: tiktok_vertical_platform
version: 1.0
description: TikTok vertical short platform constraints for mobile-first image and LTX video generation.
---

# TikTok Vertical Platform

## TRIGGER KEYWORDS
tiktok, tik tok, vertical short, vertical video, 9:16, reels, youtube shorts, short-form social

## CORE RULES
- Force a vertical 9:16 composition with 1080x1920 output intent.
- Treat the first 0-3 seconds as the hook window: close readable emotion, travel payoff, or immediate visual surprise.
- Keep the main subject centered enough for phone viewing; do not place important detail at extreme edges.
- Use bottom-third caption-safe space; faces and key action should sit above the lower caption band.
- Captions should be big, bold, white text with a black outline, under nine words when possible.
- Prefer 8-15 second pacing for LTX shorts unless the user explicitly requests another duration.

## PROMPT ARCHITECTURE
- Start with the subject and immediate hook action.
- Specify vertical mobile framing before lens detail.
- Include caption overlay instructions only as design direction, not literal scene text unless captions are being rendered.
- Add retention language: fast emotional clarity, immediate payoff, simple silhouette, readable motion.

## NEGATIVE CONTROL
- Avoid tiny text, crowded wide shots, low-contrast captions, important details behind captions, and slow establishing-only openings.
