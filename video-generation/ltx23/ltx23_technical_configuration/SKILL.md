# SKILL: LTX 2.3 Technical Configuration & Workflow Optimization
## Version: 1.0 | Hermes Agent LTX Settings, Inference Modes & Pipeline Architecture

---

### DESCRIPTION
Deeply researched technical reference for configuring and optimizing LTX 2.3 generation pipelines. This skill encodes the precise resolution rules, frame count constraints, inference mode selection (Fast Flow vs. Pro Flow vs. Distilled), CFG guidance calibration, VRAM tier configurations, Extend/Retake workflow strategies, and the native portrait (9:16) generation parameters required for production deployment. Covers quantization options, sampler configuration, the two-pass upscaling pipeline, and cost-performance optimization for high-volume workflows.

---

### TECHNICAL PARAMETERS

**LTX 2.3 Model Variants:**

| Variant | Parameters | Steps | CFG | VRAM | Speed | Quality | Best For |
|---------|-----------|-------|-----|------|-------|---------|----------|
| **Fast Flow (ltx-2.3-fast)** | 22B distilled | 8 | 1.0 | 12–16GB | 5–7x real-time | 85–90% of Pro | Rapid iteration, social drafts, concept testing |
| **Pro Flow (ltx-2.3-pro)** | 22B dev | 50+ | 3.0–7.0 | 24GB+ | 1x real-time | Maximum | Final production, cinematic output, detail-critical |
| **Distilled LoRA 384** | 22B + LoRA | 8 | 1.0 | 12–16GB | 5–7x real-time | 85–90% + style lock | Styled output with LoRA consistency |
| **FP8 Quantized** | 22B compressed | Same as base | Same | 16–20GB | Slightly slower | ~95% of full | Consumer GPU deployment, local inference |

**Resolution & Aspect Ratio Matrix:**

| Resolution | Aspect Ratio | Use Case | Notes |
|-----------|-------------|----------|-------|
| **1216 × 704** | 16:9 (default) | General video, landscape | Base resolution, fastest generation |
| **1280 × 704** | ~16:9 | Slightly wider landscape | Minor quality improvement |
| **704 × 1216** | 9:16 | Portrait, social (TikTok/Reels/Shorts) | Native portrait trained on vertical data |
| **768 × 1344** | 9:16 | Higher portrait | Better detail for talking heads |
| **1080 × 1920** | 9:16 | Full HD portrait | Requires upscaling or Pro Flow |
| **1920 × 1080** | 16:9 | Full HD landscape | Requires latent upscaler |
| **3840 × 2160** | 16:9 | 4K cinematic | Requires x2 spatial upscaler + Pro Flow |

**Critical Dimension Rules:**
- **Width and Height must be divisible by 32** — any other value causes errors or quality degradation
- **Frame count must be divisible by 8 + 1** — valid: 33, 41, 49, 65, 81, 97, 121, 145, 161, 193, 257
- **Optimal max frames:** Under 257 for quality retention
- **Extend function:** Use for sequences longer than 257 frames — splices at continuity points

**Frame Rate Selection:**

| FPS | Native Support | Motion Feel | Best For |
|-----|---------------|-------------|----------|
| **24 FPS** | ✅ Yes | Cinematic, film-like | Narrative, drama, cinematic content |
| **25 FPS** | ✅ Yes | Broadcast standard | PAL regions, broadcast, documentary |
| **30 FPS** | ✅ Yes | Smooth, video standard | General content, social media, US broadcast |
| **48 FPS** | ✅ Yes | Hyper-smooth, HFR feel | Action, sports, high-motion content |
| **50 FPS** | ✅ Yes | Broadcast smooth | PAL sports, live feel, action |
| **60 FPS** | ❌ No | — | Not natively supported; generate at 30 and interpolate |

**CFG Guidance Calibration:**

| CFG Value | Effect | Best For | Warning |
|-----------|--------|----------|---------|
| **1.0** | Distilled mode only, no extrapolation | Fast Flow, speed-critical | Cannot use with negatives effectively |
| **3.0** | Light guidance, creative freedom | Atmospheric, mood-driven | May drift from prompt on long clips |
| **4.0** | Balanced adherence | Most production work | Sweet spot for Pro Flow |
| **5.0** | Strong adherence | Technical accuracy, product | Slight over-saturation risk |
| **6.0–7.0** | Maximum adherence | Prompt-critical content | Risk of posterization, temporal stiffness |
| **7.0+** | Not recommended | — | Severe artifacting, broken motion |

---

### PROMPT ARCHITECTURE

**Configuration Decision Tree:**
```
1. What is the output destination?
   → Social vertical (9:16) / Social horizontal (16:9) / Cinematic (16:9) / Broadcast (16:9 or 9:16)

2. What is the duration needed?
   → Under 5 sec: Single generation
   → 5–10 sec: Single generation at higher frame count
   → 10–20 sec: Single generation OR Extend from shorter clip
   → 20+ sec: Extend workflow mandatory

3. What quality level is required?
   → Draft/concept: Fast Flow (8 steps)
   → Production: Pro Flow (50+ steps)
   → Maximum: Pro Flow + x2 upscaler

4. What hardware is available?
   → 12–16GB VRAM: Fast Flow or FP8 quantized Pro
   → 24GB+ VRAM: Full Pro Flow
   → 48GB+ VRAM: Pro Flow + batch generation

5. Is character consistency critical?
   → Yes: I2V anchor + ID-LoRA if talking
   → No: T2V acceptable

6. Is audio required?
   → Yes: Enable audio generation in pipeline
   → No: Disable audio VAE to save VRAM and computation
```

**The Two-Pass Upscaling Pipeline (For High Resolution):**
```
Pass 1 — Low Resolution:
- Resolution: 1216 × 704 (or target aspect ratio at base resolution)
- Steps: 50 (Pro) or 8 (Fast)
- Purpose: Generate motion structure, composition, and temporal coherence

Pass 2 — Latent Upscale:
- Node: LTXVLatentUpsampler x2
- Purpose: Double spatial resolution in latent space before decoding
- Benefit: Preserves motion while adding detail capacity

Pass 3 — High Resolution Refine:
- Resolution: Upscaled dimensions
- Steps: Additional refinement sampling
- Purpose: Lock in textures, lighting, and fine motion at higher resolution

Pass 4 — Tiled Decode:
- Node: VAEDecodeTiled
- Purpose: Prevent memory spikes at high resolution
- Output: Final frames at target resolution
```

**VRAM Tier Configuration:**

| VRAM | Mode | Resolution | Batch | Notes |
|------|------|-----------|-------|-------|
| **8–12GB** | Fast Flow FP8 | 1216×704 | 1 | Enable CPU offload, tiled decoding mandatory |
| **12–16GB** | Fast Flow or FP8 Pro | 1216×704 to 1280×704 | 1 | Tiled decoding recommended |
| **16–24GB** | Pro Flow FP8 | Up to 1920×1080 | 1 | Can run x2 upscaler with tiling |
| **24–32GB** | Pro Flow full | Up to 4K | 1–2 | Full precision, upscaler enabled |
| **32–48GB** | Pro Flow full | 4K | 2–4 | Batch generation possible |
| **48GB+** | Pro Flow full | 4K | 4+ | Maximum throughput, research workloads |

---

### ADVANCED TECHNIQUES

**1. The Fast-to-Pro Iteration Pipeline**
- Step 1 — Fast Flow Draft: Generate 10+ variations at 8 steps, 1216×704, Fast Flow
- Step 2 — Select Best: Review motion, composition, and concept
- Step 3 — Lock Seed: Note the seed of the best draft
- Step 4 — Pro Flow Final: Same prompt, same seed, switch to Pro Flow at 50+ steps
- Step 5 — Optional Upscale: Apply x2 latent upscaler for final resolution
- Time Savings: 70–80% of iterations run at Fast speed; only final render uses Pro
- Best For: Client work, iterative creative direction, high-volume production

**2. The Extend Workflow for Long-Form**
- Problem: Single generation limited to ~257 frames (~8.5 sec at 30 FPS)
- Solution: Generate in segments, use Extend function to splice
- Workflow:
  1. Generate Segment A (0–5 seconds) with strong ending frame
  2. Use Extend: Segment A's last frame becomes Segment B's anchor
  3. Prompt Segment B with continuation action, maintaining locked parameters
  4. Repeat for desired duration
- Continuity Locks: Keep camera system, lighting, film stock, and atmospheric density identical across segments
- Transition Strategy: End each segment with a natural pause or motion completion point
- Best For: Narrative films, documentary sequences, long-form content

**3. The Retake Correction Strategy**
- Problem: One segment of a longer clip has artifacts; regenerating everything wastes time
- Solution: Retake function replaces only the problematic segment
- Workflow:
  1. Identify problematic time range (e.g., frames 60–90)
  2. Adjust prompt for that segment (more guardrails, simplified motion)
  3. Generate retake with identical seed and locked parameters
  4. Splice retake into original timeline
- When to Retake vs. Regenerate:
  - Retake: Minor artifact in one segment, rest is perfect
  - Regenerate: Global issues (lighting drift, style inconsistency)
- Best For: Production workflows where time is critical

**4. The Portrait Native Optimization**
- LTX 2.3 is trained on native vertical (9:16) data — NOT cropped from horizontal
- Portrait Generation Settings:
  - Resolution: 704 × 1216 or 768 × 1344 (divisible by 32)
  - Framing: Face fills 30–40% of frame for talking heads
  - Camera: Slight high angle (10–15°) is flattering for faces
  - Motion: Minimize horizontal camera movement in vertical frame
- Talking Head Specific:
  - Use ID-LoRA for identity consistency
  - Keep shoulders visible for natural framing
  - Static or very slow push-in only — fast motion causes distortion at vertical edges
- Best For: TikTok, Reels, Shorts, vertical social content, mobile-first campaigns

**5. The I2V Anchor Lock Protocol**
- Purpose: Maximum visual consistency across a video sequence
- Anchor Generation: Use FLUX 2 Pro/Max for highest-detail still frame
- Anchor Requirements:
  - Resolution: Match target video resolution (or higher, downscale)
  - Detail: Maximum skin texture, fabric detail, environmental clarity
  - Composition: Leave room for intended camera motion direction
- I2V Prompt Focus: Describe ONLY motion and temporal change — never redescribe static visuals
- Multi-Shot Continuity:
  - Shot 1: Anchor A → I2V motion A
  - Shot 2: Generate final frame of Shot 1 → use as Anchor B → I2V motion B
  - This creates natural visual continuity between shots
- Best For: Character-driven narratives, product showcases, branded content

**6. The Batch Generation Template**
- Purpose: Efficient high-volume production with consistent style
- Setup:
  1. Create master prompt template with locked parameters
  2. Define variable slots: [SUBJECT], [ACTION], [ENVIRONMENT]
  3. Generate anchors in batch using FLUX 2 with locked seed range
  4. Feed anchors to LTX I2V with motion templates
- Automation Strategy:
  - CSV input: subject_list × motion_type combinations
  - Fixed seed increment: seed = base_seed + iteration_number
  - Output naming: `{subject}_{motion}_{seed}.mp4`
- Cost Optimization: Run Fast Flow for batch drafts; Pro Flow only for approved concepts
- Best For: E-commerce product videos, real estate walkthroughs, lookbook sequences

**7. The Sampler Sigma Tuning**
- Node: ManualSigmas + KSamplerSelect
- Principle: Higher early noise encourages broader movement; later steps consolidate texture
- Configuration Profiles:
  - **High Motion Profile:** Aggressive early sigmas, conservative late sigmas → more dynamic motion, slightly softer detail
  - **High Detail Profile:** Conservative early sigmas, aggressive late sigmas → sharper detail, more restrained motion
  - **Balanced Profile:** Linear sigma schedule → default behavior
- When to Adjust:
  - Motion too stiff: Increase early sigma range
  - Detail too soft: Extend late sigma tail
  - Temporal jitter: Smooth sigma curve between steps
- Best For: Technical fine-tuning after prompt optimization

---

### EXAMPLE PROMPTS

**Configuration-First Prompt (Template Style):**
> This prompt uses the Fast-to-Pro pipeline: generate first at Fast Flow (8 steps, CFG 1.0) to verify motion and composition, then render final at Pro Flow (50 steps, CFG 4.0) with x2 latent upscaler. Resolution: 1216×704 (16:9), frame count 65 (2.1 sec at 30 FPS), static tripod-locked camera. Scene: misty mountain lake at dawn. Subject: lone kayaker paddling slowly across still water. Motion: gentle paddle strokes creating ripples, mist drifting across water surface. Style: documentary nature cinematography, cool blue palette. Audio: paddle dipping into water, distant bird calls, absolute silence between sounds.

**Portrait Native Configuration:**
> Native portrait generation at 704×1216, 30 FPS, 49 frames (1.6 sec). Fast Flow draft first, then Pro Flow final. Subject: professional woman speaking directly to camera. Camera: static at slight high angle, head and shoulders framing. ID-LoRA identity locked. [VISUAL] Clean office background, soft key light from left. [SPEECH] "Welcome to today's briefing." [SOUNDS] Warm professional voice, clean recording, minimal reverb. Guardrails: Stable face proportions, natural lip sync, no background drift.

**Extend Workflow Specification:**
> Segment A (0–5 sec): 1216×704, 65 frames, Pro Flow, Kodak Vision3 250T style. Scene: abandoned factory interior. Camera: slow push-in from wide to medium. Subject: None — environmental only, dust particles in light beams. End frame: tight on a single broken window with light streaming through.
> Segment B (5–10 sec): Extend from Segment A end frame. Camera: static on broken window. Motion: Dust continues drifting. Light shifts slightly as clouds pass. Audio: Wind whistling through broken glass, distant creaking metal.
> Continuity locks: Film stock identical, lighting temperature identical (5600K), atmospheric density identical, no camera system change.

---

### TECHNICAL NOTES FOR AI GENERATION
- **Always verify dimensions divisible by 32** — 1216/32=38, 704/32=22, 768/32=24, 1344/32=42. Any remainder causes pipeline errors.
- **Frame count formula:** target_frames = (desired_seconds × FPS). Round down to nearest (8n + 1). Example: 5 sec at 30 FPS = 150 frames → round to 145 (8×18+1).
- **Fast Flow is NOT just "lower quality"** — it's a distilled model with different motion priors. Some motions work better in Fast; some need Pro.
- **FP8 quantization:** Use for Pro Flow on consumer GPUs. Quality loss is ~5% versus full precision but enables 4K generation on 24GB cards.
- **Tiled decoding is mandatory above 1536px width** — VAEDecodeTiled prevents OOM errors and ensures consistent frame quality.
- **Latent upscaler preserves motion** — Unlike pixel-space upscaling, LTXVLatentUpsampler x2 doubles resolution without re-interpreting motion.
- **Seed management for reproducibility:** Lock seed when iterating on prompt text. Randomize seed only after the prompt direction is confirmed.
- **Audio VAE can be disabled** — If generating video without audio, disable the audio stream to save ~20% VRAM and computation.
- **Extend vs. longer single generation:** Extend is more reliable than pushing single generation toward 257 frames. Quality degrades noticeably past ~200 frames.
- **Portrait (9:16) is natively trained** — Do not crop horizontal output. Generate at 704×1216 or 768×1344 for best vertical results.
- **CFG 1.0 in Fast Flow means negatives are weak** — Use positive guardrails instead of negative prompts in Fast mode.
- **Pro Flow CFG 3.0–7.0:** Start at 4.0. Increase to 5.0–6.0 for prompt-critical content (products, exact compositions). Never exceed 7.0.
- **Two-pass workflow for 4K:** Always generate motion at base resolution first, then upscale. Generating 4K directly from noise is unstable and slow.
- **Batch generation consistency:** Use identical locked parameters (sampler, sigmas, CFG) across batch. Vary only the intended variable (subject, motion, seed).
- **For ComfyUI workflows:** The LTXVConditioning node is the most effective place to adjust style and scene behavior without touching samplers. Favor short, clear, time-aware sentences.
