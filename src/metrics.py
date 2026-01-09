# src/metrics.py

import numpy as np

def ndcg_at_k(relevances, k=10):
    """
    Computes NDCG@k.
    """
    relevances = np.array(relevances[:k])
    discounts = 1 / np.log2(np.arange(2, k + 2))
    dcg = np.sum(relevances * discounts)
    idcg = np.sum(sorted(relevances, reverse=True) * discounts)
    return dcg / idcg if idcg > 0 else 0.0

def mean_reciprocal_rank(rankings):
    """
    rankings: list of ranks of first relevant document
    """
    return np.mean([1 / r if r > 0 else 0 for r in rankings])

def demographic_parity(selection_rates):
    """
    selection_rates: dict {group: P(Y^=1 | group)}
    """
    groups = list(selection_rates.values())
    return min(groups) / max(groups) if max(groups) > 0 else 0.0
