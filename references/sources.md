# Seedance 2.5 Source Notes

Retrieved: 2026-08-03

## Source priority

1. The current visible Dreamina or CapCut product interface and its current live model page decide availability and selectable controls.
2. Current official product pages establish published capability claims.
3. Official prompt and camera guides establish vocabulary and planning guidance.
4. Older official articles are supporting context only when they agree with the current product page; otherwise retain them as a provenance warning.
5. Community repositories may supply vocabulary, examples, and cross-checks, but never override the visible UI or official capability sources.

Use the capability labels in `model-differences.md`: published capability is not a promise that a control appears in a particular account, region, or mode.

## Official capability sources

- [Official Seedance 2.5 AI Video Generator](https://dreamina.capcut.com/seedance/seedance-2-5) — current live model/product page for the marketed 30-second standard duration, beta long-video wording up to 180 seconds, up to 50 multimodal references, R2V, localized editing, multilingual workflow, and clean output claims. Treat the beta and interface-facing details as UI-dependent.
- [Seedance 2.5 vs Seedance 2.0](https://dreamina.capcut.com/seedance/seedance-2-5-vs-seedance-2-0) — migration framing: common 2.0 4–15s workflow versus 2.5 30-second generation, 12 versus 50 references, camera direction, white-model previsualization, and related Upscale context.
- [How to use Seedance 2.5](https://dreamina.capcut.com/seedance/how-to-use-seedance-2-5) — workflow sequencing, camera examples, extended-duration wording, and multimodal setup. Use it to describe a workflow, not to infer a hidden control.
- [Seedance 2.5 for 30s AI Video Scene Control](https://www.capcut.com/tools/seedance-2-5) — timestamped prompts, 30-second scene control, extension language, and reference-guided creation. Verify the actual generation surface before promising a duration or extension path.

## Official camera and prompting sources

- [Seedance 2.5 prompt guide](https://dreamina.capcut.com/seedance/seedance-2-5-prompt) — prompt structure, shot-size-plus-move grammar, 6–8s beat guidance, end-resolution direction, and reference tagging examples. Beat lengths are compiler heuristics, not model guarantees.
- [Seedance 2.5 motion reference guide](https://dreamina.capcut.com/seedance/seedance-2-5-motion-reference-guide) — reference hierarchy, R2V, green-screen and white-model uses, timeline control, and narrow iteration.
- [Camera movements](https://www.capcut.com/resource/camera-movements) — distinctions among pan, tilt, push, pull, zoom, dolly zoom, tracking, arc, boom, and handheld or random movement. Use these terms precisely; a term does not create a dedicated model control.
- [Tracking shot](https://dreamina.capcut.com/resource/tracking-shot) — pan versus tracking and subject-relative motion.
- [Orbit videos](https://dreamina.capcut.com/resource/orbit-videos) — orbit target-lock behavior and orbit vocabulary.
- [Dollying camera movement](https://dreamina.capcut.com/resource/dollying-camera-movement) — dolly path plus start-frame and end-frame planning.

## Conflicting official pages

Some official pages retain pre-launch language while the current main Dreamina model page is the live product reference for Seedance 2.5. Resolve availability by preferring the current live product page and the visible interface; retain stale page language only as a warning against blindly copying an old launch status. If the current page's rendered copy and its interactive UI disagree, report that discrepancy and classify availability as `Beta/UI-dependent` until the user confirms their interface.

This rule deliberately separates a live product page from a claim that every visitor can currently select the model. It avoids converting stale launch copy or marketing copy into a universal availability statement.

## Community prompt references

- [Anil-matcha/awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — community collection used only to cross-check concise prompt ordering, timestamped shot-script notation, multimodal @Image/@Video/@Audio authoring conventions, and common camera vocabulary. Its README declares an MIT license, but GitHub did not expose a standalone license file during the 2026-08-03 review; paraphrase patterns and retain attribution instead of copying its prompt library. It is not an official ByteDance, Dreamina, CapCut, Volcano Ark, or provider-neutral specification. Do not promote third-party API limits, pricing, endpoint behavior, or model comparisons into official facts without separate primary-source verification.
- [Pinned analysis snapshot](community-api-prompts-analysis.md) — review and integration decisions for commit [f020c085cdaf3174279e361829cee1c8b09a37e4](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts/tree/f020c085cdaf3174279e361829cee1c8b09a37e4).

## Usage rule

For each prompt claim, cite the highest-priority official source above, attach an evidence label, and then check the user-visible UI for mode-specific controls. Preserve the exact user/UI reference tag, qualify feature availability when a control is not visible, and phrase camera, beat, timing, audio, and end-frame details as direction unless the interface or an uploaded reference makes them enforceable. When a community source is useful, label it as community guidance and use it only for authoring heuristics or vocabulary cross-checks.
