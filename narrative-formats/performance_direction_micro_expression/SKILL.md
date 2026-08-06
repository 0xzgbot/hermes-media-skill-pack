# SKILL: Performance Direction & Micro-Expressions
## Version: 1.0 | Hermes Agent AI Actor Direction

---

### DESCRIPTION
Mastery of directing AI-generated performers through precise facial expression, micro-emotion, gesture vocabulary, and physical acting notes. This skill treats the generative model as a digital actor that requires specific direction — not just "happy" or "sad" but the exact muscular configuration of emotion. Essential for campaigns where human performance carries narrative weight: testimonials, dramas, character pieces, and any content requiring authentic emotional specificity.

---

### TECHNICAL PARAMETERS

**The Facial Action Coding System (FACS) for AI:**
- **AU1 + AU2 (Inner + Outer Brow Raiser):** Surprise, fear, interest
- **AU4 (Brow Lowerer):** Anger, concentration, confusion
- **AU6 + AU7 (Cheek Raiser + Lid Tightener):** Genuine joy (Duchenne smile), pain
- **AU9 (Nose Wrinkler):** Disgust, contempt, skepticism
- **AU12 (Lip Corner Puller):** Social smile (may be false)
- **AU15 (Lip Corner Depressor):** Sadness, disappointment
- **AU20 (Lip Stretcher):** Fear, grimace, tense smile
- **AU25 + AU26 (Lips Part + Jaw Drop):** Surprise, awe, shock
- **AU43 (Eyes Closed):** Pain, pleasure, avoidance, sleep

**The Duchenne vs. Social Smile:**
- **Duchenne (Genuine):** AU6 + AU12 — crow's feet at eyes, cheek raise, symmetrical
- **Social (Performed):** AU12 only — mouth moves, eyes static, potentially asymmetrical
- **Prompt Signal:** Use "genuine smile with eye crinkles" vs "polite social smile"

**Micro-Expression Library:**

| Micro-Expression | Duration | Facial Signature | Emotional Truth |
|-----------------|---------|------------------|-----------------|
| **Flash Contempt** | 1/5 second | One-sided lip raise, slight nose wrinkle | Hidden superiority, disdain |
| **Suppressed Fear** | 1/4 second | Brief brow raise + eye white show + lip stretch | Masked anxiety, pretending calm |
| **Leakage Disgust** | 1/5 second | Quick nose wrinkle before neutral mask | Hidden revulsion, moral judgment |
| **Surprise Suppression** | 1/4 second | Brow raise + lid widening cut short | Concealed shock, poker face failing |
| **Grief Micro-Burst** | 1/3 second | Lip corner drop + chin raise + eye softening | Sudden sadness breaking through |
| **Anger Flash** | 1/5 second | Brow lower + lip press + jaw set before relaxing | Controlled rage, boundary crossed |

**Gaze Direction Vocabulary:**
- **Direct to Lens:** Confrontation, intimacy, breaking fourth wall, testimony
- **Slightly Down:** Shyness, submission, introspection, calculation
- **Slightly Up:** Hope, aspiration, prayer, remembering
- **Far Focus:** Memory, dissociation, watching something distant
- **Unfocused:** Shock, exhaustion, drugged, dream state
- **Side Glance:** Suspicion, jealousy, eavesdropping, desire
- **Eyes Closed:** Pain, ecstasy, avoidance, sleep, deep breath

---

### PROMPT ARCHITECTURE

**Core Prompt Template:**
```
[Portrait / medium shot / close-up] of [subject],
[expression: specific muscular configuration],
[gaze direction and focus],
[head angle: chin up / chin down / tilted / level],
[micro-expression detail: eye behavior, lip tension, brow position],
[emotional register: surface emotion vs. underlying truth],
[context: what just happened / what is about to happen],
photorealistic skin texture, natural asymmetry,
specific performance direction, cinematic acting
```

**Negative Prompts:**
```
generic smile, blank expression, symmetrical perfect face, mannequin look,
posed expression, frozen face, no emotional specificity, doll-like eyes,
stock photo expression, overly happy, default neutral, no subtext
```

---

### ADVANCED TECHNIQUES

**1. The Conflicted Smile**
- Mouth: Lip corners up (AU12) but pressed tight (AU24)
- Eyes: No cheek raise (no AU6) — eyes tell the truth
- Brow: Slightly lowered (AU4) — tension, concern
- Gaze: Slightly away from lens — avoiding direct confrontation
- Emotional: Social obligation masking inner turmoil
- Best For: Corporate testimonials, family tension, polite lies

**2. The Breakthrough Tear**
- Onset: Eyes suddenly soft, lid margin reddens
- Transition: One tear wells at lower lid, catches light
- Expression: Mix of relief and grief — lip corners down but jaw released
- Gaze: Up and away — accessing memory or higher power
- Emotional: Catharsis, long-held pain finally surfacing
- Best For: Testimonials, redemption stories, emotional climax

**3. The Calculating Look**
- Eyes: Narrowed slightly, focused, direct
- Brow: Lowered and drawn together (AU4)
- Mouth: Lips pressed, possible slight asymmetrical raise (contempt)
- Head: Slight forward tilt — engagement, assessment
- Micro: Brief side glance before locking back to target
- Emotional: Intelligence, strategy, hidden agenda
- Best For: Thrillers, business narratives, competitive stories

**4. The Vulnerable Openness**
- Eyes: Wide, soft focus, slight moisture
- Brow: Raised inner corners (AU1) — appeal, need
- Mouth: Slightly parted (AU25), relaxed, no tension
- Head: Chin slightly down, throat exposed
- Gaze: Direct to lens — brave honesty, asking for trust
- Emotional: Naked authenticity, begging understanding
- Best For: Charity, health stories, coming-out narratives, apology

**5. The Controlled Rage**
- Eyes: Hard, fixed, slightly widened
- Brow: Deeply lowered (AU4), vertical crease between
- Jaw: Set, masseter visible, slight forward thrust
- Mouth: Lips pressed white (AU24), corners down
- Breath: Nostrils slightly flared (AU38)
- Micro: Brief lip corner raise (contempt) before locking down
- Emotional: Fury held by thread, about to snap
- Best For: Dramatic confrontation, injustice, betrayal, action

---

### GESTURE & POSTURE DIRECTION

| Gesture | Meaning | Prompt Term |
|---------|---------|-------------|
| Hand on chest | Sincerity, vulnerability, self-reference | "hand on heart" |
| Touching face | Deception, thought, uncertainty | "finger to lips" |
| Open palms | Honesty, submission, offering | "palms open upward" |
| Crossed arms | Defense, resistance, self-protection | "arms folded" |
| Hand in hair | Flirtation, stress, distraction | "hand running through hair" |
| Pointing finger | Accusation, emphasis, direction | "pointing gesture" |
| Clenched fist | Anger, determination, solidarity | "fist clenched at side" |
| Hand over mouth | Suppressed reaction, shock, secrecy | "hand covering mouth" |

---

### EXAMPLE PROMPTS

**Conflicted Corporate Testimonial:**
> Close-up portrait of professional man, conflicted smile with lip corners raised but pressed tight showing social obligation, eyes not participating in smile — no cheek raise, slight brow tension suggesting underlying concern, gaze slightly off-camera avoiding direct confrontation, hand resting awkwardly on lapel, subtle jaw tension, photorealistic skin with natural asymmetry, corporate office background softly blurred, cinematic acting direction, emotional subtext of polite performance

**Breakthrough Catharsis:**
> Extreme close-up of woman's face, breakthrough emotional moment, eyes suddenly softened with lower lid reddening, single tear catching light at inner corner, lip corners slightly down in grief but jaw released in relief, gaze directed upward and away accessing memory, brow inner corners raised in appeal, skin texture showing pore detail and natural flush, vulnerable throat visible with chin slightly down, cinematic emotional climax, authentic human performance

---

### TECHNICAL NOTES FOR AI GENERATION
- Use specific muscular language: "cheek raise", "brow lower", "lip press"
- Distinguish genuine from social: "eye crinkles" vs "mouth-only smile"
- Gaze direction is crucial — specify precisely where eyes look
- Head angle communicates psychology: chin up = pride/defiance, chin down = submission/shyness
- For FLUX: describe facial muscles in positive detail; no negative prompts
- For LTX: specify "stable facial expression across frames" as guardrail
- Asymmetry is key to realism — mention "natural slight asymmetry"
- Context helps: "expression of someone who just received bad news but must perform"
