# Multi-Turn Revision Scenarios

Apply the skill to each conversation as a behavioral review. The final answer must follow the normal output contract; the checks below inspect only active prompt content.

## Scenario 1: Camera replacements

Initial state:

- 6–14s: slow dolly-in.
- 14–24s: clockwise orbit.

Turns:

1. “Replace the 6–14s dolly with a locked-off medium shot.”
2. “Replace the 14–24s orbit with a left-side tracking move.”

Pass criteria:

- `locked-off` is the sole primary move in 6–14s; no dolly route or approach speed remains.
- `left-side tracking` is the sole primary move in 14–24s; no orbit arc or orbit tangent remains.
- Each changed beat has compatible start, path or fixed rig, speed, blocking, focus, and end framing.
- Retired moves do not appear as negative reminders.

## Scenario 2: Delete action and retime

Initial state:

- 0–6s approach.
- 6–14s pick up a key, with key-jingle audio, rack focus to the key, and a close-follow camera cue.
- 14–24s open the door.
- 24–30s enter the room.

Turn:

“Delete picking up the key. Rebuild the timing as 0–10s approach, 10–22s open the door, 22–30s enter.”

Pass criteria:

- Only `0–10s`, `10–22s`, and `22–30s` remain.
- The ranges cover 0–30 seconds without overlap or an unrequested gap.
- The key action, key-jingle, key focus, key prop lock, and pickup camera cue are absent.
- Subject, camera, and audio use the same active ranges.

## Scenario 3: Compatible addition

Initial state:

- Final beat uses a slow physical push-in focused on the subject's face.

Turn:

“Keep the push-in and also add a rack focus from the foreground glass to the face after the subject stops.”

Pass criteria:

- The push-in remains the single translational primary move.
- Rack focus is an added focus event with a start target, end target, and timing after the stop.
- The final framing and focus target are mutually compatible.

## Scenario 4: Accumulated edits near the limit

Initial state:

- Seedance 2.5 prompt around 4,700 characters, or Fast prompt around 3,900 characters.

Turns:

1. Add a blue coat while preserving identity.
2. Replace warm sunset lighting with cold overcast daylight.
3. Remove BGM but keep diegetic footsteps.
4. Replace the final frame with a settled waist-up doorway frame.
5. Replace the final camera speed with a slow deceleration.

Pass criteria:

- Only the blue coat, cold overcast light, diegetic footsteps, new final frame, and slow deceleration remain active.
- Retired wardrobe, warm light, BGM, old final frame, and old speed are absent.
- All required structural blocks remain.
- The active prompt is at most 5,000 characters for 2.5 or 4,000 for Fast.
- Simplified Chinese fallback, if used, translates the active brief only and does not revive retired values.
