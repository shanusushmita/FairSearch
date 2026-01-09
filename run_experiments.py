# run_experiments.py

from src.retriever import Retriever
from src.audit import run_retrieval_audit
from src.metrics import demographic_parity
import json

def main():
    # Instantiate retriever (provided in starter code)
    retriever = Retriever(vector_db=None, embedding_model=None)

    with open("data/queries.json") as f:
        queries = json.load(f)

    audit_results = run_retrieval_audit(retriever, queries)

    with open("experiments/retrieval_audit.json", "w") as f:
        json.dump(audit_results, f, indent=2)

if __name__ == "__main__":
    main()
