# Bug Fix Report — Hierarchical Filtering

## Overview

During the implementation of hierarchical metadata filtering, a runtime error occurred when executing the hierarchical filtering demo:

```text
TypeError: unhashable type: 'list'
```

## Root Cause

The error originated inside the `HierarchicalFilter.expand_category()` method.

The filtering pipeline was passing a list of categories instead of a single hashable category key when accessing the category hierarchy dictionary.

Problematic behavior:

```python
CATEGORY_HIERARCHY.get(category)
```

where `category` was unexpectedly a list.

Since Python dictionaries require hashable keys, passing a list caused the retrieval pipeline to fail during hierarchical metadata expansion.

---

## Resolution

The filtering logic was updated to properly handle hierarchical category expansion by iterating through category collections before performing dictionary lookups.

The fix introduced:

* Validation of category input types
* Safe expansion of hierarchical category lists
* Proper handling of nested metadata filters
* Stable recursive category traversal

---

## Result

After the fix:

* Hierarchical filtering executes successfully
* Metadata expansion works correctly across related seismic categories
* The demo pipeline completes without runtime failures
* Retrieval results now include expanded category relationships such as:

  * `marine`
  * `offshore`
  * `tsunami`

---

## Verification

The corrected implementation was validated using the following demo query:

```text
tsunami activity
```

with hierarchical metadata filtering enabled.

The pipeline successfully returned expanded retrieval results across related marine and offshore seismic categories without errors.
