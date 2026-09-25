# Seedance 2.5 Prompt Patterns

Copy these structures, replace every brace-delimited variable, and retain the exact reference tags shown in the current UI. The declarations below name intended workflows; a visible control still determines whether a particular mode is selectable.

## Contents

- Shared prompt order
- Community-derived compacting checks
- Seedance 2.0 Fast custom profile
- Revision recompilation pattern
- Short single-shot pattern
- 30-second sequence pattern
- Image-to-video pattern
- R2V and white-model pattern
- Localized edit pattern
- Extension pattern
- Complete worked example
- Character budget and language fallback

## Shared prompt order

Use the main skill's eight visible sections in the requested language. Reference is for image/video sources; audio tags and sound-source roles belong in Audio. Put the final physical state in the last Timeline beat, camera end framing in Camera, and mode/output with non-negotiables and continuity rules in Constraints. With no visual source, mark Reference as text-only without inventing tags.

```text
참조 / Reference → 피사체 / Subject → 배경 / Background → 타임라인 / Timeline
→ 카메라 / Camera → 스타일 / Style → 오디오 / Audio → 제약 조건 / Constraints
```
Keep subject action and camera action in separate sentences. Duration, timestamps, angles, focal lengths, and speeds are approximate intent unless the current interface exposes a matching control or path reference.

## Community-derived compacting checks

The community collection [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) provides a useful cross-check for concise ordering and timestamped shot scripts. Adapt its ideas without replacing this skill's full structure:

- Keep the core scene compact while assigning its details to the eight sections above; do not insert a combined scene block that changes the visible order.
- Within each timecode, keep the local order: shot size → subject action → primary camera move/path → focus or audio cue when relevant → readable end state.
- Treat @Image1, @Video1, and @Audio1 as authoring-role labels whose exact spelling must match the user's interface; never claim that the prose tag itself is an API field.
- Use short standard motion terms only as the first pass. Compile every important move through [camera-motion.md](camera-motion.md) so orbit, tracking, rack focus, whip pan, crane, locked-off, gimbal, or FPV gains physical start/path/end behavior.

The community guide's short-prompt length suggestion does not override this skill's active character contract. Preserve the complete director-brief blocks and apply the 2.5 or Fast budget below. Read [community-api-prompts-analysis.md](community-api-prompts-analysis.md) for the full source audit and rejected claims.

## Seedance 2.0 Fast custom profile

Use this profile only when the user explicitly names Seedance 2.0 Fast. Treat the 15-second duration and its character budget as local authoring conventions rather than public or official specifications.

Keep the same shared prompt order and full control structure as Seedance 2.5: Reference, Subject, Background, Timeline, Camera, Style, Audio, and Constraints, with the existing mode/output, final state, and continuity requirements placed in their corresponding sections. Use three to five readable beats across 15 seconds; a useful default is 0–3s setup, 3–7s development, 7–11s payoff, and 11–15s resolution. Adjust the divisions when the action or synchronization requires it.

Aim for about 3,500 characters and never exceed 4,000. Count with `../scripts/count_prompt_chars.py PROMPT_PATH --limit 4000`. Tighten repeated prose before removing detail, and never remove the asset-role hierarchy, subject/camera separation, camera start/path/end, audio mode, or final frame merely to reach the smaller budget.

## Revision recompilation pattern

Use this as an internal compiler whenever the user changes an existing prompt. Do not copy this ledger into the final prompt.

```text
Revision operation: classify each change as ADD, REPLACE, DELETE, REORDER, RETIME, PRESERVE, or RESET.
Retired values: list displaced values and the camera, timing, focus, audio, prop, lighting, continuity, or final-frame clauses that depend on them; remove all of them.
Canonical active brief: rebuild profile/mode/output, reference roles, non-negotiables, scene geometry, subject beats, camera beats, lighting/style, audio, final frame, and continuity locks from active values only.
Dependency rebuild: align every changed action with its camera start/move/path/speed/blocking/focus/end and timed audio cues; replace the old range set after REORDER or RETIME.
Final validation: no retired value, no conflicting move, complete duration coverage, physically contiguous one-shot path when requested, exact active tags, and active character budget satisfied.
```

Return one complete replacement prompt in the normal shared order. Never return a patch fragment for the user to append. Read [revision-workflow.md](revision-workflow.md) for precedence, dependency cleanup, and worked cases.

## Character budget and language fallback

Select the active budget before writing: Seedance 2.5 targets 4,300–4,800 characters with a 5,000-character hard maximum; explicit Seedance 2.0 Fast aims for about 3,500 with a 4,000-character hard maximum. Count all Unicode characters in the prompt code block, including spaces and logical line breaks. Use `../scripts/count_prompt_chars.py` for 2.5 and add `--limit 4000` for Fast. Never pad a complete short prompt.

For Fast drafts between 3,501 and 4,000 characters, compress redundant wording in the requested language toward 3,500 while keeping the complete 2.5 structure. Before counting any revision, discard retired values and compile only the canonical active brief. If that draft exceeds its active hard maximum, rewrite the entire code block in concise Simplified Chinese while preserving exact active reference tags, timecodes, asset-role priority, camera geometry, final frame, and functional constraints. Preserve the exact active timecode set; when the newest instruction explicitly reorders or retimes beats, the new set replaces the old set. Count again and compress until the active limit is met. When the user explicitly forbids translation, compress in the requested language instead. Keep the asset-role table, camera rationale, and length report outside the prompt code block.
## Short single-shot pattern

Use for one self-contained action in `{DURATION}` (typically a short standard generation).

```text
참조 / Reference: {IDENTITY_TAG} is identity/style, highest priority; {MOTION_TAG} supplies subject motion only; {CAMERA_PATH_TAG} supplies camera path only. Ignore any unassigned source attributes.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: {LOCATION}, with {SPATIAL_ANCHORS}; maintain {GEOMETRY_AND_CLEARANCE}.
타임라인 / Timeline: 0–{ACTION_END}s, {SUBJECT} {SUBJECT_ACTION}; {ACTION_END}s–{DURATION}, {SUBJECT} resolves at {SUBJECT_END_POSE}. Final beat / physical end state: {FINAL_FRAME}.
카메라 / Camera: purpose: {CAMERA_PURPOSE}. Start framing: {START_FRAMING}. Primary move: {PRIMARY_MOVE}; path/direction: {CAMERA_PATH}; speed profile: {SPEED_PROFILE}. Subject blocking: {SUBJECT_SCREEN_POSITION_AND_ROUTE}. Lens/focus: {LENS_OR_NATURAL_PERSPECTIVE}; {FOCUS_RULE}. End framing: {END_FRAMING}. Continuity/edit: one contiguous physical path; no cut.
스타일 / Style: {LIGHTING_AND_STYLE}.
오디오 / Audio: {AUDIO_MODE}; {SOUND_RULE}.
제약 조건 / Constraints: Mode/output — Standard text-to-video, one continuous shot, {DURATION}. Non-negotiables — preserve {IDENTITY_TAG}'s identity; no cuts; {ASPECT_OR_OUTPUT}; {CONTENT_LOCK}. Continuity — preserve {IDENTITY_TAG}, {WARDROBE_LOCK}, {PROP_LOCK}, {LIGHTING_LOCK}, and {MOTION_DIRECTION_LOCK} through the final frame.
```

Load [camera-motion.md](camera-motion.md) when `{PRIMARY_MOVE}`, path clearance, focus behavior, or the distinction between a pan, truck, dolly, orbit, and zoom needs precise language.

## 30-second sequence pattern

Use for a standard continuous scene up to 30 seconds when the visible interface offers that duration. The four beats below are a default; change their timing when the brief demands different beats, action cadence, or synchronization.

```text
참조 / Reference: {IDENTITY_TAG} is identity/style, highest priority; {MOTION_TAG} controls {ACTOR_MOTION_SCOPE} only; {CAMERA_PATH_TAG} controls camera geometry/path only.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: {START_LOCATION} to {END_LOCATION}; preserve {LANDMARKS}, {TRAVEL_DIRECTION}, and {COLLISION_CLEARANCE}.
타임라인 / Timeline: 0–6s setup — {SETUP_ACTION}. 6–14s development — {DEVELOPMENT_ACTION}. 14–24s payoff/action — {PAYOFF_ACTION}. 24–30s resolution — {RESOLUTION_ACTION}. Final beat / physical end state: {FINAL_FRAME}.
카메라 / Camera: purpose: {CAMERA_PURPOSE}. Start framing: {START_FRAMING}. Primary move by beat: 0–6s {MOVE_1}; 6–14s {MOVE_2}; 14–24s {MOVE_3}; 24–30s {MOVE_4}. Path/direction: {CONTIGUOUS_ROUTE}. Speed profile: {SPEED_PROFILE_BY_BEAT}. Subject blocking: {SUBJECT_ROUTE_AND_SCREEN_RELATION}. Lens/focus: {LENS_OR_NATURAL_PERSPECTIVE}; {FOCUS_RULE}. End framing: {END_FRAMING}. Continuity/edit: physically contiguous route; one continuous shot; no cuts.
스타일 / Style: {LIGHTING_AND_STYLE}, continuous across all four beats.
오디오 / Audio: When supplied and supported by the UI, {AUDIO_TAG} controls audio only. {AUDIO_MODE}; {TIMED_AUDIO_CUES}; no conflicting music/dialogue instruction.
제약 조건 / Constraints: Mode/output — Standard 30-second continuous text-to-video sequence, one continuous shot. Non-negotiables — preserve {IDENTITY_TAG}; no cuts; {FORMAT_LOCK}; {SAFETY_OR_CONTENT_LOCK}. Continuity — retain {IDENTITY_TAG}, {COSTUME_AND_PROP_LOCKS}, {TIME_OF_DAY}, {DIRECTION_OF_TRAVEL}, and {FOCUS_TARGET} through the resolution.
```

Load [camera-motion.md](camera-motion.md) to compile each beat as purpose → framing → move → path → speed → blocking → focus → end frame → continuity, especially before combining moves.

## Image-to-video pattern

Use when a still image establishes the subject or opening composition and text supplies controlled movement.

```text
참조 / Reference: {IMAGE_TAG} is the opening composition and identity/style, highest priority; {MOTION_TAG} supplies {ACTOR_MOTION_SCOPE} only; {CAMERA_PATH_TAG} supplies camera motion only.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: extend only what is implied by {IMAGE_TAG}; preserve {IMAGE_ANCHORS} and {GEOMETRY_AND_CLEARANCE}.
타임라인 / Timeline: 0–{MIDPOINT}s, {SUBJECT} {ACTION_1}; {MIDPOINT}s–{DURATION}, {SUBJECT} {ACTION_2_AND_END_POSE}. Final beat / physical end state: {FINAL_FRAME}.
카메라 / Camera: purpose: {CAMERA_PURPOSE}. Start framing: match {IMAGE_TAG} as {START_FRAMING}. Primary move: {PRIMARY_MOVE}; path/direction: {CAMERA_PATH}. Speed profile: {SPEED_PROFILE}. Subject blocking: {SUBJECT_SCREEN_POSITION_AND_ROUTE}. Lens/focus: {LENS_OR_NATURAL_PERSPECTIVE}; {FOCUS_RULE}. End framing: {END_FRAMING}. Continuity/edit: evolve directly from the opening image; no cuts.
스타일 / Style: continue {IMAGE_TAG}'s {LIGHTING_STYLE_LOCK}.
오디오 / Audio: {AUDIO_MODE}; {SOUND_RULE}.
제약 조건 / Constraints: Mode/output — Image-to-video, {DURATION}, one continuous shot. Non-negotiables — begin from {IMAGE_TAG}'s visible composition; preserve {IDENTITY_LOCK}, {WARDROBE_LOCK}, and {ENVIRONMENT_LOCK}; {OUTPUT_LOCK}. Continuity — do not replace or redesign the identity, wardrobe, key props, or initial lighting established by {IMAGE_TAG}.
```

Load [camera-motion.md](camera-motion.md) when the desired movement must preserve the still's framing at the handoff while adding a physical route, focus rule, or end frame.

## R2V and white-model pattern

Use R2V material to separate appearance from motion or layout. A white-model/previs source is camera/spatial evidence, not a demand to copy its materials.

```text
참조 / Reference: {IDENTITY_TAG} is identity/style, highest priority. {ACTOR_REFERENCE_TAG} is actor motion and interaction only. {CAMERA_PATH_TAG} is a white-model/previs reference for camera geometry and path only. {STYLE_TAG} may affect palette/materials only.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: source role: {CAMERA_PATH_TAG} is white-model/previs. Geometry to preserve: {GEOMETRY_ANCHORS}. Path to preserve: {CAMERA_START_STATE} → {PATH_LANDMARKS_AND_DIRECTION} → {CAMERA_END_STATE}. Allowable visual replacement: {REPLACED_MATERIALS_LIGHTING_CHARACTERS_STYLE}. Collision handling: {DOOR_WALL_STAIR_CLEARANCE_OR_HANDOFF}. Final framing: {END_FRAMING_WITH_TARGET_FOCUS_AND_SETTLE}.
타임라인 / Timeline: {TIMESTAMPS_AND_ACTOR_ACTION}; actor motion is governed by {ACTOR_REFERENCE_TAG}, not by the camera-path source. Final beat / physical end state: {FINAL_FRAME}.
카메라 / Camera: purpose: {CAMERA_PURPOSE}. Start framing: {START_FRAMING}. Primary move: {PRIMARY_MOVE}. Path/direction: follow {CAMERA_PATH_TAG}'s {ROUTE}; speed profile: {SPEED_PROFILE}. Subject blocking: {SUBJECT_ROUTE_AND_SCREEN_RELATION}. Lens/focus: {LENS_OR_NATURAL_PERSPECTIVE}; {FOCUS_RULE}. End framing: {END_FRAMING}. Continuity/edit: {ONE_CONTIGUOUS_ROUTE_OR_NAMED_EDIT_BOUNDARY}.
스타일 / Style: {LIGHTING_AND_STYLE}, replacing only the permitted white-model appearance.
오디오 / Audio: {AUDIO_MODE}; {SOUND_RULE}.
제약 조건 / Constraints: Mode/output — R2V with white-model/previs camera-path reference, {DURATION}, {ONE_SHOT_OR_EDITED_OUTPUT}. Non-negotiables — preserve {IDENTITY_TAG}; do not inherit camera shake or appearance from {ACTOR_REFERENCE_TAG}; do not inherit white-model materials, people, or lighting from {CAMERA_PATH_TAG}. Continuity — preserve the named geometry, {IDENTITY_TAG}, actor route, camera route, and {EDIT_OR_HANDOFF_LOCK}.
```

Load [camera-motion.md](camera-motion.md) whenever the white-model path includes turns, doorway passage, height changes, or a potentially ambiguous camera move; it supplies the required geometry and clearance language.

## Localized edit pattern

Use for one named change while retaining everything outside that region and variable. If the user replaces camera, timing, audio, or another global layer, use the revision recompilation pattern instead of locking the replaced source behavior.

```text
참조 / Reference: {SOURCE_CLIP_TAG} is the immutable source for all unaffected content, highest priority; {IDENTITY_TAG} verifies identity only; {EDIT_REFERENCE_TAG} supplies {EDIT_VARIABLE} only.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: {EDIT_REGION} stays attached to {SPATIAL_ANCHOR}; retain the source geometry, occlusion order, and clearance.
타임라인 / Timeline: {EDIT_START}–{EDIT_END}, change {EDIT_VARIABLE} from {SOURCE_VALUE} to {TARGET_VALUE}; all other subject actions keep their source timing and motion. Final beat / physical end state: source-equivalent frame with only {EDIT_VARIABLE} changed to {TARGET_VALUE}: {FINAL_FRAME}.
카메라 / Camera: purpose: preserve the source shot. Start framing: match {SOURCE_CLIP_TAG} at {EDIT_START}. Primary move: retain {SOURCE_CAMERA_MOVE}; path/direction: retain {SOURCE_CAMERA_PATH}. Speed profile: retain {SOURCE_SPEED_PROFILE}. Subject blocking: retain {SOURCE_BLOCKING}. Lens/focus: retain {SOURCE_LENS_AND_FOCUS}. End framing: match {SOURCE_CLIP_TAG} at {EDIT_END}. Continuity/edit: localized edit boundary is {EDIT_REGION} only; no global reframe or added cut.
스타일 / Style: retain source lighting/style outside {EDIT_REGION}; match any changed pixels to {SOURCE_LIGHTING_CONDITIONS}.
오디오 / Audio: preserve source audio unchanged, including timing and mix.
제약 조건 / Constraints: Mode/output — Localized edit of {SOURCE_CLIP_TAG}, region {EDIT_REGION}, changing only {EDIT_VARIABLE}. Non-negotiables — alter only {EDIT_REGION}/{EDIT_VARIABLE}; treat preservation of all unaffected motion, timing, composition, lighting, audio, and identity as a continuity goal, matching the source as closely as the active interface permits; retain {SOURCE_CLIP_TAG}'s duration and output framing, then inspect the result for drift. Continuity — unaffected motion, timing, composition, lighting, audio, identity, camera behavior, and all regions outside {EDIT_REGION} remain locked.
```

Load [camera-motion.md](camera-motion.md) when the edited region crosses a moving subject, occlusion, focus shift, or camera path and the boundary must preserve the original camera behavior.

## Extension pattern

Use after a previous clip. Treat the previous final frame as the handoff target; direct the first frame to match it as closely as the active interface permits, then inspect the generated join before use.

```text
참조 / Reference: {PREVIOUS_CLIP_TAG} is the handoff image, identity, composition, motion, and lighting source, highest priority; {IDENTITY_TAG} verifies identity only; {NEW_ACTION_REFERENCE_TAG} supplies {NEW_ACTION_SCOPE} only.
피사체 / Subject: {SUBJECT_APPEARANCE_AND_INITIAL_STATE}, using only the assigned references and active brief.
배경 / Background: continue from {PREVIOUS_LOCATION_AND_GEOMETRY}; retain {SPATIAL_ANCHORS}, {DIRECTION_OF_TRAVEL}, and {CLEARANCE_RULE}.
타임라인 / Timeline: 0–{HANDOFF_SETTLE}s, hold/continue {PREVIOUS_FINAL_POSE_AND_MOTION}; {HANDOFF_SETTLE}s–{DURATION}, {SUBJECT} {NEW_ACTION}; end with {SUBJECT_END_POSE}. Final beat / physical end state: {FINAL_FRAME}.
카메라 / Camera: purpose: {CAMERA_PURPOSE}. Start framing: match {PREVIOUS_FINAL_FRAMING} as closely as the active interface permits. Primary move: {PRIMARY_MOVE_OR_CONTINUATION}. Path/direction: {CONTIGUOUS_PATH_FROM_HANDOFF}. Speed profile: {SPEED_PROFILE}. Subject blocking: {SUBJECT_SCREEN_POSITION_AND_ROUTE}. Lens/focus: continue {PREVIOUS_LENS_AND_FOCUS}, then {NEW_FOCUS_RULE}. End framing: {END_FRAMING}. Continuity/edit: aim for a visually seamless extension boundary at frame 0; direct no reset, teleport, or new cut, then inspect the join for discontinuity.
스타일 / Style: continue {PREVIOUS_LIGHTING_AND_STYLE}; only {PERMITTED_NEW_LIGHTING_CHANGE} after {CHANGE_TIME}.
오디오 / Audio: {PREVIOUS_CLIP_TAG} supplies the source audio, highest priority. continue {PREVIOUS_AUDIO_MODE}; {NEW_AUDIO_CUE_OR_SILENCE_RULE} without a join pop.
제약 조건 / Constraints: Mode/output — Extension of {PREVIOUS_CLIP_TAG}, add {DURATION} using the previous final frame as the continuity target. Non-negotiables — direct the first frame to match this handoff state as closely as the active interface permits: {PREVIOUS_FINAL_FRAME}. Preserve {IDENTITY_LOCK}, {WARDROBE_LOCK}, {PROP_LOCK}, {LIGHTING_LOCK}, {CAMERA_STATE_LOCK}, and {AUDIO_STATE_LOCK} as continuity goals at the join, then inspect the result for drift. Continuity — preserve the previous clip's identity, composition, camera height/direction, lighting, sound bed, and motion direction through the handoff.
```

Load [camera-motion.md](camera-motion.md) when the extension continues a moving camera, because the first extended camera state, path tangent, focus target, and end framing must be contiguous with the prior final frame.

## Complete worked example

### Asset-role map

| Asset | Role | Priority / exclusion |
| --- | --- | --- |
| `@Image1` | Character identity and appearance | Highest priority for face, hair, wardrobe, and body identity. |
| `@Video1` | Actor walking and door-opening motion only | Transfer the actor's walk, reach, and door interaction; do not inherit its camera, framing, setting, lighting, or audio. |

```text
참조 / Reference: @Image1 controls character identity, highest priority. @Video1 controls the actor's walking and door-opening motion only; do not transfer @Video1's camera movement, framing, environment, lighting, or audio.
피사체 / Subject: The character in @Image1, preserving its appearance and wardrobe, initially walking down the corridor.
배경 / Background: an interior corridor leads to a doorway on the character's left. Keep the corridor walls, doorframe, and door physically continuous; the camera uses clear passage beside and through the doorway and never crosses wall or door geometry.
타임라인 / Timeline: 0–4s, the character walks forward down the corridor at the walking pace in @Video1. 4–7s, the character reaches the left-side door, opens it while continuing the forward arrival, and turns naturally through the doorway. 7–12s, the character enters the room, stops inside, and turns enough for a three-quarter face to remain visible. Final beat / physical end state: clear extension handoff frame — the character is stopped inside the room, three-quarter face visible in a stable medium close-up, the half-open door remains behind them, and the camera is settled.
카메라 / Camera: purpose: reveal the character's approach, door interaction, and final reaction as one grounded route. Start framing: rear three-quarter medium-full follow, trailing behind the character. Primary move: smooth gimbal follow. Path/direction: follow behind, then make a gentle left-side reveal arc around the character while they keep walking; track alongside the door interaction with clearance from the door edge and frame; pass through the open doorway on the physically available side, then travel forward into the room. The arc is approximately a quarter-turn in intent, not a hard 90-degree control. Speed profile: match the walking pace at a calm, natural speed; decelerate through the doorway; finish with a slow physical push-in at an approximate, restrained pace as the character stops. Subject blocking: retain the character as the continuous focus target; keep their route centered-to-right during the left-side reveal, then retain the three-quarter face after entry. Lens/focus: fixed natural perspective, continuous target focus on the character's face/upper body as it comes into view; no optical zoom and no rack focus. End framing: stable medium close-up, three-quarter face visible, camera level and settled. Continuity/edit: one contiguous physical camera path, no cuts, no geometry crossing.
스타일 / Style: natural corridor-to-room lighting with a coherent exposure transition at the doorway; realistic, grounded cinematic movement.
오디오 / Audio: diegetic only — natural footsteps during the walk and the door handle/opening sound at the interaction; no BGM, dialogue, or added score.
제약 조건 / Constraints: Mode/output — Standard text-to-video, 12 seconds, one continuous shot. Non-negotiables — preserve @Image1's character identity; one continuous shot with no cuts; fixed natural perspective; continuous target focus on the character; no BGM. Continuity — preserve @Image1 identity, walking direction, door position and half-open state, fixed natural perspective, continuous target focus, diegetic sound bed, and one-shot continuity through the final frame.
```

The camera has one dominant follow route: rear follow, left-side reveal arc, physically clear doorway passage, then a slow push-in after the actor settles. The approximate quarter-turn and restrained speed communicate cinematic intent without pretending that degrees or metric speed are executable model controls. Focus stays on one target so the reveal does not become an unrequested rack-focus event.
