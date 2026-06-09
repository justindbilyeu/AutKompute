"""
models.py — Five toy constraint systems for AutKompute v0.1

Each model is a constraint system K = (X, A).
For each, we compute Aut(K) and assess gauge-like structure.

Models:
    M1 — Minimal distinguishability (baseline)
    M2 — Cyclic (tests whether cyclic constraint → cyclic automorphism)
    M3 — Complete minus one (tests symmetry breaking by single forbidden transition)
    M4 — Layered/causal (tests whether directed structure produces non-trivial Aut)
    M5 — Random sampling (probes Null 2: does gauge structure emerge generically?)

Run with: python models.py
"""

import random
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from autk import run_model, make_constraint_system, compute_automorphisms


def model_01_minimal():
    """
    Model 1 — Minimal distinguishability

    X = {a, b}
    A = {(a, b)}

    The smallest possible non-trivial constraint system.
    One configuration can transition to another. Not vice versa.
    Baseline: what does the trivial case look like?

    Expected: Aut(K) = trivial (only identity).
    Reason: φ must map (a,b) to (a,b), so φ(a)=a and φ(b)=b.
    """
    return run_model(
        name="M1 — Minimal",
        nodes=['a', 'b'],
        edges=[('a', 'b')]
    )


def model_02_cyclic():
    """
    Model 2 — Cyclic admissibility

    X = {a, b, c}
    A = {(a,b), (b,c), (c,a)}

    Each configuration transitions to exactly one other, cyclically.
    Tests: does cyclic constraint topology → cyclic automorphism group?

    Expected: Aut(K) ≅ Z3 (order 3).
    Reason: cyclic shift a→b→c→a is an automorphism, and its powers generate Z3.
    """
    return run_model(
        name="M2 — Cyclic",
        nodes=['a', 'b', 'c'],
        edges=[('a', 'b'), ('b', 'c'), ('c', 'a')]
    )


def model_03_broken():
    """
    Model 3 — Complete graph minus one edge

    X = {a, b, c, d}
    A = all (x,y) with x≠y, except (c,d)

    A near-maximally connected system with one forbidden transition.
    Tests: how does a single broken symmetry reduce Aut(K)?

    Expected: Aut(K) ≅ Z2 (order 2).
    Reason: the one missing edge (c,d) distinguishes c and d from each other
    but any permutation swapping a and b (which have identical constraint profiles)
    is an automorphism.
    """
    nodes = ['a', 'b', 'c', 'd']
    all_edges = [(x, y) for x in nodes for y in nodes if x != y]
    edges = [e for e in all_edges if e != ('c', 'd')]

    return run_model(
        name="M3 — Broken complete",
        nodes=nodes,
        edges=edges
    )


def model_04_layered():
    """
    Model 4 — Layered / causal structure

    X = {a, b, c, d}
    A = {(a,c), (a,d), (b,c), (b,d)}

    Two source nodes {a,b} each connect to two target nodes {c,d}.
    Causal directionality: information flows from layer 0 to layer 1 only.
    Tests: does directed layered structure produce non-trivial Aut?

    Expected: Aut(K) of order 4 (Z4 or Z2×Z2).
    Reason: we can independently swap (a↔b) and (c↔d) while preserving A.
    Those two independent Z2 swaps generate Z2×Z2 of order 4.
    """
    return run_model(
        name="M4 — Layered/causal",
        nodes=['a', 'b', 'c', 'd'],
        edges=[('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd')]
    )


def model_05_random(seed: int = 42, n_nodes: int = 6, n_instances: int = 5,
                    density: float = 0.35):
    """
    Model 5 — Random constraint systems

    X = 6 nodes, A randomly sampled at ~35% density.
    Repeated n_instances times.

    Tests Null 2 (Generic Emergence):
    If gauge-like structure appears frequently in random systems,
    GUES loses explanatory necessity.

    Expected: mostly trivial Aut(K).
    Reason: random constraint systems are unlikely to have non-trivial symmetry.

    Parameters
    ----------
    seed : int
        Random seed for reproducibility.
    n_nodes : int
        Size of X.
    n_instances : int
        Number of random systems to generate.
    density : float
        Probability that any directed edge is included in A.
    """
    random.seed(seed)
    nodes = [str(i) for i in range(n_nodes)]
    all_possible = [(x, y) for x in nodes for y in nodes if x != y]

    results = []
    gauge_like_count = 0

    print(f"\n{'='*50}")
    print(f"Model 5 — Random sampling")
    print(f"  |X| = {n_nodes}, density ≈ {density}, seed = {seed}")
    print(f"  {n_instances} instances")

    for i in range(n_instances):
        edges = [e for e in all_possible if random.random() < density]
        result = run_model(
            name=f"M5.{i+1} — Random instance {i+1}",
            nodes=nodes,
            edges=edges
        )
        results.append(result)
        if result['gauge_like']:
            gauge_like_count += 1

    freq = gauge_like_count / n_instances
    print(f"\n  Gauge-like frequency: {gauge_like_count}/{n_instances} = {freq:.2f}")
    print(f"  Null 2 threshold: p_crit = 0.05")
    if freq > 0.05:
        print(f"  STATUS: Null 2 NOT rejected at this sample size (inconclusive)")
    else:
        print(f"  STATUS: Consistent with Null 2 rejection (gauge structure not generic)")

    return results


if __name__ == '__main__':
    print("AutKompute — Model Suite v0.1")
    print("Computing Aut(K) for five toy constraint systems...")
    print("Methodology: github.com/justindbilyeu/The-Charter")
    print("Parent project: github.com/justindbilyeu/GUES")

    results = []
    results.append(model_01_minimal())
    results.append(model_02_cyclic())
    results.append(model_03_broken())
    results.append(model_04_layered())
    random_results = model_05_random()

    print(f"\n{'='*50}")
    print("SUMMARY — Run 01")
    print(f"{'Model':<30} {'|Aut(K)|':<12} {'Gauge-like':<12} {'Group'}")
    print('-' * 80)
    for r in results:
        print(f"{r['name']:<30} {r['|Aut(K)|']:<12} {str(r['gauge_like']):<12} {r['group_id']}")
    for r in random_results:
        print(f"{r['name']:<30} {r['|Aut(K)|']:<12} {str(r['gauge_like']):<12} {r['group_id']}")

    print(f"\nConclusion (preliminary):")
    print(f"  Random constraint systems → trivial Aut(K)")
    print(f"  Structured constraint systems → non-trivial Aut(K)")
    print(f"  Gauge-like structure is not generic — requires specific topology")
    print(f"  This is one run. It is not a result. It is a data point.")
