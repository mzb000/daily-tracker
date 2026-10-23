# 🧠 Machine Learning & Data Science Daily Lab

Welcome to the **Machine Learning & Data Science Daily Lab**! This repository is an open-source, daily-updated educational resource featuring interactive Jupyter Notebooks (`.ipynb`) with step-by-step mathematical derivations, clean runnable code, line-by-line breakdowns, and interview prep designed to help practitioners master machine learning from first principles.

---

## 📚 Complete Curriculum Index

### 📍 Week 1: Foundations of Scientific Computing & Math
- 📓 **[01_numpy_basics_and_memory.ipynb](01-python-data-science/01_numpy_basics_and_memory.ipynb)**: Contiguous memory, SIMD vectorization, float32 vs float64.
- 📓 **[02_broadcasting_and_indexing.ipynb](01-python-data-science/02_broadcasting_and_indexing.ipynb)**: Array shape alignment and high-speed Boolean masking.
- 📓 **[03_vectorization_benchmarks.ipynb](01-python-data-science/03_vectorization_benchmarks.ipynb)**: Pure Python loops vs C-compiled NumPy arrays benchmark.
- 📓 **[04_matrix_operations_linear_algebra.ipynb](01-python-data-science/04_matrix_operations_linear_algebra.ipynb)**: Dot products, matrix multiplication ($A @ B$), determinants, and inverses.
- 📓 **[05_random_sampling_distributions.ipynb](01-python-data-science/05_random_sampling_distributions.ipynb)**: Seed reproducibility, Gaussian distributions, and train/test shuffling.

---

### 📍 Week 2: Advanced Data Wrangling & Cleaning
- 📓 **[01_series_and_dataframes.ipynb](02-pandas-data-wrangling/01_series_and_dataframes.ipynb)**: Dataframe anatomy, `loc` vs `iloc` selection mechanics.
- 📓 **[02_missing_data_imputation.ipynb](02-pandas-data-wrangling/02_missing_data_imputation.ipynb)**: Median vs Mean vs Mode imputation for null hygiene.
- 📓 **[03_groupby_and_aggregations.ipynb](02-pandas-data-wrangling/03_groupby_and_aggregations.ipynb)**: Split-Apply-Combine patterns and pivot tables.
- 📓 **[04_outlier_detection_and_remediation.ipynb](02-pandas-data-wrangling/04_outlier_detection_and_remediation.ipynb)**: IQR outlier bounds, Z-Score, and Winsorization (capping).
- 📓 **[05_merging_and_joining_datasets.ipynb](02-pandas-data-wrangling/05_merging_and_joining_datasets.ipynb)**: Relational joins (Inner, Left, Outer) for multi-table features.

---

### 📍 Week 3: Exploratory Data Analysis & Feature Engineering
- 📓 **[01_eda_descriptive_stats_and_distributions.ipynb](03-exploratory-data-analysis/01_eda_descriptive_stats_and_distributions.ipynb)**: Central tendency, skewness, kurtosis, and distribution shapes.
- 📓 **[02_correlation_matrices_and_heatmaps.ipynb](03-exploratory-data-analysis/02_correlation_matrices_and_heatmaps.ipynb)**: Pearson vs Spearman correlation, Multicollinearity, and VIF.
- 📓 **[03_categorical_encoding_onehot_label.ipynb](03-exploratory-data-analysis/03_categorical_encoding_onehot_label.ipynb)**: One-Hot Encoding, Dummy Variable Trap ($K-1$), and Frequency Encoding.
- 📓 **[04_feature_scaling_standard_vs_minmax.ipynb](03-exploratory-data-analysis/04_feature_scaling_standard_vs_minmax.ipynb)**: StandardScaler vs MinMaxScaler vs RobustScaler and Data Leakage prevention.
- 📓 **[05_eda_capstone_churn_case_study.ipynb](03-exploratory-data-analysis/05_eda_capstone_churn_case_study.ipynb)**: End-to-end Telecom Churn EDA workflow and feature engineering.

---

### 📍 Week 4: Supervised Learning (Linear & Logistic Models)
- 📓 **[01_linear_regression_scratch.ipynb](04-supervised-learning/01_linear_regression_scratch.ipynb)**: Linear hypothesis, MSE loss surface, and Gradient Descent from scratch.
- 📓 **[02_regularization_ridge_lasso.ipynb](04-supervised-learning/02_regularization_ridge_lasso.ipynb)**: L1 Lasso (Feature Selection) vs L2 Ridge penalties.
- 📓 **[03_regression_evaluation_metrics.ipynb](04-supervised-learning/03_regression_evaluation_metrics.ipynb)**: MAE, MSE, RMSE, and $R^2$ score mathematical derivations.
- 📓 **[04_logistic_regression_scratch.ipynb](04-supervised-learning/04_logistic_regression_scratch.ipynb)**: Sigmoid activation function and Binary Cross-Entropy loss.
- 📓 **[05_classification_metrics_and_confusion_matrix.ipynb](04-supervised-learning/05_classification_metrics_and_confusion_matrix.ipynb)**: Confusion Matrix, Precision, Recall, and F1-Score.

---

### 📍 Week 5: Tree-Based Algorithms & Ensemble Methods
- 📓 **[01_decision_trees_entropy_gini_scratch.ipynb](05-ensemble-algorithms/01_decision_trees_entropy_gini_scratch.ipynb)**: Shannon Entropy, Gini Impurity, and recursive Information Gain splitting.
- 📓 **[02_random_forests_and_bagging_mechanics.ipynb](05-ensemble-algorithms/02_random_forests_and_bagging_mechanics.ipynb)**: Bootstrap aggregating, feature subsampling, and Out-of-Bag (OOB) scoring.
- 📓 **[03_adaboost_sequential_weighting.ipynb](05-ensemble-algorithms/03_adaboost_sequential_weighting.ipynb)**: Sequential boosting, sample reweighting, and weak learner aggregation.
- 📓 **[04_gradient_boosting_and_xgboost_scratch.ipynb](05-ensemble-algorithms/04_gradient_boosting_and_xgboost_scratch.ipynb)**: Residual error fitting, shrinkage learning rate, and second-order gradients.
- 📓 **[05_hyperparameter_tuning_grid_vs_random.ipynb](05-ensemble-algorithms/05_hyperparameter_tuning_grid_vs_random.ipynb)**: GridSearchCV vs RandomizedSearchCV vs Bayesian Optimization.

---

### 📍 Week 6: Unsupervised Learning & Dimensionality Reduction
- 📓 **[01_kmeans_clustering_from_scratch.ipynb](06-unsupervised-learning/01_kmeans_clustering_from_scratch.ipynb)**: Lloyd algorithm, Euclidean centroids, and convergence loops in NumPy.
- 📓 **[02_elbow_method_and_silhouette_analysis.ipynb](06-unsupervised-learning/02_elbow_method_and_silhouette_analysis.ipynb)**: Inertia curves, elbow detection, and silhouette cohesion scores.
- 📓 **[03_pca_covariance_eigenvectors_from_scratch.ipynb](06-unsupervised-learning/03_pca_covariance_eigenvectors_from_scratch.ipynb)**: Covariance matrix, eigenvector decomposition, and explained variance.
- 📓 **[04_hierarchical_clustering_and_dendrograms.ipynb](06-unsupervised-learning/04_hierarchical_clustering_and_dendrograms.ipynb)**: Agglomerative bottom-up clustering, linkage criteria, and dendrogram cuts.
- 📓 **[05_tsne_and_high_dimensional_visualization.ipynb](06-unsupervised-learning/05_tsne_and_high_dimensional_visualization.ipynb)**: Non-linear manifold embedding, Student-t distribution, and perplexity tuning.

---

## 🎯 Daily Cadence & Code Quality
- **Pure Jupyter Notebook Format (`.ipynb`)**: Directly viewable in your browser on GitHub.
- **Deep Explanations**: Theory, math derivations, line-by-line commentary, and interview Q&As.
- **Sequential Commits**: Each notebook is committed and pushed individually with clean conventional commit messages.

---

*Authored by Muhammad Zabiullah ([@mzb000](https://github.com/mzb000))*
