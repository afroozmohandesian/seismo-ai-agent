# Modular Near-Real-Time Seismic Event Integration System

## Technical Assessment — Option 1 (Task 1)

---

# 1. Introduction

Modern seismic monitoring systems continuously ingest earthquake events from heterogeneous external providers. However, different agencies often expose incompatible schemas, inconsistent identifiers, and asynchronous update policies, making reliable integration difficult [1].

This project presents a modular near-real-time seismic ingestion system designed for:

- continuous event acquisition,
- schema harmonization,
- scientific duplicate detection,
- incremental synchronization,
- persistent storage,
- and API-based access.

The implementation was partially inspired by recent modular seismic integration architectures proposed for near-real-time multi-source interoperability and harmonization [1].

# 2. Design Goals

The system was designed around the following engineering objectives:

| Goal | Design Choice |
|---|---|
| Modularity | Layered architecture |
| Reliability | Retry + fallback providers |
| Synchronization safety | Incremental polling |
| Duplicate prevention | Scientific deduplication |
| Extensibility | Abstract fetcher interfaces |
| Deployment portability | Docker containerization |
| API interoperability | FastAPI service layer |
| Maintainability | Pytest-based testing |

The implementation intentionally prioritizes maintainability, reliability, and architectural clarity over excessive infrastructure complexity.

# 3. System Architecture

The platform follows a layered ingestion architecture inspired by modern seismic integration pipelines [1].

Main components include:

- Fetcher layer
- Listener orchestration layer
- Validation layer
- Deduplication module
- Persistence layer
- FastAPI service layer

High-level workflow:

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

This separation of concerns improves:

- maintainability,
- extensibility,
- debugging simplicity,
- and provider independence.

# 4. Multi-Source Event Ingestion

The system integrates earthquake data from:

- USGS,
- EMSC.

Each provider is abstracted through an independent fetcher module responsible for:

- API communication,
- response parsing,
- schema conversion,
- and retry handling.

This modular design follows interoperability principles proposed in recent seismic integration literature [1].

# 5. Incremental Synchronization

Continuous polling systems must avoid repeatedly processing previously ingested events.

The implementation therefore stores synchronization metadata representing the latest processed event timestamp.

During each polling cycle:

- only newer events are requested,
- duplicate processing is minimized,
- and restart-safe synchronization is preserved.

This approach aligns with scalable near-real-time acquisition strategies discussed in [1].

# 6. Scientific Duplicate Detection

Different providers may report the same earthquake using slightly different:

- timestamps,
- coordinates,
- or identifiers.

To address this issue, the implementation combines:

- exact database deduplication,
- temporal similarity,
- geographic similarity,
- and magnitude comparison.

Geographic proximity is computed using the Haversine formula.

This follows scientific harmonization principles commonly used in cross-provider seismic integration systems [1].

# 7. Persistence and API Layer

The system uses SQLite for lightweight persistent storage.

Persistent storage guarantees:

- restart-safe ingestion,
- synchronization consistency,
- and local portability.

The platform exposes its data using FastAPI.

Implemented endpoints include:

| Endpoint | Purpose |
|---|---|
| `/health` | Service monitoring |
| `/events` | Retrieve seismic events |

FastAPI automatically generates OpenAPI documentation, improving interoperability and developer usability.

# 8. Logging, Testing, and Deployment

The system includes:

- structured logging,
- pytest-based automated testing,
- and Docker containerization.

Automated tests were implemented using pytest to validate core scientific and engineering functionality, including:

- geographic distance computation,
- scientific duplicate detection,
- synchronization behavior,
- and ingestion correctness.

Testing significantly improves:

- reliability,
- regression prevention,
- maintainability,
- and debugging safety.

Docker containerization provides:

- reproducible environments,
- deployment portability,
- and dependency isolation.

These engineering practices improve long-term scalability and production readiness.

# 9. Engineering Challenges

Several realistic engineering issues were encountered during development.

## Stable Identifier Consistency

Python hash-based identifiers initially produced inconsistent event IDs across application restarts.

This issue was resolved using stable provider-generated identifiers.

## SQLite Threading Constraints

Concurrent FastAPI access caused SQLite threading errors.

The issue was resolved using cross-thread SQLite configuration.

## Duplicate Event Handling

Different providers reported the same earthquakes with inconsistent metadata.

Scientific similarity-based deduplication resolved this issue.

# 10. Future Improvements

Potential future extensions include:

- PostgreSQL/PostGIS migration,
- asynchronous ingestion pipelines,
- Kafka-based streaming,
- distributed workers,
- probabilistic duplicate detection,
- and scalable vector-based retrieval integration.

These directions align closely with modern seismic interoperability infrastructures [1].

# 11. Conclusion

This work presents a modular near-real-time seismic event integration system for multi-source earthquake monitoring.

The implementation satisfies the primary assessment requirements:

- continuous ingestion,
- schema harmonization,
- scientific duplicate detection,
- synchronization safety,
- persistent storage,
- API interoperability,
- automated testing,
- and modular deployment.

The resulting platform behaves as a lightweight seismic integration microservice rather than a simple scripting prototype.

The architecture intentionally prioritizes:

- modularity,
- reliability,
- maintainability,
- and extensibility toward future scientific AI infrastructures.

# References

[1] Melgarejo-Hernández, J. et al. *Near-Real-Time Integration of Multi-Source Seismic Data*, Sensors, 2026.