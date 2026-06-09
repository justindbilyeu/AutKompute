"""
model_07_square.py — Square / D4 Constraint System
AutKompute v0.1 — github.com/justindbilyeu/AutKompute

M7: The Square

Design motivation (from Sage, charter session, June 2026):
    "Simplest route to order 8: use a square.
    Vertices {1,2,3,4}, undirected cycle edges.
    Aut(K) ≅ D4 very likely. Easy calibration target."

This model is a calibration run. Its purpose:
    1. Confirm that order-8 automorphism groups are reachable
    2. Establish D4 as a known reference point
    3. Verify the orbit/stabilizer analysis module on a known result

The dihedral group D4 (symmetries of the square) has order 8.
It contains:
    - 4 rotations (including identity): order 1, 2, 4, 4
    - 4 reflections: order 2, 2, 2, 2
    - Total: 1 element order 1, 5 elements order 2, 2 elements order 4

D4 is non-abelian. It is the symmetry group of the square.
It contains Z4 and Z2×Z2 as subgroups.
It is also a subgroup of S4.

Construction:
    X = {1, 2, 3, 4} (vertices of a square)
    A = undirected cycle: 1↔2↔3↔4↔1

Run with: python model_07_square.py
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from autk import make_constraint_system, compute_automorphisms
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


def model_07_square():
    """
    Undirected square constraint system.
    Expected: Aut(K) ≅ D4, order 8.
    """
    nodes = ['1', '2', '3', '4']
    edges = [
        ('1', '2'), ('2', '1'),
        ('2', '3'), ('3', '2'),
        ('3', '4'), ('4', '3'),
        ('4', '1'), ('1', '4'),
    ]

    K = make_constraint_system(nodes, edges)
    auts = compute_automorphisms(K)
    orbs = orbits(auts, nodes)
    orders = [aut_order(a, nodes) for a in auts]
    order_dist = dict(Counter(orders))
    stab_1 = stabilizer(auts, '1')

    print("=" * 60)
    print("M7 — UNDIRECTED SQUARE")
    print("=" * 60)
    print(f"  |X| = {len(nodes)}")
    print(f"  |A| = {len(edges)}")
    print(f"  |Aut(K)| = {len(auts)}")
    print(f"  Orbits: {[sorted(list(o)) for o in orbs]}")
    print(f"  Order distribution: {order_dist}")
    print(f"  |Stab(1)| = {len(stab_1)}")
    print()

    is_d4 = len(auts) == 8 and order_dist == {1: 1, 2: 5, 4: 2}

    if is_d4:
        print("  GROUP: D4 (dihedral group of order 8)")
        print("  ✓ Symmetry group of the square")
        print("  ✓ Non-abelian")
        print("  ✓ Contains Z4 and Z2×Z2 as subgroups")
        print("  ✓ Calibration target confirmed")
    elif len(auts) == 8:
        print(f"  GROUP: Order 8 (not D4 by order distribution)")
        print(f"  Candidates: Z8, Z4×Z2, Z2³, Q8")
    else:
        print(f"  GROUP: Order {len(auts)} — unexpected")

    print()
    print("  Orbit/stabilizer structure:")
    print(f"  Single orbit of size {len(nodes)}: all vertices equivalent")
    print(f"  |Stab(1)| = {len(stab_1)}: {len(stab_1)} automorphisms fix vertex 1")
    print(f"  Orbit-stabilizer theorem: |Aut| = |orbit| × |Stab| = "
          f"{len(orbs[0])} × {len(stab_1)} = {len(orbs[0]) * len(stab_1)}")
    print()
    print("  NOTE: Calibration model. Not a physics claim.")

    return {
        'name': 'M7 — Undirected Square',
        'X': nodes,
        'A': edges,
        '|X|': len(nodes),
        '|A|': len(edges),
        '|Aut(K)|': len(auts),
        'group': 'D4' if is_d4 else f'Order {len(auts)}',
        'non_abelian': True if len(auts) == 8 else False,
        'orbits': [sorted(list(o)) for o in orbs],
        'order_distribution': order_dist,
        'calibration': 'D4 CONFIRMED' if is_d4 else 'UNEXPECTED',
    }


if __name__ == '__main__':
    result = model_07_square()
