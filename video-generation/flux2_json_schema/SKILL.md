---
name: flux2_json_schema
description: "Build type-safe Flux.2 JSON payloads for ComfyUI."
version: 1.1.0
author: 0xzgbot, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [video-generation, media, cinematic]
    category: video-generation
---

Search for up-to-date info on 2026 models and ComfyUI implementations














I'll research the current state of these models and their ComfyUI implementations to provide you with accurate, production-ready schemas.

Search
FLUX 2 Dev ComfyUI workflow JSON schema 2026 Wan 2.1 LTX Video 2.3 ComfyUI node parameters temporal consistency ZImage Turbo fast image generation ComfyUI workflow
20 results


Designing JSON Schemas for ComfyUI Qwen 3B and Wan 2 Video Nodes

































Search
Wan 2.1 ComfyUI node parameters seed motion strength frame interpolation LTX Video 2.3 ComfyUI workflow JSON STG spatio-temporal guidance node
13 results


Production JSON Schemas and the FLUX 2 Text Rendering Fix


























































Here is the technical deep-dive for the production engine. These schemas are designed for the Router → Dispatcher → Remediation loop, with each payload being machine-executable by ComfyUI nodes across your GPU hosts.

1. Architecture Philosophy
The core design principle is semantic isolation: cinematic intent is decomposed into non-conflicting instruction planes before JSON serialization. The Router layer assembles high-level intent into model-specific dialects; the Dispatcher validates node compatibility; the Remediation loop adjusts guidance parameters based on artifact detection.

2. FLUX 2 Dev — Image Generation Schema
FLUX 2 Dev supports native JSON-structured prompting with precise color control and multi-reference capabilities . To prevent text-rendering artifacts, typography instructions must be strictly isolated from visual scene descriptions. When text content bleeds into visual conditioning, the Mistral 3 text encoder can over-activate glyph-rendering pathways, producing garbled or "melted" text .
2.1 Optimal Payload Structure
JSON

Copy
{
  "metadata": {
    "model_host": "flux2-dev-01",
    "job_id": "img-uuid",
    "remediation_count": 0,
    "priority": "high"
  },
  "visual_blueprint": {
    "scene": {
      "type": "Cinematic Exterior",
      "environment": "Neon-drenched cyberpunk alleyway, rain-slicked cobblestones",
      "time_of_day": "Blue Hour",
      "atmospheric_conditions": "Light fog, volumetric god-rays from signage"
    },
    "subjects": [
      {
        "id": "subject_01",
        "description": "Figure in worn leather trench coat, back to camera",
        "position": "Center foreground, rule of thirds intersection",
        "color_palette": ["#FF2A6D", "#05D9E8", "#01012B"],
        "material_properties": "Wet leather reflectivity, subsurface scattering on skin"
      }
    ],
    "lighting": {
      "key_light": "Neon pink rim light from signage, 45° behind subject",
      "fill_light": "Cyan ambient bounce from wet ground",
      "contrast_ratio": "High, 8:1"
    },
    "style": {
      "rendering_engine": "Photorealistic cinematic",
      "film_stock": "Kodak Vision3 500T",
      "quality_modifiers": ["8K UHD", "chromatic aberration subtle", "lens flare organic"]
    }
  },
  "camera_motion": {
    "rig_type": "Static Lock",
    "angle": "Low angle, 15° Dutch tilt",
    "lens_mm": 35,
    "f_number": "f/1.4",
    "focus_distance": "2.1m",
    "depth_of_field": "Shallow, bokeh hexagonal",
    "motion_blur": "Optical flow, 1/48s shutter simulation"
  },
  "typography_isolation": {
    "enabled": true,
    "text_elements": [
      {
        "content": "NIGHT CITY",
        "position": "Background signage, out of focus",
        "font_style": "Bold sans-serif, neon tube",
        "color": "#FF2A6D",
        "render_priority": "ambient_only"
      }
    ],
    "text_negative_prompt": "gibberish text, blurry letters, melted typography, watermark"
  },
  "comfyui_node_mapping": {
    "model_loader": {
      "node_id": "UNETLoader",
      "model_path": "flux2-dev-fp8.safetensors",
      "weight_dtype": "fp8_e4m3fn"
    },
    "text_encoder": {
      "node_id": "CLIPTextEncode",
      "encoder_type": "mistral3",
      "conditioning_strategy": "structured_json"
    },
    "sampler": {
      "node_id": "KSampler",
      "sampler_name": "euler",
      "scheduler": "simple",
      "steps": 28,
      "cfg": 3.5,
      "denoise": 1.0
    },
    "resolution": {
      "width": 2048,
      "height": 1152,
      "batch_size": 1
    }
  }
}

2.2 Cinematic Attribute → ComfyUI Node Mapping
Table


Cinematic Attribute
ComfyUI Node
Parameter
Value Range / Notes
Lens Choice
FLUX2_CameraRig 
lens_mm
24, 35, 50, 85, 135
Depth of Field
FLUX2_CameraRig 
f-number
f/1.2–f/22; maps to optical conditioning
Camera Angle
FLUX2_CameraRig 
angle
Low/high/Dutch tilt; injected as prefix
Color Palette
FLUX2_PromptAssembler 
color_palette
Hex array; FLUX 2 parses HTML codes natively 
Lighting Key
FLUX2_PromptAssembler 
lighting
Separated to prevent style bleed
Text Rendering
Isolated CLIPTextEncode
typography_isolation
Dedicated negative prompt plane
Prompt Adherence
KSampler
cfg
3.0–4.0 optimal for FLUX 2 
2.3 Anti-Artifact Strategy
To prevent text-rendering artifacts:
Isolate text elements in the typography_isolation object, never in visual_blueprint.scene
Use render_priority: "ambient_only" to force text into bokeh/background planes
Apply a dedicated text negative prompt to the secondary CLIP encode node
Keep CFG ≤ 3.5 to avoid over-saturating glyph pathways

3. Wan 2.1 & LTX 2.3 — Video / I2V Schema
Video models require temporal consistency anchors to prevent flicker and drift. Wan 2.1 uses a spatio-temporal VAE , while LTX 2.3 exposes independent Spatio-Temporal Guidance (STG) and cross-modal sync controls via the Multimodal Guider .
3.1 Wan 2.1 Payload
JSON

Copy
{
  "metadata": {
    "model_host": "wan21-video-01",
    "job_id": "vid-uuid",
    "pipeline_type": "i2v",
    "remediation_count": 0
  },
  "temporal_consistency_anchors": {
    "seed": 42,
    "seed_strategy": "fixed_per_generation",
    "motion_strength": 0.72,
    "motion_strength_range": [0.3, 1.0],
    "frame_interpolation": {
      "enabled": true,
      "target_fps": 24,
      "source_fps": 16,
      "interpolator": "RIFE_VFI",
      "interpolation_multiplier": 1.5
    },
    "spatio_temporal_vae": {
      "tile_size": 32,
      "temporal_window": 16
    }
  },
  "motion_vectors": {
    "camera_movement": [
      {
        "type": "dolly_in",
        "start_frame": 0,
        "end_frame": 48,
        "velocity_curve": "ease_in_out",
        "magnitude": 0.4
      },
      {
        "type": "pan_right",
        "start_frame": 24,
        "end_frame": 72,
        "velocity_curve": "linear",
        "magnitude": 0.25
      }
    ],
    "subject_motion": [
      {
        "subject_id": "subject_01",
        "action": "turning_to_face_camera",
        "start_frame": 32,
        "end_frame": 64
      }
    ]
  },
  "visual_texture_prompts": {
    "scene_description": "Cinematic interior, art deco ballroom, golden hour through stained glass",
    "material_textures": [
      {
        "surface": "Marble floor",
        "properties": "Polished Carrara, soft reflections, caustics"
      },
      {
        "surface": "Velvet curtains",
        "properties": "Deep burgundy, pile texture, light absorption"
      }
    ],
    "lighting_texture": "Warm tungsten practicals, volumetric dust particles, soft shadows"
  },
  "negative_visual_textures": {
    "artifacts": ["flicker", "sudden lighting changes", "texture popping", "watermark"]
  },
  "comfyui_node_mapping": {
    "model_loader": {
      "node_id": "WanVideoModelLoader",
      "model_path": "wan2.1-i2v-720p-fp8.safetensors"
    },
    "image_conditioning": {
      "node_id": "WanVideoClipVisionEncode",
      "start_frame": "input_image.png",
      "vision_model": "clip_vision_h"
    },
    "sampler": {
      "node_id": "WanVideoSampler",
      "sampler_name": "uni_pc",
      "scheduler": "simple",
      "steps": 25,
      "cfg": 6.0,
      "num_frames": 81
    },
    "decode": {
      "node_id": "WanVideoVAEDecode",
      "tile_size": 32
    }
  }
}

3.2 LTX 2.3 Payload
JSON

Copy
{
  "metadata": {
    "model_host": "ltx23-video-02",
    "job_id": "vid-uuid",
    "pipeline_type": "t2v",
    "remediation_count": 0
  },
  "temporal_consistency_anchors": {
    "seed": 42,
    "frame_rate": 30,
    "num_frames": 121,
    "resolution": {
      "width": 1280,
      "height": 704
    }
  },
  "motion_vectors": {
    "camera_movement": [
      {
        "type": "slow_zoom_in",
        "easing": "smooth",
        "description": "Camera gently pushes forward through tree canopy"
      }
    ],
    "environmental_motion": [
      {
        "type": "wind_through_leaves",
        "intensity": "moderate",
        "description": "Dappled sunlight shifts across forest floor"
      }
    ]
  },
  "visual_texture_prompts": {
    "scene": "Ancient redwood forest, morning mist, god-rays piercing canopy",
    "textures": {
      "bark": "Deep furrowed sequoia bark, mossy patches, damp",
      "foliage": "Fern undergrowth, dewdrops, subsurface scattering on leaves",
      "atmosphere": "Volumetric fog, pollen motes, anamorphic light streaks"
    }
  },
  "multimodal_guider": {
    "video_guidance": {
      "cfg": 3.0,
      "stg": 1.0,
      "cross_modal_sync": 2.5
    },
    "audio_guidance": {
      "cfg": 7.0,
      "stg": 0.0,
      "cross_modal_sync": 2.5
    },
    "optimization": {
      "video_skip_step": 0,
      "audio_skip_step": 1
    }
  },
  "comfyui_node_mapping": {
    "text_encoder": {
      "node_id": "GemmaAPITextEncode",
      "api_fallback": "local_gemma",
      "prompt": "motion_prompt_only"
    },
    "guider": {
      "node_id": "MultimodalGuider",
      "parameters": "GUIDER_PARAMETERS"
    },
    "sampler": {
      "node_id": "LTXVTextToVideoSampler",
      "steps": 40,
      "strength": 1.0
    },
    "conditioning_cache": {
      "save_node": "LTXVSaveConditioning",
      "load_node": "LTXVLoadConditioning",
      "reuse_across_remediation": true
    }
  }
}

3.3 Cinematic Attribute → ComfyUI Node Mapping
Table


Cinematic Attribute
ComfyUI Node
Parameter
Value Range / Notes
Motion Strength
WanVideoSampler
cfg
5.0–7.0; lower reduces flicker 
Frame Interpolation
RIFE VFI (post)
multiplier
1.5× (16→24fps) or 2× 
Temporal Smoothing
MultimodalGuider 
cross_modal_sync
2.0–3.5; increases frame coherence 
Artifact Reduction
MultimodalGuider 
stg
0.5–1.5; Spatio-Temporal Guidance
Prompt Adherence
MultimodalGuider 
cfg
2.0–5.0 for video; 3.0 default 
Motion Description
GemmaAPITextEncode 
prompt
Motion-only; scene assumed in I2V
Conditioning Reuse
LTXVSaveConditioning 
cache_path
Saves seconds per remediation pass
3.4 Motion Vector / Visual Texture Isolation
To prevent motion vectors from conflicting with visual texture prompts:
Wan 2.1: Use WanVideoSampler with motion prompts in the positive conditioning; keep texture descriptions in the start-frame image embedding via WanVideoClipVisionEncode . The spatio-temporal VAE handles the merge .
LTX 2.3: Motion prompts go through GemmaAPITextEncode as pure action descriptions ("camera pans left, water ripples") . Visual textures are either baked into the I2V start image or described in the scene prompt, never mixed with motion verbs.
Never describe texture in motion prompts — e.g., say "gentle push forward" not "push forward revealing rough bark texture."

4. ZImage Turbo — Fast-Track Schema
ZImage Turbo is a distilled 6B-parameter S3-DiT model optimized for 8-step generation . The minimal viable payload must enforce the Lumina 2 CLIP type and Qwen 3B encoder to prevent black images and text corruption .
4.1 Minimal Viable Payload
JSON

Copy
{
  "metadata": {
    "model_host": "zimage-turbo-01",
    "job_id": "fast-uuid",
    "track": "rapid_prototype",
    "max_latency_ms": 15000
  },
  "semantic_payload": {
    "positive_prompt": "Cinematic portrait, warrior queen, Rembrandt lighting, bronze armor, ember particles, shallow depth of field, 85mm lens",
    "negative_prompt": "blurry, deformed, extra limbs, oversaturated, watermark, text",
    "text_rendering": null
  },
  "sampler_config": {
    "steps": 8,
    "cfg": 3.5,
    "sampler_name": "dpmpp_sde",
    "scheduler": "ddim_uniform",
    "denoise": 1.0
  },
  "aura_flow": {
    "shift": 3.0,
    "shift_range": [2.0, 5.0],
    "note": "Higher shift increases composition creativity but may wash out detail [^2^]"
  },
  "comfyui_node_mapping": {
    "model_loader": {
      "node_id": "UNETLoader",
      "model_path": "z_image_turbo_fp8.safetensors",
      "weight_dtype": "fp8_e4m3fn"
    },
    "clip_config": {
      "node_id": "CLIPLoader",
      "type": "lumina2",
      "encoder_path": "qwen_3_4b.safetensors"
    },
    "sampling": {
      "node_id": "ModelSamplingAuraFlow",
      "shift": 3.0
    },
    "latent": {
      "node_id": "EmptySD3LatentImage",
      "width": 1024,
      "height": 1024
    },
    "decode": {
      "node_id": "VAEDecode"
    }
  }
}

4.2 Cinematic Attribute → ComfyUI Node Mapping
Table


Cinematic Attribute
ComfyUI Node
Parameter
Value Range / Notes
Speed vs Quality
UNETLoader 
model_path
z_image_turbo_fp8 (fast) vs z_image_base_bf16 (quality)
Prompt Adherence
KSampler 
cfg
3.0–5.0; 3.5 is the sweet spot
Composition Control
ModelSamplingAuraFlow 
shift
3.0 default; 5.0+ for creative composition 
Text Rendering
CLIPLoader 
type
Must be lumina2; Qwen 3B encoder
Step Count
KSampler 
steps
Exactly 8 for Turbo; 30–50 for Base
Sampler Choice
KSampler 
sampler_name
dpmpp_sde for detail; euler for speed

5. Router → Dispatcher → Remediation Integration
5.1 Router Logic
The Router selects the schema based on intent_type:
Table


Intent
Schema
Host Selection Criteria
cinematic_still
FLUX 2 Dev
≥16GB VRAM, FP8 support
motion_sequence
Wan 2.1 / LTX 2.3
≥24GB VRAM, temporal VAE available
rapid_prototype
ZImage Turbo
Any available host, <15s SLA
5.2 Dispatcher Validation
Before dispatch, validate:
Node existence: Check comfyui_node_mapping against host node registry
VRAM estimation: FLUX 2 (12GB+), LTX 2.3 13B (24GB+), ZImage (8GB+) 
CLIP compatibility: ZImage requires lumina2; LTX requires gemma
5.3 Remediation Triggers
Table


Artifact Detected
Remediation Action
Parameter Adjustment
Text gibberish (FLUX 2)
Isolate typography
Increase typography_isolation strictness; reduce CFG 0.5
Flicker (Wan 2.1)
Reduce guidance
Decrease cfg by 1.0; enable frame interpolation 
Jittery motion (LTX 2.3)
Increase cross-modal sync
Raise cross_modal_sync to 3.0; reduce cfg to 2.5 
Washed out (ZImage)
Reduce AuraFlow shift
Lower shift from 7.0 to 3.0; switch to dpmpp_sde 
Black output (ZImage)
Fix CLIP config
Force type: lumina2 and FP8 checkpoint 
5.4 Conditioning Cache for Remediation
For LTX 2.3, always enable LTXVSaveConditioning on the first pass. During remediation, the Dispatcher loads cached conditioning via LTXVLoadConditioning instead of re-encoding, saving seconds per iteration .

6. Summary Table: Cross-Model Cinematic Mapping
Table


Cinematic Intent
FLUX 2 Dev Node
Wan 2.1 Node
LTX 2.3 Node
ZImage Turbo Node
Lens / Focal Length
FLUX2_CameraRig.lens_mm 
N/A (static or motion curve)
N/A
N/A (prompt only)
Aperture / DoF
FLUX2_CameraRig.f-number 
N/A
N/A
N/A
Camera Motion
FLUX2_CameraRig.angle 
motion_vectors.camera_movement
motion_vectors.camera_movement
N/A
Lighting
FLUX2_PromptAssembler.lighting 
visual_texture_prompts.lighting_texture
visual_texture_prompts.textures
Prompt prefix
Temporal Consistency
N/A
temporal_consistency_anchors + spatio-temporal VAE 
MultimodalGuider.cross_modal_sync 
N/A
Motion Strength
N/A
KSampler.cfg (5–7) 
MultimodalGuider.cfg (2–5) 
N/A
Frame Interpolation
N/A
RIFE VFI post-process 
Native 30–50fps 
N/A
Text Rendering
typography_isolation 
Negative prompt
Negative prompt
Native bilingual 
Fast Iteration
N/A
N/A
Distilled: 4–8 steps 
8 steps, FP8 
These schemas provide the production engine with type-safe, model-specific dialects that map directly to ComfyUI node parameters while preserving cinematic intent across the distributed GPU farm.
