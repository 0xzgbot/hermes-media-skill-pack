---
name: media-pipeline-workflow
description: "Build and debug multi-stage AI media pipelines."
version: 1.0.0
author: Hermes Agent community
created: 2026
tags: [pipeline, workflow, ai-media, batch-processing]
---

# Media Pipeline Workflow — General Purpose

## Pipeline Architecture Pattern

Every AI media pipeline follows this structure:

```
Input → Processing Stage N → Output → Next Stage Input
   ↓                              ↓
Validation                    Validation
```

### Standard Stages
1. **Ingestion** — Raw input (text prompt, reference image, script)
2. **Preprocessing** — Format conversion, normalization, validation
3. **Generation** — Core AI model execution (image/video/audio)
4. **Post-processing** — Upscaling, filtering, format conversion
5. **Quality check** — Automated or manual review against criteria
6. **Delivery** — Output to final destination (file system, API, CDN)

## Batch Processing Patterns

### Sequential Pipeline
```python
for item in batch:
    result = process(item)
    if not validate(result):
        retry_or_flag(result)
    save(result)
```
- Simple, predictable, easy to debug
- Slower — processes one at a time

### Parallel with Queue
```python
queue = asyncio.Queue()
for item in batch:
    await queue.put(item)

async def worker():
    while True:
        item = await queue.get()
        result = process(item)
        save(result)
        queue.task_done()
```
- Faster — processes multiple items concurrently
- Need rate limiting for API-based generation
- Better resource utilization

### Fan-Out/Fan-In
```python
# Split one input into N sub-tasks
subtasks = generate_subtasks(input)
results = await asyncio.gather(*[process(t) for t in subtasks])
final = merge_results(results)
```
- Best for: multi-angle generation, A/B testing variants, assembling final from parts

## Error Handling Patterns

### Retry with Backoff
```python
import time
for attempt in range(max_retries):
    try:
        result = generate(prompt)
        break
    except RateLimitError:
        wait = 2 ** attempt  # exponential backoff
        time.sleep(wait)
    except ValidationError:
        fix_prompt_and_retry()
        break
```

### Circuit Breaker (for external services)
- If service fails N times consecutively, stop trying for a cooldown period
- Prevents cascading failures and wasted compute
- Resume after cooldown with a health check

### Graceful Degradation
- Primary model fails → fallback to secondary model
- High-res generation fails → generate low-res as placeholder
- Always have a "minimum viable output" path

## Resource Management

### GPU/VRAM Considerations
- Batch size limited by available VRAM, not just speed
- Monitor memory usage — OOM kills are silent and wasteful
- Use lower precision (FP16/BF16) when quality allows
- Clear cache between large batches: `torch.cuda.empty_cache()`

### Rate Limiting
- Track API calls per minute/hour
- Add jitter to retry delays (don't all retry at same time)
- Queue items that exceed limits and process in next window

## Pipeline Monitoring Checklist

After running a pipeline, verify:
- [ ] All inputs were processed (count matches)
- [ ] No silent failures (check error logs)
- [ ] Output files exist and are valid (not empty/corrupt)
- [ ] Quality meets minimum threshold (spot check random samples)
- [ ] Timing is within expected range (flag unusually slow/fast runs)

## Common Pipeline Issues & Fixes

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| All outputs identical | Same seed, no variation in input | Add randomness or vary prompts slightly |
| Pipeline hangs mid-batch | Memory leak or stuck process | Monitor memory, add timeout per item |
| Quality degrades over time | Context window pollution | Reset state between batches |
| Rate limit errors | Too many concurrent requests | Reduce batch size, add delays |
| Output files corrupted | Write interrupted by crash | Use atomic writes (write to temp, then rename) |
