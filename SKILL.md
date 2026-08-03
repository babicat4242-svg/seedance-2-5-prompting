---
name: seedance-2-5-prompting
description: Use when writing, reviewing, or repairing prompts for Seedance 2.5, 씨댄스 2.5, Seedance 2.0 Fast, 씨댄스 2.0 패스트, the latest Seedance workflow, 30-second generation, 15-second Fast generation, R2V, white-model or green-screen references, localized video edits, multimodal reference packs, or camera-motion control; also use for version-unspecified current Seedance prompt requests, while other explicit Seedance 2.0 legacy requests stay on the 2.0 skill.
---

# Seedance 2.5 Prompting

## Core principle

Treat a Seedance 2.5 or explicit Seedance 2.0 Fast prompt as a compact director's brief with explicit reference roles, readable beat timing, separate subject and camera motion, and a defined final frame. Preserve exact user/UI reference tags. Describe controllable intent; do not promise literal reproduction, frame-perfect timing, or hidden controls.

## Version routing

Use this skill for Seedance 2.5, the latest/current Seedance, an unspecified Seedance prompt, or a request that explicitly names Seedance 2.0 Fast. For explicit Seedance 2.0 Fast, select the custom Fast profile below. Treat that profile as a local authoring convention, not a public or official model specification. Route every other explicit Seedance 2.0 or legacy request to the 2.0 skill; duration alone never selects Fast. If the version is genuinely ambiguous and changes the prompt materially, state the 2.5 assumption once and proceed.

## Load references selectively

- Read [references/model-differences.md](references/model-differences.md) for feature, limit, beta, 2.0-versus-2.5, or UI questions.
- Read [references/camera-motion.md](references/camera-motion.md) for any non-static camera, camera repair, R2V path, or camera vocabulary request.
- Read [references/prompt-patterns.md](references/prompt-patterns.md) for generation, rewrite, mode selection, local edit, extension, or full prompt output.
- Read [references/sources.md](references/sources.md) when a claim needs verification or official attribution.
- Read [references/community-api-prompts-analysis.md](references/community-api-prompts-analysis.md) when adapting examples or claims from awesome-seedance-2.5-api-prompts, another community prompt library, or a third-party API guide.

## Workflow

1. Identify the profile first: Seedance 2.5 or explicit Seedance 2.0 Fast; then identify the mode: T2V, I2V, R2V, white-model transfer, extension, or localized edit.
2. Declare the deliverable: duration, aspect/output intent, single-shot or multi-shot, audio mode, and final-frame purpose.
3. Build an asset-role map. Give every reference one primary role, permitted secondary role if needed, and priority for conflicts.
4. List non-negotiables: identity, product geometry, layout, action order, eyeline, light direction, screen direction, or audio sync.
5. Divide the duration into readable beats. Prefer 6–8-second narrative beats; reserve 3–4 seconds for resolution and use finer timing only for action or synchronization.
6. Compile a camera direction for every beat.
7. Write observable subject action and physical state separately from camera movement.
8. Add lighting, atmosphere, audio, and output intent only when they affect the shot.
9. Add a small set of positive continuity locks and exclusions only for high-risk failures.
10. Draft the copy-ready prompt in the requested language, measure its exact character count, and apply the language fallback below when required.
11. Validate, then return the final bounded prompt.

## Camera compiler

For every important beat, state: narrative purpose; start framing; one primary move; path/direction; speed profile; subject blocking; lens/focus; end framing; and continuity or edit behavior. Keep translation, aim rotation, lens, focus, rig behavior, and subject motion in separate clauses.

```text
purpose → start framing → primary move → path/direction → speed → subject blocking → lens/focus → end framing → continuity/edit
```

Use one primary camera move per beat. Distinguish pan from trucking, tilt from pedestal/crane travel, dolly from optical zoom, and camera orbit from subject rotation. Prefer a clean uploaded path or white-model reference over coordinate formulas when precision matters. Use exact numeric camera settings only as soft intent unless a visible control or reference makes them enforceable.

## Reference hierarchy

Assign identity, motion, spatial layout, camera path, style/lighting, audio, and shot-order evidence separately. Preserve every supplied tag exactly, including capitalization. For R2V, green-screen, or white-model work, say what each source controls and what it must not transfer. A white-model reference normally supplies geometry/path, while its people, materials, and lighting may be replaced.

Replace blanket `완전히 참조` language with the source's role, preserved attributes, allowed changes, and priority. Resolve conflicts explicitly rather than silently blending sources.

## Duration and timeline

For Seedance 2.5, use one continuous standard 30-second prompt when that mode is visible; do not split it into two legacy 15-second stages. For explicit Seedance 2.0 Fast, use the same director-brief structure, asset-role hierarchy, camera compiler, audio selection, and final-frame contract as 2.5, but compile a custom 15-second timeline with three to five readable beats. Do not shorten Fast prompts by deleting the role map, subject/camera separation, camera start/path/end, audio mode, or final frame. Treat the Fast duration as part of this local authoring profile rather than a platform-wide official claim. Treat 5–180-second extended/long-video paths as Beta/UI-dependent and confirm the active interface before promising them. Give each beat a readable end state and make the final frame usable as a handoff for an extension or repair.

Mark beta, rollout-, account-, region-, or UI-dependent capabilities as qualified. Ask for visible controls or a screenshot when a specific setting determines the result.

## Audio selection

Choose one deliberate mode: clean visual, diegetic sound, scored soundtrack, or source-audio transfer. State silence, dialogue, music, effects, and sync points so they do not conflict. Treat source-audio transfer as Beta/UI-dependent unless the current UI accepts and tags the asset.

## Repair workflow

Classify the failure first: identity/product drift, subject motion, camera path/speed, framing, collision/continuity, lighting/style, audio/timing, or unwanted text/music. Repair the failed layer first; use localized editing when the interface exposes it and the remainder is usable. Strengthen or replace a reference when prose is insufficient, and rewrite the full brief only when several layers failed.

Replace unsupported coordinate formulas with a readable physical path, landmarks, start/end states, or a clean path reference. For a moving-camera repair, preserve the prior start state, target, route tangent, focus behavior, and end framing unless that layer failed.

## Prompt length contract

Treat the copy-ready prompt code block as a bounded deliverable. Count Unicode characters in that block only, including spaces and logical line breaks. Select the active budget before drafting:

- Seedance 2.5: target 4,300–4,800 characters for a complex 30-second or multimodal prompt; hard maximum 5,000.
- Explicit Seedance 2.0 Fast: aim for about 3,500 characters for the custom 15-second profile; hard maximum 4,000.

Use fewer characters whenever the brief is already complete and never pad to reach a target. Fast keeps the same complete prompt structure as 2.5; its smaller budget comes from fewer and tighter 15-second beats, not from dropping functional blocks.

Write the first draft in the user's requested language. Measure Seedance 2.5 with `scripts/count_prompt_chars.py` and Fast with `scripts/count_prompt_chars.py PROMPT_PATH --limit 4000` when tools are available. For Fast, if the draft is above the 3,500-character target but at or below 4,000, compress redundant wording in the requested language toward 3,500 while preserving the full structure.

If a draft exceeds its active hard maximum, rewrite the entire prompt code block in concise Simplified Chinese. Preserve every exact reference tag, timeline, camera path, final frame, and functional constraint, then measure and compress until the active hard maximum is met: 5,000 for 2.5 or 4,000 for Fast. Retain the exact set of supplied timecode ranges; do not merge, renumber, or recalculate beats. If the user explicitly forbids translation, keep the requested language and compress it instead.

Compress in this order: redundant style adjectives; repeated continuity locks; duplicated negative clauses; explanatory restatements; then low-priority decorative detail. Preserve asset roles and priorities, exact tags, required beats, separate subject and camera action, camera start/path/end, audio mode, final handoff, and every necessary UI-dependent qualification.

Report `프롬프트 길이: {N}/{ACTIVE_LIMIT}자` immediately after the code block, using 5,000 for Seedance 2.5 and 4,000 for Fast. The settings note, length line, asset-role map, rationale, and retry guidance are outside the prompt budget.
## Output contract

Return in this order:

1. A one-line assumption/settings note only when needed.
2. One copy-ready prompt code block in the user's language, or in Simplified Chinese when the fallback above applies.
3. The exact prompt length line.
4. A compact asset-role map when references exist.
5. A two-to-four-line camera rationale.
6. One narrow retry instruction only when repairing an existing result.

Keep exact user tags and avoid unnecessary explanation. For review-only requests, use the optional one-line note to name the strongest failure when needed, then preserve the return order above and provide the corrected prompt as item 2.

## Final checklist

Before returning, verify that the prompt contains:

- A declared mode, duration, and output intent.
- Every referenced asset's role and priority.
- A visible subject-action arc, separate from camera action.
- A camera start state and end state, with one primary move per beat.
- A deliberate audio mode.
- A final-frame or handoff description.
- Qualified wording for every beta/UI-dependent feature.
- A copy-ready prompt code block within the active hard limit: 5,000 characters for Seedance 2.5 or 4,000 for explicit Seedance 2.0 Fast.
- For Fast, the same complete structural blocks as 2.5 and an approximately 3,500-character target without padding.
- A concise Simplified Chinese rewrite, rechecked against the active limit, when the requested-language draft exceeded that profile's hard maximum.
- The exact supplied timecode-range set preserved without merging, renumbering, or recalculation during an over-limit rewrite.

Remove unsupported absolutes, pseudo-controls, conflicting moves, accidental cuts, and unassigned reference inheritance. Confirm that any one-shot route is physically contiguous and that every permitted edit has an explicit boundary.
