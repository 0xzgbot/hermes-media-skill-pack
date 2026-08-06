# SKILL: Motion Blur Artifacts
## Version: 1.0 | Hermes Agent Failure Pattern Library

---

### DESCRIPTION
Mastery of controlling motion blur in AI-generated imagery — both preventing unwanted blur in static images and generating appropriate blur for dynamic scenes. Motion blur occurs when the model renders movement as streaking or softness rather than crisp frozen action. In video, improper blur causes temporal instability and "smear" artifacts [^81^].

### TRIGGER KEYWORDS
motion blur, blur artifact, smear, streaking, motion smear, action blur, movement blur, frozen action, sharp motion, blur prevention, temporal blur, camera motion blur, subject blur

### CORE RULES
- To prevent unwanted blur: "sharp frozen action, no motion blur, crisp edges"
- To create intentional blur: "natural motion blur suggesting speed, directional blur showing movement"
- Specify shutter equivalent: "frozen at 1/1000s" prevents blur; "long exposure motion trail" creates it
- Specify which elements blur: background blur = allowed; face/subject = always sharp
- For video: "no motion smear between frames, temporally stable" prevents AI smear artifacts
- Fast action without blur instruction generates frozen sports aesthetic by default in Flux
- Never allow face blur: specify "sharp face regardless of motion" if body/hands are moving

---

### DETECTION SIGNALS

**Unwanted Blur in Static Images:**
- Subject edges soft when they should be sharp
- Double edges or ghosting around moving elements
- Camera shake appearance in non-handheld compositions
- Background streaking in static scenes
- Facial features blurred despite subject being still

**Inappropriate Blur in Dynamic Images:**
- Frozen motion when blur expected (sports, vehicles, action)
- Uniform sharpness across frame despite high speed
- No directional streaking on moving objects
- Wheels/limbs appearing static during motion

**Video-Specific Motion Artifacts:**
- Temporal smear between frames
- Inconsistent blur direction frame-to-frame
- Background blur while foreground stays sharp (or vice versa)
- "Rubber face" during rapid expression changes [^87^]

---

### FIX VOCABULARY — FREEZE TECHNIQUES

**For Static/Sharp Images:**
```
sharp focus, frozen motion, high shutter speed, 1/1000s shutter, tack sharp, no motion blur, pin-sharp detail, crisp edges, freeze frame, strobe light effect
```

**For Controlled Dynamic Blur:**
```
natural motion blur, 180° shutter, directional blur, background streaking, panning blur, speed blur, motion trails, kinetic energy, frozen subject with blurred background
```

**Shutter Language:**
```
fast shutter 1/2000s, sports photography shutter, high-speed sync, flash freeze, slow shutter 1/15s, long exposure, light painting, intentional camera movement
```

---

### FIX STRATEGIES

**1. The Shutter Speed Command**
- Explicitly state shutter speed to control blur:
  - `1/8000s shutter` = completely frozen, no blur
  - `1/1000s shutter` = frozen action, slight background softness
  - `1/250s shutter` = slight motion blur on fast movement
  - `1/60s shutter` = noticeable blur, panning possible
  - `1/15s shutter` = heavy artistic blur

**2. The Panning Technique**
- `panning shot, subject sharp with motion-blurred background, horizontal streaking`
- Creates sense of speed while keeping subject crisp

**3. The Flash Freeze**
- `flash photography, strobe frozen motion, subject caught mid-action with sharp detail`
- Simulates high-speed flash freezing movement

**4. The Selective Blur**
- `subject tack sharp, background motion blurred, shallow depth of field combined with motion blur`
- Isolates subject through dual separation (depth + motion)

**5. The Tripod Lock**
- `tripod-mounted camera, static frame, no camera shake, rock steady`
- Prevents unintended blur from "handheld" interpretation

**6. The Directional Blur**
- `horizontal motion blur`, `vertical blur from falling`, `radial blur from spinning`
- Specifies blur direction for coherent motion

**7. The Frame Freeze**
- `single frame extracted from high-speed video, peak action frozen`
- Frames the image as a freeze-frame from motion

---

### MODEL-SPECIFIC STRATEGIES

**SDXL / z_image:**
- Positive: `tack sharp, 1/1000s shutter, frozen motion`
- Negative: `motion blur, blurry, out of focus, camera shake, double exposure, ghosting`
- Works well with sports and action photography tokens

**Flux / Flux2:**
- Use technical photography language: `shot at 1/2000s, flash freeze, stroboscopic`
- Positive reframing: `pin-sharp throughout, no blur, crisp frozen moment`
- No negative prompts available natively

**LTX Video:**
- Critical: Specify shutter angle for motion blur authenticity [^68^]
- `180° shutter equivalent` = natural cinematic motion blur
- `90° shutter` = crisp, slightly staccato (Saving Private Ryan style)
- `360° shutter` = dreamy, smeary blur
- Guardrail: `consistent motion blur across frames, no temporal smear, stable blur direction`

---

### EXAMPLE FIX PROMPTS

**Fix: Unwanted Blur (Flux):**
> `Portrait of athlete frozen mid-jump, tack sharp at 1/8000s shutter, pin-sharp detail on face and uniform, no motion blur, strobe flash freeze, crisp edges, photorealistic sports photography`

**Fix: Appropriate Motion Blur (SDXL):**
> Positive: `Panning shot of race car at speed, car sharp with directional motion blur on background, 1/60s shutter, horizontal streaking of track and crowd, kinetic energy, motorsport photography`
> Negative: `uniform sharpness, static background, no sense of speed`

**Fix: Video Motion Consistency (LTX):**
> `Camera/Lens: Tracking dolly at constant speed, 24mm f/2.8. Motion: 180° shutter equivalent, natural motion blur on background, subject sharp. Guardrails: Consistent blur direction, no temporal smear, stable motion blur across frames.`

---

### DETECTION CHECKLIST
- [ ] Static subjects completely sharp?
- [ ] Moving subjects have appropriate blur (if desired)?
- [ ] Blur direction consistent and logical?
- [ ] No double edges or ghosting?
- [ ] No unintended camera shake?
- [ ] Video blur consistent frame-to-frame?
- [ ] Shutter speed appropriate for subject motion?

---

### TECHNICAL NOTES FOR AI GENERATION
- Explicit shutter speed language is the most reliable blur control
- 180° shutter is the cinematic standard for natural motion blur [^68^]
- In video, inconsistent blur direction between frames is a primary temporal artifact
- Flash freeze language (`strobe`, `flash photography`) reliably produces sharp frozen action
- Panning blur requires explicit directional specification (`horizontal streaking`)
- Tripod language prevents unwanted "handheld shake" aesthetic
