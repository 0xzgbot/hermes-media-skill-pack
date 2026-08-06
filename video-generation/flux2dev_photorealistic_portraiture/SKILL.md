# SKILL: FLUX.2 Dev Photorealistic Portraiture
## Version: 1.0 | Hermes Agent Flux2 Portrait & Skin Fidelity Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for achieving maximum photorealism in human portraits with FLUX.2 Dev. This skill encodes the exact token-weight hierarchy, camera-lens pairings, anatomical positive-framing strategies, and skin-texture descriptors that push FLUX.2 Dev toward pore-level fidelity without the plastic AI sheen. Covers eye detail, hair strand rendering, ethnic skin tone accuracy, age representation, and the specific positive-only constraint architecture required by FLUX.2 Dev's guidance-distilled design.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Portrait Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled — no native negative prompt support)
- **Token Priority:** First 10–15 tokens carry 60%+ of prompt weight. Subject identity MUST lead.
- **Prompt Length:** 40–80 words optimal for portraits. Under 30 = model hallucinates details. Over 150 = internal summarization drops nuance.
- **Guidance Scale:** 3.5–4.5 for portraits (distilled model; higher = plastic skin, lower = soft drift)
- **Steps:** 28–35 for production skin detail. 40+ adds micro-texture but risks over-smoothing.
- **Resolution:** 1024×1024 base for face detail; upscale via SR rather than generating >1536 directly.
- **No Prompt Weights:** `(word:1.2)`, `++`, `--` syntax is ignored or harmful in FLUX.2 Dev.

**The Anatomy Positive-Prevention System (No Negatives):**
FLUX.2 Dev cannot receive negative prompts natively. Every anatomical safeguard must be phrased as a desired positive quality:

| Problem | Negative (Forbidden) | Positive Reframe (Required) |
|---------|---------------------|----------------------------|
| Extra fingers | no extra fingers, bad hands | natural hand anatomy, five fingers visible, correct digit count |
| Blurry eyes | not blurry, bad eyes | sharp iris detail, visible catchlights, crisp eyelash definition |
| Plastic skin | not plastic, no AI look | natural skin texture, visible pores, subtle imperfections, organic epidermis |
| Asymmetrical face | symmetrical face (ambiguous) | balanced facial proportions, natural symmetry, harmonious features |
| Deformed teeth | no deformed teeth | natural dental alignment, realistic tooth spacing, organic gum line |
| Crossed eyes | not crossed | eyes looking in same direction, aligned gaze, natural ocular convergence |
| Hair artifacts | not weird hair | individual hair strands, natural hair parting, realistic follicle density |
| Flat lighting | not flat | dimensional light wrapping, modeled cheekbones, sculpted jawline |

**Camera-Lens Pairings for Portrait Fidelity:**

| Camera + Lens | F-Stop | Skin Rendering | Bokeh Character | Best For |
|--------------|--------|---------------|-----------------|----------|
| Canon EOS R5, 85mm f/1.2L | f/1.4–f/2.0 | Warm, creamy, flattering | Creamy circular, smooth transition | Beauty, headshots, glamour |
| Hasselblad X2D, 90mm f/2.5 | f/2.8–f/4.0 | Neutral, editorial, precise | Hexagonal, clinical | Editorial, skincare, fashion |
| Sony A7R V, 135mm f/1.8 GM | f/1.8–f/2.2 | Compressed, dramatic, sharp | Cat-eye oval, pronounced | Cinematic close-ups, drama |
| Leica M11, 50mm f/0.95 Noctilux | f/0.95–f/1.4 | Dreamy halation, romantic | Swirly, vintage character | Artistic portraiture, mood |
| Fujifilm GFX 100S, 110mm f/2 | f/2.0–f/2.8 | Medium format smoothness, detail | Gentle, medium-format quality | High-end editorial, luxury |
| iPhone 16 Pro, 24mm (main) | f/1.78 | Computational, candid, natural | Minimal, deep DoF | Lifestyle, selfie aesthetic, candid |

**Skin Texture Descriptor Hierarchy (Most to Least Effective):**
1. **"Visible pore structure on cheeks and forehead"** — triggers micro-detail rendering
2. **"Subtle skin imperfections, faint freckles, natural epidermal texture"** — organic realism
3. **"Fine vellus hair on jawline and upper lip"** — separates AI-smooth from human skin
4. **"Realistic sebaceous sheen on nose and forehead"** — oil rendering prevents matte plastic
5. **"Subtle undertone variation — warm cheeks, cool forehead"** — chromatic complexity
6. **"Natural collagen texture, not retouched"** — prevents beauty-filter over-smoothing

**Eye Detail Triggers:**
- **"Visible catchlights from window source in upper iris"** — life and dimension
- **"Iris fiber detail, radial striations in hazel/green/blue pigment"** — prevents flat colored circles
- **"Sharp limbal ring, natural sclera veining"** — anatomical accuracy
- **"Moisture on lower eyelid, subtle tear film reflection"** — prevents dry doll eyes
- **"Natural eyebrow hair direction, individual strands at arch"** — brow realism

---

### PROMPT ARCHITECTURE

**Core Portrait Template (FLUX.2 Dev):**
```
[Subject identity: age, ethnicity, gender, distinctive features] — FIRST 10 TOKENS CRITICAL
[Pose / action / expression] — direct gaze, three-quarter turn, candid laughter, etc.
[Camera system]: Shot on [Canon EOS R5 / Hasselblad X2D / etc.], [lens] at f/[aperture]
[Lighting]: [Key light source + direction + quality], [fill description], [color temperature]K
[Skin detail]: [Specific skin texture descriptors from hierarchy above]
[Eye detail]: [Catchlights, iris detail, moisture descriptors]
[Hair detail]: [Texture, color, style, individual strand mention]
[Background]: [Bokeh character, distance, color tone] — keep minimal to avoid subject dilution
[Atmosphere]: [Grain, film stock if analog, subtle lens effects]
```

**Guardrails (Positive-Only Anatomical Safety):**
```
natural human anatomy, correct finger count, balanced facial proportions,
realistic skin pore texture, organic epidermal surface, visible fine hair on skin,
authentic eye moisture, natural iris pigmentation, aligned ocular gaze,
realistic hair follicle density, individual strand separation,
no artificial smoothing, no plastic appearance, no digital retouching artifacts
```

**Age-Specific Prompting Modifiers:**

| Age Group | Skin Descriptors | Eye Descriptors | Lighting Approach |
|-----------|-----------------|-----------------|-------------------|
| Infant (0–2) | Soft unblemished skin, fine peach fuzz, rosy cheeks | Large irises, pure sclera, wonder gaze | Soft diffused, no hard shadows |
| Child (3–12) | Freckles, slight sun flush, smooth but not plastic | Bright alert eyes, playful expression | Natural daylight, playful catchlights |
| Teen (13–19) | Occasional blemish, oily T-zone, natural texture | Intense gaze, emotional volatility visible | Dramatic side light, moody |
| Young Adult (20–35) | Optimal collagen, subtle texture, healthy glow | Confident direct gaze, sharp focus | Versatile — any professional setup |
| Middle Age (36–55) | Expression lines, crow's feet, laugh lines, slight jowls | Warmth, wisdom, slight hooding | Soft key + moderate fill |
| Senior (56–75) | Weathered texture, age spots, pronounced wrinkles | Deep set, wisdom, slight cataract glow | Rembrandt or butterfly lighting |
| Elder (76+) | Paper-thin skin, prominent veins, deep creases | Gentle gaze, possibly cloudy, kind | Very soft, diffused, respectful |

---

### ADVANCED TECHNIQUES

**1. The Pore-Reveal Close-Up**
- Setup: Extreme close-up, face filling 80% of frame
- Camera: Hasselblad X2D, 120mm macro, f/4
- Light: Single large softbox at 45°, very close for wrap-around softness
- Skin: Explicit "visible pore structure on nose and cheeks, subtle sebaceous shine, individual vellus hairs on upper lip"
- Eyes: "Iris fiber detail visible, moisture reflection in lower lid, sharp limbal ring"
- Emotional: Raw vulnerability, unfiltered humanity
- Best For: Skincare campaigns, authenticity messaging, documentary portraiture

**2. The Environmental Character Portrait**
- Setup: Subject in their natural environment (workshop, kitchen, studio)
- Camera: Leica M11, 35mm f/1.4, f/2.0 — environmental context visible
- Light: Window light + practical sources, mixed color temperature
- Skin: Weathered hands, sun-exposed face, authentic occupational texture
- Background: Contextual but soft — tells story without competing
- Emotional: Dignity of labor, lived experience, grounded authenticity
- Best For: Documentary, brand storytelling, artisan profiles

**3. The Cinematic Eye Light**
- Setup: Medium close-up, eyes as primary focal point
- Camera: Sony A7R V, 85mm f/1.4, f/1.8 — razor-thin DoF on near eye
- Light: Large source slightly above eye line creating "sparkle" or "catchlight"
- Eye Detail: "Distinct rectangular catchlight from large soft source, iris color gradation from pupil to edge, visible radial muscle fibers"
- Background: Deep cinematic bokeh, color-complementary to iris
- Emotional: Intimacy, connection, soul-revealing
- Best For: Film posters, dramatic intros, emotional campaigns

**4. The Multi-Light Studio Headshot**
- Setup: Classic three-point but described behaviorally
- Camera: Canon EOS R5, 85mm f/1.2L, f/5.6 — sufficient DoF for corporate sharpness
- Light: "Key light from camera-left 30° creating gentle shadow on right cheek, fill from reflector below chin eliminating harshness, hair light from behind separating subject from dark background"
- Skin: "Clean but natural, subtle texture visible, no artificial smoothing"
- Background: "Neutral gray seamless, even illumination, no texture competition"
- Emotional: Professional, approachable, trustworthy
- Best For: Corporate headshots, LinkedIn, team pages, executive portraits

**5. The Golden Hour Backlit Portrait**
- Setup: Subject backlit by setting sun, face in shadow but not underexposed
- Camera: Fujifilm GFX 100S, 110mm f/2, f/2.8
- Light: "Warm golden sunset light behind subject creating translucent hair glow, face illuminated by bounced warm fill from sand/reflector/building, rim light outlining shoulder and hair"
- Skin: "Warm golden undertone, sun-kissed cheeks, natural freckles visible"
- Hair: "Individual strands catching backlight, translucent edges glowing amber"
- Emotional: Nostalgia, warmth, fleeting beauty, summer romance
- Best For: Lifestyle brands, travel, wellness, romantic narratives

**6. The Neon Night Portrait**
- Setup: Urban night, colored practical light sources
- Camera: Sony A7S III, 50mm f/1.2, f/1.4 — low light capability implied
- Light: "Magenta neon sign reflecting off wet cheek, cool blue streetlight from above creating split color on face, warm tungsten practical from shop window as fill"
- Skin: "Natural skin tone under colored light, realistic color bounce on jaw, not artificially tinted"
- Eyes: "Colored light reflected in cornea, pupil slightly dilated from low light"
- Emotional: Urban isolation, nocturnal energy, cyber-romantic
- Best For: Streetwear, music, nightlife, contemporary fiction

**7. The Generational Portrait Series**
- Setup: Same lighting/camera for 3+ generations to show genetic continuity
- Camera: Consistent across all — e.g., Hasselblad X2D, 80mm f/2.8, f/4
- Light: "Consistent large soft source, identical camera height and distance"
- Skin: Age-appropriate descriptors that show passage of time on same genetic material
- Composition: "Same framing, same background tone, subject positioned identically"
- Emotional: Legacy, time, family, genetic poetry
- Best For: Heritage brands, insurance, family services, generational wealth

---

### EXAMPLE PROMPTS

**Studio Skincare Close-Up:**
> Close-up portrait of a 28-year-old Korean woman with natural makeup, face filling 80% of frame, shot on Hasselblad X2D with 120mm macro lens at f/4, single large softbox from camera-left creating gentle wrap-around light, visible pore structure on cheeks and nose, subtle sebaceous sheen on forehead, fine vellus hairs on jawline catching light, iris fiber detail in dark brown eyes with rectangular catchlight from softbox, individual eyebrow hairs visible at arch, neutral gray seamless background, clean editorial beauty photography, ultra-sharp focus on near eye, organic skin texture, no artificial smoothing

**Environmental Artisan Portrait:**
> Environmental portrait of a 65-year-old Black male carpenter in his workshop, weathered hands resting on workbench, shot on Leica M11 with 35mm Summilux at f/2, warm window light from left creating Rembrandt pattern on face, sawdust particles visible in light beam, wood shavings on forearms, deep wrinkles around eyes from decades of squinting, warm brown eyes with gentle wisdom, short gray beard with individual coarse hairs, weathered skin with sun damage and character lines, woodworking tools soft in background bokeh, documentary photography style, dignified labor, authentic lived-in texture

**Cinematic Neon Night:**
> Night street portrait of a 22-year-old woman with short dyed blue hair, shot on Sony A7S III with 50mm f/1.2 at f/1.4, magenta neon sign from left reflecting off cheekbone, cool blue LED streetlight from above, warm tungsten spill from coffee shop window as fill, pupil slightly dilated from low light, colored reflections visible in cornea, natural skin tone preserved under mixed light, subtle lip piercing catching blue light, shallow depth of field with hexagonal bokeh from city lights, urban nocturnal atmosphere, contemporary street photography, authentic texture, no digital smoothing

---

### TECHNICAL NOTES FOR AI GENERATION
- **Lead with identity:** "28-year-old Korean woman" not "Portrait of a woman, 28, Korean" — the first 5 words carry maximum weight.
- **Never use "white background"** in FLUX.2 Dev prompts — causes fuzziness and quality degradation. Use "neutral gray seamless," "clean studio environment," or "minimal backdrop."
- **Camera system first in technical section:** "Shot on [specific camera]" triggers photorealistic rendering pipeline more reliably than "photorealistic" alone.
- **Describe light behavior, not light name:** "Warm golden light streaming through window, casting long shadows across floor" outperforms "golden hour lighting."
- **Skin texture must be explicit:** FLUX.2 defaults to moderate smoothing. "Visible pores," "fine hair," "subtle imperfections" are required triggers for organic skin.
- **Eye detail is the authenticity threshold:** If eyes look wrong, the entire portrait fails. Always specify catchlights, iris detail, and moisture.
- **Hair without strand mention = helmet hair:** "Individual hair strands," "natural parting," "flyaway hairs" prevent the plastic helmet effect.
- **Guidance 3.5–4.5 only:** Above 5 = over-saturated, plastic skin. Below 3 = subject drift and soft anatomy.
- **Steps 28–35 optimal:** Below 25 = soft detail. Above 40 = diminishing returns with increased smoothing artifacts.
- **JSON structured prompts for batch consistency:** Use the `flux2_json_schema` skill for multi-subject campaigns requiring identical lighting/camera across portraits.
