# Run 01 — First Compute Pass

## AutKompute v0.1 — June 2026

**Date:** June 2026  
**Seed:** 42  
**Methodology:** github.com/justindbilyeu/The-Charter  
**Parent project:** github.com/justindbilyeu/GUES

-----

## What Was Run

Five toy constraint systems K = (X, A). For each, Aut(K) was computed by brute-force permutation over X, checking whether each permutation preserves A exactly.

-----

## Results

|Model               ||X|||A|||Aut(K)||Group (informal)|Gauge-like|Verdict                                   |
|--------------------|---|---|--------|----------------|----------|------------------------------------------|
|M1 — Minimal        |2  |1  |1       |Trivial         |No        |Baseline established                      |
|M2 — Cyclic         |3  |3  |3       |Z₃              |Yes       |Non-trivial structure from cyclic topology|
|M3 — Broken complete|4  |11 |2       |Z₂              |Yes       |Single missing edge breaks to Z₂          |
|M4 — Layered/causal |4  |4  |4       |Z₂×Z₂           |Yes       |Independent layer swaps generate Z₂×Z₂    |
|M5.1 — Random       |6  |~10|1       |Trivial         |No        |—                                         |
|M5.2 — Random       |6  |~9 |1       |Trivial         |No        |—                                         |
|M5.3 — Random       |6  |~11|1       |Trivial         |No        |—                                         |
|M5.4 — Random       |6  |~10|1       |Trivial         |No        |—                                         |
|M5.5 — Random       |6  |~8 |1       |Trivial         |No        |—                                         |

-----

## Observations

**1. Random constraint systems produce trivial automorphism groups.**

All five random instances produced |Aut(K)| = 1. This is the expected behavior — a random admissibility structure is unlikely to have any permutation that preserves it exactly. Symmetry requires specific topology.

**2. Structured constraint systems produce non-trivial automorphism groups.**

All three structured models (cyclic, broken-complete, layered) produced non-trivial Aut(K). The structure of the automorphism group directly reflects the topology of the constraint system:

- Cyclic topology → Z₃ (cyclic group of order 3)
- Near-complete with one break → Z₂ (one remaining symmetry axis)
- Bipartite layered → Z₂×Z₂ (independent swaps within each layer)

**3. Gauge-like structure is not generic.**

Random Null 2 frequency: 0/5 = 0.00 (p < p_crit = 0.05)

This is consistent with the GUES claim that specific constraint topology is required for gauge-like structure to emerge. It is not consistent with the null hypothesis that gauge structure emerges generically.

**Caveat: n=5 is not statistically meaningful.** This observation requires n ≥ 100 at multiple densities to be formally assessed. This is a data point, not a result.

-----

## What Was Not Found

No structure resembling SU(2) or SU(3) appeared in this run. This is expected — those groups have orders 8 (for SU(2) in a finite approximation) and higher, requiring larger X and more carefully chosen A. The current models are too small to produce them.

This is not a failure. It is a calibration. We know what we need to look for next.

-----

## Preliminary Conclusion

*Structured constraint topology → non-trivial Aut(K)*  
*Random constraint topology → trivial Aut(K)*  
*Gauge-like structure requires specific topology*

This is consistent with GUES Conjecture 2 (gauge groups as constraint automorphisms) and inconsistent with Null 2 (generic emergence) at this sample size.

The conjecture has not been confirmed. It has survived its first contact with computation.

-----

## Next Run

1. Expand to |X| = 8–12
1. Identify constraint topologies producing groups of order 8 (SU(2)-adjacent)
1. Run Null 2 at n = 100 across multiple densities
1. Implement full group identification (not just order)
1. Attempt to construct a constraint system whose Aut(K) contains Z₂ × Z₂ × Z₂ as a subgroup — first step toward SU(2)-like structure

-----

*This is one run. It is not a result. It is a data point.*  
*The conjecture lives or dies by the accumulation of data points.*