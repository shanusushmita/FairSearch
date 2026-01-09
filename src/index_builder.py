import chromadb
from chromadb.utils import embedding_functions

def build_chroma_index(df, persist_dir="data/indices/chroma"):
    client = chromadb.Client(
        chromadb.config.Settings(persist_directory=persist_dir)
    )

    embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name="all-MiniLM-L6-v2"
    )

    collection = client.get_or_create_collection(
        name="arxiv",
        embedding_function=embedding_fn
    )

    collection.add(
        ids=df["paper_id"].tolist(),
        documents=df["abstract"].tolist(),
        metadatas=df[[
            "institution", "region", "category", "year"
        ]].to_dict("records")
    )

    client.persist()
