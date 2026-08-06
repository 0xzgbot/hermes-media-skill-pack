# Iterative Prompt Refinement: Logic Framework for Semantic Remediation

## 1. Error Taxonomy

Failures are classified by **domain** (what broke) and **severity** (how badly).

| Class | Error Type | Definition | Typical Trigger |
|-------|-----------|------------|-----------------|
| **Temporal** | `Temporal Drift` | Subject identity or environment changes discontinuously across frames. | Overly detailed descriptions without anchor tokens. |
| | `Motion Incoherence` | Physics-defying movement; unnatural acceleration or rigidity. | Ambiguous verb choice ("move quickly"). |
| **Anatomical** | `Anatomical Error` | Extra/missing limbs, impossible joints, or malformed features. | Dense attribute stacking on human figures. |
| | `Proportion Distortion` | Relative scale of body parts violates biological norms. | Conflicting size adjectives ("tiny head, massive eyes"). |
| **Photometric** | `Lighting Mismatch` | Light direction/color inconsistent with described environment. | Multiple unranked light sources. |
| | `Texture Flattening` | Loss of surface detail; everything appears matte or overly smooth. | Over-reliance on style keywords ("digital art"). |
| | `Color Bleed` | Unintended chromatic contamination across semantic boundaries. | Adjacent high-saturation descriptors without separators. |
| **Semantic** | `Semantic Overload` | Model ignores key elements because the prompt exceeds attention capacity. | >6 distinct entities with equal syntactic weight. |
| | `Concept Blending` | Two distinct concepts merge into an undesirable hybrid. | Parallel noun phrases without disambiguation. |
| | `Attribute Leakage` | A descriptor intended for entity A applies to entity B. | Pronoun ambiguity or parallel clause structure. |
| **Structural** | `Composition Collapse` | Violation of stated spatial relationships (e.g., "behind" ignored). | Complex prepositional stacking. |
| | `Depth Inconsistency` | Foreground/background relationships physically impossible. | Conflicting depth cues ("close-up" + "aerial view"). |

---

## 2. Refinement Protocols

Each protocol maps an error type to a **transformation function** over the prompt's Abstract Syntax Tree (AST). The engine treats prompts as structured data, not raw strings.

### Protocol A: Hierarchical Reconstruction (for `Semantic Overload`, `Composition Collapse`)

**Logic:** Restructure from flat description to ranked dependency tree.

```
Original:  "A wizard, a dragon, a castle, stormy night, lightning, flying, epic"
Refined:   "SUBJECT: ancient stone castle on cliff edge. 
            ACTION: lightning strikes the highest tower. 
            ENVIRONMENT: violent storm, night, heavy rain. 
            DETAIL[0.3]: distant silhouette of a flying dragon."
```

**Transformation Rules:**
- Enforce `Subject → Action → Environment → Detail` hierarchy.
- Move secondary entities to bracketed weight syntax (e.g., `[detail:0.3]`).
- Limit top-level entities to **3**.

---

### Protocol B: Token Weight Rebalancing (for `Texture Flattening`, `Lighting Mismatch`)

**Logic:** Increase salience of under-represented tokens via emphasis markers or positional priority.

```
Original:  "portrait of a knight, digital art, smooth lighting"
Refined:   "portrait of a knight, (intricate etched armor:1.4), 
            (volumetric candlelight from left:1.3), digital art"
```

**Transformation Rules:**
- Identify "style-dominant" tokens that may suppress detail.
- Apply scalar weights `(token:1.2–1.5)` to suppressed visual descriptors.
- Move style tokens to the **end** of the prompt (lower positional attention in most diffusion transformers).

---

### Protocol C: Negative Constraint Injection (for `Anatomical Error`, `Concept Blending`)

**Logic:** Replace ambiguous positive descriptors with explicit negative space definitions.

```
Original:  "a woman with six arms holding swords"
Refined:   "a woman holding two swords, perfect anatomy, 
            [negative: extra limbs, fused fingers, deformed hands]"
```

**Transformation Rules:**
- Detect anatomical impossibilities via ontology check.
- Convert impossible configurations into **positive constraints** ("two arms") + **negative prompts** ("extra limbs").
- Use descriptor replacement, not just addition: remove the cause, don't mask the symptom.

---

### Protocol D: Temporal Anchoring (for `Temporal Drift`, `Motion Incoherence`)

**Logic:** Inject identity-preserving anchor tokens and discretize motion.

```
Original:  "a fox running through a forest, changing seasons"
Refined:   "SEQUENCE[frame]: red fox with white-tipped tail, consistent fur pattern. 
            MOTION: galloping gait, paws contacting ground in cycle. 
            ENVIRONMENT: autumn forest, static tree positions across frames."
```

**Transformation Rules:**
- Extract `IDENTITY` tokens (unique, persistent descriptors) and prefix with `ANCHOR:`.
- Convert continuous verbs into discrete kinematic phases ("running" → "galloping gait, cyclic leg positions").
- Add `STATIC:` prefix to environmental elements that must not drift.

---

### Protocol E: Semantic Segregation (for `Attribute Leakage`, `Color Bleed`)

**Logic:** Bind attributes to specific entities using explicit scoping syntax.

```
Original:  "a red car and a blue house next to a green tree"
Refined:   "ENTITY[car]{color:red, metallic paint}, 
            ENTITY[house]{color:blue, two-story}, 
            ENTITY[tree]{color:green, deciduous}, 
            RELATION[house, tree]{adjacent}"
```

**Transformation Rules:**
- Parse ambiguous adjective-noun bindings.
- Reformat into scoped blocks or use separator tokens (`BREAK`, `AND`).
- Ensure color/texture adjectives are within **3 tokens** of their target noun.

---

## 3. Feedback Loops: Correction Payload Specification

The auditor agent outputs a **Correction Payload**—a Markdown report consumed by the remediation engine. Below is the schema and a sample.

### Payload Schema

```markdown
## Correction Payload
| Field | Value |
|-------|-------|
| `payload_id` | UUID-v4 |
| `timestamp` | ISO-8601 |
| `asset_type` | IMAGE / VIDEO / 3D |
| `failure_severity` | CRITICAL / MAJOR / MINOR |

### Correction Items
| Failure Type | Current Prompt Segment | Suggested Correction | Reasoning | Protocol Applied |
|--------------|------------------------|----------------------|-----------|------------------|
| ... | ... | ... | ... | ... |
```

### Sample Payload

```markdown
## Correction Payload
| Field | Value |
|-------|-------|
| `payload_id` | `a1b2-c3d4-e5f6-7890` |
| `timestamp` | `2026-04-20T12:20:00Z` |
| `asset_type` | VIDEO |
| `failure_severity` | MAJOR |

### Correction Items

| Failure Type | Current Prompt Segment | Suggested Correction | Reasoning | Protocol Applied |
|--------------|------------------------|----------------------|-----------|------------------|
| Temporal Drift | `"a character walking through a market, crowd, colorful stalls, changing time of day"` | `ANCHOR: protagonist with scar on left cheek, brown cloak. ENVIRONMENT: bustling market with static stall positions. TIME: locked to golden hour.` | Unanchored subject description allows facial features and clothing to mutate across frames. The "changing time of day" directive directly contradicts temporal consistency. | Protocol D |
| Semantic Overload | `"crowd, colorful stalls, changing time of day"` | `DETAIL[0.3]: background crowd. DETAIL[0.2]: market stalls with striped awnings.` | Three competing scene descriptors dilute attention. Demoting to weighted details preserves presence without overwhelming the subject. | Protocol A |
| Lighting Mismatch | `"changing time of day"` | `(warm golden-hour sidelight from west:1.3), [negative: cool tones, overhead lighting]` | Temporal lighting shift creates photometric inconsistency across the sequence. Locking a specific light vector stabilizes rendering. | Protocol B |
```

---

## 4. Python Remediation Engine: Logic Guide

The following structures are designed to be directly implemented. The engine operates on a `PromptNode` graph.

```python
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Dict

class ErrorClass(Enum):
    TEMPORAL = auto()
    ANATOMICAL = auto()
    PHOTOMETRIC = auto()
    SEMANTIC = auto()
    STRUCTURAL = auto()

class RefinementProtocol(Enum):
    HIERARCHICAL_RECONSTRUCTION = "A"
    TOKEN_WEIGHT_REBALANCING = "B"
    NEGATIVE_CONSTRAINT_INJECTION = "C"
    TEMPORAL_ANCHORING = "D"
    SEMANTIC_SEGREGATION = "E"

class Severity(Enum):
    CRITICAL = 3  # Must fix; block generation
    MAJOR = 2     # Should fix; retry once
    MINOR = 1     # Optional fix; log only

@dataclass
class PromptNode:
    """AST node for prompt decomposition."""
    node_type: str  # SUBJECT, ACTION, ENVIRONMENT, DETAIL, STYLE
    content: str
    weight: float = 1.0
    children: List['PromptNode'] = field(default_factory=list)
    negative: bool = False

@dataclass
class FailureReport:
    """Input from quality-check auditor."""
    error_type: str           # e.g., "Temporal Drift"
    error_class: ErrorClass
    severity: Severity
    affected_segment: str     # The substring in the original prompt
    visual_evidence: str      # Description of the artifact

@dataclass
class CorrectionItem:
    """Single row in the Correction Payload."""
    failure_type: str
    current_segment: str
    suggested_correction: str
    reasoning: str
    protocol: RefinementProtocol
    confidence: float  # 0.0–1.0 from the LLM auditor

@dataclass
class RemediationPlan:
    """Output of the refinement engine."""
    original_prompt: str
    corrected_prompt: str
    corrections: List[CorrectionItem]
    protocol_stack: List[RefinementProtocol]  # Ordered application sequence

# ── Engine Core Logic ──────────────────────────────────────────────

PROTOCOL_MAP: Dict[str, RefinementProtocol] = {
    "Temporal Drift": RefinementProtocol.TEMPORAL_ANCHORING,
    "Motion Incoherence": RefinementProtocol.TEMPORAL_ANCHORING,
    "Anatomical Error": RefinementProtocol.NEGATIVE_CONSTRAINT_INJECTION,
    "Proportion Distortion": RefinementProtocol.NEGATIVE_CONSTRAINT_INJECTION,
    "Lighting Mismatch": RefinementProtocol.TOKEN_WEIGHT_REBALANCING,
    "Texture Flattening": RefinementProtocol.TOKEN_WEIGHT_REBALANCING,
    "Color Bleed": RefinementProtocol.SEMANTIC_SEGREGATION,
    "Semantic Overload": RefinementProtocol.HIERARCHICAL_RECONSTRUCTION,
    "Concept Blending": RefinementProtocol.SEMANTIC_SEGREGATION,
    "Attribute Leakage": RefinementProtocol.SEMANTIC_SEGREGATION,
    "Composition Collapse": RefinementProtocol.HIERARCHICAL_RECONSTRUCTION,
    "Depth Inconsistency": RefinementProtocol.HIERARCHICAL_RECONSTRUCTION,
}

def generate_remediation_plan(
    original_prompt: str,
    failures: List[FailureReport]
) -> RemediationPlan:
    """
    1. Sort failures by Severity (CRITICAL first).
    2. Deduplicate protocols (apply each protocol at most once per pass).
    3. Transform PromptNode AST according to protocol rules.
    4. Serialize AST back to string.
    5. Emit CorrectionItems for audit trail.
    """
    failures.sort(key=lambda f: f.severity.value, reverse=True)
    
    corrections: List[CorrectionItem] = []
    applied_protocols: List[RefinementProtocol] = []
    ast = parse_prompt_to_ast(original_prompt)  # User-implemented parser
    
    for failure in failures:
        protocol = PROTOCOL_MAP.get(failure.error_type)
        if not protocol:
            continue
            
        if protocol not in applied_protocols:
            ast = apply_protocol(ast, protocol, failure)
            applied_protocols.append(protocol)
        
        corrections.append(CorrectionItem(
            failure_type=failure.error_type,
            current_segment=failure.affected_segment,
            suggested_correction=extract_segment(ast, failure.affected_segment),
            reasoning=f"Detected {failure.error_type} in segment. "
                      f"Protocol {protocol.value} restructures attention.",
            protocol=protocol,
            confidence=0.85  # Placeholder; LLM auditor provides this
        ))
    
    return RemediationPlan(
        original_prompt=original_prompt,
        corrected_prompt=serialize_ast(ast),
        corrections=corrections,
        protocol_stack=applied_protocols
    )

# ── Protocol Transformers (Stubs) ──────────────────────────────────

def apply_protocol(ast: PromptNode, protocol: RefinementProtocol, failure: FailureReport) -> PromptNode:
    if protocol == RefinementProtocol.HIERARCHICAL_RECONSTRUCTION:
        return enforce_subject_action_env_hierarchy(ast)
    elif protocol == RefinementProtocol.TOKEN_WEIGHT_REBALANCING:
        return rebalance_token_weights(ast, failure.affected_segment, scale=1.3)
    elif protocol == RefinementProtocol.NEGATIVE_CONSTRAINT_INJECTION:
        return inject_negative_constraints(ast, failure.affected_segment)
    elif protocol == RefinementProtocol.TEMPORAL_ANCHORING:
        return anchor_identity_tokens(ast)
    elif protocol == RefinementProtocol.SEMANTIC_SEGREGATION:
        return scope_attributes_to_entities(ast)
    return ast

# Implementations of the above transformers are domain-specific
# and depend on the generative model's tokenizer/attention mechanism.
```

---

## 5. Operational Constraints for the Engine

| Constraint | Rationale |
|------------|-----------|
| **Max 3 protocols per pass** | Over-correction introduces new artifacts. Queue remaining fixes for Pass 2. |
| **Never modify `ANCHOR` tokens** | Identity tokens, once fixed, are immutable across the remediation loop. |
| **Preserve original token count ±20%** | Prevents prompt length from exceeding model context or attention window. |
| **Log all negative constraints** | Negative prompts can suppress desired features; require auditor review if >3. |
| **Halt after 5 iterations** | Prevent infinite loops on fundamentally underspecified prompts. |

This framework treats prompt refinement as a **deterministic transformation over structured syntax**, not as open-ended rewriting. The LLM auditor's role is to classify failures and justify corrections; the engine's role is to apply validated transformations reliably and reversibly.