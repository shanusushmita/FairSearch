# FairSearch-arXiv: Starter RAG Repository

## Project Goal
This repository provides a **starter RAG pipeline** for the FairSearch-arXiv course project.
Your task is **not** to build a RAG system from scratch, but to **audit, evaluate, and mitigate bias**
in retrieval and generation.

## What Is Provided
- Preprocessing script for arXiv metadata (filtered to cs.*)
- Vector indexing with ChromaDB / Qdrant
- Baseline dense retrieval (cosine similarity)
- Basic RAG prompt + LLM call
- Evaluation hooks

## What You Are Expected to Implement
- Metadata enrichment (institution, region proxies)
- Retrieval bias measurement
- Fairness metrics using Fairlearn
- Re-ranking strategies (MMR, Fair-Top-K)
- Prompt redesign for perspective balancing
- Evaluation using RAGAS
- Analysis of fairness–utility tradeoffs

## What You Are NOT Expected to Do
- Train embedding models
- Build retrievers from scratch
- Scale beyond 50k documents
- Optimize LLM inference

## Deliverables
- Experimental results (JSON)
- Streamlit fairness dashboard
- Technical report (ACM/IEEE format)

## Evaluation Philosophy
This is a **Responsible AI research project**.
Grades prioritize:
- Sound experimental design
- Clear bias analysis
- Thoughtful mitigation strategies
- Honest discussion of tradeoffs

## Quick Start

1. Install dependencies:
   pip install -r requirements.txt

2. Preprocess data:
   python data/preprocess_arxiv.py

3. Index vectors:
   python src/index_builder.py

4. Run dashboard:
   streamlit run streamlit_app.py

---

© 2026 Shanu Sushmita. All rights reserved.
