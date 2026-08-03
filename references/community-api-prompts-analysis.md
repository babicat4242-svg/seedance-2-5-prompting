# Community Repository Analysis: awesome-seedance-2.5-api-prompts

## Snapshot and provenance

- Repository: [Anil-matcha/awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts)
- Reviewed commit: [f020c085cdaf3174279e361829cee1c8b09a37e4](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts/tree/f020c085cdaf3174279e361829cee1c8b09a37e4)
- Commit timestamp: 2026-08-03T07:03:29Z
- Review date: 2026-08-03
- Evidence class: community/third-party, not an official ByteDance, Dreamina, CapCut, or Volcano Ark source.
- License note: the repository README states MIT, but GitHub's repository license endpoint returned no standalone license file during review. Retain attribution, link to the snapshot, paraphrase principles, and do not bulk-copy prompt examples.

This analysis covers the repository's README prompt guide, camera vocabulary, multimodal notation, shot-script format, category examples, provider-specific API material, and stated limits.

## What the repository is useful for

The strongest value is breadth. Its examples repeatedly expose a compact prompt anatomy across cinematic work, typography/VFX, fashion, nature, products, food, beauty, UGC, anime/stylized scenes, and multi-shot sequences. That breadth is useful as a completeness check: a prompt should identify the visible subject, an observable action, a place, a camera behavior, a lighting/style treatment, audio intent when relevant, and a resolved ending.

It also provides an independent vocabulary cross-check for common production terms. The repository does not make those words executable controls; it shows that concise industry terms are useful first-pass labels that still need physical expansion.

## Adopted authoring patterns

| Community pattern | Integration in this skill | Guardrail |
| --- | --- | --- |
| Six-part concise order: subject, action, environment, camera, style, constraints | Use as a compact core-scene sentence after mode and reference roles | It is an audit/compression device, not a replacement for the full director brief |
| Timestamped shot script | Give every beat a time range, shot size, subject action, camera instruction, and readable end state | Preserve the exact user-supplied timecode ranges during rewrites |
| Common camera keywords | Use as normalized first-pass vocabulary | Compile each term into physical start/path/speed/focus/end behavior |
| @Image, @Video, @Audio prose notation | Preserve the exact UI/user tag and assign one primary role per asset | Treat tags as authoring conventions, not universal API fields |
| Lighting keyword per intended look | Select one motivated lighting system before decorative adjectives | Do not imply that a keyword is a dedicated control |
| Audio paired to action or edit rhythm | State clean/diegetic/scored/source-transfer mode and named sync points | Avoid conflicting music, silence, dialogue, and source-audio instructions |
| Category-specific prompt examples | Use as coverage inspiration for ads, UGC, product, food, fashion, nature, and stylized work | Rebuild from user intent; do not reproduce library prompts verbatim |
| End reveal or held hero frame | Give the final beat a stable framing, focus target, subject state, and handoff purpose | Do not leave the last seconds as unbounded motion |

## Camera vocabulary normalization

| Short term found in the repository | Physical interpretation required here | Minimum fields to add |
| --- | --- | --- |
| slow push in / dolly in | Camera body travels toward the subject; perspective and parallax change | Start framing, route, speed/easing, subject anchor, end framing |
| dolly out / pull back | Camera body retreats and reveals space | Start frame, retreat path, reveal, subject relationship, end frame |
| tracking shot left/right | Usually lateral camera translation, not a pan | Side, route/clearance, pace, pan target if any, end frame |
| crane up / boom up | Camera body rises on a supported vertical/diagonal path | Start height, 3D path, independent aim, clearance, end height/frame |
| steadicam follow / gimbal shot | Stabilized body travel along a named route | Lead/follow/side relation, offset, pace, horizon behavior, settle |
| orbit / 360 arc | Camera travels around a named target | Target, camera-relative direction, arc extent as intent, radius, end angle |
| whip pan | Rapid aim rotation through blur between readable endpoints | Settled start, direction, blur interval, destination, settled end/cut |
| static / locked off | No body, aim, or lens change | Fixed frame, subject blocking, focus rule, allowed edit, final frame |
| top-down / bird's-eye | Viewpoint/angle, not movement by itself | Camera position/height, aim, static or traveling behavior, end state |
| handheld | Operator-carried micro-drift over a dominant route | Route, intensity restraint, readable framing, horizon rule, settle |
| rack focus | Focus transfers between depth planes; camera need not move | Near target, far target, transfer order, motion status, final focus |
| FPV continuous long take | Free-flight camera follows a physically contiguous route | Start height, landmarks, turns/elevation, collision clearance, end frame |

Use [camera-motion.md](camera-motion.md) for full definitions and conflict repair.

## How to translate an example into this skill

1. Identify the user's active profile first: Seedance 2.5 or explicit Seedance 2.0 Fast.
2. Extract only abstract intent from the example: subject, action, space, camera function, lighting, audio, and ending.
3. Replace named or imitation-heavy aesthetics with descriptive visual traits when they are unnecessary to the user's request.
4. Rebuild the asset-role map from the user's actual sources; do not inherit example tags or provider field names.
5. Convert each beat to: timecode → shot size → subject action → primary camera path → focus/audio cue → end state.
6. Run every camera term through the camera compiler and conflict matrix.
7. Restore the full blocks: mode/output, roles, non-negotiables, scene/spatial rules, subject timeline, separate camera plan, lighting/style, audio, end state, continuity locks.
8. Apply the active length contract: 2.5 targets 4,300–4,800 and must not exceed 5,000; Fast aims near 3,500 and must not exceed 4,000.
9. If over the active hard limit, apply the skill's Simplified Chinese fallback without dropping tags, timecodes, camera geometry, audio mode, or final frame.

## Claims intentionally not imported

Do not use this repository alone as evidence for:

- Model launch status, availability, feature superiority, or a 2.0-versus-2.5 comparison.
- Maximum image/video/audio reference counts.
- Duration, resolution, aspect-ratio, codec, container, bitrate, seed, watermark, or last-frame limits.
- Third-party endpoint names, request schemas, prices, polling behavior, plan gates, or moderation variants.
- Availability of first/last-frame, Omni Reference, audio generation, localized editing, or any dedicated camera control.
- Planned 1080p/4K support or other roadmap claims.
- Guarantees that the opening words receive a fixed weight, that a keyword has the biggest quality effect, or that exact timing will be followed.
- Brand-safe, likeness, artifact-reduction, or watermark-removal claims.

Verify such facts with the current visible interface and primary official sources in [sources.md](sources.md). If verification is unavailable, state the limitation and treat the feature as UI/provider-dependent.

## Length-policy decision

The repository suggests short prompts in one portion of its guide, while also presenting much longer multi-shot examples. Neither establishes a universal model limit. This skill therefore does not adopt that word-count suggestion. The local 2.5 and explicit Fast character contracts remain authoritative, and complete structure takes priority over arbitrary padding or shortening.

## 2.5 and Fast integration

Seedance 2.5 uses the community patterns as an early compression and coverage pass inside the existing 30-second/multimodal director brief. Seedance 2.0 Fast uses exactly the same blocks in a tighter 15-second timeline. The Fast profile does not remove reference roles, subject/camera separation, start/path/end camera geometry, audio selection, final frame, or continuity locks.

For both profiles, the community camera words are merely tokens to normalize. A bare phrase such as orbit shot is incomplete until the target, direction, arc, radius, subject behavior, focus, and ending are stated.

## Review checklist

Before accepting an adapted prompt, confirm:

- No third-party API claim has been rewritten as an official Seedance fact.
- Exact user/UI asset tags and their roles are preserved.
- Each timecode has observable subject action and a readable end state.
- Camera body movement, aim rotation, lens, focus, rig, and subject motion are separate.
- One dominant camera move exists per beat and conflicting moves are repaired.
- Lighting and audio serve the narrative rather than forming an adjective list.
- The final frame is stable and useful as an ending, overlay plate, or extension handoff.
- The copy-ready block satisfies the active 5,000- or 4,000-character hard maximum.