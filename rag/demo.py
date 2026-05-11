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

    "Show reports mentioning USGS",

    "Find EMSC seismic alerts",

    "Retrieve offshore earthquake activity",

    "Find tsunami hazard reports",
]


# -----------------------------
# Run Queries
# -----------------------------

for query in queries:

    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)

    response = pipeline.query(
        query=query,
        top_k=3,
    )

    results = response["results"]

    print("\nGenerated Answer:")
    print(response["answer"])

    for idx, result in enumerate(
        results,
        start=1,
    ):

        print(f"\nResult {idx}:")

        print(result["text"][:300])

        print("-" * 60)


# -----------------------------
# Metadata Filtering Demo
# -----------------------------

print("\n")
print("=" * 80)
print("METADATA FILTERING DEMO")
print("=" * 80)

filtered_response = pipeline.query(
    query="marine seismic activity",
    top_k=20,
    filters={
        "category": "marine",
    }
)

print("\nGenerated Answer:")
print(filtered_response["answer"])

filtered_results = (
    filtered_response["results"]
)

for idx, result in enumerate(
    filtered_results,
    start=1,
):

    print(f"\nFiltered Result {idx}:")

    print(result)

    print("-" * 60)


# -----------------------------
# Hierarchical Filtering Demo
# -----------------------------

print("\n")
print("=" * 80)
print("HIERARCHICAL FILTERING DEMO")
print("=" * 80)

hierarchical_response = pipeline.query(
    query="tsunami activity",
    top_k=10,
    filters={
        "category": [
            "marine",
            "tsunami",
            "offshore",
        ],
        "region": [
            "Greece",
            "Sicily",
            "Turkey",
        ],
    }
)

print("\nGenerated Answer:")
print(hierarchical_response["answer"])

hierarchical_results = (
    hierarchical_response["results"]
)

for idx, result in enumerate(
    hierarchical_results,
    start=1,
):

    print(f"\nHierarchical Result {idx}:")

    print(result)

    print("-" * 60)