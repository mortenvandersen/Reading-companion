---
slug: aggregation-theory
first_seen: 2026-05-04
articles:
  - 2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md
tags: [framework, aggregation, internet, ben-thompson]
---

# Aggregation Theory

## Definition

Ben Thompson's central framework for the consumer-internet economy. The argument: in markets where distribution costs and transaction costs are zero, the value accrues to whoever owns the customer relationship — the *Aggregator* — rather than to suppliers. The Aggregator builds a direct relationship with users at scale, then commoditizes its suppliers by mediating their access to that user base.

Three preconditions for Aggregator dynamics:

1. **Direct relationship with users.**
2. **Zero marginal cost of serving each new user.** (See [zero-marginal-costs](./zero-marginal-costs.md).)
3. **Demand-driven multi-sided networks** with decreasing acquisition costs as the network grows.

Canonical examples: Google (search), Facebook (social), Amazon (e-commerce), Netflix (streaming), Uber/Airbnb (gig economy).

## Origin

Ben Thompson, *Stratechery*, articulated across multiple posts starting ~2015. Often referred to as "the central insight of the 2010s."

## Examples across articles

- [2026-05-04 Mythos, Muse, and the Opportunity Cost of Compute](../articles/2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md):
  - Doug O'Laughlin (Fabricated Knowledge, Jan 2025) declared the era of Aggregation Theory over because AI re-introduced marginal costs.
  - Ben's pushback: AI compute isn't a marginal-cost problem (you'll always run the chips), it's an *opportunity-cost* problem. The framework still applies; the binding constraint just shifted. See [ai-compute-opportunity-cost](./ai-compute-opportunity-cost.md).
  - Distribution and transaction costs are *still zero* for AI (ChatGPT zero-to-200M users in months proves it). So Aggregator preconditions hold.
  - Therefore: owning demand still trumps owning supply. The winners are those with the most compelling products who use that demand to fund the compute they need.

## My working understanding

(TBC)

## Evolution

- 2026-05-04 — first captured. Ben extends the framework to AI by reframing "marginal cost" critiques as "opportunity cost" reality. Sub-claim: in AI, owning *demand* still trumps owning *supply* (compute). OpenAI's massive forward-commitment to compute is the live counter-bet against this — the next 24 months will adjudicate.

## Open threads

- **Does Aggregation Theory cleanly apply to AI, or is it now a hybrid?** "Distribution + transaction costs zero" is intact, but if product quality scales with capex, the demand/supply distinction collapses into a flywheel (more compute → better model → more revenue → more compute). That's a scale economy with positive feedback, not classical Aggregation. Worth resolving.
- **Aggregation Theory was always about consumer markets.** Ben acknowledges enterprise AI was never Aggregation territory. So the framework's relevance to AI may be limited to the consumer-AI race (Meta vs. OpenAI vs. Google). Track which AI battles are framed in Aggregation terms vs. not.
- **What's the equivalent framework for B2B AI / enterprise?** Ben hasn't proposed one yet that I've seen. The opportunity-cost reframe gestures at it but isn't a full alternative.
