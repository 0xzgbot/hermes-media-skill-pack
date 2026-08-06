# SKILL: Character Consistency
## Domain: Face Embeddings, LoRA Training, IP Adapters, Wardrobe Locking, Anchor Frames
## Version: 1.0
## For: Hermes Agent — Technical Execution & Pipeline Control

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete technical workflow for maintaining character identity across AI-generated images and video sequences. It covers the four-layer anti-drift architecture (Character DNA → Character Pack → Shot Keyframes → Animation), IP Adapter/LoRA/DreamBooth training workflows, face embedding extraction, wardrobe locking, and the specific project graph graph enforcement that prevents character drift automatically.

When this skill is active, the agent should:
- Build Character DNA specs with precise visual feature definitions
- Generate anchor packs (front, 3/4, profile, expressions)
- Select the appropriate consistency method (IP-Adapter for speed, LoRA for strength)
- Apply frame-to-frame chaining with temporal coherence
- Use project graph to track character embeddings, outfit states, and prop relationships

---

## 2. THE CHARACTER DRIFT PROBLEM

AI models process each generation independently without memory of previous outputs. [^61^] Small variations accumulate across frames, causing gradual changes in facial features, proportions, lighting, and style.

**Symptoms of Drift:**
- Face shape changes between shots
- Eye color shifts subtly
- Outfit details mutate (buttons appear/disappear)
- Lighting direction flips inexplicably
- Background texture crawls

**Root Cause:** Diffusion models sample from latent noise independently per generation. Without identity conditioning, the model invents new features each time. [^61^]

---

## 3. THE FOUR-LAYER ANTI-DRIFT ARCHITECTURE [^61^]

| Layer | What It Is | Why It Matters | project graph node |
|-------|-----------|----------------|------------------|
| **1. Character DNA (Spec)** | Written definition of every visual feature | Creates constraints that prevent AI creativity from ruining consistency | `Character` node with `attributes` JSON |
| **2. Character Pack (Visual Ground Truth)** | Reference images: front, 3/4, profile, expressions | Gives AI a visual anchor to maintain identity | `Asset` nodes linked via `HAS_REFERENCE` edges |
| **3. Shot Keyframes (Camera Views)** | Static images defining each shot's composition | Locks composition before motion is added | `Shot` node with `anchor_frame` property |
| **4. Animation + Edit (Motion + Continuity)** | Video generation and post-production polish | Brings everything to life while preserving layers 1-3 | `Process` node tracing execution flow |

---

## 4. METHOD 1: IP ADAPTER / INSTANTID (Training-Free) [^61^] [^64^] [^65^]

**Best for:** Storyboards, comics, short ads, rapid iteration  
**Speed:** Fast (no training)  
**Strength:** Good for stills and short sequences  
**Weakness:** Struggles with extreme poses, heavy style changes

### How It Works
IP-Adapter extracts identity features from reference images and injects them into the model's attention layers via a lightweight adapter. The base model remains frozen. [^61^]

### Workflow
1. **Curate references:** 5–10 clean images (front, three-quarter, side), similar baseline lighting [^61^]
2. **Extract face:** Crop to face-only for FaceID variants
3. **Set adapter weight:** 0.6–1.0 (higher = stronger identity, less prompt flexibility)
4. **Combine with ControlNet:** Use OpenPose for pose control, Canny for edge structure [^61^]
5. **Prompt hygiene:** Keep stable "identity clause" in prompt (e.g., "short curly hair, red varsity jacket, scar above left eyebrow") [^61^]

### ComfyUI Node Setup
```
Load IPAdapter Model → CLIP Vision Encode (reference image) →
IPAdapter Apply (to conditioned model) → KSampler → VAE Decode
```

**Key Parameters:**
- `weight`: 0.6–1.0 (identity strength)
- `noise`: 0.0–0.1 (adds variation, use sparingly)
- `faceid_v2`: True (for face-specific extraction)

---

## 5. METHOD 2: LORA PERSONALIZATION [^61^] [^64^]

**Best for:** Episodic content, branded characters, long-form comics  
**Speed:** Slow (requires training, 10–30 min)  
**Strength:** Strongest identity lock, works across difficult poses  
**Weakness:** Setup time, risk of overfitting, model version management

### How It Works
LoRA (Low-Rank Adaptation) trains small matrices in the model's attention/convolution layers to encode a specific identity. The base model is frozen; only the LoRA weights update. [^61^]

### Training Dataset
- **10–30 curated images** spanning frontal, 3/4, side views and lighting [^61^]
- **Avoid near-duplicates** — each image must add new information
- **Accurate crops** — face should be 30–50% of frame
- **No watermarks or text overlays**
- **Consistent lighting baseline** — mixed lighting causes averaging errors

### Training Parameters
| Parameter | Recommended Value | Effect |
|-----------|------------------|--------|
| `rank` | 4–16 | Higher = more capacity, risk of overfitting |
| `alpha` | Equal to or half of rank | Learning rate scaling |
| `learning_rate` | 1e-4 to 1e-3 | Conservative to avoid memorization |
| `steps` | 1000–3000 | More steps = stronger identity, risk of overfitting |
| `trigger_word` | Unique token (e.g., "ohwx person") | Activates identity in prompt |

### Validation Checklist
- [ ] Side profile recognizable
- [ ] Different expressions maintain identity
- [ ] Changing outfit doesn't change face
- [ ] Different lighting doesn't change skin tone
- [ ] Prompts unlike training set still produce correct identity

---

## 6. METHOD 3: DREAMBOOTH [^61^]

**Best for:** Deep personalization, single-character focus  
**Speed:** Slowest (fine-tunes entire model)  
**Strength:** Maximum identity fidelity  
**Weakness:** Prone to overfitting, style entanglement, large file size

### How It Works
DreamBooth binds a subject to a unique token through fine-tuning the entire base model. The model learns to associate the trigger word with the visual identity. [^61^]

**Use only when LoRA is insufficient.** For most production workflows, LoRA + IP-Adapter is the optimal stack.

---

## 7. THE CONSISTENCY STACK [^65^]

For maximum consistency across complex scenes, combine methods in layers:

```
Layer 1: Character DNA (text spec)
    └── "Elena: oval face, hazel eyes, dark brown hair, scar above left eyebrow"

Layer 2: LoRA (identity embedding)
    └── Trained on 20 reference images, rank 8, trigger word "elena_ohwx"

Layer 3: IP-Adapter FaceID (face reinforcement)
    └── Reference: front-facing passport photo
    └── Weight: 0.8

Layer 4: ControlNet OpenPose (pose lock)
    └── Pose skeleton from reference or manual pose

Layer 5: Inpainting (detail correction)
    └── Fix eyes, hands, outfit details in post
```

**Result:** 9/10 generations maintain correct identity without manual correction. [^65^]

---

## 8. WARDROBE & PROP LOCKING

### Outfit Consistency Rules
- **Each outfit gets its own anchor pack** — 5+ images showing the outfit from multiple angles
- **Outfit description in prompt** — exact details: "blue denim jacket, white t-shirt, silver pendant"
- **Separate clothing LoRA** — If outfit is complex, train a separate style LoRA for clothing [^61^]
- **Handedness lock** — Document which hand holds which object; never flip

### Prop State Tracking
```yaml
props:
  coffee_cup:
    state: "full, steaming"
    position: "table center"
    color: "white ceramic, red logo"
    held_by: "right_hand"
```

---

## 9. TEMPORAL COHERENCE FOR VIDEO [^61^]

When generating video sequences (LTX 2.3, etc.):
- **Generate in short bursts:** 5–8 seconds maximum per clip
- **Use keyframes:** Define start frame + end frame, let model interpolate
- **Motion prompt discipline:** One action per prompt
- **Frame-to-frame chaining:** Use last frame of clip N as first frame of clip N+1
- **Deflicker in post:** Apply temporal smoothing (EbSynth, frame interpolation)

---

## 10. PROJECT GRAPH INTEGRATION

| Consistency Element | project graph Implementation |
|---------------------|---------------------------|
| Face embedding | `Character` → `HAS_EMBEDDING` → `Embedding` node (ArcFace vector) |
| Reference images | `Character` → `HAS_REFERENCE` → `Asset` nodes (front, 3/4, profile) |
| Outfit state | `Character` → `WEARS` → `Outfit` node with `anchor_pack` path |
| LoRA file | `Character` → `HAS_LORA` → `Model` node with `file_path` and `trigger_word` |
| Prop tracking | `Prop` node with `state`, `position`, `held_by` properties |
| Shot anchor | `Shot` node with `anchor_frame` property |

**MCP Tool Integration:**
- `graph_context` on Character node returns: DNA spec, reference assets, current outfit, LoRA path
- `graph_impact` on Outfit change shows all affected shots
- `graph_detect_changes` flags prop state drift between shots

---

## 11. PROMPT ENGINEERING FOR CONSISTENCY

### Identity Lock Template
```
Character: [name] locked to LoRA [lora_name] with trigger [trigger_word].
Face: [specific features from DNA].
Outfit: [exact description].
Handedness: [left/right].
Distinguishing marks: [scars, freckles, tattoos].
IP-Adapter reference: [anchor_image_path].
ControlNet pose: [pose_reference].
```

### Temporal Lock Template (Video)
```
Frame-to-frame chaining enabled.
Reference previous frame: [frame_path].
Temporal coherence: high.
No flicker, no texture crawl, no lighting pop.
```

---

## 12. NEGATIVE PROMPTS (What Breaks Consistency)

| Avoid | Why | Replace With |
|-------|-----|--------------|
| "different outfit" | Unless scene transition established | "same outfit as anchor", "wardrobe continuity locked" |
| "new hairstyle" | Hair state must match unless time passes | "same hairstyle as reference", "hair continuity maintained" |
| "dramatic lighting change" | Abr shifts cause facial feature drift | "lighting continuity locked", "gradual motivated shift" |
| "ignore previous frame" | Breaks frame-to-frame chaining | "reference previous frame", "temporal chaining active" |
| "multiple actions" | Too many changes increase failure rate | "one action at a time", "single gesture per shot" |
| "extreme angle without reference" | Side profiles fail without side-view refs | "add side-view references", "use pose ControlNet" |

---

## 13. SKILL STACKING

```
BASE SKILL: Prompt Engineering Core
TECH SKILL: Character Consistency (this file)
    └── VOCABULARY: LoRA, IP-Adapter, FaceID, anchor pack, DNA spec
STYLE SKILL: [Any Style Specialist]
    └── VOCABULARY: aesthetic vocabulary
STRUCTURE SKILL: Cinematic Continuity
    └── GRAMMAR: shot lists, temporal coherence
TECH SKILL: ComfyUI/Flux/LTX Pipeline
    └── PARAMETERS: sampler, model, conditioning nodes
```

---

## 14. SOURCES

- Skywork AI, "Character Consistency Explained" [^61^]
- arXiv, "Character-Adapter: Prompt-Guided Region Control" [^64^]
- ApexNeural, "Mastering Character Consistency in GenAI" [^65^]
- Extra-Ordinary TV, "ComfyUI IPAdapter First Attempt" [^68^]
- RunComfy, "Create Consistent Characters with IPAdapter" [^71^]

---

## 15. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering IP-Adapter, LoRA, DreamBooth, the four-layer architecture, wardrobe locking, temporal coherence, and PROJECT GRAPH INTEGRATION.
