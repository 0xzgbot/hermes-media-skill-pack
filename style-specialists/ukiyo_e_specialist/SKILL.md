# SKILL: Ukiyo-e Specialist
## Domain: Japanese Woodblock Print, Flat Color, Bold Outlines, Edo-Period Aesthetics
## Version: 1.0
## For: Hermes Agent — Prompt Engineering & Scene Planning

---

## 1. EXECUTIVE SUMMARY

This skill encodes the complete visual vocabulary of ukiyo-e — the Japanese woodblock print tradition of the Edo period (1603–1868). It covers the flat unshaded color application, bold black outlines, Prussian blue dominance, asymmetrical compositions, visible paper grain and ink bleed, and the specific subject categories (landscapes, bijin-ga, kachō-ga, musha-e) that define the genre.

When this skill is active, the agent should:
- Use ukiyo-e-specific terms (bokashi gradient, key block outline, nishiki-e full color)
- Apply flat color discipline with no shading or modeling
- Reference the Prussian blue (bero-ai) dominance and limited natural palette
- Build scenes using asymmetrical composition and aerial perspective
- Understand the emotional register: poetic, contemplative, fleeting beauty (mono no aware)

---

## 2. THE UKIYO-E AESTHETIC

Ukiyo-e means "pictures of the floating world" — capturing the transient beauty of everyday life, nature, and entertainment. [^85^] [^95^]

### Core Principles

| Principle | Description | Prompt Vocabulary |
|-----------|-------------|-----------------|
| **Flat Color** | No shading, no modeling, no chiaroscuro — pure color planes | "flat color application", "unshaded color plane", "no modeling", "pure color field" |
| **Bold Outline** | Thick black lines define all forms, like calligraphy brush strokes | "bold black outline", "calligraphic line", "key block line", "strong contour" |
| **Limited Palette** | Natural pigments: indigo, vermilion, yellow, green, brown, black | "limited natural palette", "indigo dominant", "vermilion accent", "earth pigment" |
| **Asymmetry** | Deliberately unbalanced compositions, like nature | "asymmetrical composition", "deliberate imbalance", "organic placement" |
| **Aerial Perspective** | View from above, looking down at landscape or scene | "aerial perspective", "high viewpoint", "looking down at scene" |
| **Mono no Aware** | Pathos of things — bittersweet awareness of impermanence | "mono no aware", "fleeting beauty", "transient moment", "poignant impermanence" |
| **Visible Craft** | Paper grain, ink bleed, wood grain texture are part of the beauty | "visible paper grain", "ink bleed texture", "woodblock grain", "hand-printed texture" |

---

## 3. COLOR & MATERIALS

### The Ukiyo-e Palette

| Color | Pigment | Source | Emotional Use | Hex Approximation |
|-------|---------|--------|---------------|-------------------|
| **Prussian Blue** | Bero-ai | Imported synthetic, 1820s+ | Depth, water, sky, night, modernity | #1E3F5A |
| **Indigo** | Ai | Natural plant dye | Traditional blue, depth, dusk | #4B0082 |
| **Vermilion** | Shu | Cinnabar mineral | Passion, energy, sun, festival | #E34234 |
| **Yellow Ochre** | Ki | Natural earth | Sunlight, warmth, sand, autumn | #CC7722 |
| **Malachite Green** | Rokushō | Mineral pigment | Nature, spring, vitality | #0BDA51 |
| **Brown / Sepia** | Kasshoku | Natural earth, tea | Earth, wood, autumn, grounding | #704214 |
| **Black** | Sumi | Pine soot ink | Outline, shadow, depth, structure | #0A0A0A |
| **White** | Gofun | Shell powder | Snow, wave foam, skin highlight, paper | #FFFFF0 |

### Bokashi Gradient
A unique ukiyo-e technique where color gradually fades within a single flat plane — not shading, but atmospheric transition: [^85^]
- **Sky bokashi:** Blue at top fading to white at horizon
- **Water bokashi:** Dark at foreground fading to light at distance
- **Ground bokashi:** Earth tone fading to white at edge

**Prompt Translation:**
> "bokashi gradient sky, Prussian blue fading to white at horizon, flat color with atmospheric fade, not shaded but graduated"

---

## 4. COMPOSITION & TECHNIQUE

### Key Stylistic Traits [^95^]

| Trait | Description | Prompt Terms |
|-------|-------------|------------|
| **Flat Unshaded Color** | No volume modeling; color defines shape only | "flat unshaded color", "no volume modeling", "color defines shape" |
| **Bold Clear Outlines** | Thick black lines like calligraphy brush strokes | "bold clear outline", "calligraphic brush line", "thick black contour" |
| **Asymmetrical Composition** | Deliberately unbalanced, like nature | "asymmetrical composition", "deliberate imbalance", "organic arrangement" |
| **Aerial Perspective** | View from above the action | "aerial perspective", "high viewpoint", "looking down" |
| **Extended Beyond Frame** | Composition continues past picture edge | "composition beyond frame", "extended past edge", "overflowing picture plane" |
| **Foreground/Middle/Background** | Three distinct depth planes | "three-plane depth", "foreground middle background", "layered landscape" |
| **Cartouches / Text Blocks** | Banners with artist name, title, series | "cartouche text block", "Japanese text banner", "artist signature block" |

### Subject Categories

| Category | Subject | Famous Examples | Prompt Terms |
|----------|---------|----------------|--------------|
| **Meisho-e** | Famous places, landscapes | Hokusai's *36 Views of Mount Fuji*, Hiroshige's *53 Stations of the Tōkaidō* | "famous place landscape", "travel scene", "mountain view" |
| **Bijin-ga** | Beautiful women, courtesans, geisha | Utamaro's portraits | "beautiful woman portrait", "courtesan figure", "elegant feminine" |
| **Kachō-ga** | Birds and flowers | Hokusai's *Birds and Flowers* | "bird and flower print", "nature study", "botanical illustration" |
| **Musha-e** | Warriors, samurai, historical battles | Kuniyoshi's warrior prints | "warrior print", "samurai figure", "historical battle" |
| **Shunga** | Erotic scenes | Hokusai's *The Dream of the Fisherman's Wife* | (use with discretion) |
| **Yakusha-e** | Kabuki actors | Sharaku's portraits | "kabuki actor portrait", "theatrical figure", "dramatic pose" |

---

## 5. THE HOKUSAI / HIROSHIGE LANDSCAPE FORMULA

| Element | Description | Prompt Terms |
|---------|-------------|------------|
| **Mount Fuji** | Sacred mountain, often small in distance, white peak | "Mount Fuji in distance", "sacred white peak", "small mountain in vast scene" |
| **Great Wave** | Dynamic water, claw-like fingers, white foam | "great wave", "claw-like water", "dynamic sea", "white foam crest" |
| **The Red Sun** | Large, flat, red disc — often low on horizon | "red sun disc", "large flat sun", "low red horizon" |
| **Rain** | Vertical lines, grey-blue palette, atmospheric | "vertical rain lines", "grey-blue rain palette", "atmospheric rain" |
| **Bridge** | Wooden structure, human figures crossing, connection | "wooden bridge", "figures crossing", "architectural connection" |
| **Boats** | Small human figures, scale reference, livelihood | "small boats", "human scale reference", "fishing vessels" |
| **Trees** | Stylized, rhythmic brush strokes, seasonal | "stylized trees", "rhythmic brush strokes", "seasonal foliage" |

---

## 6. PROMPT ENGINEERING

### Layer 1: Technique
```
traditional Japanese ukiyo-e woodblock print style, flat unshaded color,
bold black outline, calligraphic brush line, visible paper grain,
ink bleed texture, woodblock print texture, hand-printed quality,
bokashi gradient fade, not shaded but graduated
```

### Layer 2: Color
```
limited natural palette, Prussian blue dominant, indigo depth,
vermilion accent, yellow ochre warmth, malachite green nature,
brown earth tone, black sumi outline, white gofun highlight,
natural pigment color
```

### Layer 3: Composition
```
asymmetrical composition, aerial perspective, high viewpoint,
three-plane depth foreground middle background,
composition extending beyond frame, cartouche text block,
Japanese text banner, deliberate organic imbalance
```

### Layer 4: Subject
```
Mount Fuji in distance, great wave claw-like water, red sun disc,
wooden bridge with figures, small boats on water, stylized trees,
beautiful woman in kimono, bird and flower nature study,
samurai warrior figure, kabuki actor portrait
```

### Complete Prompt Template
```
A [subject] in traditional Japanese ukiyo-e woodblock print style,
[technique description], [color description], [composition description],
[specific Hokusai/Hiroshige elements], [emotional register].

Example:
"Mount Fuji at dawn in traditional Japanese ukiyo-e woodblock print style,
flat unshaded color application with bold black calligraphic outlines,
Prussian blue dominant sky with bokashi gradient fading to white horizon,
vermilion red sun disc low on horizon, snow-capped peak glowing pink,
three-plane depth with foreground pine trees, middle ground lake,
background mountain range, asymmetrical composition extending beyond frame,
visible paper grain and ink bleed texture, hand-printed woodblock quality,
limited natural pigment palette, serene poetic atmosphere,
mono no aware fleeting beauty, Hokusai Red Fuji aesthetic"
```

---

## 7. NEGATIVE PROMPTS

| Avoid | Why | Replace With |
|-------|-----|--------------|
| "shading / modeling" | Ukiyo-e uses flat color only | "flat color", "unshaded", "no volume modeling" |
| "photorealistic" | Ukiyo-e is stylized, hand-printed | "woodblock print", "hand-printed", "stylized" |
| "perspective depth" | Ukiyo-e uses flat planes and aerial view | "flat plane", "aerial perspective", "layered depth" |
| "symmetrical balance" | Ukiyo-e is deliberately asymmetrical | "asymmetrical composition", "organic imbalance" |
| "smooth digital texture" | Ukiyo-e has visible grain and bleed | "paper grain", "ink bleed", "woodblock texture" |
| "Western color palette" | Ukiyo-e uses specific natural pigments | "natural pigment", "Prussian blue", "vermilion" |

---

## 8. SKILL STACKING

```
BASE SKILL: Prompt Engineering Core
STYLE SKILL: Ukiyo-e Specialist (this file)
    └── VOCABULARY: ukiyo-e, bokashi, Prussian blue, bold outline, asymmetry
STYLE SKILL: [Any Style Specialist]
    └── VOCABULARY: domain-specific aesthetic
STRUCTURE SKILL: Cinematic Continuity
    └── GRAMMAR: shot lists, anchor frames
TECH SKILL: ComfyUI/Flux Pipeline
    └── PARAMETERS: sampler, model, CFG
```

**Ukiyo-e + Cyberpunk Stack (Unexpected):**
> "Cyberpunk cityscape rendered as ukiyo-e woodblock print — flat unshaded neon colors with bold black outlines, Prussian blue night sky with magenta and cyan as vermilion/green accents, bokashi gradient in toxic fog, asymmetrical composition with aerial perspective, visible paper grain"

---

## 9. QUICK REFERENCE: UKIYO-E DESCRIPTOR MATRIX

| Subject | Primary Color | Secondary | Accent | Composition | Texture | Mood |
|---------|--------------|-----------|--------|-------------|---------|------|
| Landscape (Hokusai) | Prussian blue | White | Vermilion | Asymmetrical, aerial | Paper grain | Majestic, poetic |
| Portrait (Utamaro) | Soft pink | Black | Vermilion | Centered, intimate | Ink bleed | Elegant, serene |
| Nature (Kachō-ga) | Malachite green | White | Yellow ochre | Asymmetrical, close | Wood grain | Delicate, contemplative |
| Rain (Hiroshige) | Grey-blue | White | Black | Vertical lines, aerial | Rain streak | Melancholic, atmospheric |
| Warrior (Kuniyoshi) | Vermilion | Black | Gold | Dynamic, diagonal | Bold line | Dramatic, heroic |

---

## 10. SOURCES

- Dreamina / CapCut, "How to Create Ukiyo-e Style Art" [^85^]
- Birmingham Museum of Art, "Quick Guide to Japanese Woodblock Prints" [^95^]

---

## 11. VERSION HISTORY

- **v1.0** (2026-04-24): Initial comprehensive skill covering flat color technique, bold outlines, Prussian blue palette, bokashi gradient, asymmetrical composition, subject categories, and Hokusai/Hiroshige landscape formula.
