"""
model_06_fiber.py — Fiber Prototype Constraint System
AutKompute v0.1 — github.com/justindbilyeu/AutKompute

M6: The Fiber Prototype

Design motivation (from Sage, charter session, June 2026):
    "A true gauge bundle analogue would need something closer to
    X = B × F where B = base structure, F = internal fiber,
    and automorphisms satisfy Aut(K) = Aut(B) ⋉ Aut(F) or similar."

This model tests whether a single constraint system K can produce
non-abelian semidirect product structure from entangled base and fiber
admissibility rules — without constructing two independent systems.

Construction:
    Base B = {x, y, z} with DIRECTED 3-cycle x→y→z→x (forward)
    Fiber F = {+, -} with REVERSED cycle on minus strand x→z→y→x

    States: (x+), (x-), (y+), (y-), (z+), (z-)

    Admissibility rules:
        + strand:  x+ → y+ → z+ → x+  (forward base cycle)
        - strand:  x- → z- → y- → x-  (REVERSED base cycle)
        Fiber swap: x+ ↔ x-,  y+ ↔ y-,  z+ ↔ z-

    The key design choice: the fiber swap REVERSES the base cycle direction.
    This creates non-commutativity: swapping fiber then rotating base
    ≠ rotating base then swapping fiber.

Expected result: S3 = Z3 ⋊ Z2 (non-abelian, order 6)

Why this matters:
    If a single K can produce non-abelian structure from entangled
    base and fiber constraints, the federated hypothesis (which assumes
    base and fiber must be independent primitives) is not required by
    the data. This is a direct test of GUES vs. FEDERATED.

Run with: python model_06_fiber.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from autk import make_constraint_system, compute_automorphisms, run_model
from itertools import permutations
from collections import Counter


def aut_order(a, nodes):
    identity = {n: n for n in nodes}
    current = dict(a)
    for k in range(1, 25):
        if current == identity:
            return k
        current = {n: a[current[n]] for n in nodes}
    return -1


def orbits(auts, X):
    visited = set()
    orbs = []
    for node in X:
        if node not in visited:
            orbit = set()
            for aut in auts:
                orbit.add(aut[node])
            orbs.append(frozenset(orbit))
            visited.update(orbit)
    return orbs


def stabilizer(auts, node):
    return [a for a in auts if a[node] == node]


def model_06_fiber():
    """
    Fiber prototype constraint system.

    The + strand runs forward: x+ → y+ → z+ → x+
    The - strand runs backward: x- → z- → y- → x-
    Fiber swaps are bidirectional at each base node.

    This asymmetry between strands encodes the Z2 action on Z3:
    the fiber flip reverses the base cycle, producing non-commutativity.
    """
    nodes = ['x+', 'x-', 'y+', 'y-', 'z+', 'z-']
    edges = [
        # + strand: forward base cycle
        ('x+', 'y+'), ('y+', 'z+'), ('z+', 'x+'),
        # - strand: REVERSED base cycle
        ('x-', 'z-'), ('z-', 'y-'), ('y-', 'x-'),
        # fiber swaps (bidirectional)
        ('x+', 'x-'), ('x-', 'x+'),
        ('y+', 'y-'), ('y-', 'y+'),
        ('z+', 'z-'), ('z-', 'z+'),
    ]

    K = make_constraint_system(nodes, edges)
    auts = compute_automorphisms(K)
    orbs = orbits(auts, nodes)
    orders = [aut_order(a, nodes) for a in auts]
    order_dist = dict(Counter(orders))

    print("=" * 60)
    print("M6 — FIBER PROTOTYPE")
    print("=" * 60)
    print(f"  |X| = {len(nodes)}")
    print(f"  |A| = {len(edges)}")
    print(f"  |Aut(K)| = {len(auts)}")
    print(f"  Orbits: {[sorted(list(o)) for o in orbs]}")
    print(f"  Non-trivial orbits: {len([o for o in orbs if len(o) > 1])}")
    print(f"  Order distribution: {order_dist}")
    print()

    # Group identification
    is_s3 = order_dist == {1: 1, 2: 3, 3: 2}
    is_z6 = order_dist == {1: 1, 2: 1, 3: 2, 6: 2}

    if is_s3:
        print("  GROUP: S3 = Z3 ⋊ Z2 (non-abelian, order 6)")
        print("  ✓ First non-abelian group in the run")
        print("  ✓ Contains Z3 subgroup (base rotations)")
        print("  ✓ Contains Z2 elements (fiber-reversing reflections)")
    elif is_z6:
        print("  GROUP: Z6 = Z3 × Z2 (abelian, order 6)")
        print("  Note: abelian — base and fiber commute")
    else:
        print(f"  GROUP: Order {len(auts)}, unclassified by order distribution alone")

    print()

    # Subgroup analysis
    z3_subgroup = [a for a in auts if aut_order(a, nodes) in [1, 3]]
    z2_elements = [a for a in auts if aut_order(a, nodes) == 2]
    print(f"  Z3 subgroup (base rotations): {len(z3_subgroup)} elements")
    print(f"  Z2 elements (fiber reflections): {len(z2_elements)} elements")
    print()

    # Federated hypothesis assessment
    print("  FEDERATED HYPOTHESIS TEST:")
    print("  Question: Can a single K produce non-abelian structure")
    print("            without constructing two independent systems?")
    if is_s3:
        print("  Answer: YES")
        print("  S3 = Z3 ⋊ Z2 emerged from a single admissibility structure.")
        print("  The non-commutativity came from constraint topology,")
        print("  not from independent base and fiber primitives.")
        print("  → Federated hypothesis not required by this data point.")
    else:
        print("  Answer: INCONCLUSIVE (group is abelian)")
        print("  → No evidence against federation from this model.")

    print()
    print("  NOTE: This is one data point. It is not a result.")

    return {
        'name': 'M6 — Fiber Prototype',
        'X': nodes,
        'A': edges,
        '|X|': len(nodes),
        '|A|': len(edges),
        '|Aut(K)|': len(auts),
        'group': 'S3' if is_s3 else ('Z6' if is_z6 else f'Order {len(auts)}'),
        'non_abelian': is_s3,
        'orbits': [sorted(list(o)) for o in orbs],
        'order_distribution': order_dist,
        'federated_test': 'SINGLE K PRODUCED NON-ABELIAN' if is_s3 else 'INCONCLUSIVE',
    }


if __name__ == '__main__':
    result = model_06_fiber()
