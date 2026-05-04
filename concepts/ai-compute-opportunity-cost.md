---
slug: ai-compute-opportunity-cost
first_seen: 2026-05-04
articles:
  - 2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md
tags: [ai, strategy, capital-allocation, hyperscalers]
related:
  - aggregation-theory
  - zero-marginal-costs
---

# AI Compute as Opportunity Cost (not Marginal Cost)

## Definition

The strategic constraint in AI isn't *marginal cost* (the cost of running one more inference) — it's *opportunity cost* (which workload you point your compute at). AI chips are a fixed cost: you bought them, you're going to run them at full utilization. The decision that matters is which customer / product / market gets fed by those running chips, because compute spent on one workload cannot be spent on another.

This is the analytical reframe that keeps [Aggregation Theory](./aggregation-theory.md) alive in the AI era: the apparent return of marginal costs (compute is expensive!) misnames the constraint. The constraint is allocation, not cost.

## Origin

Ben Thompson, *Mythos, Muse, and the Opportunity Cost of Compute* (2026-05-04). Reframes Doug O'Laughlin's January 2025 "end of Aggregation Theory" claim.

## Examples across articles

Five actors, five different opportunity-cost trade-offs, all from the same article:

- **Microsoft.** Missed Azure growth expectations not because demand was short but because GPUs went to higher-LTV internal workloads (M365 Copilot, GitHub Copilot, R&D, talent retention). CFO Amy Hood explicitly admitted: had they fed all new GPUs to Azure, the growth number would've been "over 40." Trade-off: hyperscaler-for-customers vs. own-software-stack.

- **Hyperscalers generally.** Each balances three demands: external cloud customers, internal product workloads, and frontier-lab partner workloads. Microsoft (Azure / Copilot / OpenAI). Amazon (retail / AWS / Anthropic). Google (GCP / consumer / Anthropic stake). Every hour of compute is a vote on which business to grow.

- **Anthropic.** Compute-constrained. Mythos restricted to high-paying customers not just for safety theater but because broad release would cannibalize compute already serving paying customers. *Bonus:* the anti-distillation campaign is itself an offensive opportunity-cost play — denying open-source competitors the ability to use hyperscaler compute productively, so Anthropic can buy that compute instead.

- **OpenAI.** ChatGPT's massive consumer base — long treated as the moat — is now a *drag* on the strategic priority (enterprise / agentic workloads with higher gross margin and LTV). Until ad monetization at scale shows up, every consumer query is compute that didn't go to a paying enterprise customer. The most striking inversion in the piece: yesterday's distribution moat is today's opportunity cost.

- **Meta.** The structural outlier. *No* opportunity cost on consumer compute because no enterprise / cloud business exists to compete for chips. And the consumer compute is already monetized via ads. This is why Ben argues Meta should open-source Muse: hurts frontier labs, costs Meta little (see note's pushback re: Apple), locks in their consumer position.

## My working understanding

(TBC)

## Evolution

- 2026-05-04 — first captured. The through-line of the article: opportunity cost is the binding constraint for every player except Meta. Useful as a one-question diagnostic for AI strategy: *for actor X, what is the highest-LTV use of one more hour of compute?* The answer tells you what they're sacrificing to do anything else.

## Open threads

- **OpenAI's forward-commit bet is a literal attempt to escape the opportunity-cost trap by buying so much capacity that allocation isn't a zero-sum game.** Does that work? If yes, the opportunity-cost frame may have a shelf life. If no (algorithmic efficiency outruns capacity, financing breaks), it confirms the frame.
- **For incumbent companies considering AI: where does AI compete with existing internal compute spend?** The Microsoft Azure-vs-Copilot trade-off is a useful template — what's the equivalent at non-hyperscaler enterprises?
- **Is "opportunity cost > marginal cost" a feature of AI specifically, or any compute-constrained moment in tech?** The 1990s saw similar logic applied to bandwidth and server capacity. May not be as novel as Ben presents it.
