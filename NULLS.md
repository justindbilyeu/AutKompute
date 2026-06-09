# NULLS.md — Formal Null Hypotheses Under Test

## AutKompute v0.1

These nulls are inherited from GUES v0.2 and the adversarial review session (Sage, charter mode, June 2026).

All thresholds are set before any data is examined. No post-hoc adjustment.

-----

## Null 1 — Non-Uniqueness

**GUES Claim:** A unique constraint structure underlies the observed gauge physics.

**Null:** There exist K₁ ≠ K₂ such that Aut(K₁) ≅ Aut(K₂) — they produce isomorphic automorphism groups — despite having different admissibility structures.

**Why this matters:** If many different constraint systems produce the same Aut(K), then Aut(K) does not uniquely identify a fundamental substrate. G loses explanatory necessity.

**Operational test:** For each model in the suite, compare Aut(K) order and structure across models. If multiple structurally different systems produce isomorphic automorphism groups, record as evidence for Null 1.

**Rejection threshold:** Null 1 is not rejected by finding two systems with the same group — that is expected and likely. Null 1 would be rejected only if we demonstrate that *for the specific constraint topology required to produce Standard Model gauge groups*, the topology is unique up to isomorphism.

**Current status:** Not yet testable — we have not yet identified constraint topologies producing SU(2) or SU(3)-like structures.

-----

## Null 2 — Generic Emergence

**GUES Claim:** Observed gauge structure requires the proposed constraint hierarchy — specific topology is necessary.

**Null:** Randomly sampled constraint systems generate gauge-like automorphism structure with frequency p > p_crit.

**Threshold:** p_crit = 0.05 (set before sampling).

**Operational definition of “gauge-like”:** For this run, gauge-like means:

1. |Aut(K)| > 1
1. At least one non-trivial orbit under Aut(K)
1. Group order ≥ 2

Note: this is a weak definition. It does not require the group to be isomorphic to any Standard Model gauge group. It is a first-pass filter only.

**Current result (Run 01, seed=42, n=5, density=0.35):**

- Gauge-like frequency: 0/5 = 0.00
- p = 0.00 < p_crit = 0.05
- STATUS: Consistent with Null 2 rejection at this sample size

**Caveat:** 5 instances is not statistically meaningful. This is a data point, not a result. Requires n ≥ 100 at multiple densities before Null 2 can be formally assessed.

**What would confirm Null 2:** If at n=100 random instances, more than 5 produce gauge-like Aut(K), Null 2 is not rejected and GUES loses the claim that specific constraint topology is required.

-----

## Null 3 — Information Primacy Failure

**GUES Claim:** Information is derived from constraints — it cannot be defined prior to distinction.

**Null:** A mathematically coherent formal system exists satisfying:

1. Information is defined
1. No distinguishable states exist
1. No hidden constraints are present

**Operational test:** This null is not directly testable by computation. It requires formal mathematical argument. It is listed here for completeness and tracked as an open theoretical question.

**Current status:** Open. No counterexample found. No proof provided.

-----

## Null 4 — Ladder Collapse

*Added from Sage adversarial review, June 2026.*

**GUES Claim:** Constraint → Distinction is the first necessary rung of the emergence ladder.

**Null:** There exists a mathematically coherent formalism in which distinction is primitive and constraints are derived — i.e., the ladder can be entered from a different rung with equal or greater explanatory power.

**Why this matters:** If distinction can be taken as primitive without assuming constraints, the constraint-first hierarchy loses its privileged status. It becomes one of many possible orderings rather than the necessary one.

**Operational test:** Not directly computable. Requires formal argument. A candidate counterexample would be a formal system where “distinguishable” is an axiom and constraint structure emerges as a derived notion.

**Current status:** Open. This is the most dangerous null for the GUES hierarchy and has not been addressed.

-----

## Running the Tests

```bash
# Install dependencies
pip install -r requirements.txt

# Run all models
python models/models.py

# Run just random sampling (Null 2 probe)
python -c "from models.models import model_05_random; model_05_random(n_instances=100)"
```

-----

## Record of Results

|Run   |Date     |Null 2 (n, freq)|Notes                                  |
|------|---------|----------------|---------------------------------------|
|Run 01|June 2026|n=5, freq=0.00  |Baseline. Not statistically meaningful.|

*Thresholds set before runs. No modification after.*

-----

*No claims without tests.*  
*No tests without thresholds.*  
*No thresholds without numbers.*  
*No numbers without a run.*