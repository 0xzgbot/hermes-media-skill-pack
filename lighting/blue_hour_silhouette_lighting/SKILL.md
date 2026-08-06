# SKILL: Blue Hour & Silhouette Lighting
## Version: 1.0 | Hermes Agent Twilight & Shadow Cinematography

---

### DESCRIPTION
Mastery of blue hour twilight cinematography and silhouette lighting techniques for AI-generated campaigns. This skill encodes the visual grammar of the liminal zone between day and night: the specific color temperature of deep twilight, the dramatic power of silhouetted forms, rim light separation, and the emotional register of shadow as subject rather than absence. Essential for creating images of mystery, transition, isolation, and grandeur.

---

### TECHNICAL PARAMETERS

**The Blue Hour Window:**
- **Timing:** 20–40 minutes after sunset or before sunrise
- **Color Temperature:** 9000K–12000K — deep blue-cyan sky
- **Light Level:** 1–10 lux — dark but not black
- **Direction:** Omnidirectional ambient from sky dome; no direct sun
- **Duration:** Brief — requires efficiency and planning
- **Emotional Register: Melancholy, transition, anticipation, liminality**

**Blue Hour Color Science:**
- **Sky Gradient:** Deep indigo at zenith → cyan at horizon → faint orange at exact horizon
- **Artificial Light Dominance:** Streetlights, building lights become primary sources
- **Color Contrast:** Warm tungsten (3200K) against cool sky (10000K) creates maximum vibrational tension
- **Exposure Balance:** Sky 1–2 stops brighter than foreground; silhouettes natural
- **Reflection Quality:** Wet surfaces mirror sky color; becomes secondary light source

**Silhouette Types:**

| Type | Light Position | Subject Treatment | Background | Emotional Effect |
|------|---------------|-------------------|------------|------------------|
| **Pure Silhouette** | Directly behind subject | Completely black, no detail | Bright, colorful | Mystery, anonymity, universal symbol |
| **Semi-Silhouette** | Behind + slight side | Edge detail visible, face dark | Bright | Vulnerability, hidden emotion, intimacy |
| **Rim Lit** | Behind + slightly above | Glowing edge separation, subject visible | Any | Heroic, divine, isolated, beautiful |
| **Reflected Silhouette** | Below subject (water) | Mirror image in dark surface | Sky above | Symmetry, dream, duality |
| **Partial Silhouette** | Side-back light | Half face lit, half in shadow | Variable | Internal conflict, duality, dramatic tension |

**Rim Light Physics:**
- **Source Position:** 15°–45° behind subject, slightly above eye level
- **Intensity:** 2–3 stops brighter than key; creates glowing edge
- **Quality:** Hard source = sharp rim; soft source = diffused halo
- **Color:** Can be warm (golden hour) or cool (moonlight) — defines emotional temperature
- **Spread:** Tight beam = precise rim; wide beam = atmospheric glow

---

### PROMPT ARCHITECTURE

**Core Prompt Template (Blue Hour):**
```
Blue hour twilight cinematography, [time: post-sunset / pre-dawn],
deep indigo-cyan sky gradient from zenith to horizon,
cool 10000K ambient light from sky dome,
[artificial sources: city lights / streetlamps / building illumination],
warm tungsten points against cool blue atmosphere,
[subject] positioned against luminous sky,
wet surface reflections mirroring sky color,
15–30 minute twilight window, liminal light quality,
melancholic transitional atmosphere
```

**Core Prompt Template (Silhouette):**
```
Silhouette cinematography, [silhouette type: pure / semi / rim-lit / reflected],
bright background behind dark subject,
[light source: sun / moon / practical / artificial] positioned behind subject,
[edge treatment: sharp black / glowing rim / partial illumination],
[background: colorful sky / window light / neon city / natural landscape],
shape-based composition, form over detail,
[emotional register: mystery / heroism / isolation / vulnerability]
```

**Negative Prompts:**
```
flat midday lighting, even exposure, visible facial detail in silhouette,
overexposed sky, underexposed subject with detail, gray flat sky,
front-lit subject, flash photography, studio lighting, 
no background separation, cluttered silhouette shape
```

---

### ADVANCED TECHNIQUES

**1. The Blue Hour City**
- Setup: Urban environment 30 minutes after sunset
- Sky: Deep indigo transitioning to cyan at horizon
- Lights: Streetlamps, neon, building windows become stars on ground
- Subject: Small against vast city, walking or standing
- Reflection: Wet streets mirror sky and lights
- Emotional: Loneliness in crowds, urban melancholy, possibility
- Best For: City films, travel, night-before-morning transitions

**2. The Golden Rim Hero**
- Setup: Subject backlit by setting sun or large soft source
- Light: Warm golden rim outlining entire figure
- Subject: Slightly underexposed, face in shadow but visible
- Background: Bright, blown-out sky or window
- Lens: Long telephoto compresses figure against light
- Emotional: Heroic, divine, isolated greatness, aspiration
- Best For: Sports, leadership, triumph, spiritual content

**3. The Reflection Silhouette**
- Setup: Subject at water's edge during blue hour or dawn
- Water: Calm surface mirrors subject and sky
- Composition: Subject and reflection form symmetrical shape
- Sky: Color gradient doubles in reflection
- Emotional: Duality, introspection, dream state, peace
- Best For: Travel, meditation, luxury resorts, romantic moments

**4. The Neon Rim Cyberpunk**
- Setup: Subject in dark space with single colored light source behind
- Rim: Magenta, cyan, or acid green LED strip or neon tube
- Subject: Near-pure silhouette with colored edge glow
- Background: Black void or distant city bokeh
- Emotional: Mysterious, technological, alienated, cool
- Best For: Tech brands, sci-fi, music videos, futuristic fashion

**5. The Partial Silhouette Portrait**
- Setup: Side-back light hitting half the face
- Effect: One eye illuminated, one in shadow; half smile visible
- Background: Soft, out of focus, non-competing
- Emotional: Internal conflict, hidden depths, dramatic complexity
- Best For: Character introductions, psychological drama, intimate portraits

---

### EXAMPLE PROMPTS

**Blue Hour City Solitude:**
> Blue hour twilight cinematography, 30 minutes after sunset, deep indigo sky transitioning to cyan at horizon, lone figure standing on rain-slicked rooftop overlooking vast cityscape, warm tungsten window lights punctuating cool blue atmosphere, wet roof surface reflecting sky gradient and city lights, subject as small silhouette against luminous urban horizon, cool 10000K ambient light, streetlamp bokeh in foreground, melancholic transitional atmosphere, cinematic twilight aesthetic

**Golden Rim Athlete:**
> Silhouette cinematography with golden rim lighting, athlete standing on hilltop at sunset, sun positioned directly behind figure creating brilliant amber edge glow around entire body, subject slightly underexposed with heroic shape visible, warm 3000K backlight creating luminous halo, blown-out golden sky background, long telephoto lens compressing figure against light, rim-lit silhouette type, sense of triumph and isolation, aspirational sports cinematography

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "blue hour" or "twilight" explicitly for specific color temperature
- Specify Kelvin values: "10000K blue hour" or "3200K warm rim"
- For silhouettes: describe background brightness and subject darkness separately
- "Rim light" triggers edge-glow rendering; "silhouette" triggers form-over-detail
- For FLUX: describe color relationships in positive terms
- For LTX: specify "stable silhouette shape across frames" as guardrail
- Wet surfaces amplify blue hour effect — always mention if applicable
- Combine with lens: "silhouette through 85mm" isolates form; "silhouette through 24mm" emphasizes environment
