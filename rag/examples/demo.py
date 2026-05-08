from rag.pipeline import RAGPipeline


pipeline = RAGPipeline()


# -----------------------------
# Ingest dataset
# -----------------------------

pipeline.ingest(
    "rag/datasets/earthquake_reports.txt"
)


# -----------------------------
# Example Queries
# -----------------------------

queries = [

    "Show tsunami activity near Greece",

    "Retrieve volcanic tremor reports near Italy",

    "Find marine seismic activity near Algeria",

    "Show aftershock sequences following earthquakes",

    "Retrieve reports related to soil saturation and seismic activity",

    "Find tectonic instability near the Mediterranean region",

    "Show earthquake reports associated with infrastructure damage",

    "Retrieve underwater seismic disturbances and tsunami risks",

    "Find volcanic tremor activity combined with seismic monitoring",

    "Show coastal hazard monitoring near Morocco",
]


# -----------------------------
# Run Queries
# -----------------------------

for query in queries:

    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)

    results = pipeline.query(
        query=query,
        top_k=3,
    )

    for idx, result in enumerate(results, start=1):

        print(f"\nResult {idx}:")

        print(result["text"][:300])

        print("-" * 60)