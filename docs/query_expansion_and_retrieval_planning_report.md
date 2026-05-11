# Query Expansion and Retrieval Planning Report

## Overview

This report describes the implementation and evaluation of the query expansion layer integrated into the hybrid Retrieval-Augmented Generation (RAG) pipeline.

The objective of this enhancement was to improve semantic retrieval coverage and retrieval flexibility through lightweight query planning and semantic query enrichment.

The implemented architecture introduces a preprocessing stage between the user query and the hybrid retrieval engine.

---

# Motivation

Initial retrieval experiments revealed several limitations:

- acronym-sensitive queries were partially retrieved,
- entity-oriented retrieval remained inconsistent,
- semantic coverage was limited for short queries,
- and conceptually related hazard reports were sometimes missed.

Examples included:

```text
USGS
EMSC
tsunami
offshore activity
```

Although hybrid dense-sparse retrieval improved lexical robustness, retrieval quality still depended heavily on the exact wording of the user query.

---

# Architectural Goal

The goal of query expansion was to improve:

- semantic recall,
- contextual retrieval coverage,
- retrieval flexibility,
- and retrieval planning behavior.

This enhancement also moves the architecture closer to modern agentic retrieval systems.

---

# Query Expansion Architecture

A dedicated retrieval planning component was implemented:

```text
rag/retrieval/query_expander.py
```

The component performs lightweight semantic expansion before retrieval execution.

---

# Retrieval Flow

The updated retrieval pipeline now follows:

```text
User Query
    ↓
Query Expansion
    ↓
Hybrid Retrieval
    ↓
Metadata Filtering
    ↓
Retrieval Evaluation
```

This introduces a lightweight retrieval orchestration layer.

---

# Query Expansion Strategy

The expansion mechanism uses predefined semantic mappings.

Example:

```python
"tsunami": [
    "marine hazard",
    "offshore seismic activity",
    "underwater displacement",
]
```

Additional expansions were implemented for:

- earthquakes,
- volcanic activity,
- USGS,
- EMSC,
- and seismic monitoring terminology.

---

# Example Expansion

Example input query:

```text
Show tsunami activity near Greece
```

Expanded query:

```text
Show tsunami activity near Greece
marine hazard
offshore seismic activity
underwater displacement
```

The expanded query is then embedded and passed into the hybrid retrieval pipeline.

---

# Observed Improvements

The query expansion layer improved retrieval behavior in several scenarios.

Notable improvements included:

- broader semantic coverage,
- stronger marine hazard retrieval,
- improved offshore activity matching,
- and increased retrieval diversity.

The expansion layer also interacted effectively with hierarchical metadata filtering.

---

# Synergy with Hierarchical Filtering

Query expansion and hierarchical metadata filtering worked together successfully.

Example:

```text
tsunami
```

expanded into:

- marine hazard,
- offshore activity,
- underwater displacement.

At retrieval time, hierarchical filtering additionally expanded:

```text
marine
```

into:

- tsunami,
- offshore,
- underwater.

This significantly increased semantic recall.

---

# Retrieval Recall Improvements

Several tsunami and marine hazard queries produced stronger retrieval diversity after expansion.

The retrieval system successfully surfaced:

- offshore events,
- underwater tectonic disturbances,
- marine hazard alerts,
- and tsunami preparedness reports.

This indicates improved semantic retrieval flexibility.

---

# Important Retrieval Tradeoff

The evaluation also revealed an important production-level retrieval tradeoff.

Query expansion improved:

- semantic recall,
- contextual coverage,
- and retrieval flexibility.

However, query expansion also introduced broader retrieval behavior.

In some cases, retrieval precision decreased.

---

# Example Precision Tradeoff

Example query:

```text
Show reports mentioning USGS
```

Expanded query:

```text
USGS seismic monitoring earthquake surveillance hazard assessment
```

This broader semantic context improved recall but also retrieved more generalized seismic reports.

As a result:

- semantic coverage increased,
- but exact source specificity decreased.

---

# Key Engineering Insight

The evaluation demonstrates an important retrieval systems principle:

```text
Query expansion improves recall,
but can reduce precision.
```

This is a realistic tradeoff commonly observed in production retrieval systems.

The behavior observed during evaluation closely resembles enterprise search and large-scale RAG architectures.

---

# Architectural Significance

This enhancement introduces lightweight retrieval planning capabilities into the system.

The retrieval pipeline now performs:

- semantic query enrichment,
- retrieval-aware query preprocessing,
- contextual expansion,
- and retrieval orchestration.

These patterns are strongly aligned with:

- agentic retrieval systems,
- retrieval planning architectures,
- and modern AI workflow orchestration.

---

# Limitations

The current implementation remains rule-based.

The system does not yet support:

- dynamic query rewriting,
- learned semantic expansion,
- probabilistic query planning,
- or weighted retrieval expansion.

Expanded terms currently receive equal importance during retrieval.

---

# Future Improvements

Potential future extensions include:

- weighted query expansion,
- retrieval reranking,
- adaptive semantic rewriting,
- ontology-aware expansion,
- and LLM-based retrieval planning.

These enhancements would improve retrieval precision while preserving semantic recall.

---

# Engineering Outcome

The implemented query expansion layer successfully improved retrieval flexibility and semantic coverage.

The evaluation demonstrated:

- improved semantic recall,
- stronger hazard-oriented retrieval,
- successful interaction with hierarchical filtering,
- and realistic precision-recall tradeoffs.

The resulting architecture now more closely resembles production-oriented agentic retrieval systems.

---

# Conclusion

Query expansion and retrieval planning were successfully integrated into the hybrid RAG pipeline.

The enhancement introduced:

- semantic query enrichment,
- lightweight retrieval planning,
- contextual retrieval expansion,
- and improved semantic retrieval flexibility.

The evaluation also revealed realistic precision-recall tradeoffs, highlighting important engineering considerations for production-scale retrieval systems.