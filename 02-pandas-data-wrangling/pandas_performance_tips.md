# ⚡ Pandas Memory Optimization & Performance Guide

When working with production datasets (millions of rows), default Pandas settings can consume gigabytes of RAM.

---

## 1. Downcast Numeric Types
Pandas defaults integers to `int64` (8 bytes) and floats to `float64` (8 bytes).
If values fit into smaller ranges:
- `int8`: -128 to 127
- `int16`: -32,768 to 32,767
- `float32`: Single precision (reduces RAM by 50%)

```python
df['age'] = df['age'].astype('int16')
df['score'] = df['score'].astype('float32')
```

---

## 2. Convert Low-Cardinality Strings to Categorical
If a column with 1,000,000 rows has only 5 unique values (e.g., country, gender, status), converting it to `category` can reduce RAM usage by up to **90%**!

```python
df['status'] = df['status'].astype('category')
```

---

## 3. Avoid `.iterrows()` at all costs
Iterating over rows in a Python loop is 100x slower than vectorized operations:
- ❌ `for index, row in df.iterrows(): ...`
- ✅ Vectorized: `df['total'] = df['price'] * df['quantity']`
- ✅ If unavoidable, use `.apply()` with NumPy or Cython.
