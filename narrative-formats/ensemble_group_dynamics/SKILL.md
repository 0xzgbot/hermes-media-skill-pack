# SKILL: Ensemble Group Dynamics
## Version: 1.0 | Hermes Agent Character & Direction System

---

### DESCRIPTION
Mastery of multi-subject framing that communicates hierarchy, relationships, power shifts, and emotional states through spatial positioning, eyeline vectors, and body language geometry. Every ensemble frame is a social diagram — the audience reads status, alliance, and tension instantly from who stands where, who touches whom, and where attention flows.

### TRIGGER KEYWORDS
ensemble, group shot, multiple characters, team photo, group framing, hierarchy, relationships, crowd composition, social dynamic, group of people, family portrait, board of directors, gang, squad, group interaction

### CORE RULES
- Every spatial relationship is a power statement: center = dominant, edge = marginal, forward = important
- Eyeline vectors reveal alliances and tensions: who looks at whom, who looks away
- Physical touch or proximity signals connection; distance signals conflict or independence
- Height and elevation signal hierarchy: higher = more powerful (unless deliberately subverted)
- Overlapping figures signal group cohesion; isolated figures signal conflict or independence
- The dominant subject draws the most compositional lines toward them
- Group shots need a clear visual entry point: one figure draws the eye first, then leads through

---

### TECHNICAL PARAMETERS

**Hierarchy in Frame:**
- Vertical Position: Higher in frame = higher status (standing vs seated, elevated ground)
- Center Dominance: Center of frame = narrative focus; edges = supporting roles
- Foreground/Background: Foreground subjects read as more immediate/aggressive; background subjects as reactive/observing
- Size Relative: Larger in frame = more power (closer to camera or physically larger)
- Framing by Architecture: Doorways, windows, arches can "crown" a subject with symbolic framing
- Isolation vs Cluster: Isolated subject = outsider, leader, or target; clustered group = alliance, conspiracy, family

**Interaction Vectors:**
- Eyeline Triangles: Three subjects create triangular attention pattern = complex dynamics
- Parallel Gazes: Two subjects look same direction = alliance, shared objective
- Opposing Gazes: Subjects face each other = confrontation, dialogue, intimacy
- Broken Vectors: Subject looks away from group = betrayal, secret-keeping, distraction
- Cascading Attention: A looks at B, B looks at C, C looks at object = information flow, chain of command
- The Ignored Subject: Group looks everywhere except one person = ostracism, invisibility

**Attention Flow:**
- Leading Lines: Architecture, furniture, roads direct eye to dominant subject
- Light Pool: Brightest area of frame draws attention = current narrative focus
- Motion Magnet: Moving subject draws eye in static group
- Color Pop: Subject in contrasting color against muted group = focus
- Negative Space Arrow: Empty space points toward important subject
- Depth Stacking: Sharp subject against blurred group = isolation within community

**Body Language Geometry:**
- Open Posture: Arms uncrossed, legs apart, facing group = confidence, openness, leadership
- Closed Posture: Arms crossed, turned away, hunched = defensiveness, exclusion, subordination
- Touch Zones: Hand on shoulder = alliance; hand on throat = threat; hands clasped = unity
- Proxemics: Intimate distance (<18in) = romance/family; personal (1.5–4ft) = friendship; social (4–12ft) = professional; public (12ft+) = estrangement
- Mirroring: Two subjects in similar poses = rapport, similarity, unconscious alliance
- Contrasting Poses: One relaxed, one rigid = power imbalance, tension

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
Ensemble [wide shot/medium shot] of [number] subjects, 
[hierarchy: leader positioned center-elevated/outsider isolated at edge/alliance clustered], 
interaction vectors creating [triangle/parallel/opposing/cascading] attention pattern, 
[body language: open/closed/mirrored/contrasting] signaling [relationship type], 
attention flow directed to [dominant subject] through [leading lines/light/motion/color], 
[environmental framing: architecture/furniture/landscape] reinforcing hierarchy, 
depth of field [deep/shallow] keeping [all subjects sharp/leader sharp only], 
cinematic group composition, 
social dynamics readable in single frame
```

**Negative Prompts:**
```
flat line of people, everyone same height and spacing, 
random positioning without purpose, all subjects looking at camera, 
equal framing for all, no eyeline logic, 
cluttered composition without hierarchy, 
body language disconnected from narrative, 
all subjects same size in frame, no depth staging
```

---

### ADVANCED TECHNIQUES

**1. The Power Pyramid**
- Setup: Three or more subjects arranged in triangular depth
- Apex: Leader at back center, elevated (standing on step, seated on throne)
- Base: Subordinates flanking in foreground, lower position
- Eyelines: Subordinates look up/toward leader; leader looks forward or down
- Emotional: Clear hierarchy, feudal structure, organized power
- Best For: Corporate, military, royal, criminal organization

**2. The Broken Circle (Outsider)**
- Setup: Group forms rough circle or cluster; one subject stands apart
- Distance: Outsider at edge of frame or separated by negative space
- Eyelines: Group looks inward or at each other; outsider looks at group or away
- Light: Group in warm pool; outsider in cooler or dimmer light
- Emotional: Exclusion, jealousy, leadership gap, impending betrayal
- Best For: Drama, thriller, family tension, workplace conflict

**3. The Confrontational Line**
- Setup: Two groups facing each other across horizontal frame divide
- Composition: Invisible vertical line separates sides; no one crosses center
- Eyelines: Opposing gazes locked across the divide
- Body Language: Closed postures, forward leans, tension in shoulders
- Emotional: Standoff, negotiation, war, sports rivalry, divorce
- Best For: Action, western, courtroom, sports, political drama

**4. The Cascading Secret**
- Setup: Chain of attention — A whispers to B, B reacts, C notices from distance
- Framing: Depth staging with three distinct planes
- Eyelines: A→B (intimate), B→A (reactive), C→A/B (observing)
- Body Language: A and B closed/intimate; C open but attentive
- Emotional: Gossip, conspiracy, betrayal, information as power
- Best For: Period drama, office politics, thriller, comedy

**5. The Mirror Alliance**
- Setup: Two subjects in matching poses, facing same direction
- Framing: Equal size, symmetrical positioning
- Touch: Shoulder touch, arm link, or synchronized gesture
- Eyelines: Parallel, looking at same off-screen objective
- Emotional: Partnership, romance, shared mission, twin energy
- Best For: Buddy films, romance, heist teams, family bonds

**6. The Fading Depth (Crowd Abstraction)**
- Setup: Large group (10+) with one subject in sharp focus
- Depth: Leader sharp in foreground; crowd blurs into background layers
- Light: Leader illuminated; crowd in shadow or flat ambient
- Emotional: Leadership, isolation in popularity, cult of personality
- Best For: Concert, rally, classroom, army, crowd scenes

---

### ENSEMBLE COMPOSITION MATRIX
| Dynamic | Spatial Pattern | Eyeline Pattern | Body Language | Genre |
|---------|-----------------|-----------------|---------------|-------|
| Leadership | Pyramid, center | Downward/outward | Open, upright | Corporate, military |
| Romance | Close pair, center | Mutual gaze | Mirroring, touch | Drama, romance |
| Conspiracy | Tight cluster | Inward circle | Closed, huddled | Thriller, crime |
| Betrayal | Broken circle | Away from target | Contrasting | Drama, noir |
| Confrontation | Opposing lines | Locked opposition | Forward lean | Action, western |
| Family | Scattered cluster | Dispersed | Mixed open/closed | Drama, comedy |

---

### EXAMPLE PROMPTS

**Power Pyramid:**
> Wide shot of corporate boardroom with five executives, CEO positioned at head of table in center-back of frame elevated by chair height, four subordinates flanking table sides in foreground creating triangular depth hierarchy, all subordinate eyelines directed toward CEO who looks forward past camera with controlled expression, deep focus keeping all subjects sharp to read body language, CEO in tailored dark suit while subordinates in varied business casual creating subtle status differentiation, architectural lines of boardroom converging toward CEO's position, cold overhead lighting creating pools of illumination on table surface, cinematic group composition communicating clear organizational hierarchy

**Broken Circle Outsider:**
> Medium wide shot of family dinner table, six family members clustered in warm golden light on left and center of frame laughing and interacting, one subject standing apart at right edge of frame separated by empty chair and negative space, outsider's body language closed with arms crossed while family members display open animated gestures, outsider's eyeline directed at family group with complex expression, warm tungsten on family contrasting with cooler window light on isolated figure, shallow depth of field keeping family sharp while outsider slightly softer, cinematic composition signaling exclusion and longing in single frame

---

### TECHNICAL NOTES FOR AI GENERATION
- Specify number of subjects explicitly for composition logic
- Use "center" or "elevated" for hierarchy; "edge" or "isolated" for outsider
- Include "eyelines" or "gaze direction" to create attention vectors
- Mention "body language" descriptors ("open", "closed", "mirrored")
- Use "depth staging" or "foreground/midground/background" for layered groups
- Specify "deep focus" if all subjects need to be readable; "shallow" for isolation
- Include architectural elements ("doorway", "staircase") for framing hierarchy
