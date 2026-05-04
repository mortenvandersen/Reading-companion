---
slug: distillation
first_seen: 2026-05-04
articles:
  - 2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md
tags: [ai, training, competitive-strategy, ip]
---

# Distillation

## Definition

A model-training technique in which a smaller / cheaper model ("student") is trained on the outputs of a larger, more capable model ("teacher"). The student learns to mimic the teacher's behavior at a fraction of the original training cost.

Distillation is a legitimate, widely used technique — frontier labs distill their own models internally to ship cheaper variants. It becomes a strategic problem when **competitors distill *your* model** to fast-follow your capabilities without paying for the underlying R&D and compute.

## Origin

ML technique, mainstream since ~2015 (Hinton et al., "Distilling the Knowledge in a Neural Network"). Became a strategic / competitive issue in 2024-2025 with the rise of open-source frontier models that appeared to be distilled from closed labs.

## Examples across articles

- [2026-05-04 Mythos, Muse, and the Opportunity Cost of Compute](../articles/2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md):
  - Anthropic publicly accused DeepSeek, Moonshot, and MiniMax of running "industrial-scale" distillation campaigns: ~16M Claude exchanges via ~24,000 fraudulent accounts, in violation of TOS.
  - Strategic significance: distillation lets open-source competitors fast-follow at a tiny fraction of the cost. This compresses frontier-lab pricing power *and* — Ben's deeper point — denies frontier labs access to compute supply that open-source models would otherwise consume.
  - Anthropic's anti-distillation push is therefore both *defensive* (margin protection) and *offensive* (an [opportunity-cost play](./ai-compute-opportunity-cost.md) to free up hyperscaler compute they can buy).

## My working understanding

(TBC)

## Evolution

- 2026-05-04 — first captured. Note the dual nature: distillation is the standard way labs ship cheap variants of their own models *and* the standard way competitors steal their work. The line is whether the teacher model was used with permission.

## Open threads

- **Is anti-distillation enforceable?** TOS violations + account bans are slow. Watermarking model outputs (so distillation can be detected post-hoc) is technically possible but not yet standard. Without enforcement, the strategic threat compounds.
- **What's the equivalent of "fair use" for AI distillation?** Open-source labs argue they're advancing the field; closed labs argue it's IP theft. Likely heading to court / regulation eventually.
- **Does distillation actually preserve the gap, or just close it?** A distilled student is bounded by the teacher's quality. If the frontier keeps moving, distillation always lags. If it plateaus, distilled models catch up. So anti-distillation is most valuable in regimes where progress is *fast* (lab can keep ahead) and least valuable where progress is *slow*.
