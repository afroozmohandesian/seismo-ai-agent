# seismo-ai-agent

A modular AI-driven seismic analysis platform for:

- near-real-time seismic ingestion,
- hybrid Retrieval-Augmented Generation (RAG),
- probabilistic BELIEF-state propagation,
- uncertainty-aware scientific computing,
- and scalable AI engineering workflows.

The repository was developed as part of an advanced AI software engineering technical assessment focused on:

- scientific-computing architectures,
- modular AI systems,
- probabilistic reasoning,
- seismic data integration,
- and retrieval-based AI pipelines.

---

# Repository

GitHub Repository:

https://github.com/afroozmohandesian/seismo-ai-agent

---

# Project Overview

The project combines three major subsystems:

| Module | Purpose |
|---|---|
| Perception System | Near-real-time seismic ingestion and synchronization |
| Hybrid RAG Pipeline | Semantic seismic information retrieval |
| BELIEF-State System | Probabilistic uncertainty propagation |

The implementation intentionally prioritizes:

- modularity,
- maintainability,
- explainability,
- probabilistic reasoning,
- scientific-computing principles,
- scalable architecture design.

---

# Repository Structure

```text
seismo-ai-agent/
│
├── api/
├── belief/
├── perception/
├── rag/
├── shared/
├── tests/
├── docs/
├── diagram/
│
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# 1. Perception System — Option 1 (Task 1)

The perception subsystem implements a modular near-real-time seismic ingestion pipeline.

Main capabilities include:

- continuous polling,
- multi-provider ingestion,
- schema harmonization,
- synchronization tracking,
- scientific duplicate detection,
- SQLite persistence,
- FastAPI exposure,
- pytest-based testing.

Supported providers:

- USGS
- EMSC

---

## Main Components

```text
perception/
├── fetchers/
├── listeners/
├── storage/
├── validators/
├── models/
└── deduplication/
```

---

## Key Engineering Features

- incremental synchronization,
- retry handling,
- restart-safe ingestion,
- scientific deduplication,
- API interoperability,
- Docker deployment,
- structured logging,
- automated testing.

---

## High-Level Workflow

```text
External Providers (USGS / EMSC)
            ↓
       Fetchers
            ↓
      Normalization
            ↓
       Validation
            ↓
 Scientific Deduplication
            ↓
        SQLite
            ↓
        FastAPI
            ↓
      API Consumers
```

---

# Perception System Documentation

## Main Technical Report

- [Perception System Report](docs/option1_perception_system_report.md)

Based on the scientific paper:

- [Near-Real-Time Integration of Multi-Source Seismic Data](docs/references/near_real_time_seismic_data_integration.pdf)

---

## Engineering Notes and Debug Reports

### Stable Event Identifier Bug

- [Stable Event Identifier Bug Report](docs/engineering_notes/deduplication_bug_report.md)

Resolved unstable Python hash-based event identifiers causing duplicate persistence across ingestion restarts.

---

### FastAPI + SQLite Threading Issue

- [FastAPI SQLite Threading Issue](docs/engineering_notes/fastapi_sqlite_threading_issue.md)

Resolved SQLite thread-safety issues caused by FastAPI worker-thread execution.

---

### Pytest Import Resolution Issue

- [Pytest Package Resolution Bug Report](docs/engineering_notes/pytest_import_issue.md)

Resolved pytest module resolution issues in the modular package structure.

---

# 2. Hybrid RAG Retrieval Pipeline — Option 1 (Task 2)

The RAG subsystem implements an advanced hybrid retrieval architecture for seismic and geological information retrieval.

Main capabilities include:

- document ingestion,
- semantic chunking,
- vector embeddings,
- FAISS vector indexing,
- BM25 retrieval,
- hybrid ranking,
- query expansion,
- metadata filtering,
- retrieval completeness scoring,
- answer generation.

---

## Main Components

```text
rag/
├── ingestion/
├── embeddings/
├── retrieval/
├── filtering/
├── evaluation/
└── generation/
```

---

## Retrieval Features

- Dense Retrieval
- BM25 Retrieval
- Hybrid Retrieval
- Query Expansion
- Metadata Filtering
- Hierarchical Filtering
- Retrieval Deduplication
- Explainable Ranking

---

# RAG Documentation

## Main Technical Report

- [Hybrid RAG Pipeline Report](docs/option1_rag_pipeline_report.md)

---

## Engineering Notes

- [Hierarchical Filtering Bugfix Report](docs/engineering_notes/hierarchical_filtering_bugfix_report.md)
- [Hierarchical Metadata Filtering Report](docs/engineering_notes/hierarchical_metadata_filtering_report.md)
- [Hybrid Retrieval Evaluation Report](docs/engineering_notes/hybrid_retrieval_evaluation_report.md)
- [Query Expansion and Retrieval Planning Report](docs/engineering_notes/query_expansion_and_retrieval_planning_report.md)
- [Retrieval Duplication Debug Report](docs/engineering_notes/retrieval_duplication_debug_report.md)

---

# 3. BELIEF-State System — Option 2

The BELIEF subsystem implements a modular probabilistic state-propagation architecture for uncertainty-aware seismic S-wave velocity estimation.

Main capabilities include:

- Bayesian belief refinement,
- Kalman uncertainty propagation,
- tensor-oriented scientific storage,
- reliability tracking,
- memory-mapped persistence,
- concurrent regional processing,
- probabilistic confidence estimation.

---

## Main Components

```text
belief/
├── concurrency/
├── core/
├── examples/
├── models/
├── storage/
├── tracking/
└── updates/
```

---

## Architectural Features

- Strategy Pattern
- Repository Pattern
- Orchestrator Pattern
- Tensor-oriented scientific computing
- Modular probabilistic updates
- Concurrent regional processing
- Memory-mapped persistence

---

# BELIEF-State Documentation

## Main Technical Report

- [BELIEF-State Architecture Report](docs/option2_belief_state_report.md)

---

## Architecture Diagram

- [Option 2 System Architecture Diagram](diagram/Option2_diagram.png)

---

# Scientific References

The repository includes scientific papers used during architectural design and implementation.

```text
docs/references/
```

Included references:

- `near_real_time_seismic_data_integration.pdf`
- `ensemble_kalman_epistemic_uncertainty_2024.pdf`
- `epistemic_uncertainty_survey_2021.pdf`
- `pinn_uncertainty_hypocenter_determination_2025.pdf`
- `uncertainty_propagation_seismic_inversion_2024.pdf`

---

# Installation

## Clone Repository

```bash
git clone git@github.com:afroozmohandesian/seismo-ai-agent.git
cd seismo-ai-agent
```

---

## Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

## Start API

```bash
python main.py
```

---

## Run Tests

```bash
pytest
```

---

# Docker

## Build Docker Image

```bash
docker build -t seismo-ai-agent .
```

---

## Run Docker Container

```bash
docker run -p 8000:8000 seismo-ai-agent
```

---

# API Endpoints

| Endpoint | Purpose |
|---|---|
| `/health` | Service health monitoring |
| `/events` | Retrieve seismic events |

FastAPI automatically exposes OpenAPI documentation.

---

# Branch Organization

| Branch | Purpose |
|---|---|
| `feature/perception-listener` | Near-real-time seismic ingestion system |
| `feature/rag-system` | Hybrid RAG retrieval pipeline |
| `feature/belief-state-system` | BELIEF-state uncertainty propagation |
| `main` | Integrated stable branch |

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | API layer |
| SQLite | Lightweight persistence |
| NumPy | Tensor computation |
| FAISS | Vector similarity retrieval |
| Sentence Transformers | Embedding generation |
| BM25 | Keyword retrieval |
| Pydantic | Typed probabilistic models |
| Pytest | Automated testing |
| Docker | Containerization |

---

# Engineering Focus

This project intentionally emphasizes:

- uncertainty-aware AI systems,
- modular architecture,
- scientific-computing design,
- explainable retrieval,
- scalable probabilistic reasoning,
- AI engineering best practices,
- maintainable research-oriented codebases.

The resulting platform behaves as a lightweight scientific AI framework rather than a collection of isolated scripts.

---

# Future Improvements

Potential future extensions include:

- distributed retrieval systems,
- GPU tensor execution,
- probabilistic spatial propagation,
- asynchronous orchestration,
- distributed workers,
- reranking models,
- physics-informed neural operators,
- scalable vector databases,
- multi-agent orchestration.

---

# Author

Afrooz Mohandesian