# Seedance 2.5 Camera Motion Reference

## Contents

- Camera instruction schema
- Translation moves
- Rotation moves
- Lens and focus behavior
- Rig and operator behavior
- Transition moves
- Combination rules
- Conflict matrix
- Reference-driven camera paths
- Failure diagnosis
- Community vocabulary cross-check
- Quick phrase library

Camera wording is a **prompting vocabulary and compiler heuristic**, not a promise of a dedicated camera control or frame-perfect reproduction. Follow the capability qualifications in [model-differences.md](model-differences.md): the visible interface and uploaded references determine what is selectable or enforceable.

## Camera instruction schema

Use one ordered clause chain for each beat:

```text
purpose → start framing → primary move → path/direction → speed profile
→ subject blocking → lens/focus → end framing → continuity/edit
```

Name one dominant move before adding a secondary move. Describe a beat's contiguous start state and end state; time ranges, degrees, focal lengths, and speeds are intent cues unless an available control or path reference makes them enforceable. For longer scenes, 6–8 second beats are a useful heuristic, not a timing guarantee.

## Translation moves

### Push / dolly in

- **Physical change:** The camera body travels toward the subject, changing perspective and parallax.
- **Required fields:** Start framing; target; forward path; speed profile; end framing.
- **Stable relationship:** Keep the subject's screen position or intended size explicit while foreground/background parallax evolves.
- **Compatible with:** Rack focus, controlled handheld, pan or tilt as separately named aim.
- **Conflicts with:** Locked-off; unspecified simultaneous zoom-in.
- **Seedance-ready phrase:** `Medium shot; physical dolly in along the table toward the actor, restrained acceleration, actor stays center-frame, foreground parallax increases, end in close-up.`

### Pull / dolly out

- **Physical change:** The camera body travels away from the subject, revealing more spatial depth and parallax.
- **Required fields:** Start framing; retreat path; subject relation; reveal; end framing.
- **Stable relationship:** Preserve the subject anchor while the environment opens around it.
- **Compatible with:** Crane down, rack focus, dissolve after the settled end.
- **Conflicts with:** Locked-off; unspecified simultaneous zoom-out.
- **Seedance-ready phrase:** `Close-up to wide: physical dolly out from the actor, maintain center framing, reveal the doorway and room depth, settle before the cut.`

### Truck left

- **Physical change:** The camera body moves laterally to camera-left; it is not a pan.
- **Required fields:** Start framing; lateral direction; path clearance; pan target if any; end framing.
- **Stable relationship:** Hold the stated subject screen-side relationship while foreground parallax travels opposite the body motion.
- **Compatible with:** Pan toward a named target, side tracking, gimbal.
- **Conflicts with:** Locked-off; a bare `pan left` when translation is intended.
- **Seedance-ready phrase:** `Truck camera left along the storefront, keep the walker on the right third, pan gently to retain the face, finish aligned with the door.`

### Truck right

- **Physical change:** The camera body moves laterally to camera-right; it is not a pan.
- **Required fields:** Start framing; lateral direction; path clearance; pan target if any; end framing.
- **Stable relationship:** Keep the designated subject or architectural edge anchored as the camera translates.
- **Compatible with:** Pan toward a named target, side tracking, gimbal.
- **Conflicts with:** Locked-off; a bare `pan right` when translation is intended.
- **Seedance-ready phrase:** `Truck camera right beside the counter, maintain the chef in profile, leave clearance from the stools, settle on the plated dish.`

### Pedestal up

- **Physical change:** The camera body rises vertically in space while its aim may remain independent.
- **Required fields:** Start height/framing; upward path; aim behavior; subject blocking; end framing.
- **Stable relationship:** State whether the subject remains eye-level, drops in frame, or is reframed by an independent tilt.
- **Compatible with:** Tilt, gimbal, lead tracking.
- **Conflicts with:** Locked-off; calling it a tilt when only height changes.
- **Seedance-ready phrase:** `Pedestal up from table height to eye level, keep the seated actor centered with a gentle independent tilt, end in a clean medium shot.`

### Pedestal down

- **Physical change:** The camera body descends vertically in space while its aim may remain independent.
- **Required fields:** Start height/framing; downward path; aim behavior; ground clearance; end framing.
- **Stable relationship:** Preserve the stated framing anchor while vertical perspective changes.
- **Compatible with:** Tilt, gimbal, rack focus.
- **Conflicts with:** Locked-off; calling it a tilt when only height changes.
- **Seedance-ready phrase:** `Pedestal down from eye level to the child’s level, retain the face near center, end with the toy foreground visible.`

### Crane / boom

- **Physical change:** A supported camera travels through a larger vertical or diagonal spatial arc; a boom may combine rise, descent, and reach.
- **Required fields:** Start framing/height; three-dimensional path; clearance; aim behavior; end framing.
- **Stable relationship:** Specify both body path and what remains framed during the rise or descent.
- **Compatible with:** Tilt, orbit segment, wide reveal.
- **Conflicts with:** Locked-off; a vague `tilt up` used to request spatial elevation.
- **Seedance-ready phrase:** `Crane up and slightly forward from behind the crowd, independently tilt down to hold the singer, clear the stage edge, finish in a high wide.`

### Lead tracking

- **Physical change:** The camera translates ahead of the moving subject and travels backward or forward with it, facing the subject.
- **Required fields:** Start framing; camera-subject offset; travel direction; pace; end framing.
- **Stable relationship:** Keep the camera ahead at a named relative distance and retain facial framing.
- **Compatible with:** Gimbal, controlled handheld micro-drift, rack focus.
- **Conflicts with:** A follow-tracking instruction with no handoff; fixed focus on a different plane.
- **Seedance-ready phrase:** `Lead tracking in front of the runner, move backward at their pace, keep face in medium close-up, maintain safe clearance, settle as they stop.`

### Follow tracking

- **Physical change:** The camera translates behind a moving subject, following the route and revealing what approaches.
- **Required fields:** Start framing; trailing offset; route; pace; reveal/end framing.
- **Stable relationship:** Maintain the stated following distance and subject back/shoulder placement.
- **Compatible with:** Gimbal, FPV/drone path, occlusion wipe at a doorway.
- **Conflicts with:** Lead tracking in the same beat without a named handoff.
- **Seedance-ready phrase:** `Follow tracking behind the cyclist through the corridor, preserve a trailing over-the-shoulder view, keep the exit centered, end when the cyclist enters daylight.`

### Side tracking

- **Physical change:** The camera translates alongside the subject, usually laterally relative to its direction of travel.
- **Required fields:** Side designation; matching pace; lens/aim; background relation; end framing.
- **Stable relationship:** Keep a consistent side-by-side offset and profile or three-quarter view.
- **Compatible with:** Truck motion, gimbal, controlled handheld.
- **Conflicts with:** Pan-only wording; an opposite-side instruction in the same beat.
- **Seedance-ready phrase:** `Side tracking on the actor’s camera-left, match walking pace, retain a three-quarter profile, storefronts slide behind, end on the café entrance.`

### Arc / orbit

- **Physical change:** The camera body moves around a target on a curved path; an orbit is not a turntable spin.
- **Required fields:** Target; clockwise/counterclockwise direction from camera view; arc extent as intent; radius/path; end angle.
- **Stable relationship:** Keep the named target central or deliberately reframe it while the background parallax revolves.
- **Compatible with:** Target lock, dolly change, gimbal.
- **Conflicts with:** Locked-off; unassigned subject spin; ambiguous left/right direction.
- **Seedance-ready phrase:** `Camera orbits clockwise around the stationary actor from front three-quarter to profile, keep the face near center, background parallax revolves, end on the window side.`

### FPV / drone path

- **Physical change:** A flying or FPV-style camera follows a continuous aerial or free-flight route through space.
- **Required fields:** Start height/framing; path landmarks; elevation changes; collision clearance; end framing.
- **Stable relationship:** Tie the route to visible geometry and state whether the subject is followed, led, or merely passed.
- **Compatible with:** White-model path reference, follow tracking, crane-like reveal.
- **Conflicts with:** Locked-off; handheld; a route that passes through unaddressed walls or doors.
- **Seedance-ready phrase:** `FPV/drone path begins above the courtyard, descends through the arch with clear center clearance, follows the dancer into the plaza, then rises to a wide end frame.`

## Rotation moves

### Pan

- **Physical change:** The view rotates horizontally from a fixed camera position.
- **Required fields:** Fixed position; start target; pan direction; end target; settle.
- **Stable relationship:** The camera body stays fixed; only horizontal aim changes.
- **Compatible with:** Tripod, locked body position, separately named truck motion.
- **Conflicts with:** Calling lateral body travel a pan; locked-off if any rotation is requested.
- **Seedance-ready phrase:** `From a fixed tripod position, pan right from the empty doorway to the actor, then settle in a medium frame.`

### Tilt

- **Physical change:** The view rotates vertically from a fixed camera position.
- **Required fields:** Fixed position; start target; tilt direction; end target; settle.
- **Stable relationship:** The camera body stays fixed; only vertical aim changes.
- **Compatible with:** Tripod, separately named pedestal or crane path.
- **Conflicts with:** Calling a height change a tilt; locked-off if rotation is requested.
- **Seedance-ready phrase:** `From a fixed camera position, tilt up from the letter to the actor’s face, hold the final medium close-up.`

### Roll

- **Physical change:** The view rotates around the lens axis, changing horizon orientation.
- **Required fields:** Start horizon; roll direction; emotional purpose; end orientation; settle/cut.
- **Stable relationship:** Keep the subject framing intentional while the horizon rotates.
- **Compatible with:** Controlled handheld, orbit, match cut.
- **Conflicts with:** Level-horizon requirement; unspecified competing rotation.
- **Seedance-ready phrase:** `Hold the actor in close-up while the camera slowly rolls clockwise into unease, end on a deliberately tilted horizon.`

## Lens and focus behavior

### Optical zoom

- **Physical change:** Focal length changes without translating the camera body; perspective position remains fixed.
- **Required fields:** Fixed camera position; zoom direction; target; speed; end framing.
- **Stable relationship:** Subject size changes through optical compression while parallax does not indicate camera travel.
- **Compatible with:** Locked body position, tripod pan/tilt, rack focus.
- **Conflicts with:** A dolly request unless the special effect is intentional.
- **Seedance-ready phrase:** `Keep camera position fixed; optical zoom in on the actor’s hands, minimal parallax change, finish tight on the key.`

### Dolly zoom

- **Physical change:** Camera translation and opposite optical zoom combine to hold subject size while background perspective changes.
- **Required fields:** Dolly direction; inverse zoom direction; subject size lock as intent; target; end framing.
- **Stable relationship:** State that the subject remains approximately the same screen size while the background expands or compresses.
- **Compatible with:** Locked target, dramatic reveal, controlled tripod/rig movement.
- **Conflicts with:** Locked-off; unspecified same-direction dolly and zoom.
- **Seedance-ready phrase:** `Dolly in while zooming out, keep the actor’s head size visually stable, let the hallway stretch behind them, settle on the reaction.`

### Rack focus

- **Physical change:** Focus shifts between depth planes; it is not a camera move.
- **Required fields:** Near target; far target; order; camera motion status; end focus target.
- **Stable relationship:** Keep camera path separate and name the object or face that becomes sharp.
- **Compatible with:** Locked-off, dolly, pan, target lock after the shift.
- **Conflicts with:** Simultaneous fixed focus on a different target; ambiguous multiple focus targets.
- **Seedance-ready phrase:** `Camera remains still; rack focus from the foreground glass to the actor at the window, hold focus on the actor for the end frame.`

### Fixed focus / target lock

- **Physical change:** Focus remains assigned to one target or depth plane while motion continues.
- **Required fields:** Focus target; target movement allowance; camera path; fallback if occluded; end focus.
- **Stable relationship:** Keep the named target sharp as practical; do not imply guaranteed pixel-perfect lock.
- **Compatible with:** Tracking, orbit, gimbal, rack focus entering or leaving the lock.
- **Conflicts with:** A simultaneous rack focus to another target; abrupt depth-plane changes without a transition.
- **Seedance-ready phrase:** `Track beside the dancer with fixed focus on her eyes; if a passerby occludes her, recover focus on her face as she clears frame.`

### Depth-of-field transition

- **Physical change:** The amount or placement of apparent sharpness changes, often with focus, lens, or staging.
- **Required fields:** Initial sharp plane; final sharp plane/look; subject blocking; camera motion; end emphasis.
- **Stable relationship:** Identify which story element gains or loses attention rather than treating blur as random decoration.
- **Compatible with:** Rack focus, push-in, optical zoom.
- **Conflicts with:** Simultaneous demand for deep focus across all planes unless explicitly staged.
- **Seedance-ready phrase:** `Begin with the foreground flowers soft and the couple sharp; transition attention to the flowers as the couple recedes, end with flowers in focus.`

## Rig and operator behavior

### Locked-off

- **Physical change:** No camera position, orientation, or focal-length change, and no deliberate operator drift.
- **Required fields:** Fixed framing; subject blocking; focus rule; allowed edit point; end framing.
- **Stable relationship:** The frame stays stable while action enters, exits, or changes within it.
- **Compatible with:** Rack focus, static staging, and subject action within the fixed frame.
- **Conflicts with:** Orbit, pan, tilt, truck, pedestal, crane, handheld, gimbal drift, and optical zoom; describe optical zoom as a separate fixed-position optical-zoom shot, not locked-off.
- **Seedance-ready phrase:** `Locked-off wide shot of the doorway; actors cross within the frame, fixed focus on the threshold, no camera movement, cut only after they exit.`

### Tripod pan / tilt

- **Physical change:** A fixed-position tripod supports controlled horizontal pan and/or vertical tilt.
- **Required fields:** Fixed position; rotation axis; start target; end target; settle.
- **Stable relationship:** The body remains in place and the horizon remains stable unless roll is separately requested.
- **Compatible with:** Optical zoom, rack focus, static staging.
- **Conflicts with:** Translation described as if it were tripod rotation; handheld shake.
- **Seedance-ready phrase:** `Tripod pan left, then tilt down from the clock to the actor’s hands; fixed camera position and a clean settled end.`

### Gimbal

- **Physical change:** Stabilized operator or rig translation/rotation follows a named route with smooth horizon behavior.
- **Required fields:** Dominant path; target relation; stabilization character; clearance; end framing.
- **Stable relationship:** Preserve a smooth, deliberate path rather than floating without motivation.
- **Compatible with:** Lead/follow/side tracking, orbit, pedestal, controlled micro-drift.
- **Conflicts with:** Locked-off; chaotic handheld; exact route without a path reference or landmarks.
- **Seedance-ready phrase:** `Smooth gimbal follow behind the actor through the lobby, stable horizon, clear the columns, finish at the elevator doors.`

### Controlled handheld

- **Physical change:** Operator-carried camera has restrained, purposeful micro-drift over a dominant path.
- **Required fields:** Dominant path; intensity qualifier; subject relation; stable horizon rule; end settle.
- **Stable relationship:** The framing remains readable and path-led; motion is not random shake.
- **Compatible with:** Follow tracking, lead tracking, fixed focus, brief whip pan.
- **Conflicts with:** Locked-off; exact reference path unless micro-drift is explicitly layered; chaotic shake.
- **Seedance-ready phrase:** `Controlled handheld follow, restrained micro-drift over a clear forward path, keep the actor’s face readable, settle before the final line.`

### Shoulder camera

- **Physical change:** Shoulder-mounted operator movement carries human-weight sway and responsive reframing.
- **Required fields:** Dominant path; proximity; sway restraint; subject blocking; end framing.
- **Stable relationship:** Retain readable composition and an intentional operator response to action.
- **Compatible with:** Documentary follow tracking, controlled handheld, rack focus.
- **Conflicts with:** Locked-off; precision white-model path treated as rigid; perfectly frictionless gimbal language.
- **Seedance-ready phrase:** `Shoulder camera stays close beside the speaker, subtle human sway but readable framing, reframe to the listener, settle at the exchange end.`

## Transition moves

### Hard cut

- **Physical change:** No continuous camera movement is implied across the edit; the shot changes at a named point.
- **Required fields:** Outgoing end frame; cut trigger; incoming start frame; continuity relationship; audio intent.
- **Stable relationship:** Preserve only the stated match element, such as gaze, motion direction, or sound.
- **Compatible with:** Any settled shot; match cut; whip-pan cut destination.
- **Conflicts with:** A one-shot requirement; an unnamed cut that reads as accidental.
- **Seedance-ready phrase:** `Hold the close-up until the door slams, then hard cut to the exterior wide with the slam continuing in audio.`

### Match cut

- **Physical change:** Two shots cut by matching a specified shape, action, orientation, or composition.
- **Required fields:** Outgoing match element; incoming match element; cut point; intentional difference; continuity rule.
- **Stable relationship:** Name what matches so the edit is not mistaken for a continuous camera path.
- **Compatible with:** Hard cut, graphic transition, repeated subject pose.
- **Conflicts with:** One-shot requirement; vague `match` with no shared element.
- **Seedance-ready phrase:** `Match cut from the round cup seen from above to the full moon in the same centered circular framing.`

### Whip-pan transition

- **Physical change:** A settled start rotates rapidly with intentional blur, then reaches a settled end or an explicit cut destination.
- **Required fields:** Settled start; rotational direction; blur interval; settled end or cut destination; readable-action placement.
- **Stable relationship:** A whip pan requires a settled start, rapid rotational blur, and a settled end or explicit cut destination.
- **Compatible with:** Tripod pan, controlled handheld, hard cut at the blur peak.
- **Conflicts with:** Long readable action during the blur; undefined destination; locked-off.
- **Seedance-ready phrase:** `Settle on the actor’s reaction, whip pan right into brief motion blur, then settle on the arriving car; keep readable action before and after the whip.`

### Occlusion wipe

- **Physical change:** A foreground object or darkness intentionally covers the lens/frame and reveals the next view.
- **Required fields:** Occluding object; entry direction; full-cover moment; reveal target; continuity/edit rule.
- **Stable relationship:** The occluder must be physically motivated by the path or subject blocking.
- **Compatible with:** Follow tracking, doorway handoff, match cut, white-model clearance reference.
- **Conflicts with:** A promised uninterrupted readable view; unaddressed geometry collision.
- **Seedance-ready phrase:** `Follow the actor until a passing coat fills the frame as an occlusion wipe; reveal the actor entering the next room on the same walking direction.`

### Dissolve

- **Physical change:** Two images overlap over a deliberate edit interval; it is not continuous physical camera travel.
- **Required fields:** Outgoing held frame; incoming start frame; shared motif; dissolve purpose; final settled frame.
- **Stable relationship:** Declare the visual or temporal link between layers and where the dissolve ends.
- **Compatible with:** Locked-off frames, slow pushes, memory/time transition.
- **Conflicts with:** One-shot requirement; rapid readable action that must stay unambiguous.
- **Seedance-ready phrase:** `Hold the empty chair, dissolve into the same chair at sunrise, end on the new wide frame with no implied camera teleport.`

## Combination rules

- Assign body translation, aim rotation, lens behavior, focus behavior, and subject blocking to separate clauses. Example: `truck camera left; pan right to retain the actor; rack focus from sign to face` is clearer than `move left around actor.`
- Choose one primary move per beat. Add a secondary move only when it has a distinct job and independent required fields.
- Use `dolly` when perspective/parallax should change. Use `optical zoom` when focal-length change from a fixed position is intended. Use a `dolly zoom` only when opposite movements intentionally preserve apparent subject size.
- Describe clockwise/counterclockwise orbit from the camera's view and name whether the subject is stationary, walking, or spinning independently.
- Treat a turntable as subject rotation: `subject rotates on turntable; camera remains fixed`—never substitute it for an orbit.
- Keep rack focus separate from motion: it changes focus target, not camera position or aim.
- For a continuous scene, place a readable action in settled portions of the beat; reserve a whip-pan blur for an intentional transition or explicitly state its cut destination.
- For one-shot work, say `one continuous shot; no cuts` and use only physically contiguous paths. For edits, name every allowed cut point and its matching continuity element.

## Conflict matrix

| Pair | Verdict | Repair |
| --- | --- | --- |
| Locked-off + orbit | Conflict | Choose locked framing or an orbit beat, not both. |
| Pan + lateral tracking | Distinct; combine only deliberately | Name camera translation and pan target separately. |
| Tilt + crane rise | Compatible when motivated | State rising path and independent aim behavior. |
| Push-in + zoom-in | Usually redundant | Choose dolly for parallax or zoom for optical compression. |
| Dolly-in + zoom-out | Compatible special effect | State subject size remains stable and background perspective changes. |
| Orbit + subject spin | High ambiguity | Assign camera orbit and subject rotation separately with directions. |
| Handheld + exact reference path | Risky | Use controlled micro-drift layered over the reference path or omit handheld. |
| Whip pan + long readable action | Conflict in the blur interval | Put readable action before or after the whip. |
| Rack focus + fixed focus on another target | Conflict | Choose the focus handoff or retain a single target lock. |
| Pan + truck with one direction word | Ambiguous | State `truck camera left; pan right to keep target framed`, with separate targets if needed. |
| Tilt + pedestal/crane described as one move | Ambiguous | State body height path and vertical aim behavior independently. |
| Orbit + locked horizon + roll | Conditional | Keep the horizon level or name a deliberate roll as a separate effect. |

## Reference-driven camera paths

### Priority order

1. Clean white-model/previs or camera-path video.
2. Start/end frames plus path prose.
3. Timestamped camera prose.
4. Generic camera keywords.

Use this as priority for camera-path evidence, while retaining the overall reference hierarchy in [model-differences.md](model-differences.md). Preserve each visible UI reference tag exactly. A reference gives strong directional evidence, not a guarantee of literal path, timing, camera settings, or collision behavior.

### Split path and actor instructions

Write separate clauses whenever both are present:

- **Camera-path reference clause:** identify the reference tag; state its source role; specify camera geometry/path/framing to transfer; state allowable visual replacements.
- **Actor-motion reference clause:** identify the reference tag; state performer/body action, pace, interaction, and what must not be inherited as camera motion.

Example: `Camera path: [PATH_TAG] is a white-model reference for the gimbal route only—preserve its doorway approach, left turn, and final wide framing; replace all materials, people, and lighting. Actor motion: [ACTOR_TAG] supplies the dancer's arm sequence only; do not inherit its camera movement.`

### White-model transfer fields

For any white-model/previs reference, write all six fields:

| Field | Direction to supply |
| --- | --- |
| Source role | Identify it as white-model/previs or camera-path video, and name the exact UI tag. |
| Geometry to preserve | Name spatial anchors such as doorway, corridor, stairs, furniture, elevation, and left/right turn. |
| Path to preserve | Give a contiguous camera route, start state, landmarks, movement direction, and end state. |
| Allowable visual replacement | State what may change: materials, lighting, characters, style, set dressing, or environment. |
| Collision handling | State clearance, camera handoff, occlusion, or route adjustment at doors, walls, stairs, and narrow passages. |
| Final framing | Name the final shot size, target placement, focus, horizon/angle if material, and whether to settle or cut. |

If camera and actor references disagree, say which governs each dimension rather than asking for an impossible blend. Narrowly revise the failing beat or reference assignment before changing unrelated direction.

## Failure diagnosis

| Symptom | Likely ambiguity | Repair |
| --- | --- | --- |
| Unwanted cut | Continuity was not selected or permitted cuts were not named. | Explicitly select `one continuous shot; no cuts`, or name allowed cut points with outgoing/incoming frames. |
| Subject leaves frame | No tracking relationship, end framing, or source headroom was specified. | State camera-to-subject relationship, end framing, and source headroom/lead room. |
| Orbit becomes subject spin | The moving agent and rotation directions were unassigned. | State `camera moves around a stationary/independently moving subject`; assign camera orbit and subject rotation separately. |
| Dolly looks like zoom | Physical body travel and parallax were omitted. | State physical camera travel and the expected foreground/background parallax. |
| Camera path jumps | Beats lack contiguous start/end states or the path evidence is weak. | Give contiguous start/end states per beat, or use a clean path reference. |
| Handheld becomes chaotic | Shake was requested without a dominant route or restraint. | Request restrained micro-drift and retain a dominant path. |
| Door/wall collision | Geometry, clearance, or the shot handoff was unspecified. | Use white-model geometry or describe clearance and camera handoff. |
| Late drift in 30s | Later beats have no resolved targets. | Allocate 6–8s beats and give every beat an end state; this is a heuristic, not a duration guarantee. |

## Community vocabulary cross-check

The community guide [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) independently uses common terms such as slow push in/dolly in, dolly out, tracking shot, crane up, steadicam follow, orbit, whip pan, locked off, top-down, handheld, gimbal, rack focus, and FPV continuous long take. Treat this only as a vocabulary cross-check, not proof of dedicated Seedance controls. See [community-api-prompts-analysis.md](community-api-prompts-analysis.md) for provenance and exclusions.

Normalize those short keywords through this reference before drafting: decide whether the camera body translates, the aim rotates, the lens changes, or focus moves; then add start framing, physical route, direction, speed, subject relation, end framing, and settle/cut behavior. For example, expand a bare tracking shot left into either side tracking or truck-left plus a separately named pan target. Expand rack focus with near target, far target, transfer order, and final focus target. Expand orbit with target, camera-relative direction, arc intent, radius, and end angle.

Do not copy a camera-word list into the prompt. Select one dominant move per beat, express the physical behavior, and reject conflicts using the matrix above.

## Quick phrase library

Use these as copy-ready direction. They describe intent; exact degrees, speeds, focal lengths, and frame timing are not guaranteed unless the current interface or an uploaded reference exposes them.

| Korean phrase | Concise English camera terminology | Use |
| --- | --- | --- |
| `고정된 카메라 위치에서 오른쪽으로 팬하여 배우에게 멈춘다.` | `Pan right from a fixed position and settle on the actor.` | Horizontal aim rotation, no body travel. |
| `카메라 본체가 왼쪽으로 트럭 이동하고, 배우를 유지하려고 오른쪽으로 팬한다.` | `Truck camera left; pan right to retain the actor.` | Separate translation from aim. |
| `물리적으로 돌리 인하며 전경과 배경의 패럴랙스가 변한다.` | `Physical dolly in; foreground/background parallax changes.` | Perspective change through travel. |
| `카메라는 고정하고 광학 줌인한다; 패럴랙스 변화는 최소화한다.` | `Keep camera fixed; optical zoom in with minimal parallax change.` | Lens change, not dolly. |
| `카메라가 인물 주위를 시계 방향으로 오빗하고, 인물은 독립적으로 정지해 있다.` | `Camera orbits clockwise around a stationary subject.` | Avoids orbit/subject-spin ambiguity. |
| `전경의 열쇠에서 창가의 얼굴로 랙 포커스한다; 카메라 이동은 없다.` | `Rack focus from the foreground key to the face; no camera move.` | Focus-only shift. |
| `짐벌로 인물 뒤를 부드럽게 따라가며 수평선을 안정적으로 유지한다.` | `Smooth gimbal follow; stable horizon.` | Stabilized follow route. |
| `절제된 핸드헬드 미세 흔들림을 유지하되, 주된 전진 경로를 따른다.` | `Restrained handheld micro-drift over a dominant forward path.` | Controlled handheld, not chaos. |
| `시작 구도를 안정적으로 잡은 뒤 오른쪽으로 빠르게 휩팬하고, 자동차에서 다시 안정화한다.` | `Settle, whip pan right through blur, settle on the car.` | Whip-pan transition with readable endpoints. |
| `화이트 모델 참조의 문 통과 경로와 최종 와이드 구도를 보존하고, 재질과 조명만 교체한다.` | `Preserve the white-model doorway path and final wide; replace only materials and lighting.` | Camera-path reference transfer. |
| `배우 동작 참조와 카메라 경로 참조를 별도 절로 지정한다.` | `Assign actor-motion and camera-path references in separate clauses.` | Prevents reference-role collision. |
| `6–8초 비트마다 끝 구도를 명시한다.` | `Give each 6–8s beat an end frame.` | Planning heuristic for long scenes. |
