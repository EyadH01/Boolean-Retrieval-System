# Boolean Retrieval System

**Author:** Eyad Harb  
**Language:** Python

---

## Overview
This project implements a simple **Boolean Retrieval System** in Python. It allows users to:

- Add documents to the system.
- Build an inverted index for efficient term-based retrieval.
- Perform **boolean AND queries** to find documents containing all query terms.
- Retrieve the actual document texts based on query results.

---

## Features
- Case-insensitive indexing.
- Efficient term-document mapping using an inverted index.
- Supports multiple document additions and queries.
- Easy to extend for OR/NOT queries.

---

## Usage
```python
from boolean_retrieval_system import BooleanRetrievalSystem

brs = BooleanRetrievalSystem()
brs.add_document(1, "the quick brown fox")
brs.add_document(2, "the slow brown dog")
brs.add_document(3, "the quick red fox")

# Query for documents containing both 'quick' and 'fox'
result = brs.query("quick AND fox")
print("Documents matching query:", brs.get_documents(result))
