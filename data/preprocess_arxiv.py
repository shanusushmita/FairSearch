import json
import pandas as pd
from tqdm import tqdm

INPUT_PATH = "data/raw/arxiv-metadata-oai-snapshot.json"
OUTPUT_PATH = "data/processed/papers.parquet"

def extract_institution(authors):
    # Simple heuristic (students can improve)
    for a in authors:
        if "university" in a.lower():
            return "University"
    return "Unknown"

def map_region(institution):
    # Proxy mapping (simplified)
    if institution in ["MIT", "Stanford", "Oxford"]:
        return "Global_North"
    return "Global_South"

def main(limit=50000):
    records = []
    with open(INPUT_PATH, "r") as f:
        for i, line in enumerate(tqdm(f)):
            if i >= limit:
                break
            paper = json.loads(line)

            if not paper["categories"].startswith("cs."):
                continue

            institution = extract_institution(paper.get("authors", []))
            region = map_region(institution)

            records.append({
                "paper_id": paper["id"],
                "title": paper["title"],
                "abstract": paper["abstract"],
                "authors": paper.get("authors", []),
                "institution": institution,
                "region": region,
                "category": paper["categories"],
                "year": int(paper["versions"][0]["created"][-4:])
            })

    df = pd.DataFrame(records)
    df.to_parquet(OUTPUT_PATH, index=False)
    print(f"Saved {len(df)} papers to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
