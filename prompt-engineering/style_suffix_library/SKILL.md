# SKILL: Style Suffix Library
## Version: 1.0 | Hermes Agent SD Prompt Craft (Technical)

---

### DESCRIPTION
Curated style suffix clusters that reliably trigger specific aesthetic modes across model families. Style suffixes function as distribution shifters — they push the generation toward specific visual territories. These are organized by aesthetic family with model-specific efficacy notes.

### TRIGGER KEYWORDS
style suffix, style tokens, aesthetic mode, style cluster, visual style, film still, illustration style, cinematic suffix, photorealistic suffix, anime style, oil painting, watercolor, style vocabulary, style descriptor

### CORE RULES
- Style suffixes go at end of prompt after subject/action/environment/lighting
- Cinematic cluster: "cinematic, film still, movie quality, bokeh, depth of field, 35mm"
- Photorealistic cluster: "photorealistic, DSLR photograph, natural light, sharp focus"
- Painting cluster: "oil painting, classical, fine art, brushwork visible, gallery quality"
- Anime/illustration cluster: "anime style, cel-shaded, 2D illustration, clean line art"
- Flux responds to descriptive suffixes; SDXL to established training terms
- Don't mix incompatible clusters: "photorealistic anime" confuses model — pick one

---

### PHOTOREALISTIC FAMILY

**Core Suffixes (All Models):**
```
photorealistic, realistic photograph, documentary photography, RAW photo, DSLR, shot on [camera] with [lens]
```

**Sub-Styles:**
- Portrait: `studio portrait, headshot, environmental portrait, candid portrait, street portrait`
- Landscape: `landscape photography, nature photography, National Geographic, aerial photography, drone photography`
- Fashion: `fashion editorial, runway photography, lookbook, street style photography`
- Product: `product photography, commercial photography, catalog shot, hero shot, still life`
- Documentary: `documentary photography, photojournalism, reportage, candid, decisive moment`
- Vintage Photo: `vintage photograph, 1970s Kodachrome, 1980s Polaroid, 1960s black and white, sepia toned`

**Model Notes:**
- SDXL: Add `photorealistic` early in prompt for strong effect
- Flux: Weave camera/lens specs into technical clause; "photorealistic" alone is sufficient [^57^]
- LTX: Use `documentary cinematography` or `cinematic realism` for video

---

### CINEMATIC FAMILY

**Core Suffixes:**
```
cinematic, film still, movie screenshot, anamorphic, 35mm film, 16mm film, IMAX, cinematic color grading, film grain
```

**Sub-Styles:**
- Noir: `film noir, neo-noir, chiaroscuro lighting, black and white noir, 1940s noir`
- Sci-Fi: `cinematic sci-fi, cyberpunk film, space opera, dystopian film, retro-futurist film`
- Horror: `cinematic horror, giallo, psychological thriller, body horror, folk horror`
- Western: `spaghetti western, revisionist western, classic western, modern western`
- Drama: `cinematic drama, period drama, character study, indie film, arthouse`
- Action: `cinematic action, blockbuster, stunt sequence, vehicular action, martial arts film`
- Comedy: `cinematic comedy, screwball, dark comedy, rom-com, satire`

**Technical Spec Suffixes:**
```
shot on ARRI Alexa, shot on RED Komodo, shot on Sony Venice, anamorphic lens, Cooke S4 lens, Panavision lens, 2.39:1 aspect ratio, cinematic widescreen, film grain, Kodak Vision3, Fujifilm Eterna
```

**Model Notes:**
- All models respond strongly to specific camera/lens names
- Flux: "anamorphic lens" triggers oval bokeh and horizontal flare [^57^]
- SDXL: "film grain" + "Kodak Vision3" produces authentic photochemical texture

---

### EDITORIAL / COMMERCIAL FAMILY

**Core Suffixes:**
```
editorial photography, magazine editorial, advertising photography, commercial campaign, brand film still
```

**Sub-Styles:**
- Fashion Editorial: `Vogue editorial, Harper's Bazaar, high fashion, couture editorial, backstage`
- Beauty Editorial: `Allure beauty, skincare campaign, cosmetics editorial, beauty close-up, glow editorial`
- Lifestyle Editorial: `Architectural Digest, travel editorial, food editorial, home editorial`
- Automotive Editorial: `car commercial still, Top Gear, automotive campaign, racing editorial`
- Tech Editorial: `tech review aesthetic, unboxing photography, gadget editorial, product launch`

**Model Notes:**
- SDXL: Strong response to magazine names as style anchors
- Flux: "editorial" + specific publication name yields consistent styling
- LTX: "brand film" + "commercial" triggers polished movement and lighting

---

### CONCEPT ART / ILLUSTRATION FAMILY

**Core Suffixes:**
```
concept art, digital painting, illustration, matte painting, key art, promotional art
```

**Sub-Styles:**
- Fantasy: `epic fantasy art, high fantasy, dark fantasy, sword and sorcery, mythological art`
- Sci-Fi: `science fiction concept art, space art, mecha design, vehicle concept, environment concept`
- Character: `character design, character sheet, turnaround, expression sheet, costume design`
- Environment: `environment concept art, landscape concept, world building, vista, megastructure`
- Stylized: `stylized illustration, graphic novel art, comic book art, cartoon style, animated film style`
- Painterly: `oil painting, watercolor, gouache, acrylic, impasto, alla prima`

**Artist-Style Suffixes (Safe References):**
```
in the style of Greg Rutkowski, in the style of Alphonse Mucha, in the style of Craig Mullins, in the style of Sparth, in the style of James Gurney, in the style of Jean-Baptiste Monge
```

**Model Notes:**
- SDXL: Artist names work reliably; combine 2–3 for hybrid styles
- Flux: Artist references work but are less dominant; style descriptors matter more [^70^]
- Pony: Use `source_anime` or `source_cartoon` for domain specification [^69^]

---

### ANIME / MANGA FAMILY

**Core Suffixes:**
```
anime style, manga illustration, cel shaded, 2d animation, key visual, promotional art
```

**Sub-Styles:**
- Modern Anime: `modern anime, contemporary anime, 2020s anime, seasonal anime`
- Retro Anime: `1980s anime, 1990s anime, retro cel animation, VHS aesthetic, CRT scanlines`
- Studio Styles: `Studio Ghibli style, Kyoto Animation style, Ufotable style, MAPPA style, Madhouse style`
- Genre: `shonen anime, shojo anime, seinen anime, mecha anime, isekai anime, slice of life`
- Technical: `cel shaded, limited animation, 12fps animation, broadcast anime, OVA quality`

**Model Notes:**
- Pony Diffusion: Use `source_anime` tag [^69^]
- SDXL: NAI (NovelAI) finetunes respond strongly to anime tokens
- Flux: Anime style requires explicit reinforcement; add `2d illustration` to prevent 3D render drift

---

### ARCHITECTURAL / DESIGN FAMILY

**Core Suffixes:**
```
architectural photography, architectural visualization, interior design photography, real estate photography, 3d architectural render
```

**Sub-Styles:**
- Modern: `modernist architecture, brutalist architecture, minimalist interior, contemporary design`
- Historic: `classical architecture, Gothic cathedral, Art Deco, Bauhaus, Victorian interior`
- Futuristic: `futuristic architecture, parametric design, biomorphic architecture, smart city`
- Organic: `organic architecture, biophilic design, earth architecture, sustainable design`

---

### FINE ART / MUSEUM FAMILY

**Core Suffixes:**
```
fine art photography, museum quality, gallery print, archival pigment print, platinum print, large format photography
```

**Sub-Styles:**
- Classical: `Dutch Golden Age painting, Baroque, Rococo, Neoclassical, Romanticism`
- Modern: `Impressionism, Post-Impressionism, Expressionism, Cubism, Surrealism`
- Contemporary: `contemporary art, conceptual art, installation photography, performance documentation`
- Photography: `large format photography, medium format photography, contact print, cyanotype, daguerreotype`

---

### STYLE COMBINATION MATRIX

| Base Style | + Modifier 1 | + Modifier 2 | Result |
|------------|---------------|--------------|--------|
| photorealistic | cinematic | film grain | Movie still aesthetic |
| photorealistic | editorial | Vogue | High fashion photography |
| concept art | epic fantasy | Greg Rutkowski | AAA game key art |
| anime | Studio Ghibli | watercolor | Soft Ghibli illustration |
| cinematic | noir | chiaroscuro | Classic film noir |
| editorial | automotive | Top Gear | Car commercial still |
| architectural | brutalist | golden hour | Dramatic concrete photography |
| fine art | Impressionism | oil on canvas | Painterly museum piece |

---

### EXAMPLE PROMPTS BY STYLE

**Photorealistic + Cinematic:**
> `Cinematic film still of lone astronaut standing on Mars ridge, Earth visible as small blue dot in black sky, dust devils in distance, shot on 65mm IMAX with anamorphic lens, film grain, Kodak Vision3, 2.39:1 widescreen, dramatic side-lighting, photorealistic, cinematic color grading`

**Editorial + Beauty:**
> `Vogue beauty editorial close-up, model with dewy glass skin and natural freckles, soft pink and gold palette, shot on Hasselblad with 120mm macro, beauty campaign lighting, editorial photography, unretouched skin texture, high fashion aesthetic`

**Concept Art + Fantasy:**
> `Epic fantasy concept art of sky-city suspended by massive chains above storm clouds, bioluminescent architecture, dragons circling towers, digital painting by Greg Rutkowski and Sparth, highly detailed, vibrant colors, key art composition, matte painting quality`

**Anime + Retro:**
> `1980s anime style, mecha pilot in cockpit, CRT scanlines, cel shaded, VHS aesthetic, retro futurism, broadcast anime quality, dramatic lighting, limited animation style, 4:3 aspect ratio`

---

### TECHNICAL NOTES FOR AI GENERATION
- Combine 2–3 style suffixes maximum; beyond that causes style mush
- Artist names work best when paired with medium descriptors ("oil painting by...", "photography by...")
- Flux: Style is better controlled through detailed scene description than suffix stacking [^57^]
- SDXL: Style suffixes at the end of prompt still carry significant weight
- LTX: "Cinematic" + specific camera movement yields most reliable video style [^68^]
- Test style combinations in small batches; log which combinations produce keeper rates
