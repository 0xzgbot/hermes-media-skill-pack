# SKILL: Volumetric God Rays & Light Shafts
## Version: 1.0 | Hermes Agent Atmospheric Lighting

---

### DESCRIPTION
Mastery of volumetric god rays, crepuscular rays, and atmospheric light shafts for AI-generated cinematic imagery. This skill encodes the physics of light scattering through particulate matter — dust, mist, haze, water droplets, smoke — creating visible beams of light that transform ordinary illumination into divine, dramatic, or mysterious atmosphere. Essential for sacred spaces, forest interiors, underwater scenes, dusty interiors, and any moment requiring transcendent or dramatic light quality.

---

### TECHNICAL PARAMETERS

**The Physics of God Rays:**
God rays (crepuscular rays) become visible when light passes through a medium containing suspended particles:
- **Particle Type:** Dust, smoke, fog, mist, water droplets, pollen, ash
- **Particle Density:** Too sparse = invisible; too dense = whiteout; optimal = clearly defined beams
- **Light Source:** Must be directional and significantly brighter than ambient environment
- **Occlusion:** Beams need edges — objects casting shadows create the visible boundaries of rays
- **Scattering Type:** Mie scattering (particles similar to light wavelength) creates forward-scattered beams

**God Ray Taxonomy:**

| Type | Source | Medium | Environment | Emotional Effect |
|------|--------|--------|-------------|------------------|
| **Crepuscular Rays** | Sun behind clouds | Atmospheric moisture | Sky, landscape | Divine, awe, nature's grandeur |
| **Window Light Shafts** | Sun through window | Dust in air | Interiors, abandoned spaces | Sacred, forgotten, time passing |
| **Forest God Rays** | Sun through canopy | Mist + pollen | Woods, jungle | Mystery, enchantment, primordial |
| **Underwater Light Shafts** | Sun through surface | Water + plankton | Ocean, pools, caves | Otherworldly, weightless, alien |
| **Artificial God Rays** | Spotlight / projector | Haze / fog | Theaters, concerts, clubs | Theatrical, dramatic, performative |
| **Smoke Beam** | Single hard source | Smoke / incense | Religious, mystical, noir | Spiritual, secret, ritual |
| **Dust Mote Dance** | Any directional source | Heavy dust | Attics, ruins, old buildings | Memory, decay, time frozen |

**Quality Parameters:**
- **Beam Sharpness:** Hard source + low density = sharp defined beams; soft source + high density = diffuse glow
- **Beam Color:** Inherits source color temperature; can be filtered (amber church, cyan underwater)
- **Angle:** Low sun = long dramatic shafts; overhead sun = short vertical columns
- **Visibility:** Backlit beams visible to camera; front-lit beams illuminate subjects
- **Falloff:** Beams fade with distance from source due to scattering attenuation

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Volumetric god ray cinematography, [light source: sun / moon / spotlight / practical]
passing through [medium: dust / mist / fog / smoke / water],
creating visible light shafts and crepuscular rays,
[sharp defined beams / soft diffuse glow / dramatic columns],
[environment: forest / cathedral / underwater / abandoned interior],
particles visible dancing in light beam,
[color temperature: warm golden / cool cyan / neutral white],
atmospheric light scattering, volumetric atmosphere,
sacred dramatic lighting, transcendent luminous quality
```

**Negative Prompts:**
```
flat even lighting, no atmosphere, clean sterile air, studio lighting,
no visible light beams, haze without structure, overexposed whiteout,
no particle definition, clear air, ambient only without directional source
```

---

### ADVANCED TECHNIQUES

**1. The Cathedral Window**
- Source: Sun through stained glass or tall arched window
- Medium: Incense smoke or centuries of dust
- Beams: Long, colored, dramatic diagonal shafts
- Particles: Slow-moving, golden, catching light like floating gold
- Subject: Silhouette or half-lit figure in prayer or awe
- Emotional: Divine presence, sacred space, spiritual transcendence
- Best For: Religious content, meditation, heritage, spiritual brands

**2. The Forest Mystery**
- Source: Morning sun through dense canopy gaps
- Medium: Ground mist, pollen, evaporating dew
- Beams: Vertical columns breaking through horizontal leaf layer
- Color: Warm gold shifting to cool green in deeper forest
- Subject: Small figure dwarfed by towering trees and light
- Emotional: Enchantment, fairy tale, primordial wonder, isolation
- Best For: Nature brands, fantasy, wellness, environmental content

**3. The Abandoned Memory**
- Source: Single window in ruined building
- Medium: Heavy dust disturbed by air movement
- Beams: Sharp diagonal shaft cutting through darkness
- Particles: Dancing dust motes, visible, almost tactile
- Subject: Empty chair, old object, or figure in memory sequence
- Emotional: Nostalgia, loss, time stopped, forgotten stories
- Best For: Documentary, heritage, historical fiction, melancholy brands

**4. The Underwater Cathedral**
- Source: Surface sun penetrating water
- Medium: Water itself + plankton particles
- Beams: Blue-cyan shafts fading with depth
- Caustics: Light patterns dancing on surfaces below
- Subject: Diver, marine life, or submerged structure
- Emotional: Otherworldly, alien beauty, weightless peace, mystery
- Best For: Ocean content, luxury travel, meditation, sci-fi

**5. The Noir Smoke Beam**
- Source: Single hard practical — desk lamp, window, door crack
- Medium: Cigarette smoke or atmospheric haze
- Beams: Tight, defined, often diagonal
- Color: Warm amber or cool blue depending on source
- Subject: Detective, femme fatale, or mysterious figure
- Emotional: Secrets, moral ambiguity, hidden truth, intimacy
- Best For: Noir, thriller, mystery, intimate drama

**6. The Concert Divine**
- Source: Follow spot or stage lights from above/back
- Medium: Haze from fog machine
- Beams: Dramatic cones visible in dark venue
- Color: Often colored gels — magenta, cyan, amber
- Subject: Performer illuminated in beam center
- Emotional: Worship, adoration, performative transcendence
- Best For: Music videos, concert films, event coverage, worship

---

### EXAMPLE PROMPTS

**Cathedral Transcendence:**
> Volumetric god ray cinematography, morning sun streaming through tall stained glass windows of gothic cathedral, heavy incense smoke creating visible golden light shafts at steep diagonal angles, dust and smoke particles dancing slowly in beams like floating gold, deep blue and amber colored light from stained glass mixing in air, solitary figure kneeling in prayer silhouetted against luminous column of light, sharp defined beams cutting through relative darkness, sacred atmospheric lighting, transcendent divine presence, cinematic spiritual grandeur

**Forest Enchantment:**
> Volumetric god ray cinematography, dawn sun breaking through dense old-growth forest canopy creating vertical golden columns of light, ground mist and pollen particles catching illumination, beams shifting from warm gold at canopy to cool green in deeper forest, small human figure standing dwarfed by towering trees and luminous shafts, sharp defined light columns contrasting with dark undergrowth, enchanted primordial atmosphere, fairy tale forest lighting, cinematic nature wonder

**Noir Smoke Mystery:**
> Volumetric light shaft cinematography, single hard light source from partially opened door creating tight diagonal beam through darkness, cigarette smoke thickening the air and making light path visible, dust motes dancing in amber beam, private detective sitting in pool of light with face half-shadowed, sharp defined beam with dark edges, claustrophobic noir atmosphere, secrets illuminated in darkness, cinematic mystery lighting

---

### TECHNICAL NOTES FOR AI GENERATION
- Always include both the light source AND the medium (dust, smoke, mist, water) — rays need particles to be visible
- Specify beam quality: "sharp defined shafts" vs "soft diffuse glow"
- For FLUX: describe particles explicitly — "dust motes dancing in light beam"
- For LTX: specify "stable light beam position across frames" as guardrail
- Color the medium: "golden dust" or "blue water particles" for emotional temperature
- Contrast is essential — rays need dark surroundings to be visible
- Include occluding objects (window frames, tree branches, clouds) to create beam edges
- Underwater god rays need caustic patterns mentioned: "light caustics dancing on seafloor"
