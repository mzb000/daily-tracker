# 📊 Outlier Detection: IQR & Z-Score Methods

Outliers can severely distort linear models and mean-based calculations. Here are the two standard mathematical techniques for detecting and handling them.

---

## 1. Interquartile Range (IQR) Method
- Calculate Quartile 1 ($Q_1$, 25th percentile) and Quartile 3 ($Q_3$, 75th percentile).
- $IQR = Q_3 - Q_1$
- **Lower Bound**: $Q_1 - 1.5 \times IQR$
- **Upper Bound**: $Q_3 + 1.5 \times IQR$
- Any value outside these bounds is flagged as an outlier.

```python
q1 = df['val'].quantile(0.25)
q3 = df['val'].quantile(0.75)
iqr = q3 - q1
outliers = df[(df['val'] < q1 - 1.5 * iqr) | (df['val'] > q3 + 1.5 * iqr)]
```

---

## 2. Z-Score Method (Standard Score)
Assumes the data is approximately normally distributed.
$$z = \frac{x - \mu}{\sigma}$$
- If $|z| > 3$, the data point lies more than 3 standard deviations from the mean (less than 0.3% probability in standard normal).
