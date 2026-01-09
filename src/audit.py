# src/audit.py

from collections import Counter
from typing import List, Dict

def institutional_distribution(results: List[Dict]) -> Dict[str, float]:
    """
    Computes the distribution of institutions or regions
    in the retrieved Top-K results.
    """
    groups = [r["region"] for r in results]
    counts = Counter(groups)
    total = sum(counts.values())
    return {g: c / total for g, c in counts.items()}

def run_retrieval_audit(retriever, queries: List[str], k: int = 10):
    """
    Runs retrieval bias audit across multiple queries.
    """
    audit_results = []

    for q in queries:
        results = retriever.retrieve_with_metadata(q, k)
        dist = institutional_distribution(results)

        audit_results.append({
            "query": q,
            "distribution": dist
        })

    return audit_results
