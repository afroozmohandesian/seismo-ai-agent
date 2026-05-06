# FastAPI SQLite Threading Issue

## Summary

The `/events` FastAPI endpoint returned an internal server error when accessing the SQLite persistence layer.

The issue appeared after integrating the SQLite event store with the FastAPI service layer.

---

## Affected Components

- FastAPI Service Layer
- SQLite Persistence Layer
- Event Retrieval Endpoint (`/events`)

---

## Problem Description

The FastAPI application initialized a shared SQLite connection during application startup:

```python
store = SQLiteStore()
```

When the `/events` endpoint was called, FastAPI executed the request handler inside a worker thread.

However, the SQLite connection had originally been created in the main application thread.

This caused SQLite to reject the operation.

---

## Observed Error

```text
sqlite3.ProgrammingError:
SQLite objects created in a thread can only be used in that same thread.
```

---

## Root Cause Analysis

SQLite connections are thread-bound by default.

The original database connection initialization used:

```python
sqlite3.connect(db_path)
```

This configuration prevents the same connection object from being accessed across different threads.

FastAPI internally executes synchronous endpoint functions using worker threads, which triggered the threading constraint.

---

## Expected Behavior

The FastAPI `/events` endpoint should access the persistence layer successfully and return stored seismic events as JSON responses.

---

## Actual Behavior

The endpoint failed with HTTP 500 Internal Server Error whenever the SQLite connection was accessed from a different execution thread.

---

## Resolution

The SQLite connection was updated to allow cross-thread usage.

### Previous Implementation

```python
self.connection = sqlite3.connect(db_path)
```

### Updated Implementation

```python
self.connection = sqlite3.connect(
    db_path,
    check_same_thread=False,
)
```

This configuration allows the SQLite connection object to be safely reused across FastAPI worker threads in the current application setup.

---

## Result

After applying the fix:

- the `/events` endpoint responded successfully
- FastAPI could access persisted events correctly
- SQLite operations worked across request threads
- the API service layer became operational

---

## Engineering Impact

This issue highlighted an important interaction between synchronous database clients and asynchronous web frameworks.

It also reinforced the need to consider threading and concurrency behavior when integrating persistence layers with API services.

---

## Lessons Learned

- SQLite connections are thread-constrained by default.
- FastAPI executes synchronous endpoint handlers in worker threads.
- Persistence layers should be configured with concurrency behavior in mind.
- Threading issues can emerge even in lightweight local service architectures.

---

## Status

Resolved ✅