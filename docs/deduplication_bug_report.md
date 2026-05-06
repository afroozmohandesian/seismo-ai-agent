# Stable Event Identifier Bug Report

## Summary

Duplicate seismic events were not being detected correctly after restarting the ingestion pipeline.

Although the SQLite persistence layer enforced a composite primary key for deduplication, previously ingested events were inserted again during subsequent executions instead of being rejected as duplicates.

---

## Affected Component

- Perception Module
- SQLite Persistence Layer
- Event Deduplication Logic

---

## Problem Description

The ingestion pipeline relied on generated event identifiers derived from the upstream provider event ID.

The original implementation used Python’s built-in `hash()` function:

```python
eid = hash(feature["id"])
```

This caused unstable event identifiers across application restarts.

As a result, the same upstream seismic event could receive a different identifier in different execution sessions.

---

## Root Cause Analysis

Python’s built-in `hash()` function is intentionally non-deterministic between interpreter sessions because of hash randomization security mechanisms.

Therefore:

- identical upstream events
- produced different `eid` values
- after each application restart

This broke persistence-level duplicate detection because SQLite interpreted those events as new records.

---

## Expected Behavior

Previously stored events should be rejected by the database deduplication constraints:

```sql
PRIMARY KEY (eid, timestamp)
```

Repeated ingestion runs should not insert duplicate seismic events.

---

## Actual Behavior

Duplicate events were repeatedly inserted into the SQLite database because event identifiers changed between executions.

The persistence layer therefore failed to recognize already-ingested records.

---

## Resolution

The unstable hashed identifier was replaced with the provider’s original stable identifier.

### Previous Implementation

```python
eid = hash(feature["id"])
```

### Updated Implementation

```python
eid = str(feature["id"])
```

Additional changes were required to support stable identifiers consistently across the pipeline.

### Schema Updates

#### Event Model

```python
eid: int
```

Updated to:

```python
eid: str
```

#### SQLite Schema

```sql
eid INTEGER
```

Updated to:

```sql
eid TEXT
```

The SQLite database was recreated after the schema update.

---

## Result

After applying the fix:

- event identifiers remain stable across executions
- duplicate ingestion is correctly prevented
- persistence behaves consistently after restarts
- database deduplication constraints function as intended
- ingestion behavior is now restart-safe

---

## Engineering Impact

This issue highlighted the importance of deterministic identifiers in persistent ingestion systems.

It also reinforced the need for stable upstream provenance tracking in multi-source seismic pipelines.

---

## Lessons Learned

- Application-level hashing should not be used for persistent identifiers unless deterministic hashing is explicitly guaranteed.
- Upstream provider identifiers are preferable for long-term consistency and traceability.
- Persistence-layer deduplication critically depends on stable canonical identifiers.
- Deduplication logic should always be validated across restart scenarios.

---

## Status

Resolved ✅