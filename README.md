# AutKompute

> *No claims without a run.*

**Status:** Active — First compute pass  
**Version:** 0.1  
**Parent project:** [GUES](https://github.com/justindbilyeu/GUES)  
**Methodology:** [The-Charter v2.7](https://github.com/justindbilyeu/The-Charter)

-----

## What This Is

AutKompute computes the automorphism group Aut(K) for finite constraint systems K = (X, A).

A constraint system is the primitive object proposed in GUES v0.2:

- **X** — a finite set of possible configurations
- **A ⊆ X × X** — the set of admissible transitions (allowed vs forbidden)

The automorphism group Aut(K) is the set of all permutations of X that preserve A exactly — every allowed transition maps to an allowed transition, every forbidden transition maps to a forbidden transition.

GUES proposes that Aut(K) is the ambient object G — that Standard Model gauge groups emerge as stabilizer subgroups of Aut(K) at different energy scales. This repo exists to test whether that claim has any empirical foothold at all, starting from the simplest possible cases.

-----

## Why This Exists

GUES v0.2 was reviewed by Sage (charter session), who identified the central problem:

> *“Aut(K) is carrying enormous weight. It has not been computed for any nontrivial K. Not even a toy model. Under RG² rules: No claim without a run.”*

This repo is the run.

If gauge-like structures begin appearing in Aut(K) for well-chosen constraint systems, the conjecture gains its first empirical foothold.

If they do not appear, we learn something equally valuable.

-----

## Structure

```
AutKompute/
├── README.md
├── src/
│   └── autk.py              — core Aut(K) computation engine
├── models/
│   ├── model_01_minimal.py  — smallest non-trivial constraint system
│   ├── model_02_cyclic.py   — cyclic admissibility → Z3
│   ├── model_03_broken.py   — complete graph minus one edge
│   ├── model_04_layered.py  — causal layered structure
│   └── model_05_random.py   — random sampling (probes Null 2)
├── results/
│   └── run_01.md            — first compute pass results
└── NULLS.md                 — formal null hypotheses under test
```

-----

## First Results

|Model               |X||A|||Aut(K)||Structure  |Gauge-like?|
|--------------------|-|---|--------|-----------|-----------|
|M1 — Minimal        |2|1  |1       |Trivial    |No         |
|M2 — Cyclic         |3|3  |3       |Z₃         |Candidate  |
|M3 — Broken complete|4|11 |2       |Z₂         |No         |
|M4 — Layered        |4|4  |4       |Z₄ or Z₂×Z₂|Candidate  |
|M5 — Random (×3)    |6|~10|1       |Trivial    |No         |

**Initial observation:** Random constraint systems produce trivial automorphism groups. Structured constraint systems (cyclic, layered) produce non-trivial groups. Gauge-like structure requires specific constraint topology — it does not emerge generically. This is evidence against Null 2 (generic emergence) and consistent with the GUES claim that specific constraint structure is required.

This is one run. It is not a result. It is a data point.

-----

## Null Hypotheses Under Test

See `NULLS.md` for full formal statement. Summary:

**Null 1 — Non-uniqueness:** Do different constraint systems produce the same Aut(K)?  
**Null 2 — Generic emergence:** Does gauge-like structure appear in random constraint systems?  
**Null 4 — Ladder collapse:** Can distinction be defined without constraints?

First run: Null 2 shows initial negative result for random systems. More runs required.

-----

## Next Steps

- Expand to models with |X| = 8–12 to check for SU(2)-like structure
- Systematic sweep over structured constraint topologies
- Define “gauge-like” operationally — current assessment is informal
- Implement group identification (not just order)

-----

## Related

- [GUES](https://github.com/justindbilyeu/GUES) — parent conjecture
- [Resonance_Geometry](https://github.com/justindbilyeu/Resonance_Geometry) — dynamical systems work
- [The-Charter](https://github.com/justindbilyeu/The-Charter) — governing methodology

-----

*The conjecture lives or dies here.*  
*That is the point.*
