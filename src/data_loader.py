import pandas as pd

class ArxivDataset:
    def __init__(self, path="data/processed/papers.parquet"):
        self.df = pd.read_parquet(path)

    def get_documents(self):
        return self.df[["paper_id", "title", "abstract"]]

    def get_metadata(self):
        return self.df[[
            "paper_id", "institution", "region", "category", "year"
        ]]

    def filter_by_category(self, category_prefix="cs."):
        return self.df[self.df["category"].str.startswith(category_prefix)]

    def sample(self, n=1000, seed=42):
        return self.df.sample(n=n, random_state=seed)
