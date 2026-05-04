---
slug: zero-marginal-costs
first_seen: 2026-05-04
articles:
  - 2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md
tags: [framework, economics, internet, foundational]
related:
  - aggregation-theory
  - ai-compute-opportunity-cost
---

# Zero Marginal Costs

## Definition

In a typical physical-goods business, **marginal cost** is what it costs to make one more unit (raw materials, energy, labor that scales with output). Marginal cost provides the price floor: as long as price > marginal cost, the business will keep producing even if it's losing money on fixed-cost depreciation.

In tech, marginal cost is approximately zero: digital outputs have no raw-material cost, and the fixed costs (servers, talent) are so large that energy and headcount get treated as fixed too. You'll always run your servers at full capacity, because every additional unit of revenue is profit at the margin.

This is the structural feature that underpins most of internet-era economics. It's the substrate under [Aggregation Theory](./aggregation-theory.md), the App Store's 30% take, hyperscaler economics, and the entire "scale-then-monetize" playbook.

## Origin

Foundational economics concept; applied to tech most prominently by Carl Shapiro and Hal Varian (*Information Rules*, 1998) and woven into Ben Thompson's Aggregation Theory thereafter.

## Examples across articles

- [2026-05-04 Mythos, Muse, and the Opportunity Cost of Compute](../articles/2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md):
  - Doug O'Laughlin's claim: AI broke zero-marginal-cost economics; therefore Aggregation Theory is dead.
  - Ben's correction: AI compute is *still* effectively a fixed cost, not a marginal cost. The chips are running either way. The misnamed "marginal cost" is actually [opportunity cost](./ai-compute-opportunity-cost.md). Zero-marginal-cost economics survives in modified form.

## My working understanding

(TBC)

## Evolution

- 2026-05-04 — first captured. The most interesting current question: does AI inference (especially at frontier scale) actually preserve zero-marginal-cost economics, or do massive electricity + chip-depreciation costs at scale reintroduce marginal cost meaningfully? Ben says fixed costs dominate so much that marginal cost rounds to zero; O'Laughlin says no. Worth tracking as inference economics mature.

## Open threads

- **Is electricity a marginal cost at AI inference scale?** Energy has historically been ~5-10% of data center TCO, treated as fixed. At frontier-AI scale (GW data centers) this may flip — energy is closer to chip cost in some configurations. If energy becomes a meaningful fraction of inference cost and varies with utilization, marginal cost is non-trivial again.
- **Does the framework hold for agentic workloads?** Agents consume orders of magnitude more tokens per task than chat. If each task has a meaningful per-token cost passed back to the user, the marginal-cost-zero abstraction breaks for the *user-facing pricing model* even if it holds at the infrastructure level.
