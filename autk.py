"""
autk.py — Core Aut(K) computation engine
AutKompute v0.1 — github.com/justindbilyeu/AutKompute

A constraint system K = (X, A) where:
    X = finite set of configurations
    A ⊆ X × X = admissible transitions

Aut(K) = set of permutations of X that preserve A exactly.

No geometry assumed. No information assumed.
Only the distinction between allowed and forbidden.
"""

from itertools import permutations
from typing import Any


def make_constraint_system(nodes: list, edges: list[tuple]) -> dict:
    """
    Create a constraint system K = (X, A).

    Parameters
    ----------
    nodes : list
        The configuration space X.
    edges : list of (a, b) tuples
        The admissible transitions A.

    Returns
    -------
    dict with keys 'X' and 'A'.
    """
    return {'X': list(nodes), 'A': set(edges)}


def compute_automorphisms(K: dict) -> list[dict]:
    """
    Compute Aut(K) by brute force over all permutations of X.

    A permutation φ is an automorphism iff:
        (a, b) ∈ A  ⟺  (φ(a), φ(b)) ∈ A

    Parameters
    ----------
    K : dict
        Constraint system with keys 'X' and 'A'.

    Returns
    -------
    List of automorphisms, each as a dict mapping node → node.
    """
    X = K['X']
    A = K['A']
    auts = []

    for perm in permutations(X):
        mapping = dict(zip(X, perm))
        mapped_A = frozenset((mapping[a], mapping[b]) for a, b in A)
        if mapped_A == frozenset(A):
            auts.append(mapping)

    return auts


def automorphism_order(K: dict) -> int:
    """Return |Aut(K)|."""
    return len(compute_automorphisms(K))


def identify_group(order: int) -> str:
    """
    Attempt informal identification of group by order.
    This is not a full group identification — order alone is not sufficient.
    Use only as a first-pass label.
    """
    table = {
        1: 'Trivial {e}',
        2: 'Z2',
        3: 'Z3',
        4: 'Z4 or Z2×Z2',
        5: 'Z5',
        6: 'Z6 or S3',
        8: 'Z8, Z4×Z2, Z2³, D4, or Q8',
        9: 'Z9 or Z3×Z3',
        10: 'Z10 or D5',
        12: 'Z12, Z2×Z6, A4, D6, or Dic3',
        16: 'one of 14 groups of order 16',
        24: 'S4, A4×Z2, or others',
        48: 'possible GL(2,3) or others',
        120: 'S5 or A5×Z2',
    }
    return table.get(order, f'Order {order} — unclassified, requires full structure analysis')


def is_gauge_like(auts: list[dict], K: dict) -> tuple[bool, str]:
    """
    Informal first-pass check for gauge-like properties.

    A structure is 'gauge-like' here if:
    1. |Aut(K)| > 1 (non-trivial symmetry exists)
    2. Automorphisms act non-trivially on at least some nodes
    3. There exist orbits under Aut(K) (nodes related by symmetry)

    This is NOT a rigorous definition of gauge symmetry.
    It is a first-pass filter for interesting structure.
    """
    order = len(auts)

    if order == 1:
        return False, "Trivial automorphism group — no symmetry"

    # Compute orbits
    X = K['X']
    orbits = []
    visited = set()
    for node in X:
        if node not in visited:
            orbit = set()
            for aut in auts:
                orbit.add(aut[node])
            orbits.append(frozenset(orbit))
            visited.update(orbit)

    non_trivial_orbits = [o for o in orbits if len(o) > 1]

    if not non_trivial_orbits:
        return False, "All orbits trivial despite non-trivial group"

    return True, (
        f"Non-trivial Aut(K) of order {order}. "
        f"{len(non_trivial_orbits)} non-trivial orbit(s): "
        f"{[list(o) for o in non_trivial_orbits]}"
    )


def run_model(name: str, nodes: list, edges: list[tuple], verbose: bool = True) -> dict:
    """
    Full analysis pipeline for a single constraint system.

    Returns dict with all computed properties.
    """
    K = make_constraint_system(nodes, edges)
    auts = compute_automorphisms(K)
    order = len(auts)
    group_id = identify_group(order)
    gauge_like, gauge_note = is_gauge_like(auts, K)

    result = {
        'name': name,
        'X': nodes,
        'A': list(edges),
        '|X|': len(nodes),
        '|A|': len(edges),
        '|Aut(K)|': order,
        'group_id': group_id,
        'gauge_like': gauge_like,
        'gauge_note': gauge_note,
    }

    if verbose:
        print(f"\n{'='*50}")
        print(f"Model: {name}")
        print(f"  X = {nodes}")
        print(f"  |A| = {len(edges)}")
        print(f"  |Aut(K)| = {order}")
        print(f"  Group: {group_id}")
        print(f"  Gauge-like: {gauge_like}")
        print(f"  Note: {gauge_note}")

    return result


if __name__ == '__main__':
    # Quick sanity check
    print("AutKompute — sanity check")
    print("Expected: M1→1, M2→3")

    K1 = make_constraint_system(['a', 'b'], [('a', 'b')])
    K2 = make_constraint_system(['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a')])

    assert automorphism_order(K1) == 1, "M1 failed"
    assert automorphism_order(K2) == 3, "M2 failed"
    print("Sanity check passed.")
