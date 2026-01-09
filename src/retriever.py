# src/retriever.py

from typing import List, Dict
import numpy as np

class Retriever:
    def __init__(self, vector_db, embedding_model):
        self.vector_db = vector_db
        self.embedding_model = embedding_model

    def retrieve(self, query: str, k: int = 10) -> List[Dict]:
        """
        Baseline dense retrieval using cosine similarity.
        Returns a list of documents with metadata.
        """
        query_emb = self.embedding_model.encode(query)
        results = self.vector_db.search(query_emb, k=k)
        return results

    def retrieve_with_metadata(self, query: str, k: int = 10) -> List[Dict]:
        """
        Same as retrieve(), but explicitly returns institution/region metadata.
        """
        results = self.retrieve(query, k)
        return [
            {
                "paper_id": r["id"],
                "score": r["score"],
                "institution": r["metadata"].get("institution"),
                "region": r["metadata"].get("region"),
                "abstract": r["document"],
            }
            for r in results
        ]
