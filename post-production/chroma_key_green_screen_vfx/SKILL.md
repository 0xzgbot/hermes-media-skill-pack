# SKILL: Chroma Key & Green Screen VFX
## Version: 1.0 | Hermes Agent Compositing & Virtual Production

---

### DESCRIPTION
Mastery of chroma key compositing, green screen production, and virtual production techniques for AI-generated cinematic content. This skill encodes the technical and aesthetic requirements for creating believable composites: proper screen lighting, spill suppression, edge refinement, color space matching, and the integration of foreground subjects with digital or practical backgrounds. Essential for fantastical environments, impossible locations, weather effects, and any production requiring subjects to exist in spaces that cannot be practically filmed.

---

### TECHNICAL PARAMETERS

**The Chroma Key Pipeline:**
```
Foreground Subject (lit separately from screen)
    ↓
Chroma Screen (green or blue, evenly lit)
    ↓
Keying Algorithm (color difference, luminance key, despill)
    ↓
Matte Refinement (edge blur, choke, garbage mask)
    ↓
Background Plate (practical footage, CGI, AI-generated)
    ↓
Color Matching (foreground/background harmony)
    ↓
Final Composite (grain matching, atmospheric integration)
```

**Screen Color Selection:**

| Color | Best For | Avoid When | Prompt Term |
|-------|----------|-----------|-------------|
| **Green** | Most productions, digital sensors sensitive to green | Green costume, foliage, nature scenes | "green screen" |
| **Blue** | Night scenes, water, green costumes, blonde hair | Blue sky reflection, blue costumes | "blue screen" |
| **Magenta** | Rare — used for specific costume conflicts | Most general cases | "magenta screen" |

**Screen Lighting Requirements:**
- **Evenness:** No hotspots or shadows on screen; within 0.5 stop across entire surface
- **Separation:** Subject must be 6–10 feet from screen to prevent spill and shadow
- **Color Temperature:** Screen lit to match background plate intention
- **No Reflection:** Subject lighting must not bounce green onto subject
- **Screen Exposure:** 1–1.5 stops below key light on subject

**The Spill Problem:**
Green light reflecting from screen onto subject creates "spill" — green tint on edges, hair, and transparent materials.
- **Detection:** White areas near screen edge show green tint; hair becomes chartreuse
- **Prevention:** Distance, flags, negative fill on screen side, backlight color correction
- **Fix:** Despill algorithms, color suppression, edge replacement

---

### PROMPT ARCHITECTURE

**Core Prompt Template (Green Screen Production):**
```
Chroma key cinematography, subject filmed against [green / blue] screen,
proper screen separation with no spill on subject,
evenly lit chroma background, subject lit with [lighting setup],
[edge detail: hair / glass / motion blur] preserved for clean key,
foreground subject prepared for compositing,
professional VFX production setup, clean matte edges
```

**Core Prompt Template (Final Composite):**
```
VFX composite, [foreground subject] integrated into [background environment],
matched lighting direction and color temperature between foreground and background,
[atmospheric integration: haze / fog / dust] unifying layers,
edge refinement on [hair / fabric / transparent elements],
color grading harmony between elements,
matched grain and lens characteristics,
believable spatial relationship, professional compositing quality
```

**Negative Prompts:**
```
green spill on subject, uneven screen lighting, shadow on chroma background,
chromatic aberration on edges, mismatched lighting direction,
foreground floating on background, no contact shadow,
unmatched color temperature, sharp cut edges without motion blur
```

---

### ADVANCED TECHNIQUES

**1. The Perfect Hair Key**
- Challenge: Fine hair strands let background show through; edges look buzzed
- Solution: Backlight separation (rim light on hair), increased distance, higher resolution
- Key Settings: Fine edge detail, reduced choke, increased edge blur slightly
- Despill: Aggressive on hair edges; replace green with background color
- Prompt: "fine hair detail preserved against chroma background, backlight rim separation, no green spill in hair"

**2. The Atmospheric Composite**
- Challenge: Foreground looks pasted onto background; no environmental integration
- Solution: Add matching haze, dust, or moisture between layers; match depth of field
- Color: Foreground lifted blacks to match atmospheric perspective of background
- Edge: Slight atmospheric blur on distant edges
- Prompt: "foreground subject with atmospheric haze matching background environment, depth-integrated composite, environmental particles unifying layers"

**3. The Impossible Weather**
- Technique: Subject shot on green screen, composited into extreme weather
- Integration: Rain/snow must fall IN FRONT of subject as well as behind
- Lighting: Lightning flashes must illuminate both foreground and background
- Reflection: Wet ground must reflect both subject and background
- Motion: Wind effects on hair/clothing must match background conditions
- Best For: Storm coverage, apocalyptic scenes, fantasy weather, action

**4. The Virtual Production Volume**
- Technique: LED wall displaying real-time background instead of green screen
- Lighting: Background provides interactive light on subject
- Reflections: Metallic and glass surfaces reflect LED content naturally
- Camera Tracking: Background perspective shifts with camera movement
- Advantage: No spill, no keying artifacts, natural reflections
- Prompt: "virtual production LED volume, real-time background providing interactive light on subject, natural environmental reflections"

**5. The Transparent Material Key**
- Challenge: Glass, water, smoke, fire — all partially transparent
- Green Screen: Smoke and glass show background color through them
- Solution: Shoot against black for transparency; multiple passes; rotoscope
- Edge: No hard key; use luminance or difference matte instead
- Best For: Ghosts, spirits, magical effects, water creatures, glass artifacts

---

### COMPOSITING QUALITY CHECKLIST

| Element | Check | Fix Strategy |
|---------|-------|--------------|
| **Edge Halos** | Green or blue fringe around subject | Despill, edge replacement, choke |
| **Edge Hardening** | Hair looks buzzed or cut out | Increase edge detail, reduce choke, use hair key |
| **Floating Subject** | No ground contact or shadow | Add contact shadow, ambient occlusion |
| **Mismatched Grain** | Foreground smooth, background grainy | Add grain to foreground or reduce from background |
| **Color Temperature** | Warm subject, cool background | Color correction to match |
| **Light Direction** | Subject lit from left, background from right | Choose matching plates or relight digitally |
| **Depth of Field** | Subject sharp, background sharp (should vary) | Add blur to background or sharpen subject edges |
| **Motion Blur** | Subject blur doesn't match background | Analyze camera movement, match motion vectors |

---

### EXAMPLE PROMPTS

**Green Screen Production Setup:**
> Chroma key production cinematography, actor in period costume positioned 8 feet from green screen with proper separation, even green screen lighting with no hotspots or shadows, subject lit with soft key from camera-left and backlight rim separation preventing green spill, fine hair detail visible against chroma background, no green reflection on costume or skin, professional VFX setup, clean matte edges preserved, studio green screen environment

**Fantasy Composite:**
> VFX composite, warrior figure standing on cliff edge integrated into fantastical floating island environment, matched golden hour lighting direction casting consistent shadows, atmospheric haze and clouds unifying foreground and background layers, edge refinement on fur cloak and hair, contact shadow grounding figure to rock surface, matched lens characteristics and grain, environmental dust particles floating between layers, cinematic compositing quality, believable spatial integration

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "green screen" or "chroma key" explicitly when describing production setup
- Use "composite" or "composited" when describing final integrated image
- For FLUX: describe the final composite in positive unified terms rather than separate layers
- For LTX: specify "stable edge detail across frames" as guardrail for keyed subjects
- Green spill is the most common artifact — explicitly request "no green spill"
- Contact shadows are essential for grounding — always mention "contact shadow"
- Atmospheric integration (haze, dust, moisture) sells the composite more than perfect edges
- Reference "virtual production" or "LED volume" for modern spill-free approach
