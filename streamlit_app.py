# app/streamlit_app.py

import streamlit as st
import plotly.express as px
from src.retriever import Retriever
from src.rerank import fair_rerank
from src.metrics import demographic_parity

st.title("FairSearch-arXiv: Fairness Diagnostic")

query = st.text_input("Enter your search query")

if query:
    # Instantiate retriever (already built)
    retriever = Retriever(vector_db=None, embedding_model=None)

    # Baseline retrieval
    baseline_results = retriever.retrieve_with_metadata(query, k=10)

    # Fairness-aware retrieval
    fair_results = fair_rerank(baseline_results)

    def region_distribution(results):
        dist = {}
        for r in results:
            region = r["region"]
            dist[region] = dist.get(region, 0) + 1
        return dist

    base_dist = region_distribution(baseline_results)
    fair_dist = region_distribution(fair_results)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Standard Search")
        st.write(base_dist)
        fig = px.bar(x=base_dist.keys(), y=base_dist.values())
        st.plotly_chart(fig)

    with col2:
        st.subheader("FairSearch")
        st.write(fair_dist)
        fig = px.bar(x=fair_dist.keys(), y=fair_dist.values())
        st.plotly_chart(fig)
