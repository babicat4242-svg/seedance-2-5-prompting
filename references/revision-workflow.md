# Seedance Multi-Turn Revision Workflow

Use this reference whenever a user changes an existing Seedance 2.5 or explicit Seedance 2.0 Fast prompt. Its purpose is to prevent revision history from becoming prompt content.

## Canonical active brief

Before drafting, reduce the conversation and current prompt to one active state:

| Layer | Active fields |
| --- | --- |
| Output | profile, mode, duration, aspect/output intent, one-shot or edited structure |
| References | exact tag, primary role, permitted secondary role, priority, exclusions |
| Story | scene geometry, subject identity/state, action order, beat ranges |
| Camera | purpose, start, move, path, speed, blocking, lens/focus, end, continuity |
| Look | lighting, atmosphere, style, exposure continuity |
| Audio | clean, diegetic, scored, or source-transfer; timed cues and exclusions |
| Finish | final frame, handoff state, continuity locks, UI qualifications |

The previous prompt is evidence for these fields, not a string to edit in place. Keep only values that remain active after the newest request. Do not store retired instructions as negative reminders.

## Operation classifier

- `ADD`: retain the current value and add a compatible value. Use only for explicit language such as “also,” “add,” “keep X and add Y,” or “both.”
- `REPLACE`: remove the prior value in the named layer and install the new value. “Change,” “instead,” “make it Y,” and “use Y” default to replacement when they target an existing value.
- `DELETE`: remove the named value and every clause that depends only on it. “Remove,” “delete,” “drop,” “without,” and “빼/삭제” signal deletion.
- `REORDER`: preserve the requested active events but rebuild their order, beat ranges, transitions, and camera coordination.
- `RETIME`: replace the active range set with the newest range set, then align subject, camera, audio, focus, and final-frame cues to it.
- `PRESERVE`: lock the explicitly named value while another layer changes. It does not protect values that the same or a later instruction replaces or deletes.
- `RESET`: discard the named scope—such as the camera plan, audio plan, or ending—and rebuild it from the new direction.

A request may contain several operations. Apply them in conversational order, with the latest explicit instruction winning inside the same field. If “add” would create two incompatible primary camera moves in one beat, ask only when intent cannot be resolved; otherwise keep the newly requested move as primary and convert the compatible secondary behavior into a subordinate rig, aim, or focus clause.

Apply the same compatibility check inside every control channel, including focus, audio, lighting, geometry, and subject state. If the user gives a clear order, timing, or condition, sequence the values into non-overlapping phases; otherwise ask one narrow question instead of preserving contradictory values.

## Precedence and retirement

Use this precedence order:

1. The newest explicit user instruction for the field.
2. Explicit current-turn `PRESERVE` locks.
3. Active non-negotiables that do not conflict with items 1–2.
4. Assigned reference roles and priorities.
5. Values inferred from the previous prompt.

When a higher item conflicts with a lower item, retire the lower value. Retired values must be absent from the copy-ready prompt, asset-role map, camera rationale, and retry instruction. Do not write “no orbit” merely to counter a retired orbit unless the user independently requires orbit exclusion as an active constraint.

## Dependency cleanup

After applying the revision, remove or rebuild downstream instructions:

- Deleting a subject action also removes its exclusive prop state, sound cue, focus cue, reaction, and camera-follow instruction.
- Replacing lighting also removes obsolete exposure, shadow-direction, reflection, color-temperature, and continuity locks.
- Removing music also removes beat sync, score mood, tempo, and mix instructions while retaining explicitly requested diegetic sound.
- Replacing the final frame also updates the resolution beat, camera settle, focus target, prop state, and extension handoff.
- Reordering or retiming beats replaces the old range set everywhere. Cover the full duration without overlap or unrequested gaps.
- Changing an asset role removes old permitted inheritance and exclusions that no longer apply.

After cleanup, scan each functional block for names, states, ranges, and directions that refer only to a retired value.

## Camera recompile

For every affected beat, rebuild this chain rather than swapping only the move name:

```text
purpose → start framing → primary move → path/direction → speed
→ subject blocking → lens/focus → end framing → continuity/edit
```

Apply these invariants:

- One primary camera move per beat.
- A replaced move's route, tangent, speed, blocking assumptions, focus behavior, and end framing are revalidated; they are preserved only when still physically compatible.
- A locked-off replacement has no residual dolly, truck, crane, or orbit translation in that beat.
- A dolly replacement uses physical camera travel and does not retain optical-zoom language.
- A side-track replacement defines the camera's side, travel direction, subject-screen relationship, clearance, and end frame; it does not retain an orbit arc.
- Reordered subject action forces the camera's beat timing and arrival states to be rebuilt from the new action order.
- The end state of one beat must be a physically compatible start state for the next in a one-shot route.

Use [camera-motion.md](camera-motion.md) for the physical vocabulary and collision checks after precedence is resolved here.

## Compile sequence

1. Parse the newest request into one or more operations.
2. Apply the operations to the canonical active brief.
3. Mark displaced values as retired and remove their dependencies.
4. Rebuild the active subject timeline.
5. Recompile affected camera beats and timed audio/focus cues.
6. Check contradictions, path continuity, beat coverage, density, and final-frame compatibility.
7. Draft one complete replacement prompt using the normal shared structure.
8. Count only that active prompt. If it exceeds the limit, compress or translate the active brief—not the revision history.

Do not expose the operation ledger, retired values, or compile notes inside the copy-ready prompt.

## Worked revision cases

### Replace a camera move

Active beat: `6–14s slow dolly-in toward the subject.`

User: “Change that beat to locked-off.”

Operation: `REPLACE` the beat's camera move. Retire the dolly travel, approach speed, and any end frame caused only by the push-in. Rebuild the beat with a fixed camera position, stable framing, subject blocking that works inside the frame, and a compatible static end frame. The final prompt contains no dolly instruction or negative reminder about dolly.

### Delete an action and retime

Active beats: `0–6 approach / 6–14 pick up key / 14–24 open door / 24–30 enter.`

User: “Delete picking up the key and use 0–10 approach / 10–22 open door / 22–30 enter.”

Operations: `DELETE` the key action and `RETIME` the scene. Remove the key prop state, pickup sound, key focus cue, and pickup camera behavior. Use only the three new ranges across subject, camera, audio, and final-frame planning.

### Replace lighting and remove music

User: “Change golden-hour light to cold overcast daylight, and remove the BGM but keep footsteps.”

Operations: `REPLACE` lighting and `DELETE` scored music with `PRESERVE` for footsteps. Retire warm rim-light, sunset color, musical tempo, and score sync. Keep diegetic footsteps and rebuild exposure continuity for the overcast state.

### Add a compatible focus event

User: “Keep the final push-in and also add a rack focus from the foreground glass to the face after the subject stops.”

Operations: `PRESERVE` the push-in and `ADD` the rack focus. Keep one translational primary move and add the focus event only after the subject settles, with explicit start target, end target, and timing.

### Multiple edits near the limit

After every edit, discard retired wardrobe, lighting, audio, ending, speed, and timeline values before counting. Keep the same complete structure for 2.5 and Fast. Translate to concise Simplified Chinese only if the canonical active prompt still exceeds 5,000 characters for 2.5 or 4,000 for Fast.
