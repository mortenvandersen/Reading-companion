---
date: 2026-05-04
source: stratechery
source_url: https://stratechery.com/2026/mythos-muse-and-the-opportunity-cost-of-compute/
title: "Mythos, Muse, and the Opportunity Cost of Compute"
article_file: ../articles/2026-05-04-mythos-muse-and-the-opportunity-cost-of-compute-stratechery-by-ben-thompson.md
tags: [ai, aggregation-theory, opportunity-cost, openai, anthropic, meta, strategy]
concepts:
  - aggregation-theory
  - ai-compute-opportunity-cost
  - zero-marginal-costs
  - distillation
---

# Mythos, Muse, and the Opportunity Cost of Compute

## TL;DR

- Aggregation Theory isn't dead — the binding constraint just shifted from *marginal cost* to *opportunity cost*. AI compute is a fixed cost (you'll always run the chips you bought); the strategic question is *which workload* to point them at.
- Compute allocation is now the central strategic decision at every hyperscaler and frontier lab. Microsoft missed Azure expectations to feed Copilot. Anthropic restricting Mythos is partly compute allocation in safety language. The anti-distillation push is also offensive opportunity-cost play (denying compute supply to open-source competitors).
- Meta is structurally advantaged for consumer AI: no enterprise/cloud business = no opportunity cost on consumer compute, plus an existing ad-monetization stack. Ben argues Meta should open-source Muse (Llama playbook).
- OpenAI's ChatGPT consumer base has flipped from moat to drag — every consumer query is compute that didn't go to a higher-LTV enterprise customer. Inverse of the Aggregation Theory bet.
- Ben's call: owning demand still beats owning supply. OpenAI is wagering the opposite with massive forward-compute commitments. The piece is a thesis on which strategy wins the next 24 months.

## Where the discussion pushed back

### 1. "Demand trumps supply" — Ben asserts but doesn't argue it

Ben's own words, then walked past: *"if more compute is the key to better products, then does supply matter most?"* He doesn't answer. The empirical record this year cuts against him: OpenAI shipped o1, GPT-5-class scale-ups, and Sora because they bought the most compute earliest. If product quality is now a function of capex, the demand/supply distinction collapses into a flywheel: more compute → better model → more revenue → more compute. That's a scale economy, not Aggregation Theory.

### 2. "Own vs. rent compute" is the wrong frame

Both OpenAI and Anthropic *rent* — neither owns fabs or data centers. The real distinction is **how aggressively each forward-commits to supply**:

- **OpenAI:** over-commit early. Microsoft + Stargate + Oracle + Coreweave deals lock up multi-hundred-billion-dollar capacity ahead of demand. Bet: forward-commitment is a moat money alone can't replicate later, because chip and data-center buildout is the binding constraint.
- **Anthropic:** let supply follow demand. Sign for what you need, expect to acquire more as cash flow arrives. Bet: better product wins customers wins cash flow wins compute.

### 3. OpenAI's bet is positive-EV but high-variance

If demand for compute (industry-wide) keeps growing exponentially, over-building is mostly a timing error. Excess capacity gets absorbed. But that depends on three contestable conditions:

1. **Algorithmic efficiency gains don't outrun capacity expansion.** DeepSeek showed 5–10x gains were possible in 2024. If the next round comes, locked-in supply becomes overhang.
2. **Compute is fungible enough to resell.** True at the hyperscaler level (Microsoft can redirect to other Azure customers); less true at OpenAI's balance sheet — the obligations are *not* optional draws.
3. **Financing survives a demand-vs-supply lag.** Load-bearing. If demand catches up in 2027, fine. If it catches up in 2030, OpenAI may not exist to see it.

Honest read: Ben dresses up his demand-trumps-supply call as a *strategy* claim, but it's really a *risk-management* claim. Anthropic's strategy degrades gracefully if compute demand stalls; OpenAI's could collapse. They're choosing different points on the risk/return curve.

### 4. "Open-sourcing Muse costs Meta nothing" is sloppy

Ben's claim is rhetorical shorthand, not literal accounting. Real cost analysis:

- **Apple is the live risk.** Per the Cook piece, Apple just rented Gemini for Siri because they don't have their own frontier model. Open-source Muse hands Apple a free escape hatch — fine-tune Muse, run it on-device, kill the Gemini dependency. Meta would have handed its biggest consumer-surface competitor a critical capability.
- **ByteDance, Snap, X, Pinterest** each get a free model upgrade. Closes their quality gap to Meta.
- **Distribution moats are weaker for AI than for social.** Per Ben's own argument, AI distribution and switching costs are near zero — see ChatGPT zero-to-200M in months.

What survives: open-sourcing weights doesn't open-source inference cost; the actors who can fully exploit Muse are mostly Meta peers anyway; the Llama precedent (Meta gained position by open-sourcing) is real evidence. *Expected* damage to frontier labs >> *expected* damage to Meta's moat. So the move is positive-EV — just not zero-cost. Cost is concentrated on Apple specifically.

## Connection back to the Tim Cook piece

The Cook piece argued vertical integration — *own and control your primary technologies* — was Apple's structural identity, and that renting Gemini for Siri was strategic surrender. This piece argues the opposite for Anthropic: renting hyperscaler compute is fine because they own *demand*.

Hidden refinement of the Cook Doctrine: **own the layer where your differentiation accrues; rent the rest.** Apple's mistake isn't that they're renting — it's that they're renting the layer (intelligence) where their value (OS integration) is supposed to come from. Anthropic is renting the layer (compute) where their value (product, customer relationship) is *not* supposed to come from. Same principle, opposite conclusions, depending on where value accrues.

This raises a sharp question for OpenAI: what's their differentiation layer? If it's compute capacity (which Stargate implies), the principle says they're consistent. If it's product (ChatGPT), they're locking up the wrong layer at huge cost.

## Open questions

1. Does Aggregation Theory still apply cleanly to AI, or has the opportunity-cost shift created a hybrid model? Specifically: is "distribution + transaction costs are zero" enough to crown Aggregators when product quality now requires capex?
2. Will Apple use an open-source Muse (or a Llama-derivative) to break free of Gemini? If yes, "open-source costs Meta nothing" is disproven and Meta should rethink. Track this concretely over the next 12 months.
3. Is OpenAI's compute over-commitment a strategic moat or a financial liability? Resolution depends on (a) whether algorithmic efficiency gains collapse compute demand, (b) whether OpenAI's financing can survive a 12–24 month demand-vs-supply lag.

## Related past notes

- [2026-05-04 Tim Cook's Impeccable Timing](./2026-05-04-tim-cooks-impeccable-timing-stratechery-by-ben-thompson.md) — The Cook piece's "own and control" doctrine is refined here: own the *layer where value accrues*. Apple's Gemini-as-Siri and Anthropic's renting-of-hyperscaler-compute look like the same kind of move only if you ignore where value lives.
