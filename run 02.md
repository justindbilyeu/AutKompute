# Run 02 — Fiber Prototype and D4 Calibration

## AutKompute v0.1 — June 2026

**Date:** June 2026  
**Models:** M6 (Fiber Prototype), M7 (Undirected Square)  
**Preceding run:** run_01.md  
**Methodology:** github.com/justindbilyeu/The-Charter

-----

## What Was Run

Two new constraint systems designed in response to Sage adversarial review:

**M6 — Fiber Prototype:** Tests whether a single K can produce non-abelian semidirect product structure from entangled base and fiber admissibility rules.

**M7 — Undirected Square:** Calibration target. Tests whether order-8 automorphism groups (D4) are reachable.

-----

## Results

|Model                 ||X|||A|||Aut(K)||Group       |Non-abelian|Key result             |
|----------------------|---|---|--------|------------|-----------|-----------------------|
|M6 — Fiber Prototype  |6  |12 |6       |S3 = Z3 ⋊ Z2|YES        |First non-abelian group|
|M7 — Undirected Square|4  |8  |8       |D4          |YES        |Calibration confirmed  |

-----

## M6 — Fiber Prototype: Detailed Analysis

**Design:**

- Base B = {x, y, z} with directed 3-cycle
- Fiber F = {+, −} at each base node
- - strand: forward cycle x+→y+→z+→x+
- − strand: REVERSED cycle x−→z−→y−→x−
- Fiber swaps: x+↔x−, y+↔y−, z+↔z− (bidirectional)

**The key design choice:** The − strand reverses the base cycle direction. This creates non-commutativity: swapping fiber then rotating base ≠ rotating base then swapping fiber.

**Result:** Aut(K6) ≅ S3 = Z3 ⋊ Z2

Order distribution: {1:1, 2:3, 3:2}

This is the signature of S3: one identity, three elements of order 2 (reflections), two elements of order 3 (rotations).

**Subgroup structure:**

- Z3 subgroup (3 elements): the base rotations, preserving fiber orientation
- Z2 elements (3 elements): fiber-reversing reflections, each also permuting base nodes

**Orbit structure:** Single orbit containing all 6 states. All states are reachable from each other via automorphisms. Base and fiber are fully entangled in the symmetry structure.

-----

## M7 — Undirected Square: Calibration

**Design:** 4 vertices, undirected cycle 1↔2↔3↔4↔1

**Result:** Aut(K7) ≅ D4, order 8

Order distribution: {1:1, 2:5, 4:2}

This is the signature of D4: 1 identity, 5 reflections (order 2), 2 rotations (order 4).

Orbit-stabilizer theorem confirmed: |Aut| = |orbit| × |Stab(1)| = 4 × 2 = 8 ✓

Calibration target confirmed. Order-8 automorphism groups are reachable from simple constraint topologies.

-----

## The Most Important Result: Federated Hypothesis Test

The fiber prototype (M6) was designed as a direct test of the GUES vs. FEDERATED question.

**The question:** Can a single constraint system K produce non-abelian structure from entangled base and fiber constraints, without constructing two independent systems?

**The answer from M6:** YES.

S3 = Z3 ⋊ Z2 emerged from a single admissibility structure A defined over X = {x+, x−, y+, y−, z+, z−}. The non-commutativity was not put in by hand. It was not produced by taking two separate systems and combining them. It came from the constraint topology — specifically from the reversal of the base cycle direction in the − strand.

**Implication for FEDERATED.md:**

The federated hypothesis requires that non-abelian gauge-like structure can only be produced by combining independent primitive systems. M6 shows this is not necessary — a unified K can produce non-abelian structure.

This does not prove GUES. It shows that the federated hypothesis is not forced by the mathematical structure of finite constraint systems.

**Charter statement:** This is two data points accumulated across two runs. It is not a result. It is a pattern beginning to form.

-----

## Cumulative Results: Runs 01 + 02

|Model               ||Aut(K)||Group       |Non-abelian|Gauge-like|
|--------------------|--------|------------|-----------|----------|
|M1 — Minimal        |1       |Trivial     |No         |No        |
|M2 — Cyclic         |3       |Z3          |No         |Candidate |
|M3 — Broken complete|2       |Z2          |No         |Candidate |
|M4 — Layered        |4       |Z2×Z2       |No         |Candidate |
|M5.1-5.10 — Random  |1 (all) |Trivial     |No         |No        |
|M6 — Fiber Prototype|6       |S3 = Z3 ⋊ Z2|**YES**    |**YES**   |
|M7 — Square         |8       |D4          |**YES**    |**YES**   |

**Emerging pattern:**

1. Random systems → trivial Aut(K)
1. Structured systems → non-trivial Aut(K)
1. Entangled base+fiber constraints → non-abelian Aut(K)
1. Non-abelian groups achievable from single K without independent subsystems

-----

## What Was Not Found

No structure resembling SU(2), SU(3), or U(1) appeared in this run. This remains expected — those require larger X, specific topologies, and the mathematical machinery to identify continuous limits of discrete automorphism structures.

The current models produce finite groups. The path to continuous gauge groups requires:

1. Larger constraint systems (|X| >> 6)
1. Coarse-graining analysis (does the group structure stabilize under K → K_coarse?)
1. Identification of fixed points under repeated coarse-graining

-----

## Next Run

Priority targets based on Sage’s updated metric hierarchy:

**High priority — Orbit decomposition:**

- Build constraint systems with explicit base/fiber orbit decomposition
- Test whether Aut(K) = Aut(B) ⋊ Aut(F) is producible from single K
- This is the test closest to actual gauge bundle structure

**Medium priority — Larger systems:**

- |X| = 8 targeting Q8 (quaternion group) — non-abelian double cover of Z2×Z2
- Q8 is structurally closer to SU(2) than D4

**Low priority (deferred):**

- E8 analysis — currently five layers above evidence
- Continuous group limits — requires coarse-graining machinery not yet built

-----

## Updated Null 2 Status

Random sampling frequency remains 0/10 = 0.00.  
Structured models continue to produce non-trivial Aut(K).  
Null 2 (generic emergence) remains consistent with rejection at current sample size.  
Formal assessment requires n ≥ 100.

-----

*Two data points.*  
*A pattern beginning to form.*  
*Not a result.*  
*Keep running.*