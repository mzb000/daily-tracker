# 📋 EDA & Data Preprocessing Interview Reference

### Top Questions & Answers:
1. **When should you use Median instead of Mean?**
   - When the feature distribution is skewed or contains extreme outliers (e.g., household wealth, income). The median represents the true typical observation.
2. **What is Data Leakage?**
   - When information from outside the training dataset (such as test set statistics) is used to create the model. Example: Computing `StandardScaler.fit()` on the whole dataset before train/test split. ALWAYS fit on Train, transform Test!
3. **What is the Dummy Variable Trap?**
   - High collinearity introduced when all $K$ categories are one-hot encoded without dropping the intercept ($K-1$ columns).
