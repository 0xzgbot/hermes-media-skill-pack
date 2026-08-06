# SKILL: Documentary & Interview Format
## Version: 1.0 | Hermes Agent Non-Fiction Cinematic Grammar

---

### DESCRIPTION
Mastery of documentary cinematography and interview-based storytelling for AI-generated campaigns. This skill encodes the visual grammar of non-fiction filmmaking: the ethical observer position, B-roll coverage logic, interview lighting conventions, archival integration, and the specific rhythm of truth-telling through image. Essential for explainer content, brand documentaries, testimonials, and any campaign rooted in authenticity.

---

### TECHNICAL PARAMETERS

**The Documentary Observer Contract:**
- Camera is a witness, not a performer — movement should feel discovered, not choreographed
- Subjects look slightly off-camera (at interviewer) for interview; at lens for direct address
- Natural light is preferred motivation; artificial light must feel incidental
- Environments are real locations, not sets — clutter is character
- Time markers (clocks, calendars, seasonal light) ground narrative in reality

**Interview Framing Standards:**
- **The Talking Head:** Medium close-up, eyes at upper third, nose room toward look space
- **The Two-Shot:** Subject + interviewer visible; establishes power dynamic
- **The Profile:** Side view for emotional vulnerability; reveals environment behind
- **The Over-Shoulder:** Looking past interviewer shoulder; intimate, conversational
- **Safe Margins:** Keep subject in center 50% for caption/subtitle safety

**Interview Lighting Conventions:**
- **Key Light:** Large soft source, 45° high, 45° side — flattering, unobtrusive
- **Fill Light:** Minimal or bounce-only — preserve dimension, eliminate harshness
- **Back Light:** Subtle separation from background; never dramatic
- **Background Light:** Practical sources motivate ambient; avoid visible equipment
- **Eye Light:** Tiny catchlight for life; avoid large reflective umbrellas in eyes

**B-Roll Coverage Logic:**
- Cutaway: Detail of what subject describes (hands, objects, environment)
- Establishing: Wide shot of location; grounds viewer in space
- Process: Subject doing what they discuss (working, walking, creating)
- Atmosphere: Texture of place (weather, traffic, nature, architecture)
- Archival: Photos, documents, old footage — treated with period-appropriate grade
- Cutaway Ratio: 3:1 minimum (3 B-roll shots per 1 interview shot)

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Documentary cinematography, [interview or observational style],
[framing: medium close-up / two-shot / over-shoulder],
naturalistic [lighting motivation: window light / practical lamps / overcast],
subject looking [slightly off-camera / at lens for direct address],
[location: real environment with authentic detail],
[background: contextual, slightly soft, environmental storytelling],
unobtrusive camera presence, ethical observer aesthetic,
[color treatment: desaturated / warm archival / cool objective],
authentic human moment, non-fiction visual grammar
```

**Negative Prompts:**
```
studio backdrop, perfect lighting, glamorous makeup, posed expression,
overly cinematic movement, dramatic lens flare, artificial set,
clean sterile environment, stock photo aesthetic, promotional corporate look,
visible lighting equipment, green screen, heavy color grading
```

---

### ADVANCED TECHNICAL FORMATS

**1. The Direct Address Testimonial**
- Framing: Medium close-up, subject looks directly into lens
- Lighting: Large soft key, minimal fill, subtle eye light
- Background: Contextual but soft; office, home, or workspace
- Emotional: Honest, vulnerable, authoritative
- Color: Slightly desaturated; skin tones preserved
- Best For: Customer testimonials, expert interviews, founder stories

**2. The Observational Fly-on-Wall**
- Camera: Static or slow handheld; never acknowledges camera
- Framing: Wide to medium; subjects small in environment
- Lighting: Available light only; windows, practicals, sun
- Sound Visual: Implied through environment (no visible boom)
- Emotional: Objective, intimate, unfiltered
- Best For: Process documentaries, day-in-the-life, social realism

**3. The Archival Integration**
- Old Photos: Sepia or faded color, visible grain, paper texture
- Documents: Shallow depth of field on text, dramatic raking light
- Period Footage: Appropriate film stock, scratches, gate weave
- Modern Intercut: Desaturated or color-matched to archival
- Best For: Historical documentaries, brand heritage, biographical

**4. The Explainer / Educational**
- Subject: Expert in active workspace, not sterile studio
- Graphics: Clean lower-thirds, data visualization, map overlays
- B-Roll: Process shots, macro details, location establishing
- Pacing: Deliberate, information-dense, respectful of viewer attention
- Best For: Educational content, how-to, science communication, corporate training

**5. The Vérité Moment**
- Framing: Reactive, found — camera responds to action
- Light: Changing, imperfect, real-world conditions
- Subject: Unaware or minimally aware of camera
- Emotional: Peak authenticity, unrepeatable, spontaneous
- Best For: Event coverage, breaking stories, human drama

---

### EXAMPLE PROMPTS

**Customer Testimonial:**
> Documentary interview cinematography, medium close-up of professional woman looking slightly off-camera at interviewer, large soft window light as key from camera-left creating gentle modeling on face, minimal bounce fill preserving dimension, authentic modern office background softly blurred with contextual details, natural skin texture without glamour retouching, desaturated warm color grade, subtle eye light catchlight, nose room toward look space, honest conversational expression, non-fiction testimonial aesthetic, clean unmarked image

**Day-in-the-Life Observational:**
> Observational documentary cinematography, wide shot of artisan working at wooden bench in sunlit workshop, available window light creating natural patterns on work surface, camera positioned as unobtrusive witness, subject focused on craft unaware of lens, environmental details of tools and materials visible in background, warm natural color temperature, fine dust particles in sunbeams, slow deliberate pacing, vérité visual grammar, authentic human labor

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "documentary" or "non-fiction" as primary genre signal
- Specify "looks slightly off-camera" for interview; "looks at lens" for direct address
- Mention "natural light" or "available light" to avoid studio aesthetic
- Include environmental clutter as character — "lived-in workspace" not "clean studio"
- For FLUX: describe authenticity in positive terms; no negative prompts
- For LTX: specify "stable documentary framing, no artificial camera movement" as guardrail
- Desaturated color grades signal objectivity; warm grades signal nostalgia
