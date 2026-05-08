# Task 2 — Advanced RAG Retrieval Pipeline Documentation

## Overview

This project implements an advanced Retrieval-Augmented Generation (RAG) pipeline for seismic and geological event analysis.

The goal of the system is to:

* Read seismic reports
* Store them in a searchable format
* Understand user questions
* Retrieve the most relevant seismic information
* Generate a readable answer from retrieved reports

The pipeline combines multiple retrieval techniques and filtering strategies to improve search quality and relevance.

---

# What Is a RAG System?

A RAG (Retrieval-Augmented Generation) system is an AI architecture that combines:

1. Information Retrieval
2. Language Generation

Instead of generating answers only from a pre-trained AI model, the system first searches relevant documents and then builds an answer using the retrieved information.

In simple terms:

* The system searches documents like a search engine
* Then it writes an answer like an AI assistant

---

# High-Level Pipeline

The full pipeline works in the following order:

1. Load seismic reports
2. Split reports into smaller chunks
3. Convert chunks into vector embeddings
4. Store embeddings in a vector database
5. Enrich chunks with metadata
6. Expand user queries
7. Retrieve relevant chunks
8. Combine Dense Retrieval and BM25 Retrieval
9. Filter results using metadata
10. Remove duplicate results
11. Score retrieval completeness
12. Generate final answer

---

# Step 1 — Document Loading

The system first loads a seismic dataset from a text file.

Example:

```python
pipeline.ingest(
    "rag/datasets/earthquake_reports.txt"
)
```

The dataset contains multiple seismic reports such as:

* Earthquakes
* Tsunami activity
* Offshore seismic disturbances
* Volcanic tremors
* Infrastructure damage
* Marine hazard alerts

---

# Step 2 — Text Chunking

Large documents are difficult to search directly.

To solve this problem, the pipeline splits the document into smaller sections called chunks.

Each chunk contains a small group of related seismic reports.

Example:

```text
Report 1
Report 2
Report 3
```

Chunking improves:

* Retrieval accuracy
* Embedding quality
* Search efficiency

---

# Step 3 — Embedding Generation

The system converts each text chunk into a numerical vector representation called an embedding.

Embeddings allow the system to understand semantic meaning.

This means:

* Similar texts produce similar vectors
* Related seismic concepts become searchable

Example:

A query about:

```text
underwater seismic activity
```

can still retrieve documents mentioning:

```text
marine tectonic disturbances
```

because their semantic meaning is similar.

---

# Step 4 — Vector Database Storage

The embeddings are stored in a FAISS vector database.

FAISS enables fast similarity search across many embeddings.

The vector store allows the system to:

* Compare embeddings efficiently
* Retrieve semantically similar reports
* Perform dense retrieval

---

# Step 5 — Metadata Enrichment

Each chunk is enriched with additional metadata.

Metadata helps the system organize and filter information.

Examples of metadata:

| Metadata Type | Example |
| ------------- | ------- |
| Region        | Greece  |
| Category      | Marine  |
| Source        | USGS    |
| Hazard Type   | Tsunami |

Example enriched document:

```python
{
    "region": "Greece",
    "category": "marine",
    "source": "USGS"
}
```

Metadata enables advanced filtering during retrieval.

---

# Step 6 — Query Expansion

User queries are automatically expanded with related seismic terminology.

Example:

Original query:

```text
Show tsunami activity near Greece
```

Expanded query:

```text
Show tsunami activity near Greece marine hazard offshore seismic activity underwater displacement
```

This improves retrieval quality because the system searches for:

* Exact keywords
* Related concepts
* Semantically similar terms

Query expansion increases recall and retrieval coverage.

---

# Step 7 — Dense Retrieval

Dense retrieval uses vector similarity search.

The query embedding is compared against stored document embeddings.

The system retrieves chunks that are semantically similar to the user query.

Advantages:

* Understands meaning
* Finds related concepts
* Works beyond exact keyword matching

Example:

A search for:

```text
volcanic tremor
```

may retrieve:

```text
magma movement
```

because they are semantically related.

---

# Step 8 — BM25 Retrieval

BM25 is a traditional keyword-based retrieval algorithm.

Unlike dense retrieval, BM25 focuses on:

* Exact keywords
* Word frequency
* Term importance

Advantages:

* Strong exact-match retrieval
* Reliable keyword search
* Useful for technical terminology

---

# Step 9 — Hybrid Retrieval

The system combines:

* Dense Retrieval
* BM25 Retrieval

This approach is called Hybrid Retrieval.

Why combine both?

Because:

* Dense retrieval understands meaning
* BM25 understands exact keywords

Together they improve:

* Precision
* Recall
* Search robustness

---

# Step 10 — Hybrid Scoring

Each retrieved document receives:

* Dense score
* BM25 score
* Hybrid score

Example:

```python
{
    "dense_score": 0.9,
    "bm25_score": 0.85,
    "hybrid_score": 0.88
}
```

The hybrid score combines semantic similarity and keyword relevance.

This helps rank the most relevant seismic reports first.

---

# Step 11 — Deduplication

Sometimes multiple retrieval methods return the same document.

The pipeline removes duplicate results automatically.

Benefits:

* Cleaner output
* Reduced redundancy
* Better ranking quality

---

# Step 12 — Metadata Filtering

Users can retrieve documents using metadata filters.

Example:

```python
filters={
    "category": "marine"
}
```

This restricts retrieval to marine seismic reports only.

Filtering improves:

* Search precision
* Domain targeting
* Result relevance

---

# Step 13 — Hierarchical Filtering

The system also supports hierarchical category expansion.

Example:

Searching for:

```text
tsunami
```

can automatically include related categories such as:

* Marine
* Offshore
* Underwater seismic activity

This improves retrieval completeness.

---

# Step 14 — Retrieval Completeness Scoring

The pipeline evaluates how well retrieved results cover the user query.

Example:

```text
Retrieval Completeness Score: 0.82
```

Higher scores indicate:

* Better retrieval quality
* Better query coverage
* More relevant retrieved information

---

# Step 15 — Answer Generation

After retrieval, the system generates a readable answer.

The answer is built using:

* Retrieved reports
* Relevant seismic insights
* Combined retrieval context

Example:

```text
Generated Answer:
Tsunami monitoring systems remained active after offshore seismic activity near Greece.
```

---

# Example Queries

The pipeline supports many seismic retrieval scenarios.

Examples:

* Show tsunami activity near Greece
* Retrieve volcanic tremor reports near Italy
* Find marine seismic activity near Algeria
* Show aftershock sequences following earthquakes
* Find tectonic instability near the Mediterranean region
* Show reports mentioning USGS
* Find EMSC seismic alerts

---

# Example Retrieval Output

Example result:

```python
{
    "region": "Greece",
    "category": "marine",
    "source": "USGS",
    "dense_score": 0.8,
    "bm25_score": 0.79,
    "hybrid_score": 0.80
}
```

This shows:

* Retrieved region
* Hazard category
* Data source
* Semantic similarity score
* Keyword relevance score
* Final hybrid ranking score

---

# Technologies Used

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Main programming language       |
| FAISS                 | Vector similarity search        |
| Sentence Transformers | Embedding generation            |
| BM25                  | Keyword retrieval               |
| RAG Architecture      | Retrieval + generation pipeline |

---

# Main Features Implemented

## Retrieval Features

* Dense Retrieval
* BM25 Retrieval
* Hybrid Retrieval
* Query Expansion
* Retrieval Deduplication

## Filtering Features

* Metadata Filtering
* Hierarchical Filtering

## Evaluation Features

* Retrieval Completeness Scoring
* Hybrid Score Inspection
* Ranking Analysis

## Generation Features

* Answer Generation
* Retrieval Context Integration
* Explainable Retrieval Outputs

---

# Final Result

The final system is a fully working advanced RAG retrieval pipeline capable of:

* Understanding seismic queries
* Retrieving semantically relevant reports
* Combining keyword and vector search
* Filtering retrieval results
* Ranking results using hybrid scoring
* Generating readable answers

The pipeline successfully demonstrates:

* Modern RAG architecture
* Hybrid information retrieval
* Semantic search
* Metadata-aware retrieval
* Explainable ranking outputs
* End-to-end AI retrieval workflow

---

# Conclusion

This project extends a basic RAG system into a more advanced retrieval architecture.

The pipeline combines:

* Semantic vector search
* Traditional keyword retrieval
* Query expansion
* Filtering systems
* Hybrid scoring
* Retrieval evaluation

The result is a more accurate, flexible, and explainable seismic retrieval system suitable for advanced AI retrieval experiments and information analysis workflows.
