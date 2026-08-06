# SKILL: Seed Strategy
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Mastery of pseudorandom seed management for reproducibility, iteration, and character consistency. The seed initializes the latent noise pattern; locking it while varying the prompt produces controlled variations of the same base image. This is the foundation of character consistency pipelines, A/B testing, and production workflows where predictability matters.

### TRIGGER KEYWORDS
seed, seed strategy, seed lock, reproducibility, consistent generation, same seed, random seed, seed number, latent noise, character seed, seed variation, seed management, production seed

### CORE RULES
- Lock seed + keep prompt = reproducible output; change seed = entirely different image
- Seed range 1–4294967295 (32-bit); seeds close in value produce slightly similar noise patterns
- Character consistency workflow: find good seed with test prompt, lock it, vary poses/lighting
- A/B testing: same seed, different prompts — isolates the effect of prompt changes
- -1 or random seed for exploration; named integer for production
- Seed + model + sampler + steps + CFG must all be locked for true reproducibility
- Batch generation: increment seed by 1 for controlled variation series

---

### SEED FUNDAMENTALS

**What a Seed Controls:**
- The initial random noise tensor that diffusion denoises into an image
- Same seed + same prompt + same model + same settings = identical image
- Same seed + different prompt = variation on same base composition
- Different seed + same prompt = completely different interpretation

**Seed Range:**
- Typical range: 0 to 2^32–1 (0 to 4,294,967,295)
- Common practice: 6–10 digit seeds (e.g., 123456789, 42, 1337)
- Zero or -1: Random seed (new noise each time)

---

### WHEN TO LOCK VS. WHEN TO RANDOMIZE

**Lock the Seed When:**
1. **Character Consistency:** Same character across multiple poses/expressions/outfits
2. **A/B Testing:** Changing one prompt element while holding all else constant
3. **Iterative Refinement:** Small prompt tweaks to improve a near-perfect image
4. **Series Production:** Multiple images in same style/setting for editorial or story
5. **Negative Prompt Testing:** Testing which negatives actually fix artifacts
6. **Upscale Pass:** Generating base image then upscaled version from same seed

**Randomize the Seed When:**
1. **Exploration:** Searching for happy accidents and unexpected compositions
2. **Divergent Concepts:** Same prompt, wildly different interpretations to choose from
3. **Batch Generation:** Producing 10–50 variations for selection
4. **Fixing Bad Anatomy:** A locked seed with bad hands may never fix them; new seed often helps
5. **Breaking Stagnation:** When iterations on locked seed stop improving
6. **Creative Discovery:** Early ideation phase before locking direction

---

### CHARACTER SEED MANAGEMENT

**The Character Consistency Pipeline:**

**Step 1: Base Seed Discovery**
- Generate 10–20 random seeds with your character description
- Select the seed that produces the best base face/body/proportions
- Record: seed number, model, sampler, steps, CFG, resolution

**Step 2: Lock Base Seed**
- Use locked seed for all subsequent character images
- Vary only: action, outfit, environment, lighting, expression
- Keep constant: subject description core, seed, model, technical settings

**Step 3: Controlled Variation**
```
Base prompt (locked seed): "Portrait of [character description], [ACTION], [ENVIRONMENT], [LIGHTING], [STYLE]"
Variation A (seed locked): "Portrait of [character], smiling, coffee shop, warm window light, candid photography"
Variation B (seed locked): "Portrait of [character], serious, rooftop at night, neon backlight, cyberpunk aesthetic"
Variation C (seed locked): "Portrait of [character], laughing, park at golden hour, natural backlight, lifestyle photography"
```

**Step 4: Drift Management**
- After 5–10 variations, check for subtle drift in face shape, eye color, or proportions
- If drift occurs: Return to base prompt, regenerate, compare, adjust prompt to reinforce constants
- Use face-specific reinforcement: `same face, identical eyes, consistent features`

---

### SEED + PROMPT VARIATION MATRIX

| Strategy | Seed | Prompt Change | Result | Use Case |
|----------|------|---------------|--------|----------|
| Clone | Locked | None | Identical image | Reproduction, verification |
| Micro-tune | Locked | 1 word changed | Subtle shift | Iterative refinement |
| Pose shift | Locked | Action clause changed | Same person, new pose | Character series |
| Wardrobe | Locked | Clothing changed | Same person, new outfit | Fashion series |
| Location | Locked | Environment changed | Same person, new place | Story sequence |
| Mood | Locked | Lighting changed | Same person, new mood | Emotional arc |
| Style | Locked | Style suffix changed | Same person, new medium | Art exploration |
| Parallel | Locked | Major rewrite | Related but different | Alternative takes |
| Fresh | Random | Same prompt | New interpretation | Exploration, selection |
| Batch | Random series | Same prompt | 10–50 options | Client selection |

---

### ADVANCED SEED TECHNIQUES

**1. The Seed Ladder (Progressive Variation)**
- Start with seed X
- Generate variations at seeds X+1, X+2, X+3...
- Result: Related but progressively diverging images
- Best for: Finding the sweet spot between consistency and variety

**2. The Prompt Sandwich (Seed Lock with Variable Filling)**
```
[Constant prefix: character description + seed locked]
+
[Variable middle: action, environment, lighting]
+
[Constant suffix: quality tokens + technical specs]
```
This keeps identity stable while allowing scene variation.

**3. The Negative Seed Test**
- Generate image with seed X
- Generate same prompt with seed X but different negatives
- Compare to identify which negatives actually matter
- Log results per model [^56^]

**4. The Subseed / Variation Seed (SD WebUI)**
- Some interfaces support "subseed" or "variation seed"
- Controls how much the image deviates from base seed
- Low variation: Nearly identical; High variation: Completely different
- Best for: Fine-tuning without full prompt rewrite

**5. The Batch Grid (A/B/C Testing)**
- Same prompt, 9 seeds in a 3×3 grid
- Same seed, 9 prompt variations in a grid
- Visual comparison reveals what matters most

**6. The Character Seed Vault**
- Maintain a database of proven character seeds:
```
Character: "Cyberpunk Hacker Girl"
Model: SDXL Pony v6
Seed: 847291056
Base prompt: "score_9, score_8_up, 1girl, cyberpunk hacker, neon hair, techwear..."
Tested variations: 23
Drift after: 15 generations
Notes: Best at 768×1344, slight eye drift after 12th gen
```

---

### SEED STRATEGY BY WORKFLOW TYPE

**SDXL / z_image Character Workflow:**
1. Random search: Generate 20 random seeds
2. Select best: Lock seed with best face
3. Variation series: 10 poses with locked seed
4. Drift check: Compare #1 and #10
5. If drift > threshold: New seed search or prompt reinforcement

**Flux Character Workflow:**
1. Random search: Generate 15 random seeds (Flux is more consistent natively)
2. Select best: Lock seed
3. Variation series: Vary action/environment; keep subject core identical
4. Flux advantage: Better natural consistency; less drift than SDXL
5. Note: Flux doesn't use negative prompts; rely on positive reinforcement

**LTX Video Workflow:**
1. Seed determines initial noise for first frame
2. Subsequent frames use temporal consistency mechanisms
3. Lock seed for scene consistency across clip
4. Vary seed between scenes for scene breaks
5. Use same seed + same character prompt for character continuity across shots

**Product / Commercial Workflow:**
1. Lock seed for product consistency (same object, different angles)
2. Vary camera angle, lighting, environment
3. Maintain seed for color accuracy and material consistency
4. New seed only when exploring entirely different product presentations

---

### EXAMPLE WORKFLOWS

**Character Portrait Series (SDXL):**
```
Base: seed=847291056 (locked)
Prompt core: "score_9, score_8_up, 1girl, olive skin, dark curly hair, green eyes, sharp cheekbones, soft smile"

Shot 1: "...standing in sunlit library, warm afternoon light, medium shot"
Shot 2: "...sitting at café table, rain on window, cool blue ambient, close-up"
Shot 3: "...walking through autumn park, golden backlight, full body, 2:3 vertical"
Shot 4: "...reading by fireplace, warm tungsten, intimate close-up"
Shot 5: "...on rooftop at dusk, city lights behind, dramatic silhouette, 16:9"
```

**Product Hero Shots (Flux):**
```
Base: seed=338104 (locked)
Prompt core: "Sharp focus product photography of titanium water bottle"

Shot 1: "...floating in pure white void, soft even lighting, 1:1 square"
Shot 2: "...on marble countertop in modern kitchen, window light, 4:5 vertical"
Shot 3: "...in hiker's hand on mountain summit, golden hour, 16:9 horizontal"
Shot 4: "...extreme macro of cap threading, studio lighting, 1:1 square"
```

**LTX Video Scene Consistency:**
```
Scene 1 seed: 552781 (locked for café scene)
Scene 2 seed: 552782 (locked for street scene — related but distinct)
Scene 3 seed: 552783 (locked for home scene)
Character prompt core identical across all three seeds
```

---

### SEED LOGGING TEMPLATE

```
PROJECT: [Name]
MODEL: [Model name + version]
DATE: [YYYY-MM-DD]

BASE SEED: [Number]
BASE PROMPT: [Full prompt]
SETTINGS:
  - Sampler: [Name]
  - Steps: [Number]
  - CFG: [Value]
  - Resolution: [W×H]
  - Ratio: [Aspect]

VARIATIONS TESTED: [Count]
DRIFT OBSERVED: [Yes/No, after how many]
BEST USE CASE: [Portrait/Product/Scene]

VARIATION LOG:
  - V01: [Change made, result, keep/discard]
  - V02: [Change made, result, keep/discard]
```

---

### TECHNICAL NOTES FOR AI GENERATION
- Seed consistency requires ALL parameters locked: model, sampler, steps, CFG, resolution, prompt
- Changing sampler or steps with same seed produces different images
- SDXL: Character drift is common after 8–12 variations; plan for prompt reinforcement
- Flux: More naturally consistent; character drift is slower but still occurs after 15+ variations
- LTX: Seed affects first frame most strongly; temporal consistency handles subsequent frames
- Save seeds obsessively: The perfect image without saved seed cannot be reproduced
- Use seed + prompt pairs as "recipes" that can be shared across team members
- For commercial workflows, maintain a "seed vault" of proven character/product seeds
