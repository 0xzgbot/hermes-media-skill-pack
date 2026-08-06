# SKILL: FLUX.2 Dev Architectural & Environment Rendering
## Version: 1.0 | Hermes Agent Flux2 Architecture & Real Estate Specialist

---

### DESCRIPTION
Deeply researched prompting doctrine for generating photorealistic architectural visualization, interior design imagery, and environmental landscapes with FLUX.2 Dev. This skill encodes the precise perspective control vocabulary, material specification language, natural light integration strategies, and scale-accurate spatial description required for architecture portfolios, real estate marketing, and environment concept art. Covers verticals (buildings), horizontals (landscapes), and interiors (spaces) with FLUX.2 Dev's specific positive-only constraint architecture.

---

### TECHNICAL PARAMETERS

**FLUX.2 Dev Architectural Architecture:**
- **Model:** FLUX.2 Dev (32B, guidance-distilled)
- **Token Priority:** Building type + style must lead. "Modernist concrete villa cantilevered over cliff" not "A beautiful house on a hill."
- **Prompt Length:** 60–120 words for complex architecture. Interiors 50–80. Landscapes 40–70.
- **Guidance Scale:** 4.0–5.0 for architecture (high adherence needed for geometric accuracy)
- **Steps:** 32–40 for material detail and perspective precision.
- **Resolution:** 1280×1024 or 1536×1024 for exteriors; 1024×1280 for vertical interiors.
- **JSON Advantage:** Architecture benefits enormously from JSON structured prompts for multi-element scenes.

**Perspective & Viewpoint Control:**

| View Type | Description | Lens Choice | Emotional Effect |
|-----------|------------|-------------|-----------------|
| **Worm's Eye** | Camera below subject, looking up | 16–24mm ultra-wide | Monumentality, power, awe, oppression |
| **Eye Level** | Camera at average human height | 35–50mm natural | Honest, approachable, documentary |
| **High Angle** | Camera above subject, looking down | 24–35mm wide | Overview, control, diminishment |
| **Aerial / Drone** | Extreme elevation, bird's perspective | 24mm or implied drone | Context, scale, planning, god's eye |
| **Two-Point Perspective** | Corner view of building, both sides receding | 35–50mm | Dynamic, architectural drawing feel |
| **One-Point Perspective** | Straight-on view, single vanishing point | 50–85mm | Formal, symmetrical, imposing |
| **Interior Wide** | Inside space, showing volume and layout | 16–24mm ultra-wide | Spaciousness, grandeur, context |
| **Detail Close-Up** | Material or construction detail | 90–150mm macro | Craft, texture, material honesty |

**Architectural Material Rendering Triggers:**

| Material | Primary Trigger | Secondary Triggers | Light Response |
|----------|----------------|-------------------|----------------|
| **Raw Concrete** | Board-formed concrete texture, pour lines visible | Aggregate exposure, void pockets, formwork pattern | Raking light shows texture; soft light flattens |
| **Glass Curtain Wall** | Reflective glazing, curtain wall system, mullion grid | Sky reflection, transparency to interior, specular bounce | Mirror-like sky reflection; shows time of day |
| **Weathered Steel (Corten)** | Rust patina, oxidized surface, weathered steel | Color variation from orange to brown, streaking | Warm under overcast; glows at sunset |
| **Natural Stone** | Veining pattern, crystalline structure, honed finish | Fossil inclusions, bookmatched slabs, thermal finish | Raking light shows three-dimensional texture |
| **Timber / CLT** | Cross-laminated timber grain, wood grain direction | Knot pattern, end-grain exposure, charred surface | Warm light amplifies color; shows growth rings |
| **White Plaster / Stucco** | Trowel texture, lime plaster, imperfect smoothness | Hairline cracks, patina, hand-finished variation | Even light shows subtle surface variation |
| **Brick** | Bond pattern visible, mortar joints, firing variation | Weathering, efflorescence, repointing texture | Raking light emphasizes relief and pattern |
| **Terracotta Tile** | Hand-formed irregularity, glaze variation, stacking pattern | Weathering, moss growth in joints, color shift | Warm light brings out earth tones |

**Natural Light Integration for Architecture:**
- **Morning light (east-facing):** Crisp shadows, cool fill from west, fresh atmosphere
- **Midday light (overhead):** Minimal shadow, even illumination, least dramatic
- **Golden hour (west-facing):** Long shadows, warm surfaces, glowing materials
- **Overcast (diffuse):** Even, no harsh shadows, material color most accurate, no glare
- **Blue hour (twilight):** Interior lights become visible, sky gradients, artificial warmth
- **Night:** Interior glow visible through glass, exterior lighting design prominent, material disappears

---

### PROMPT ARCHITECTURE

**Core Exterior Architecture Template (FLUX.2 Dev):**
```
[Building type + style]: [Modernist villa / Brutalist museum / Traditional Japanese temple / etc.]
[Materials]: [Primary material], [secondary material], [texture detail]
[Setting]: [Urban / rural / coastal / mountain / desert], [vegetation], [context buildings]
[Viewpoint]: [Worm's eye / eye level / aerial / two-point perspective]
[Camera]: Shot on [technical camera / DSLR], [lens]mm, f/[aperture]
[Light]: [Time of day], [direction], [quality], [color temperature]K
[Atmosphere]: [Weather, haze, season, time of year]
[Style]: [Architectural photography / photorealistic render / documentary]
[Composition]: [Subject placement, horizon line, foreground element]
```

**Core Interior Template:**
```
[Space type]: [Living room / gallery / restaurant / cathedral / office]
[Design style]: [Minimalist / Art Deco / Industrial / Scandinavian / etc.]
[Materials palette]: [Floor], [walls], [ceiling], [fixtures]
[Furniture/fixtures]: [Key pieces, brands if relevant, arrangement]
[Light]: [Natural source + direction], [artificial sources], [color temp mix]
[Camera]: Shot on [camera], [wide lens]mm, f/[aperture for deep focus]
[Atmosphere]: [Occupancy, life signs, time of day, mood]
```

**Guardrails (Positive-Only Architecture Safety):**
```
coherent perspective lines, consistent vanishing point, believable structural engineering,
accurate material scale, realistic shadow casting from architecture, natural light falloff,
plausible window reflection, consistent horizon line, proportional human scale reference,
no floating elements, no impossible cantilevers without engineering justification,
no texture stretching, no perspective distortion on verticals
```

---

### ADVANCED TECHNIQUES

**1. The Heroic Worm's Eye Monument**
- Setup: Camera at ground level looking up at imposing structure
- Building: "Brutalist concrete government building, massive scale, raw board-formed concrete with visible pour lines and aggregate, geometric repetition of rectangular windows"
- Viewpoint: "Extreme worm's eye perspective from plaza level, looking straight up facade, converging vertical lines emphasizing height"
- Light: "Harsh midday sun creating deep shadows in window reveals, strong contrast between illuminated concrete and black shadow"
- Camera: "Shot on technical camera with 24mm tilt-shift lens, f/11, perspective correction maintaining vertical lines"
- Atmosphere: "Clear blue sky as negative space framing building top, small human figure at base for scale"
- Emotional: State power, imposing authority, civic grandeur, human insignificance
- Best For: Government, institutional, civic architecture, monument documentation

**2. The Warm Interior Golden Hour**
- Setup: Residential interior bathed in late afternoon light
- Space: "Minimalist Japanese-inspired living room, white oak flooring, shoji screen partitions, low modern furniture"
- Light: "Golden hour sunlight streaming through floor-to-ceiling window from west, long shadows across oak floor, warm 3000K light filling space, cool 6500K fill from north window"
- Materials: "White oak with visible grain, hand-troweled white plaster walls, linen upholstery, bronze hardware"
- Camera: "Shot on Canon EOS R5 with 16–35mm at 20mm, f/5.6, deep focus throughout interior"
- Life: "Coffee cup on table, book open on sofa, subtle signs of occupancy without clutter"
- Emotional: Warmth, sanctuary, slow living, domestic poetry
- Best For: Residential real estate, interior design portfolios, lifestyle architecture

**3. The Blue Hour Urban Mixed-Use**
- Setup: Contemporary building at twilight, interior and exterior visible
- Building: "Mixed-use tower with retail podium, glass curtain wall above with randomized frit pattern, corten steel retail facade at street level"
- Time: "Blue hour twilight, 30 minutes after sunset, deep indigo sky, building interior lights warm and inviting"
- Light: "Cool 9000K sky light on exterior glass, warm 2700K tungsten visible through windows, sodium streetlights 2200K at sidewalk"
- Camera: "Shot on Sony A7R V with 24mm tilt-shift at f/8, two-point perspective from street corner"
- Atmosphere: "Light rain creating reflections on pavement, atmospheric haze softening distant towers, city energy"
- Emotional: Urban vitality, 24-hour life, transparency and invitation
- Best For: Commercial real estate, urban developments, mixed-use marketing

**4. The Overcast Material Study**
- Setup: Single material focus under even overcast light
- Building: "Rammed earth chapel, layers of earth in warm ochre and sienna tones, slight variation in compaction visible"
- Light: "Heavy overcast sky, even diffused light from all directions, no hard shadows, material color most accurate"
- Camera: "Shot on Phase One IQ4 with 80mm at f/8, detail view of rammed earth wall filling frame"
- Detail: "Individual earth layers 300mm thick, small stones visible in matrix, slight vertical formwork marks, hand-smoothed top edge"
- Background: "Soft gray sky, no distraction, material is the subject"
- Emotional: Earth, humility, craft, geological time
- Best For: Material libraries, sustainable architecture, craft documentation

**5. The Aerial Context Shot**
- Setup: Drone or elevated view showing building in landscape context
- Building: "Modernist villa with flat roof and infinity pool, white render, horizontal emphasis"
- Context: "Cliff edge overlooking Mediterranean Sea, terraced olive grove, winding approach road"
- Viewpoint: "Aerial perspective from 100m elevation, slight angle showing roofscape and landscape relationship"
- Light: "Late afternoon golden hour, long shadows from villa and trees, warm light on white walls, deep blue sea"
- Camera: "Shot on DJI drone equivalent perspective, 24mm wide angle, f/5.6"
- Scale: "Human figure on terrace providing scale, car on approach road, yacht in distant water"
- Emotional: Privilege, harmony with landscape, Mediterranean dream, architectural humility
- Best For: Luxury real estate, resort marketing, architectural competition boards

**6. The Historic Adaptive Reuse**
- Setup: Old industrial building converted to new use
- Building: "Former textile mill with exposed brick walls, cast iron columns, original timber truss ceiling, now contemporary art gallery"
- Contrast: "Historic industrial fabric — patinated brick, iron columns with paint layers — against pristine white gallery walls and modern lighting"
- Light: "North-facing clerestory windows providing even gallery light, LED track lighting on artwork, warm industrial pendant lights in circulation"
- Camera: "Shot on Canon EOS R5 with 16–35mm at 24mm, f/5.6, central aisle view showing depth and repetition"
- Life: "Visitors small in scale, contemporary art on walls, cafe in former loading bay"
- Emotional: Memory, continuity, respect for past, cultural regeneration
- Best For: Adaptive reuse projects, cultural buildings, heritage architecture

**7. The Desert Landscape Integration**
- Setup: Building designed for extreme climate, landscape as partner
- Building: "Desert research station, rammed earth walls same color as sand, solar shade canopy, minimal footprint"
- Landscape: "Sahara desert, dunes in rhythmic patterns, sparse vegetation, vast sky dominance"
- Light: "Harsh midday sun, minimal shadow, building almost disappearing into sand color, slight heat shimmer on horizon"
- Camera: "Shot on technical camera with 50mm at f/11, eye-level perspective, building small in vast landscape"
- Material: "Rammed earth matching dune color #C2B280, weathered timber shading structure, no reflective surfaces"
- Emotional: Humility, environmental integration, survival, scientific isolation
- Best For: Sustainable architecture, research stations, desert resorts, environmental design

---

### EXAMPLE PROMPTS

**Brutalist Worm's Eye:**
> Extreme worm's eye perspective of brutalist concrete government building from plaza level looking straight up facade, massive raw board-formed concrete with visible pour lines and exposed aggregate, geometric repetition of deep rectangular window reveals creating rhythm, harsh midday sun creating extreme contrast between illuminated concrete and black shadow in windows, shot on technical camera with 24mm tilt-shift lens at f/11 with perspective correction maintaining vertical lines, clear blue sky as negative space framing building crown, small human figure at base providing scale, state power and civic grandeur, imposing monumentality, architectural photography

**Japanese Interior Golden Hour:**
> Minimalist Japanese-inspired living room with white oak flooring and visible grain, hand-troweled white plaster walls, shoji screen partitions filtering light, golden hour sunlight streaming through floor-to-ceiling window from west creating long shadows across floor, warm 3000K light filling space with cool 6500K fill from north window, low modern furniture in natural linen upholstery, bronze hardware on sliding doors, coffee cup on low table, book open on sofa, shot on Canon EOS R5 with 20mm at f/5.6 deep focus throughout, sanctuary warmth domestic poetry, slow living interior architecture

**Blue Hour Mixed-Use Tower:**
> Contemporary mixed-use tower at blue hour twilight with glass curtain wall above and corten steel retail facade at street level, deep indigo sky 30 minutes after sunset, warm 2700K interior lights visible through windows creating amber glow, cool 9000K sky reflecting on glass facade, sodium streetlights 2200K illuminating sidewalk, shot on Sony A7R V with 24mm tilt-shift at f/8 from street corner two-point perspective, light rain creating reflections on pavement, atmospheric haze softening distant towers, urban vitality and 24-hour life, commercial architectural photography

---

### TECHNICAL NOTES FOR AI GENERATION
- **Building type first:** "Brutalist museum" or "Modernist villa" — architectural style must lead within first 5 tokens.
- **Perspective named explicitly:** "Worm's eye," "two-point perspective," "aerial drone view" — FLUX.2 responds to named perspective types.
- **Lens + aperture for DoF control:** Architecture generally needs deep focus (f/8–f/11). Mention explicitly: "deep focus throughout" or "f/11 for front-to-back sharpness."
- **Material described physically:** "Board-formed concrete with visible timber grain pattern" outperforms "concrete wall" — physical process descriptions trigger realistic texture.
- **Light direction from named source:** "South-facing window" or "clerestory north light" — FLUX.2 understands architectural daylighting terminology.
- **Scale references essential:** Architecture without human scale references often renders at ambiguous scale. Include "human figure," "car," or "furniture" for scale anchoring.
- **Guidance 4.0–5.0:** Architecture needs higher adherence than portraits for geometric accuracy. 4.5 is the sweet spot.
- **Tilt-shift language:** "Perspective correction maintaining vertical lines" prevents converging verticals distortion common in AI architecture.
- **Weather as mood:** Overcast = material accuracy. Golden hour = warmth and drama. Blue hour = urban vitality. Night = lighting design showcase.
- **Interior-exterior relationship:** "Interior visible through glass" or "warm glow from within" — describe the relationship for transparency realism.
- **For landscape architecture:** Include seasonal vegetation: "Autumn maple with red foliage" or "Spring cherry blossom" — temporal specificity grounds the scene.
- **JSON for complex scenes:** Multi-building developments or mixed-use projects benefit from structured JSON with subjects array for each building component.
