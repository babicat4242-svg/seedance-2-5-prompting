# Seedance 2.5 Capability and Migration Reference

## Contents

- Evidence labels define how downstream guidance may state a claim.
- The migration table separates published capabilities from compiler heuristics.
- The remaining sections cover references, duration, audio, interface variability, and unsafe claims.

## Evidence labels

- `Confirmed`: stated on a current official Dreamina or CapCut page and not contradicted by a newer live page.
- `Beta/UI-dependent`: officially described but dependent on rollout, account, region, mode, or visible interface.
- `Heuristic`: a prompting recommendation, not a model guarantee.
- `Unverified`: exclude from confident output unless the user confirms it in their interface.

Use the label with the claim, rather than silently converting a page description into an interface guarantee. The dated claim-to-source mapping is in [sources.md](sources.md).

## 2.0 to 2.5 migration table

| Topic | Seedance 2.0 baseline | Seedance 2.5 handling | Status |
| --- | --- | --- | --- |
| Standard duration | Common 4–15s workflow | Up to 30s continuous standard generation | Confirmed |
| Long duration | Extension/stitching | 5–180s extended/long-video mode where exposed | Beta/UI-dependent |
| Reference capacity | Up to 12 combined inputs in the legacy skill | Up to 50 multimodal inputs in Omni reference mode | Confirmed capability; UI availability may vary |
| R2V | General multimodal reference transfer | Green-screen and white-model references for motion, spatial layout, and interaction | Confirmed |
| Local repair | Broad regeneration or extension | Localized/region editing while preserving surrounding continuity | Confirmed capability; exact controls UI-dependent |
| Camera | Basic keyword list | Shot size plus move, reference path, timing, blocking, and end framing | Confirmed guidance plus heuristic compiler |
| Beat length | Fixed 3s segmentation | 6–8s narrative beats by default; finer timestamps for action/sync; 3–4s resolution | Heuristic grounded in official prompt guidance |
| Audio | Often forced BGM in legacy skill | Clean, diegetic, scored, or source-transfer mode chosen deliberately | Confirmed options plus heuristic selection |
| Reference tags | Legacy lowercase examples | Preserve the exact tag shown by the UI/user, including case | Confirmed examples vary; safest interface rule |
| Output resolution | Legacy skill claimed up to 2K | Official pages market 4K/native 4K and also describe Upscale | Confirmed marketing claim; exact delivery path UI-dependent |

## Reference hierarchy

1. Treat uploaded references and their visible UI tags as the highest-priority creative evidence. Preserve the tag exactly as supplied, including case; do not normalize legacy examples.
2. Separate the job of each reference: identity/style, spatial layout, motion path, interaction, or audio. R2V material is most useful when a green-screen or white-model reference makes motion and blocking visible.
3. Use text to resolve intent that is not encoded in the reference: shot size, move, timing, lighting, action, and ending frame. Keep conflicting requests explicit so the user can decide which source should win.
4. Iterate narrowly: change the reference assignment or the affected beat before rewriting unrelated direction. This is a `Heuristic`, even where region editing is described officially.

`완전히 참조`, exact degrees, metric coordinates, focal lengths, apertures, camera speeds, and frame-perfect timing are intent signals unless an interface control or uploaded reference makes them enforceable. Do not represent them as literal model controls.

## Duration and beat planning

- Plan a standard request as one continuous scene of up to 30 seconds when the current interface exposes that duration (`Confirmed` capability; verify the selected mode).
- Treat 5–180s extended or long-video work as `Beta/UI-dependent`: inspect the visible mode, limits, and extension path before promising it.
- Use 6–8 second narrative beats as the default planning rhythm. For action or synchronization, use finer timestamps and resolve events to approximately 3–4 seconds. Both are `Heuristic` compiler choices grounded in official prompt guidance, not a required segmentation scheme.
- State the end frame or resolution for each beat so transitions, extensions, and local repairs have a target. The instruction is useful direction, not proof that a precise frame will result.

## Audio modes

- **Clean:** request no incidental soundtrack, subtitles, or dialogue when the clip should remain editable. Clean output is an officially marketed outcome; verify visible audio settings when they matter.
- **Diegetic:** describe only sounds produced by the scene (for example, footsteps or an engine). This is a prompt policy, not a separate confirmed model toggle.
- **Scored:** specify the intended music role, timing, and mood. Confirm the available soundtrack or audio controls in the interface.
- **Source-transfer:** bind an uploaded audio source only when the current UI accepts and tags it. The exact transfer behavior is `Beta/UI-dependent` unless the interface exposes it.

Choose one mode deliberately and make silence, speech, music, and sound effects non-conflicting. That selection rule is a `Heuristic`.

## Interface-dependent behavior

- Availability, long-video mode, reference count, audio inputs, regional repair controls, output delivery, and rendering options can vary by rollout, account, region, selected model, and current UI.
- A page-level capability establishes a supported product direction; the visible interface establishes what the current user can select.
- Ask for a screenshot or the visible control labels when a prompt depends on a particular duration, reference tag, audio route, edit region, or export setting.
- Mark missing controls as `Unverified`; offer a fallback prompt rather than inventing a setting.

## Claims to avoid

- Do not claim that the model reproduces a reference, camera path, timing, identity, audio, or text with perfect fidelity.
- Do not turn marketing claims for 4K, continuity, local editing, or multimodal input into a promise about a specific account's output.
- Do not infer a launch state, feature rollout, duration limit, reference limit, output route, or regional availability from an older article.
- Do not use numerical lens, exposure, coordinate, speed, or degree values as though they are executable controls unless the user identifies the corresponding control.
