# SKILL: Drone & Aerial Framing
## Version: 1.0 | Hermes Agent Camera & Lens Language

---

### DESCRIPTION
Mastery of unmanned aerial vehicle (UAV) cinematography and elevated static perspectives. Aerial framing reveals spatial relationships invisible from ground level, creates geometric abstraction through top-down views, and delivers dramatic scale reveals. Covers drone-specific movements (orbit, reveal, pull-out, push-in) and the unique psychological impact of god's-eye perspective.

### TRIGGER KEYWORDS
drone shot, aerial, bird's eye view, overhead shot, top-down, aerial photography, drone footage, God's eye, aerial reveal, pull-out drone, orbit shot, aerial landscape, high altitude, birds eye, elevation, aerial cinematography

### CORE RULES
- Altitude determines meaning: low = intimate context, medium = environmental, high = abstraction/insignificance
- Nadir (straight down) creates geometric graphic patterns — subjects become shapes
- Drone orbit reveals subject in context: use for establishing location, not just beauty
- Human figures at high altitude signal isolation or insignificance — use this intentionally
- Shadows become design elements from aerial perspective, especially at golden hour
- Pull-out reveal: start close to hide scale, pull back to reveal the surprise of context
- Always specify "smooth stabilized" — unstabilized aerial reads as equipment failure

---

### TECHNICAL PARAMETERS

**Altitude Categories:**
- Low Aerial: 10–50 ft — Slightly elevated, still intimate, reveals local context
- Medium Aerial: 50–200 ft — Full environment visible, human scale readable
- High Aerial: 200–400 ft — Landscape patterns dominant, humans become dots
- Ceiling Limit: 400 ft AGL (Above Ground Level) — FAA/standard regulatory limit
- Orbital Ceiling: Lower altitudes (50–150 ft) for smooth orbit shots

**Drone Movement Types:**
- Push-In: Camera moves toward subject, increasing emotional intensity [^30^]
- Pull-Out/Reveal: Camera retreats from subject, revealing wider context [^30^]
- Orbit: Circular path around subject at constant radius [^30^]
- Top-Down/Bird's Eye: Camera pointing straight down at 90° [^30^]
- Crane/Jib Simulation: Vertical rise or fall revealing layers
- Dolly: Horizontal tracking at altitude
- Fly-Through: Passing through gaps (trees, buildings, arches)

**Top-Down Geometry:**
- Perspective: 90° nadir view eliminates horizon
- Pattern Recognition: Natural and man-made geometries become abstract design
- Symmetry: Human constructions often reveal perfect symmetry from above
- Scale Ambiguity: Without horizon reference, scale becomes difficult to judge
- Shadow Direction: Reveals time of day; long shadows add dimension to flat view

**Reveal Shot Mechanics:**
- Start Frame: Tight on subject or obscured view
- Movement: Pull-out, rise, or clear obstacle
- End Frame: Wide context revealed
- Emotional Arc: From intimacy/uncertainty to understanding/awe
- Pacing: Slow, deliberate; 3–8 seconds for full reveal

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Drone/Aerial] [shot type: top-down/orbit/reveal/push-in] cinematography, 
[camera movement: rising/pulling back/orbiting/pushing in], 
[subject] viewed from [altitude/angle], 
[geometric pattern: symmetry/lines/texture] revealed from elevated perspective, 
[scale relationship: human vs environment/subject vs landscape], 
[smooth/dynamic] camera motion, 
cinematic aerial perspective, 
[time of day] light casting [shadow quality], 
photorealistic environmental detail, 
[emotional effect: awe/isolation/revelation]
```

**Negative Prompts:**
```
ground level perspective, eye level camera, 
handheld shake, interior confined space, 
flat lighting without shadow, low altitude without context, 
unrealistic drone physics, video game environment, 
close-up without environmental relationship
```

---

### ADVANCED TECHNIQUES

**1. The Grand Reveal (Pull-Out)**
- Start: Close on subject (person, building detail, vehicle)
- Movement: Smooth backward and upward flight
- End: Wide environmental context revealed
- Emotional: "Oh, I see now" — understanding, awe, insignificance
- Best For: Location introductions, story turning points, scale realization [^30^]

**2. Top-Down Abstract Geometry**
- Altitude: 100–300 ft
- Subject: Agricultural fields, city blocks, parking lots, beaches
- Effect: Human activity becomes pattern/texture
- Color: Natural or man-made color blocks create graphic design
- Emotional: Order, chaos, human impact on nature, abstraction
- Best For: Documentary openers, transition sequences, art pieces [^30^]

**3. Orbital Spotlight**
- Movement: Perfect circular orbit around subject
- Radius: 20–50 ft from subject
- Altitude: 20–50 ft above subject
- Speed: Slow, majestic (10–30 seconds per revolution)
- Emotional: Subject importance, 360° appreciation, scrutiny
- Best For: Architecture, monuments, vehicles, dramatic character moments [^30^]

**4. Fly-Through Immersion**
- Movement: Forward flight through natural or architectural gap
- Speed: Moderate to fast (15–40 mph)
- Effect: Viewer sensation of flight, danger, freedom
- Risk: Obstacle proximity creates tension
- Emotional: Adventure, discovery, thrill, liberation
- Best For: Forests, canyons, city streets, architectural interiors

**5. Vertical Crane Reveal**
- Movement: Straight vertical rise from low to high altitude
- Start: Ground level, intimate detail
- End: Bird's eye, full context
- Emotional: Ascension, overview, power shift, death/rebirth metaphor
- Best For: Weddings, ceremonies, landscape transitions, narrative climaxes

**6. Tracking Follow**
- Movement: Camera follows moving subject from aerial perspective
- Distance: 20–50 ft behind/to side
- Altitude: 15–30 ft
- Effect: Subject maintains consistent frame size while environment flows past
- Emotional: Journey, pursuit, documentary observation
- Best For: Vehicles, runners, animals, adventure sports

---

### AERIAL SHOT TYPE MATRIX
| Shot Type | Altitude | Movement | Emotional Use | Technical Note |
|-----------|----------|----------|---------------|----------------|
| Top-Down | 100–300 ft | Static or slow drift | Abstraction, pattern | 90° nadir, no horizon |
| Reveal | Variable | Pull-out + rise | Awe, understanding | Start tight, end wide |
| Orbit | 20–50 ft radius | Circular path | Importance, scrutiny | Constant radius, smooth |
| Push-In | 10–50 ft | Forward flight | Intensity, focus | Increasing subject size |
| Fly-Through | 0–30 ft | Forward through gap | Thrill, immersion | Obstacle proximity tension |
| Crane Rise | Variable | Vertical only | Ascension, overview | Straight up, no lateral |

---

### EXAMPLE PROMPTS

**Top-Down Vineyard:**
> Aerial top-down drone shot at 200ft, vineyard rows creating perfect geometric lines of green and gold, autumn light casting long shadows between rows adding dimension to flat nadir view, tractor moving through field creating curved disturbance in pattern, geometric abstraction of agricultural landscape, no horizon visible, photorealistic environmental detail, contemplative order, cinematic drone cinematography, warm afternoon light

**Grand Reveal Coastal:**
> Cinematic drone reveal shot, starting tight on lone figure standing on dark rock, camera smoothly pulling back and rising to reveal vast coastal cliff landscape, figure shrinking to scale dot against towering sea cliffs and crashing waves, golden hour light from side illuminating rock texture, dramatic scale realization of human insignificance against nature, smooth professional drone motion, photorealistic ocean and cliff detail, awe-inspiring environmental reveal

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify "aerial" or "drone" explicitly to trigger elevated perspective
- Use "top-down" or "bird's eye" for 90° nadir geometry
- Include "smooth camera motion" to prevent jerky unrealistic movement
- Mention "pulling back" or "rising" for reveal mechanics
- Use "geometric pattern" or "abstract" for top-down graphic quality
- Specify altitude range for scale context
- Include "no horizon" for pure top-down abstraction
