# SKILL: Explainer & Educational
## Version: 1.0 | Hermes Agent Genre & Format Expertise

---

### DESCRIPTION
Mastery of cinematographic and compositional strategies that prioritize clarity, comprehension, and retention over beauty. Educational content must deliver information efficiently while maintaining engagement. The frame is a classroom — every element must either teach or get out of the way. Annotation-friendly composition ensures that graphics, text, and highlights can be added without fighting the image.

### TRIGGER KEYWORDS
explainer, educational, tutorial, how-to, instructional, teach, learn, explain, demonstration, step-by-step, infographic, educational video, educational content, explainer video, teaching visual

### CORE RULES
- Clarity over beauty: if beautiful but confusing, it has failed
- Annotation-friendly framing: leave space for text overlays, arrows, and callouts
- Single concept per frame: do not overcrowd — one thing to understand per shot
- Direct address builds trust: subject looking at camera creates teacher-student relationship
- Neutral backgrounds remove distraction: subject and concept share attention equally
- Step-sequence framing: consistent angle and scale across related steps for easy comparison
- Color-coding is effective: consistent color assignment helps viewers track multiple concepts

---

### TECHNICAL PARAMETERS

**Clarity Over Beauty:**
- Subject Isolation: The object of learning must be the only bright/sharp/dynamic element
- Background Simplicity: Solid color, gradient, or subtle texture — never competing
- Lighting Evenness: Key light + soft fill eliminating confusing shadows on subject
- Color Neutrality: No heavy color cast that distorts subject accuracy
- Focus Stability: Subject remains sharp; no rack focus unless demonstrating depth
- Contrast Control: Sufficient contrast for visibility but not so much that detail clips
- Motion Restriction: Camera movement only when it aids understanding (orbit around object, push-in to detail)

**Annotation-Friendly Framing:**
- Headroom: Top 20% of frame kept clear for titles, arrows, or text callouts
- Negative Space: Left or right third available for bullet points, labels, or diagrams
- Center Safe Zone: Primary subject in center 50% where graphics won't overlap
- Bottom Zone: Lower 15% reserved for captions, progress bars, or lower-thirds
- Color Separation: Subject color distinct from background so highlight boxes read clearly
- Static Background: Moving backgrounds make text overlays difficult to read
- Resolution: 1080p minimum; 4K preferred for zoom-and-pan post flexibility

**Information Hierarchy in Frame:**
- Primary Subject: Largest, sharpest, most central = what viewer must learn
- Secondary Context: Smaller, softer, peripheral = supporting information
- Tertiary Reference: Background, out of focus = environmental context only
- Hands/Pointer: Human element guides attention; hand enters from edge to indicate
- Scale Reference: Ruler, coin, hand, familiar object for size comprehension
- Before/After Split: Vertical or horizontal divide showing transformation

**Retention & Engagement:**
- Pacing: One concept per 5–10 seconds; cut on concept completion
- Visual Metaphor: Abstract concepts represented by physical objects
- Repetition: Key element shown from 2–3 angles for reinforcement
- Progress Indication: Visual suggestion of "step 1 of 5" through composition
- Surprise: Occasional unexpected angle or reveal prevents attention decay
- Human Presence: Face or hand every 15–20 seconds maintains social engagement

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Educational/explainer [video/frame], [subject] as primary learning object, 
[subject] isolated in [center/clear zone] with [even lighting/neutral background], 
[headroom/negative space] preserved for [text overlay/annotation/diagram], 
[scale reference: hand/ruler/coin] providing size context, 
[demonstration angle: top-down/side/cross-section] optimizing comprehension, 
[clarity lighting: soft even/no color cast] ensuring accuracy, 
[human element: hand/pointer/face] guiding attention, 
[static/demonstration motion] supporting learning without distraction, 
educational cinematography prioritizing clarity, 
annotation-friendly composition
```

**Negative Prompts:**
```
beautiful but confusing background, heavy color grading, 
dramatic shadows hiding detail, artistic blur, 
cluttered frame with multiple subjects, 
moving background making text unreadable, 
insufficient headroom for titles, 
no scale reference, abstract without concrete representation, 
shallow depth of field hiding important detail, 
fast cuts preventing comprehension, 
no human presence for 30+ seconds
```

---

### ADVANCED TECHNIQUES

**1. The Isolated Demonstration**
- Setup: Single object on clean surface, top-down or 45° angle
- Light: Even, shadowless, accurate color temperature
- Background: White, light gray, or brand color
- Annotation Space: Entire frame except object is clear for labels
- Motion: Hand enters to manipulate; object rotates on turntable
- Best For: Product features, assembly, cooking, tools, unboxing

**2. The Split-Screen Comparison**
- Setup: Before/After or Option A/Option B in same frame
- Division: Clean vertical or horizontal line
- Light: Matched exactly on both sides
- Annotation: Labels above each side; arrow between
- Emotional: Transformation, choice, improvement
- Best For: Product comparison, tutorials, medical, fitness, renovation

**3. The Process Timeline**
- Setup: Same frame position showing progression over time
- Technique: Stop-motion or jump cuts in same composition
- Annotation: Step numbers appear in reserved space
- Motion: Minimal camera movement; subject changes state
- Best For: Recipes, assembly, growth, chemical reactions, makeup

**4. The Transparent View**
- Setup: Cross-section, X-ray, or see-through view
- Technique: CGI overlay or physical cutaway model
- Annotation: Labels on internal parts
- Light: Backlit for transparency; front-lit for detail
- Best For: Anatomy, engineering, architecture, product internals

**5. The Guided Tour**
- Setup: Camera follows guide through environment
- Framing: Guide in foreground, subject in background
- Annotation: Labels appear over subjects as guide mentions them
- Pace: Walking speed; cuts on room/section changes
- Best For: Real estate, factory tours, museum, software UI walkthrough

**6. The Hand as Teacher**
- Setup: Extreme close-up of hands performing task
- Background: Solid color or blurred neutral
- Annotation: Arrow and text appear near fingers
- Light: Bright even; no shadows on workspace
- Motion: Slow, deliberate; every movement teaches
- Best For: Crafts, repairs, art, cooking, instrument tutorials

**7. The Abstract-to-Concrete**
- Setup: Abstract concept (inflation, neural network, supply chain)
- Visualization: Physical metaphor — balloons, water pipes, dominoes
- Annotation: Labels connect metaphor to real concept
- Light: Bright, cheerful, accessible
- Emotional: Complexity made simple, empowerment
- Best For: Finance, science, tech, economics, philosophy

---

### EDUCATIONAL FRAMING MATRIX
| Subject | Best Angle | Background | Light | Annotation Zone | Scale Ref |
|---------|------------|------------|-------|-------------------|-----------|
| Product | 45° or top-down | White/gray | Even, 5500K | Top and sides | Hand, coin |
| Anatomy | Cross-section | Dark | Backlit + front | Labels on parts | Full body |
| Cooking | Top-down | Kitchen surface | Warm, even | Bottom for steps | Hand, utensils |
| Software | Screen capture | N/A | Screen brightness | Cursor + highlights | N/A |
| Science | Side or macro | Black or white | Dramatic or even | Side labels | Ruler, beaker |
| Assembly | 45° or eye level | Workbench | Bright practical | Step numbers | Hand, tools |
| Nature | Eye level or macro | Natural | Natural | Side text | Hand, coin |

---

### EXAMPLE PROMPTS

**Isolated Product Demonstration:**
> Educational explainer frame, wireless keyboard isolated on clean light gray surface at 45-degree angle, product centered in frame filling 35% with generous headroom and left third negative space preserved for text annotation overlay, even 5500K softbox lighting creating minimal shadows for accurate color rendering, hand entering from right edge pointing to specific key with index finger guiding attention, scale reference of standard coffee mug in background providing size context, annotation-friendly composition with clear separation between white keyboard and gray background, crisp focus throughout product ensuring every keycap detail visible, educational product photography prioritizing clarity over style, commercial tutorial aesthetic

**Abstract-to-Concrete Finance:**
> Educational explainer visualization, animated physical metaphor showing water flowing through pipes of different diameters to explain cash flow concept, clean isometric 3D style with bright cheerful lighting, primary concept (cash) represented by glowing blue water visible in central pipes, annotation space preserved in top 20% and left third for text labels and arrows, secondary elements (expenses, revenue) color-coded in distinct hues with clear separation, human hand miniature figure at bottom providing scale and human engagement point, static background in soft cream color ensuring text readability, motion limited to water flow animation supporting comprehension, educational clarity over artistic abstraction, annotation-friendly composition with generous negative space

---

### TECHNICAL NOTES FOR AI GENERATION
- Use "educational" or "explainer" explicitly for clarity priority
- Specify "annotation-friendly" or "text overlay space" for post-production
- Include "even lighting" or "shadowless" for detail visibility
- Mention "neutral background" or "solid color" to prevent clutter
- Use "top-down" or "45-degree" for optimal demonstration angles
- Include "scale reference" for size comprehension
- Mention "headroom" or "negative space" percentages ("top 20% clear")
- Use "human hand" or "pointer" for attention guidance
- Specify "static background" if text will be added later
- Mention "one concept" or "single subject" for focus discipline
