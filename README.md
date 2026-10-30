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
- 📓 **[06_einsum_and_tensor_contractions.ipynb](01-python-data-science/06_einsum_and_tensor_contractions.ipynb)**: Einstein summation convention, tensor contractions, and batched multi-head attention scores.
- 📓 **[07_memory_strides_and_c_vs_fortran_layout.ipynb](01-python-data-science/07_memory_strides_and_c_vs_fortran_layout.ipynb)**: Array memory strides, C-order vs Fortran layout, zero-copy views, and cache line locality.
- 📓 **[08_numpy_memory_mapping_and_memmap.ipynb](01-python-data-science/08_numpy_memory_mapping_and_memmap.ipynb)**: Out-of-core processing with `np.memmap`, OS virtual memory page faults, and chunked binary I/O.
- 📓 **[09_numpy_c_api_and_cython_acceleration.ipynb](01-python-data-science/09_numpy_c_api_and_cython_acceleration.ipynb)**: Typed memoryviews, C-stride pointers, Amdahl's law speedup, and GIL release acceleration.


- 🔬 **[10_numpy_ufuncs_and_vectorize_internals.ipynb](01-python-data-science/10_numpy_ufuncs_and_vectorize_internals.ipynb)**: Universal functions (`ufunc`), fast loop dispatch, C-level type loops, and custom `@np.vectorize` kernels.
- 🔬 **[11_sparse_matrices_csr_csc_coo_scratch.ipynb](01-python-data-science/11_sparse_matrices_csr_csc_coo_scratch.ipynb)**: Sparse matrix storage formats (CSR, CSC, COO) and Sparse Matrix-Vector Multiplication (SpMV) from scratch.
- 🔬 **[12_svd_singular_value_decomposition_scratch.ipynb](01-python-data-science/12_svd_singular_value_decomposition_scratch.ipynb)**: Singular Value Decomposition ($A = U \Sigma V^T$), Eckart-Young low-rank approximation, and image compression.
- 🔬 **[13_pseudo_inverse_moore_penrose_scratch.ipynb](01-python-data-science/13_pseudo_inverse_moore_penrose_scratch.ipynb)**: Moore-Penrose Pseudoinverse ($A^+$), condition numbers, and SVD numerical regularization.
---

### 📍 Week 2: Advanced Data Wrangling & Cleaning
- 📓 **[01_series_and_dataframes.ipynb](02-pandas-data-wrangling/01_series_and_dataframes.ipynb)**: Dataframe anatomy, `loc` vs `iloc` selection mechanics.
- 📓 **[02_missing_data_imputation.ipynb](02-pandas-data-wrangling/02_missing_data_imputation.ipynb)**: Median vs Mean vs Mode imputation for null hygiene.
- 📓 **[03_groupby_and_aggregations.ipynb](02-pandas-data-wrangling/03_groupby_and_aggregations.ipynb)**: Split-Apply-Combine patterns and pivot tables.
- 📓 **[04_outlier_detection_and_remediation.ipynb](02-pandas-data-wrangling/04_outlier_detection_and_remediation.ipynb)**: IQR outlier bounds, Z-Score, and Winsorization (capping).
- 📓 **[05_merging_and_joining_datasets.ipynb](02-pandas-data-wrangling/05_merging_and_joining_datasets.ipynb)**: Relational joins (Inner, Left, Outer) for multi-table features.
- 📓 **[06_advanced_datetime_and_window_functions.ipynb](02-pandas-data-wrangling/06_advanced_datetime_and_window_functions.ipynb)**: Rolling windows, Exponentially Weighted Moving Averages (EWMA), and lag feature engineering.
- 📓 **[07_memory_optimization_categorical_and_downcasting.ipynb](02-pandas-data-wrangling/07_memory_optimization_categorical_and_downcasting.ipynb)**: Integer/float downcasting, Categorical dictionary encoding, and chunked CSV streaming.
- 📓 **[08_pandas_to_arrow_and_polars_interop.ipynb](02-pandas-data-wrangling/08_pandas_to_arrow_and_polars_interop.ipynb)**: Apache Arrow zero-copy memory layout, PyArrow string dtypes, and Polars lazy query plan optimization.
- 📓 **[09_custom_rolling_apply_and_numba.ipynb](02-pandas-data-wrangling/09_custom_rolling_apply_and_numba.ipynb)**: High-performance rolling window analytics, Welford's algorithm for rolling variance, and Numba JIT acceleration.


- 🔬 **[10_multiindex_hierarchical_dataframes.ipynb](02-pandas-data-wrangling/10_multiindex_hierarchical_dataframes.ipynb)**: MultiIndex hierarchical indexing, tuple keys, level cross-section slicing (`xs`), and `unstack` reshaping.
- 🔬 **[11_time_series_resampling_and_asof_joins.ipynb](02-pandas-data-wrangling/11_time_series_resampling_and_asof_joins.ipynb)**: Financial time-series resampling, custom calendar frequencies, and point-in-time `merge_asof` without lookahead bias.
- 🔬 **[12_string_vectorization_and_regex_wrangling.ipynb](02-pandas-data-wrangling/12_string_vectorization_and_regex_wrangling.ipynb)**: High-speed vectorized string methods (`.str`), regex pattern extraction, and Unicode normalization (`NFKD`).
- 🔬 **[13_streaming_chunked_etl_pipelines.ipynb](02-pandas-data-wrangling/13_streaming_chunked_etl_pipelines.ipynb)**: Out-of-core chunked ETL pipelines, memory-bounded batch processing, and generator-based streaming aggregations.
---

### 📍 Week 3: Exploratory Data Analysis & Feature Engineering
- 📓 **[01_eda_descriptive_stats_and_distributions.ipynb](03-exploratory-data-analysis/01_eda_descriptive_stats_and_distributions.ipynb)**: Central tendency, skewness, kurtosis, and distribution shapes.
- 📓 **[02_correlation_matrices_and_heatmaps.ipynb](03-exploratory-data-analysis/02_correlation_matrices_and_heatmaps.ipynb)**: Pearson vs Spearman correlation, Multicollinearity, and VIF.
- 📓 **[03_categorical_encoding_onehot_label.ipynb](03-exploratory-data-analysis/03_categorical_encoding_onehot_label.ipynb)**: One-Hot Encoding, Dummy Variable Trap ($K-1$), and Frequency Encoding.
- 📓 **[04_feature_scaling_standard_vs_minmax.ipynb](03-exploratory-data-analysis/04_feature_scaling_standard_vs_minmax.ipynb)**: StandardScaler vs MinMaxScaler vs RobustScaler and Data Leakage prevention.
- 📓 **[05_eda_capstone_churn_case_study.ipynb](03-exploratory-data-analysis/05_eda_capstone_churn_case_study.ipynb)**: End-to-end Telecom Churn EDA workflow and feature engineering.
- 📓 **[06_target_encoding_and_leakage_prevention.ipynb](03-exploratory-data-analysis/06_target_encoding_and_leakage_prevention.ipynb)**: Out-of-fold target encoding, M-estimate empirical Bayes smoothing, and leakage prevention.
- 📓 **[07_automated_data_profiling_and_drift_inspection.ipynb](03-exploratory-data-analysis/07_automated_data_profiling_and_drift_inspection.ipynb)**: Programmatic statistical health audit, zero-variance alerts, and kurtosis thresholds.
- 📓 **[08_copula_and_multivariate_dependence.ipynb](03-exploratory-data-analysis/08_copula_and_multivariate_dependence.ipynb)**: Copulas for non-linear feature correlation, Sklar's theorem, Clayton lower-tail dependence, and synthetic generation.
- 📓 **[09_umap_uniform_manifold_approximation.ipynb](03-exploratory-data-analysis/09_umap_uniform_manifold_approximation.ipynb)**: Uniform Manifold Approximation and Projection (UMAP), fuzzy simplicial sets, and local metric learning.


- 🔬 **[10_feature_interactions_polynomial_and_crosses.ipynb](03-exploratory-data-analysis/10_feature_interactions_polynomial_and_crosses.ipynb)**: Polynomial interaction features, categorical Cartesian crosses, and sparsity-aware interaction selection.
- 🔬 **[11_weight_of_evidence_and_information_value.ipynb](03-exploratory-data-analysis/11_weight_of_evidence_and_information_value.ipynb)**: Weight of Evidence (WoE) and Information Value (IV) for credit risk modeling and monotonic binning.
- 🔬 **[12_missingness_mechanisms_mcar_mar_mnar.ipynb](03-exploratory-data-analysis/12_missingness_mechanisms_mcar_mar_mnar.ipynb)**: Little's MCAR statistical test, missingness mechanisms (MCAR, MAR, MNAR), and pattern indicators.
- 🔬 **[13_distribution_testing_shapiro_and_anderson.ipynb](03-exploratory-data-analysis/13_distribution_testing_shapiro_and_anderson.ipynb)**: Shapiro-Wilk, Anderson-Darling normality hypothesis testing, and automated Box-Cox power transforms.
---

### 📍 Week 4: Supervised Learning (Linear & Logistic Models)
- 📓 **[01_linear_regression_scratch.ipynb](04-supervised-learning/01_linear_regression_scratch.ipynb)**: Linear hypothesis, MSE loss surface, and Gradient Descent from scratch.
- 📓 **[02_regularization_ridge_lasso.ipynb](04-supervised-learning/02_regularization_ridge_lasso.ipynb)**: L1 Lasso (Feature Selection) vs L2 Ridge penalties.
- 📓 **[03_regression_evaluation_metrics.ipynb](04-supervised-learning/03_regression_evaluation_metrics.ipynb)**: MAE, MSE, RMSE, and $R^2$ score mathematical derivations.
- 📓 **[04_logistic_regression_scratch.ipynb](04-supervised-learning/04_logistic_regression_scratch.ipynb)**: Sigmoid activation function and Binary Cross-Entropy loss.
- 📓 **[05_classification_metrics_and_confusion_matrix.ipynb](04-supervised-learning/05_classification_metrics_and_confusion_matrix.ipynb)**: Confusion Matrix, Precision, Recall, and F1-Score.
- 📓 **[06_elastic_net_regularization_from_scratch.ipynb](04-supervised-learning/06_elastic_net_regularization_from_scratch.ipynb)**: Combining L1 and L2 penalties with Coordinate Descent soft-thresholding from scratch.
- 📓 **[07_cost_sensitive_classification_and_bayes_decision_theory.ipynb](04-supervised-learning/07_cost_sensitive_classification_and_bayes_decision_theory.ipynb)**: Asymmetric cost matrices, Bayes decision theory, and financially optimal probability thresholds.
- 📓 **[08_quantile_regression_scratch.ipynb](04-supervised-learning/08_quantile_regression_scratch.ipynb)**: Pinball loss function, conditional quantiles, subgradient descent, and heteroscedastic prediction intervals.
- 📓 **[09_ordinal_logistic_regression.ipynb](04-supervised-learning/09_ordinal_logistic_regression.ipynb)**: Ordinal Logistic Regression, proportional odds model, cumulative logits, and monotonic cutpoint optimization.


- 🔬 **[10_poisson_and_negative_binomial_regression.ipynb](04-supervised-learning/10_poisson_and_negative_binomial_regression.ipynb)**: Generalized Linear Models (GLMs) for count data: Poisson log-linear regression and Negative Binomial overdispersion.
- 🔬 **[11_huber_and_ransac_robust_regression.ipynb](04-supervised-learning/11_huber_and_ransac_robust_regression.ipynb)**: Robust regression against severe outliers: Huber loss piecewise gradient and RANSAC consensus fitting.
- 🔬 **[12_multinomial_logistic_regression_scratch.ipynb](04-supervised-learning/12_multinomial_logistic_regression_scratch.ipynb)**: Softmax regression for multi-class classification, Cross-Entropy loss gradients, and Hessian updates.
- 🔬 **[13_isotonic_regression_nonparametric_calibration.ipynb](04-supervised-learning/13_isotonic_regression_nonparametric_calibration.ipynb)**: Non-parametric monotonic regression via Pool Adjacent Violators Algorithm (PAVA) and probability calibration.
---

### 📍 Week 5: Tree-Based Algorithms & Ensemble Methods
- 📓 **[01_decision_trees_entropy_gini_scratch.ipynb](05-ensemble-algorithms/01_decision_trees_entropy_gini_scratch.ipynb)**: Shannon Entropy, Gini Impurity, and recursive Information Gain splitting.
- 📓 **[02_random_forests_and_bagging_mechanics.ipynb](05-ensemble-algorithms/02_random_forests_and_bagging_mechanics.ipynb)**: Bootstrap aggregating, feature subsampling, and Out-of-Bag (OOB) scoring.
- 📓 **[03_adaboost_sequential_weighting.ipynb](05-ensemble-algorithms/03_adaboost_sequential_weighting.ipynb)**: Sequential boosting, sample reweighting, and weak learner aggregation.
- 📓 **[04_gradient_boosting_and_xgboost_scratch.ipynb](05-ensemble-algorithms/04_gradient_boosting_and_xgboost_scratch.ipynb)**: Residual error fitting, shrinkage learning rate, and second-order gradients.
- 📓 **[05_hyperparameter_tuning_grid_vs_random.ipynb](05-ensemble-algorithms/05_hyperparameter_tuning_grid_vs_random.ipynb)**: GridSearchCV vs RandomizedSearchCV vs Bayesian Optimization.
- 📓 **[06_catboost_ordered_boosting_and_target_statistics.ipynb](05-ensemble-algorithms/06_catboost_ordered_boosting_and_target_statistics.ipynb)**: Ordered boosting principle, oblivious symmetric trees, and prediction shift elimination.
- 📓 **[07_stacking_and_blending_ensembles_from_scratch.ipynb](05-ensemble-algorithms/07_stacking_and_blending_ensembles_from_scratch.ipynb)**: Multi-model stacking meta-learners and out-of-fold cross-validation blending from scratch.
- 📓 **[08_lightgbm_goss_and_efb_scratch.ipynb](05-ensemble-algorithms/08_lightgbm_goss_and_efb_scratch.ipynb)**: LightGBM Gradient-based One-Side Sampling (GOSS), histogram binning, and variance gain estimation from scratch.
- 📓 **[09_isolation_forest_path_derivation.ipynb](05-ensemble-algorithms/09_isolation_forest_path_derivation.ipynb)**: Isolation Forest BST average path length $c(n)$ derivation, random hyperplane cuts, and anomaly score thresholding.


- 🔬 **[10_quantile_regression_forests.ipynb](05-ensemble-algorithms/10_quantile_regression_forests.ipynb)**: Quantile Regression Forests (QRF) for conditional prediction intervals and non-parametric epistemic uncertainty.
- 🔬 **[11_extremely_randomized_trees_extratrees.ipynb](05-ensemble-algorithms/11_extremely_randomized_trees_extratrees.ipynb)**: ExtraTrees architecture: fully randomized split thresholds, variance reduction, and bias-variance analysis.
- 🔬 **[12_partial_dependence_and_ale_plots.ipynb](05-ensemble-algorithms/12_partial_dependence_and_ale_plots.ipynb)**: Explainable AI (XAI): Partial Dependence Plots (PDP) vs Accumulated Local Effects (ALE) from scratch.
- 🔬 **[13_xgboost_regularization_gamma_lambda.ipynb](05-ensemble-algorithms/13_xgboost_regularization_gamma_lambda.ipynb)**: XGBoost regularization mechanics: L1 ($alpha$), L2 ($lambda$), tree complexity ($gamma$), and split gain math.
---

### 📍 Week 6: Unsupervised Learning & Dimensionality Reduction
- 📓 **[01_kmeans_clustering_from_scratch.ipynb](06-unsupervised-learning/01_kmeans_clustering_from_scratch.ipynb)**: Lloyd algorithm, Euclidean centroids, and convergence loops in NumPy.
- 📓 **[02_elbow_method_and_silhouette_analysis.ipynb](06-unsupervised-learning/02_elbow_method_and_silhouette_analysis.ipynb)**: Inertia curves, elbow detection, and silhouette cohesion scores.
- 📓 **[03_pca_covariance_eigenvectors_from_scratch.ipynb](06-unsupervised-learning/03_pca_covariance_eigenvectors_from_scratch.ipynb)**: Covariance matrix, eigenvector decomposition, and explained variance.
- 📓 **[04_hierarchical_clustering_and_dendrograms.ipynb](06-unsupervised-learning/04_hierarchical_clustering_and_dendrograms.ipynb)**: Agglomerative bottom-up clustering, linkage criteria, and dendrogram cuts.
- 📓 **[05_tsne_and_high_dimensional_visualization.ipynb](06-unsupervised-learning/05_tsne_and_high_dimensional_visualization.ipynb)**: Non-linear manifold embedding, Student-t distribution, and perplexity tuning.
- 📓 **[06_dbscan_density_based_clustering_from_scratch.ipynb](06-unsupervised-learning/06_dbscan_density_based_clustering_from_scratch.ipynb)**: Density-based clustering, $\epsilon$ neighborhoods, core/border/noise points from scratch.
- 📓 **[07_gaussian_mixture_models_em_algorithm_scratch.ipynb](06-unsupervised-learning/07_gaussian_mixture_models_em_algorithm_scratch.ipynb)**: Soft probabilistic clustering and the Expectation-Maximization (EM) algorithm from scratch.
- 📓 **[08_hdbscan_hierarchical_density_clustering.ipynb](06-unsupervised-learning/08_hdbscan_hierarchical_density_clustering.ipynb)**: HDBSCAN mutual reachability distance, core distances, condensed cluster trees, and persistence stability selection.
- 📓 **[09_spectral_clustering_normalized_cuts.ipynb](06-unsupervised-learning/09_spectral_clustering_normalized_cuts.ipynb)**: Normalized Graph Laplacian cuts, RBF affinity matrices, Fiedler eigenvector projections, and manifold clustering.


- 🔬 **[10_kernel_pca_nonlinear_manifolds.ipynb](06-unsupervised-learning/10_kernel_pca_nonlinear_manifolds.ipynb)**: Non-linear dimensionality reduction: Kernel trick ($K_{ij} = k(x_i, x_j)$), Gram matrix centering, and manifold unfolding.
- 🔬 **[11_gaussian_random_projection_johnson_lindenstrauss.ipynb](06-unsupervised-learning/11_gaussian_random_projection_johnson_lindenstrauss.ipynb)**: Johnson-Lindenstrauss lemma and Gaussian random projection for ultra-high-dimensional feature compression.
- 🔬 **[12_optics_density_ordering_clustering.ipynb](06-unsupervised-learning/12_optics_density_ordering_clustering.ipynb)**: OPTICS clustering: Core distances, reachability distances, and cluster extraction across variable densities.
- 🔬 **[13_mean_shift_clustering_scratch.ipynb](06-unsupervised-learning/13_mean_shift_clustering_scratch.ipynb)**: Non-parametric mode-seeking: Kernel Density Estimation (KDE) gradient ascent and bandwidth tuning from scratch.
---

### 📍 Week 7: Deep Learning Foundations & Neural Networks
- 📓 **[01_single_layer_perceptron_scratch.ipynb](07-deep-learning-foundations/01_single_layer_perceptron_scratch.ipynb)**: Artificial neuron, threshold activation, boolean logic gates, and the XOR problem.
- 📓 **[02_activation_functions_relu_sigmoid_tanh_gelu.ipynb](07-deep-learning-foundations/02_activation_functions_relu_sigmoid_tanh_gelu.ipynb)**: Vanishing gradients, dying ReLU, and modern GELU activations.
- 📓 **[03_feedforward_neural_network_numpy_scratch.ipynb](07-deep-learning-foundations/03_feedforward_neural_network_numpy_scratch.ipynb)**: Multi-Layer Perceptron (MLP) forward pass, matrix shapes, and cross-entropy in pure NumPy.
- 📓 **[04_backpropagation_calculus_chain_rule.ipynb](07-deep-learning-foundations/04_backpropagation_calculus_chain_rule.ipynb)**: Calculus chain rule, partial derivatives, and complete XOR training loop.
- 📓 **[05_pytorch_tensor_fundamentals_and_autograd.ipynb](07-deep-learning-foundations/05_pytorch_tensor_fundamentals_and_autograd.ipynb)**: PyTorch tensors, GPU acceleration, automatic differentiation, and `nn.Module`.
- 📓 **[06_optimizers_sgd_momentum_rmsprop_adam.ipynb](07-deep-learning-foundations/06_optimizers_sgd_momentum_rmsprop_adam.ipynb)**: SGD with momentum, RMSProp adaptive rates, and Adam optimizer implementation.
- 📓 **[07_regularization_dropout_batchnorm_weight_decay.ipynb](07-deep-learning-foundations/07_regularization_dropout_batchnorm_weight_decay.ipynb)**: Inverted dropout from scratch, batch normalization, and weight decay.
- 📓 **[08_convolutional_neural_networks_cnn_basics.ipynb](07-deep-learning-foundations/08_convolutional_neural_networks_cnn_basics.ipynb)**: 2D convolution from scratch, Sobel edge filter kernels, stride, padding, and pooling.
- 📓 **[09_recurrent_neural_networks_and_lstm_from_scratch.ipynb](07-deep-learning-foundations/09_recurrent_neural_networks_and_lstm_from_scratch.ipynb)**: Long Short-Term Memory cell gating equations ($f, i, \tilde{C}, o$) and constant error carousel from scratch.
- 📓 **[10_gru_gated_recurrent_unit_scratch.ipynb](07-deep-learning-foundations/10_gru_gated_recurrent_unit_scratch.ipynb)**: Gated Recurrent Unit (GRU) forward pass, reset and update gates, and BPTT math from scratch.
- 📓 **[11_weight_initialization_xavier_he.ipynb](07-deep-learning-foundations/11_weight_initialization_xavier_he.ipynb)**: Variance preservation math across deep layers, Xavier Glorot vs He Kaiming initialization derivation.


- 🔬 **[12_layer_normalization_vs_batch_norm.ipynb](07-deep-learning-foundations/12_layer_normalization_vs_batch_norm.ipynb)**: Deep learning normalization comparative audit: LayerNorm vs BatchNorm vs GroupNorm vs RMSNorm mechanics.
- 🔬 **[13_learning_rate_schedulers_cosine_warmup.ipynb](07-deep-learning-foundations/13_learning_rate_schedulers_cosine_warmup.ipynb)**: Modern learning rate scheduling: Linear warmup with Cosine Annealing decay and cyclical restarts.
- 🔬 **[14_gradient_clipping_norm_vs_value.ipynb](07-deep-learning-foundations/14_gradient_clipping_norm_vs_value.ipynb)**: Vanishing and exploding gradients: Global L2 norm clipping vs value threshold clamping.
- 🔬 **[15_residual_connections_and_identity_mapping.ipynb](07-deep-learning-foundations/15_residual_connections_and_identity_mapping.ipynb)**: Deep residual architectures: Identity mapping proofs, gradient highways, and degradation mitigation.
---

### 📍 Week 8: Natural Language Processing (NLP) & Text Embeddings
- 📓 **[01_text_preprocessing_tokenization_lemmatization.ipynb](08-nlp-and-text-embeddings/01_text_preprocessing_tokenization_lemmatization.ipynb)**: Regex cleaning, tokenization, stop word filtering, and stemming vs lemmatization.
- 📓 **[02_bag_of_words_and_tfidf_from_scratch.ipynb](08-nlp-and-text-embeddings/02_bag_of_words_and_tfidf_from_scratch.ipynb)**: Term frequency, inverse document frequency, and L2 normalization from scratch.
- 📓 **[03_word_embeddings_word2vec_cosine_similarity.ipynb](08-nlp-and-text-embeddings/03_word_embeddings_word2vec_cosine_similarity.ipynb)**: Dense semantic vectors, Word2Vec skip-gram intuition, and vector arithmetic (King - Man + Woman = Queen).
- 📓 **[04_sentiment_analysis_naive_bayes_nlp.ipynb](08-nlp-and-text-embeddings/04_sentiment_analysis_naive_bayes_nlp.ipynb)**: Bayes theorem, Laplace smoothing, and multinomial spam classification.
- 📓 **[05_recurrent_neural_networks_rnn_and_lstm.ipynb](08-nlp-and-text-embeddings/05_recurrent_neural_networks_rnn_and_lstm.ipynb)**: Sequence memory, hidden state propagation, and LSTM gating mechanics.
- 📓 **[06_subword_tokenization_sentencepiece_and_unigram.ipynb](08-nlp-and-text-embeddings/06_subword_tokenization_sentencepiece_and_unigram.ipynb)**: SentencePiece Unigram tokenization model, Viterbi segmentation, and vocabulary pruning.
- 📓 **[07_fasttext_subword_embeddings.ipynb](08-nlp-and-text-embeddings/07_fasttext_subword_embeddings.ipynb)**: FastText subword character n-gram hashing, FNV-1a hash buckets, and Out-of-Vocabulary (OOV) generalization.
- 📓 **[08_bert_masked_language_model_scratch.ipynb](08-nlp-and-text-embeddings/08_bert_masked_language_model_scratch.ipynb)**: BERT Masked Language Modeling (MLM) 80/10/10 masking rule, Cloze cross-entropy loss, and bidirectional pretraining.


- 🔬 **[09_textrank_keyword_and_summary_extraction.ipynb](08-nlp-and-text-embeddings/09_textrank_keyword_and_summary_extraction.ipynb)**: Graph-based unsupervised NLP: PageRank random walks on word co-occurrence graphs for keyword extraction.
- 🔬 **[10_edit_distance_levenshtein_and_damerau.ipynb](08-nlp-and-text-embeddings/10_edit_distance_levenshtein_and_damerau.ipynb)**: Dynamic programming string metrics: Levenshtein distance, Damerau transposition, and fuzzy matching.
- 🔬 **[11_bpe_vs_wordpiece_tokenization_comparison.ipynb](08-nlp-and-text-embeddings/11_bpe_vs_wordpiece_tokenization_comparison.ipynb)**: Modern LLM subword tokenizers: Byte-Pair Encoding (BPE) vs WordPiece likelihood merge criteria.
- 🔬 **[12_cross_lingual_embeddings_alignment_procrustes.ipynb](08-nlp-and-text-embeddings/12_cross_lingual_embeddings_alignment_procrustes.ipynb)**: Multilingual embedding alignment: Orthogonal Procrustes problem, SVD rotation, and bilingual lexicons.
---

### 📍 Week 9: Transformers, Attention & Large Language Models (LLMs)
- 📓 **[01_self_attention_mechanism_from_scratch.ipynb](09-transformers-and-llms/01_self_attention_mechanism_from_scratch.ipynb)**: Queries ($Q$), Keys ($K$), Values ($V$), and Scaled Dot-Product Attention in NumPy.
- 📓 **[02_multi_head_attention_and_positional_encoding.ipynb](09-transformers-and-llms/02_multi_head_attention_and_positional_encoding.ipynb)**: Multi-Head attention splitting and sinusoidal positional encodings.
- 📓 **[03_transformer_encoder_decoder_architecture.ipynb](09-transformers-and-llms/03_transformer_encoder_decoder_architecture.ipynb)**: Encoder (BERT) vs Decoder (GPT), LayerNorm, and Residual skip connections.
- 📓 **[04_tokenization_bpe_byte_pair_encoding.ipynb](09-transformers-and-llms/04_tokenization_bpe_byte_pair_encoding.ipynb)**: Subword tokenization and Byte-Pair Encoding (BPE) algorithm from scratch.
- 📓 **[05_prompt_engineering_and_rag_foundations.ipynb](09-transformers-and-llms/05_prompt_engineering_and_rag_foundations.ipynb)**: Chain-of-Thought prompting, vector database retrieval, and RAG architecture.
- 📓 **[06_rotary_positional_embeddings_rope_math.ipynb](09-transformers-and-llms/06_rotary_positional_embeddings_rope_math.ipynb)**: Rotary Positional Embeddings (RoPE), complex rotation matrices, and relative distance invariance.
- 📓 **[07_flash_decoding_and_multi_query_attention.ipynb](09-transformers-and-llms/07_flash_decoding_and_multi_query_attention.ipynb)**: Multi-Query Attention (MQA), KV cache memory bandwidth bottlenecks, and FlashDecoding parallel sequence reductions.
- 📓 **[08_grouped_query_attention_gqa.ipynb](09-transformers-and-llms/08_grouped_query_attention_gqa.ipynb)**: Grouped-Query Attention (GQA), head projection broadcasting, and LLaMA 2/3 inference optimizations.


- 🔬 **[09_alibi_attention_with_linear_biases.ipynb](09-transformers-and-llms/09_alibi_attention_with_linear_biases.ipynb)**: Attention with Linear Biases (ALiBi): Eliminating positional embeddings for extrapolation to longer contexts.
- 🔬 **[10_swiglu_activation_mechanisms.ipynb](09-transformers-and-llms/10_swiglu_activation_mechanisms.ipynb)**: Gated Linear Units: SwiGLU activation formula, gradient flow, and LLaMA FFN blocks.
- 🔬 **[11_sliding_window_attention_mistral.ipynb](09-transformers-and-llms/11_sliding_window_attention_mistral.ipynb)**: Mistral-style Local Attention: Sliding Window Attention, rolling KV cache buffers, and theoretical receptive field.
- 🔬 **[12_speculative_sampling_rejection_criteria.ipynb](09-transformers-and-llms/12_speculative_sampling_rejection_criteria.ipynb)**: Speculative Sampling: Modified rejection sampling distribution proof and theoretical speedup formulas.
---

### 📍 Week 10: Model Evaluation, Explainable AI (XAI) & MLOps
- 📓 **[01_cross_validation_stratified_kfold_time_series.ipynb](10-mlops-and-explainable-ai/01_cross_validation_stratified_kfold_time_series.ipynb)**: Stratified K-Fold and TimeSeriesSplit to prevent lookahead leakage.
- 📓 **[02_roc_curves_auc_and_precision_recall_curves.ipynb](10-mlops-and-explainable-ai/02_roc_curves_auc_and_precision_recall_curves.ipynb)**: ROC-AUC vs PR-AUC curves, threshold calibration, and business cost matrices.
- 📓 **[03_shap_and_lime_explainable_ai.ipynb](10-mlops-and-explainable-ai/03_shap_and_lime_explainable_ai.ipynb)**: Shapley values from cooperative game theory and feature attributions.
- 📓 **[04_data_drift_and_concept_drift_detection.ipynb](10-mlops-and-explainable-ai/04_data_drift_and_concept_drift_detection.ipynb)**: Covariate shift, Kolmogorov-Smirnov test, and Population Stability Index (PSI).
- 📓 **[05_model_serialization_onnx_and_fastapi_serving.ipynb](10-mlops-and-explainable-ai/05_model_serialization_onnx_and_fastapi_serving.ipynb)**: ONNX runtime export and low-latency FastAPI REST microservice schemas.
- 📓 **[06_model_calibration_platt_scaling_isotonic.ipynb](10-mlops-and-explainable-ai/06_model_calibration_platt_scaling_isotonic.ipynb)**: Expected Calibration Error (ECE), Reliability Diagrams, and Platt Scaling from scratch.
- 📓 **[07_ab_testing_bayesian_vs_frequentist.ipynb](10-mlops-and-explainable-ai/07_ab_testing_bayesian_vs_frequentist.ipynb)**: Frequentist two-proportion z-tests vs Bayesian Beta-Binomial conjugate updating, and the peeking problem.
- 📓 **[08_evidently_drift_monitoring.ipynb](10-mlops-and-explainable-ai/08_evidently_drift_monitoring.ipynb)**: Production data drift monitoring, Population Stability Index (PSI), and Wasserstein-1 Earth Mover's Distance.


- 🔬 **[09_feature_importance_permutation_vs_tree.ipynb](10-mlops-and-explainable-ai/09_feature_importance_permutation_vs_tree.ipynb)**: Model Interpretability: Permutation Feature Importance vs Mean Decrease in Impurity (MDI) bias.
- 🔬 **[10_fairness_metrics_disparate_impact_scratch.ipynb](10-mlops-and-explainable-ai/10_fairness_metrics_disparate_impact_scratch.ipynb)**: Algorithmic Fairness: Demographic Parity, Equalized Odds, and Disparate Impact ratio from scratch.
- 🔬 **[11_shadow_deployments_and_canary_routing.ipynb](10-mlops-and-explainable-ai/11_shadow_deployments_and_canary_routing.ipynb)**: Safe ML Deployments: Shadow testing, canary traffic splitting, and automated rollback triggers.
- 🔬 **[12_prometheus_grafana_model_telemetry.ipynb](10-mlops-and-explainable-ai/12_prometheus_grafana_model_telemetry.ipynb)**: Production Observability: Real-time Prometheus metrics, request latency histograms, and drift counters.
---

### 📍 Week 11: Specialized Topics & Advanced Machine Learning
- 📓 **[01_imbalanced_data_smote_and_class_weights.ipynb](11-advanced-specialized-ml/01_imbalanced_data_smote_and_class_weights.ipynb)**: SMOTE synthetic interpolation and cost-sensitive balanced class weighting.
- 📓 **[02_feature_selection_rfe_lasso_boruta.ipynb](11-advanced-specialized-ml/02_feature_selection_rfe_lasso_boruta.ipynb)**: Recursive Feature Elimination (RFE) and Boruta random shadow feature testing.
- 📓 **[03_anomaly_detection_isolation_forest.ipynb](11-advanced-specialized-ml/03_anomaly_detection_isolation_forest.ipynb)**: Isolation Forest average path length and unsupervised outlier scoring.
- 📓 **[04_recommender_systems_collaborative_filtering.ipynb](11-advanced-specialized-ml/04_recommender_systems_collaborative_filtering.ipynb)**: User-Item interaction matrix, Collaborative Filtering, and Cosine similarity.
- 📓 **[05_time_series_forecasting_arima_and_seasonality.ipynb](11-advanced-specialized-ml/05_time_series_forecasting_arima_and_seasonality.ipynb)**: Stationarity testing, differencing, and ARIMA $(p, d, q)$ parameters.
- 📓 **[06_causal_inference_propensity_score_matching.ipynb](11-advanced-specialized-ml/06_causal_inference_propensity_score_matching.ipynb)**: Rubin Potential Outcomes model, confounder isolation, and Propensity Score Matching (PSM).
- 📓 **[07_synthetic_data_ctgan_copulas.ipynb](11-advanced-specialized-ml/07_synthetic_data_ctgan_copulas.ipynb)**: CTGAN tabular data synthesis, Mode-Specific Normalization with Variational Gaussian Mixtures, and conditional WGANs.
- 📓 **[08_two_tower_recommender_embeddings.ipynb](11-advanced-specialized-ml/08_two_tower_recommender_embeddings.ipynb)**: Two-Tower user/item neural retrieval, in-batch negative contrastive loss, and sub-millisecond MIPS ANN candidate generation.


- 🔬 **[09_survival_analysis_kaplan_meier_cox.ipynb](11-advanced-specialized-ml/09_survival_analysis_kaplan_meier_cox.ipynb)**: Time-to-event modeling: Kaplan-Meier non-parametric survival curve and Cox Proportional Hazards regression.
- 🔬 **[10_conformal_prediction_valid_prediction_sets.ipynb](11-advanced-specialized-ml/10_conformal_prediction_valid_prediction_sets.ipynb)**: Conformal prediction sets: Finite-sample valid prediction sets and distribution-free coverage guarantees.
- 🔬 **[11_matrix_factorization_als_scratch.ipynb](11-advanced-specialized-ml/11_matrix_factorization_als_scratch.ipynb)**: Recommender Systems: Alternating Least Squares (ALS) with implicit feedback confidence weighting.
- 🔬 **[12_genetic_algorithms_feature_selection.ipynb](11-advanced-specialized-ml/12_genetic_algorithms_feature_selection.ipynb)**: Evolutionary Optimization: Genetic algorithms, crossover, mutation, and roulette selection for feature subsets.
---

### 📍 Week 12: Generative AI, Multimodal Architectures & Diffusion
- 📓 **[01_autoencoders_and_variational_autoencoders_vae.ipynb](12-generative-ai-and-diffusion/01_autoencoders_and_variational_autoencoders_vae.ipynb)**: Latent bottleneck compression, reparameterization trick, and KL-divergence loss from scratch.
- 📓 **[02_generative_adversarial_networks_gan_from_scratch.ipynb](12-generative-ai-and-diffusion/02_generative_adversarial_networks_gan_from_scratch.ipynb)**: Min-max zero-sum game, Generator vs. Discriminator adversarial loss, and mode collapse.
- 📓 **[03_diffusion_models_ddpm_and_denoising_math.ipynb](12-generative-ai-and-diffusion/03_diffusion_models_ddpm_and_denoising_math.ipynb)**: Forward Markov noise schedule, reverse score denoising, and U-Net epsilon prediction math.
- 📓 **[04_vision_transformers_vit_patch_projection.ipynb](12-generative-ai-and-diffusion/04_vision_transformers_vit_patch_projection.ipynb)**: Image patch flattening, linear projection, [CLS] token classification, and self-attention in CV.
- 📓 **[05_clip_and_multimodal_contrastive_learning.ipynb](12-generative-ai-and-diffusion/05_clip_and_multimodal_contrastive_learning.ipynb)**: OpenAI CLIP dual-encoders, cross-modal cosine similarity, and zero-shot image classification.
- 📓 **[06_classifier_free_guidance_cfg_diffusion.ipynb](12-generative-ai-and-diffusion/06_classifier_free_guidance_cfg_diffusion.ipynb)**: Classifier-Free Guidance (CFG) equation, conditioning dropout, and prompt alignment extrapolation.
- 📓 **[07_latent_consistency_models_lcm.ipynb](12-generative-ai-and-diffusion/07_latent_consistency_models_lcm.ipynb)**: Latent Consistency Models (LCM), PF-ODE trajectory distillation, and 1-to-4 step fast diffusion generation.
- 📓 **[08_flow_matching_rectified_flows.ipynb](12-generative-ai-and-diffusion/08_flow_matching_rectified_flows.ipynb)**: Continuous Normalizing Flows, Rectified Flow Matching with straight vector fields, and fast ODE Euler integration.


- 🔬 **[09_dpm_solver_fast_ode_diffusion.ipynb](12-generative-ai-and-diffusion/09_dpm_solver_fast_ode_diffusion.ipynb)**: Diffusion Acceleration: High-order exponential integrators (DPM-Solver) for 10-15 step sampling.
- 🔬 **[10_score_based_generative_sde_foundations.ipynb](12-generative-ai-and-diffusion/10_score_based_generative_sde_foundations.ipynb)**: Score-based Generative Modeling: Forward/reverse Stochastic Differential Equations (SDEs) and Langevin dynamics.
- 🔬 **[11_controlnet_spatial_conditioning_zero_conv.ipynb](12-generative-ai-and-diffusion/11_controlnet_spatial_conditioning_zero_conv.ipynb)**: Controllable Diffusion: ControlNet architecture, locked weights, and Zero Convolution layers.
- 🔬 **[12_ip_adapter_image_prompt_cross_attention.ipynb](12-generative-ai-and-diffusion/12_ip_adapter_image_prompt_cross_attention.ipynb)**: Multimodal Conditioning: IP-Adapter decoupled cross-attention for image prompt conditioning.
---

### 📍 Week 13: Reinforcement Learning (RL) & Human Alignment (RLHF)
- 📓 **[01_reinforcement_learning_markov_decision_process_mdp.ipynb](13-reinforcement-learning-and-rlhf/01_reinforcement_learning_markov_decision_process_mdp.ipynb)**: Markov Decision Processes (MDP), Bellman optimality equations, and state-value iteration.
- 📓 **[02_q_learning_and_temporal_difference_from_scratch.ipynb](13-reinforcement-learning-and-rlhf/02_q_learning_and_temporal_difference_from_scratch.ipynb)**: Model-free tabular Q-learning, Temporal Difference (TD) updates, and epsilon-greedy exploration.
- 📓 **[03_deep_q_networks_dqn_experience_replay.ipynb](13-reinforcement-learning-and-rlhf/03_deep_q_networks_dqn_experience_replay.ipynb)**: Deep Q-Networks, experience replay memory buffers, and frozen target networks.
- 📓 **[04_policy_gradients_reinforce_and_actor_critic.ipynb](13-reinforcement-learning-and-rlhf/04_policy_gradients_reinforce_and_actor_critic.ipynb)**: REINFORCE policy gradient theorem, log-derivative trick, and Advantage Actor-Critic (A2C).
- 📓 **[05_rlhf_reinforcement_learning_human_feedback.ipynb](13-reinforcement-learning-and-rlhf/05_rlhf_reinforcement_learning_human_feedback.ipynb)**: 3-step RLHF pipeline: SFT, Bradley-Terry reward modeling, and PPO alignment with KL penalties.
- 📓 **[06_proximal_policy_optimization_ppo_clipped_objective.ipynb](13-reinforcement-learning-and-rlhf/06_proximal_policy_optimization_ppo_clipped_objective.ipynb)**: PPO-Clip mathematical surrogate objective, probability ratio clamping, and trust region stability.
- 📓 **[07_direct_preference_optimization_vs_kto.ipynb](13-reinforcement-learning-and-rlhf/07_direct_preference_optimization_vs_kto.ipynb)**: Kahneman-Tversky Optimization (KTO), human loss aversion modeling, and alignment with unpaired binary feedback.
- 📓 **[08_multi_agent_reinforcement_learning_marl.ipynb](13-reinforcement-learning-and-rlhf/08_multi_agent_reinforcement_learning_marl.ipynb)**: Centralized Training Decentralized Execution (CTDE), QMIX monotonic value factorization, and hypernetwork mixing.


- 🔬 **[09_sac_soft_actor_critic_maximum_entropy.ipynb](13-reinforcement-learning-and-rlhf/09_sac_soft_actor_critic_maximum_entropy.ipynb)**: Continuous RL: Soft Actor-Critic (SAC), maximum entropy objective, and adaptive temperature tuning.
- 🔬 **[10_td3_twin_delayed_deep_deterministic.ipynb](13-reinforcement-learning-and-rlhf/10_td3_twin_delayed_deep_deterministic.ipynb)**: Continuous Control: Twin Delayed DDPG (TD3), clipped double Q-learning, and target policy smoothing.
- 🔬 **[11_orpo_odds_ratio_preference_optimization.ipynb](13-reinforcement-learning-and-rlhf/11_orpo_odds_ratio_preference_optimization.ipynb)**: Monolithic Alignment: Odds Ratio Preference Optimization (ORPO) without reference models or SFT warmup.
- 🔬 **[12_constitutional_ai_critique_revision.ipynb](13-reinforcement-learning-and-rlhf/12_constitutional_ai_critique_revision.ipynb)**: Self-Supervised Alignment: Anthropic Constitutional AI critique-revision loops and RLAIF.
---

### 📍 Week 14: LLM Fine-Tuning (PEFT), Quantization & AI Agents
- 📓 **[01_lora_low_rank_adaptation_from_scratch.ipynb](14-llm-finetuning-and-peft/01_lora_low_rank_adaptation_from_scratch.ipynb)**: Low-Rank Adaptation (LoRA) weight decomposition $W + B \cdot A$, rank $r$ bottleneck, and parameter savings.
- 📓 **[02_qlora_and_4bit_quantization_nf4.ipynb](14-llm-finetuning-and-peft/02_qlora_and_4bit_quantization_nf4.ipynb)**: 4-bit NormalFloat (NF4) quantization, double quantization, and paged optimizers for consumer GPUs.
- 📓 **[03_direct_preference_optimization_dpo.ipynb](14-llm-finetuning-and-peft/03_direct_preference_optimization_dpo.ipynb)**: Direct Preference Optimization (DPO) mathematical derivation, closed-form objective, and bypassing separate reward models.
- 📓 **[04_speculative_decoding_and_kv_cache.ipynb](14-llm-finetuning-and-peft/04_speculative_decoding_and_kv_cache.ipynb)**: KV-Cache memory mechanics, memory bandwidth bottlenecks, and Speculative Decoding draft verification.
- 📓 **[05_ai_agents_function_calling_and_tool_use.ipynb](14-llm-finetuning-and-peft/05_ai_agents_function_calling_and_tool_use.ipynb)**: ReAct (Reason + Act) loop, JSON tool schemas, multi-step tool execution, and error handling.
- 📓 **[06_unsloth_and_flash_attention_mechanics.ipynb](14-llm-finetuning-and-peft/06_unsloth_and_flash_attention_mechanics.ipynb)**: FlashAttention IO-awareness, GPU SRAM memory tiling, and online streaming softmax from scratch.
- 📓 **[07_bitnet_1bit_llm_quantization.ipynb](14-llm-finetuning-and-peft/07_bitnet_1bit_llm_quantization.ipynb)**: BitNet b1.58 ternary weight quantization $\{-1, 0, 1\}$, BitLinear layer, and multiplication-free matrix multiplication.
- 📓 **[08_prefix_tuning_and_prompt_tuning.ipynb](14-llm-finetuning-and-peft/08_prefix_tuning_and_prompt_tuning.ipynb)**: Prefix Tuning vs Prompt Tuning, virtual Key/Value attention prefixes, and MLP parameterization.


- 🔬 **[09_dora_weight_decomposed_low_rank.ipynb](14-llm-finetuning-and-peft/09_dora_weight_decomposed_low_rank.ipynb)**: Parameter-Efficient Fine-Tuning: Weight-Decomposed Low-Rank Adaptation (DoRA) magnitude and direction decoupling.
- 🔬 **[10_fp8_e4m3_e5m2_mixed_precision_training.ipynb](14-llm-finetuning-and-peft/10_fp8_e4m3_e5m2_mixed_precision_training.ipynb)**: Hardware Acceleration: FP8 formats (E4M3 vs E5M2), dynamic scaling factors, and Hopper Tensor Cores.
- 🔬 **[11_gguf_llama_cpp_quantization_formats.ipynb](14-llm-finetuning-and-peft/11_gguf_llama_cpp_quantization_formats.ipynb)**: Edge Inference: GGUF binary format, block quantization (Q4_K, Q8_0), and SIMD integer dot products.
- 🔬 **[12_mcp_model_context_protocol_tool_calling.ipynb](14-llm-finetuning-and-peft/12_mcp_model_context_protocol_tool_calling.ipynb)**: AI Agent Architecture: Model Context Protocol (MCP) JSON-RPC 2.0 schemas, dynamic tool discovery, and SSE transport.
---

### 📍 Week 15: Graph Neural Networks & Geometric Deep Learning
- 📓 **[01_graph_fundamentals_adjacency_laplacian_scratch.ipynb](15-graph-neural-networks-and-geometric-dl/01_graph_fundamentals_adjacency_laplacian_scratch.ipynb)**: Adjacency matrix, degree matrix, unnormalized and symmetric normalized Laplacian from scratch.
- 📓 **[02_graph_convolutional_networks_gcn_scratch.ipynb](15-graph-neural-networks-and-geometric-dl/02_graph_convolutional_networks_gcn_scratch.ipynb)**: Kipf & Welling first-order spectral propagation rule and semi-supervised node classification.
- 📓 **[03_graph_attention_networks_gat.ipynb](15-graph-neural-networks-and-geometric-dl/03_graph_attention_networks_gat.ipynb)**: Graph Attention Networks, masked dynamic neighbor attention, and multi-head projection.
- 📓 **[04_graphsage_neighborhood_sampling.ipynb](15-graph-neural-networks-and-geometric-dl/04_graphsage_neighborhood_sampling.ipynb)**: Inductive representation learning and fixed-size neighborhood mini-batch sampling.
- 📓 **[05_link_prediction_and_molecular_graphs.ipynb](15-graph-neural-networks-and-geometric-dl/05_link_prediction_and_molecular_graphs.ipynb)**: TransE knowledge graph embeddings, negative edge sampling, and molecular property ranking.
- 📓 **[06_graph_pooling_diffpool_and_graph_classification.ipynb](15-graph-neural-networks-and-geometric-dl/06_graph_pooling_diffpool_and_graph_classification.ipynb)**: Differentiable Graph Pooling (DiffPool), soft cluster assignment matrices, and whole-graph classification.
- 📓 **[07_heterogeneous_graph_neural_networks.ipynb](15-graph-neural-networks-and-geometric-dl/07_heterogeneous_graph_neural_networks.ipynb)**: Relational Graph Convolutional Networks (RGCN), basis decomposition, and heterogeneous metapath message passing.
- 📓 **[08_temporal_graph_networks_tgn.ipynb](15-graph-neural-networks-and-geometric-dl/08_temporal_graph_networks_tgn.ipynb)**: Temporal Graph Networks (TGN) for continuous-time dynamic graphs, node memory banks, and Bochner Fourier time encoding.


- 🔬 **[09_weisfeiler_lehman_isomorphism_gnn_expressive.ipynb](15-graph-neural-networks-and-geometric-dl/09_weisfeiler_lehman_isomorphism_gnn_expressive.ipynb)**: Geometric Expressiveness: 1-Weisfeiler-Lehman (1-WL) graph isomorphism test and Graph Isomorphism Networks (GIN).
- 🔬 **[10_edge_convolution_point_clouds_dgcnn.ipynb](15-graph-neural-networks-and-geometric-dl/10_edge_convolution_point_clouds_dgcnn.ipynb)**: 3D Deep Learning: Dynamic Graph CNN (DGCNN) and EdgeConv operations in dynamic feature space.
- 🔬 **[11_oversquashing_and_oversmoothing_in_gnns.ipynb](15-graph-neural-networks-and-geometric-dl/11_oversquashing_and_oversmoothing_in_gnns.ipynb)**: Graph Bottlenecks: Dirichlet energy decay, Ricci curvature bottlenecks, and DropEdge mitigation.
- 🔬 **[12_se3_equivariant_graph_neural_networks.ipynb](15-graph-neural-networks-and-geometric-dl/12_se3_equivariant_graph_neural_networks.ipynb)**: Equivariant Architectures: SE(3) and SO(3) equivariant message passing for molecular physics.
---

### 📍 Week 16: Advanced MLOps, Distributed Training & Model Optimization
- 📓 **[01_data_parallelism_ddp_and_gradient_allreduce.ipynb](16-distributed-training-and-model-optimization/01_data_parallelism_ddp_and_gradient_allreduce.ipynb)**: Distributed Data Parallel (DDP), Ring-AllReduce ring topology, and multi-GPU scaling mechanics.
- 📓 **[02_tensor_parallelism_and_pipeline_parallelism.ipynb](16-distributed-training-and-model-optimization/02_tensor_parallelism_and_pipeline_parallelism.ipynb)**: Megatron-LM 1D tensor splitting (Column & Row parallel) and pipeline bubble scheduling.
- 📓 **[03_zero_redundancy_optimizer_deepspeed.ipynb](16-distributed-training-and-model-optimization/03_zero_redundancy_optimizer_deepspeed.ipynb)**: ZeRO Stage 1, 2, 3 memory breakdown and FSDP sharding calculations.
- 📓 **[04_model_pruning_and_knowledge_distillation.ipynb](16-distributed-training-and-model-optimization/04_model_pruning_and_knowledge_distillation.ipynb)**: Hinton knowledge distillation loss with temperature and weight magnitude pruning.
- 📓 **[05_feature_stores_feast_and_realtime_inference.ipynb](16-distributed-training-and-model-optimization/05_feature_stores_feast_and_realtime_inference.ipynb)**: Point-in-time correctness as-of joins and dual-store architecture preventing data leakage.
- 📓 **[06_activation_checkpointing_and_cpu_offload.ipynb](16-distributed-training-and-model-optimization/06_activation_checkpointing_and_cpu_offload.ipynb)**: Activation Checkpointing, gradient recomputation, and $O(\sqrt{L})$ memory scaling.
- 📓 **[07_pipeline_parallel_interleaved_1f1b.ipynb](16-distributed-training-and-model-optimization/07_pipeline_parallel_interleaved_1f1b.ipynb)**: Pipeline Parallelism 1F1B schedule, peak activation memory reduction, and interleaved virtual stages.
- 📓 **[08_fsdp_hybrid_sharding_strategies.ipynb](16-distributed-training-and-model-optimization/08_fsdp_hybrid_sharding_strategies.ipynb)**: Fully Sharded Data Parallel (FSDP), Hybrid Sharding (HSDP), All-Gather and Reduce-Scatter collective memory dynamics.


- 🔬 **[09_megatron_sequence_parallelism.ipynb](16-distributed-training-and-model-optimization/09_megatron_sequence_parallelism.ipynb)**: Megatron-LM Sequence Parallelism, LayerNorm activation sharding, and Ring Attention.
- 🔬 **[10_expert_parallelism_moe_distributed.ipynb](16-distributed-training-and-model-optimization/10_expert_parallelism_moe_distributed.ipynb)**: Distributed Mixture of Experts (MoE), Top-2 router gating, All-to-All dispatch, and balance loss.
- 🔬 **[11_lora_distributed_fsdp_integration.ipynb](16-distributed-training-and-model-optimization/11_lora_distributed_fsdp_integration.ipynb)**: Large-Scale PEFT: Fully Sharded Data Parallel (FSDP) integration with LoRA adapter modules.
- 🔬 **[12_kv_cache_offloading_and_pinning.ipynb](16-distributed-training-and-model-optimization/12_kv_cache_offloading_and_pinning.ipynb)**: High-Throughput LLM Serving: PagedAttention block tables and CUDA pinned memory host offloading.
---

### 📍 Week 17: Production Retrieval-Augmented Generation (Advanced RAG) & Vector Search
- 📓 **[01_vector_indexing_hnsw_and_ivf_pq.ipynb](17-advanced-rag-and-vector-search/01_vector_indexing_hnsw_and_ivf_pq.ipynb)**: Approximate Nearest Neighbor search with HNSW and IVF-PQ quantization from scratch.
- 📓 **[02_hybrid_search_bm25_dense_reciprocal_rank_fusion.ipynb](17-advanced-rag-and-vector-search/02_hybrid_search_bm25_dense_reciprocal_rank_fusion.ipynb)**: BM25 lexical keyword search, dense cosine embeddings, and Reciprocal Rank Fusion (RRF).
- 📓 **[03_reranking_cross_encoders_and_colbert.ipynb](17-advanced-rag-and-vector-search/03_reranking_cross_encoders_and_colbert.ipynb)**: Bi-Encoder vs Cross-Encoder reranking and ColBERT late interaction MaxSim.
- 📓 **[04_chunking_strategies_and_contextual_retrieval.ipynb](17-advanced-rag-and-vector-search/04_chunking_strategies_and_contextual_retrieval.ipynb)**: Semantic boundary splitting and hierarchical parent-child indexing.
- 📓 **[05_rag_triad_evaluation_ragas_and_truelens.ipynb](17-advanced-rag-and-vector-search/05_rag_triad_evaluation_ragas_and_truelens.ipynb)**: Automated context relevance, faithfulness, and answer groundedness scoring.
- 📓 **[06_graph_rag_knowledge_graphs_with_llm.ipynb](17-advanced-rag-and-vector-search/06_graph_rag_knowledge_graphs_with_llm.ipynb)**: GraphRAG entity-relationship extraction, Leiden community clustering, and hierarchical global summaries.
- 📓 **[07_raptor_recursive_abstractive_processing.ipynb](17-advanced-rag-and-vector-search/07_raptor_recursive_abstractive_processing.ipynb)**: RAPTOR recursive abstractive summarization trees, hierarchical clustering, and multi-level thematic retrieval.
- 📓 **[08_self_rag_adaptive_retrieval.ipynb](17-advanced-rag-and-vector-search/08_self_rag_adaptive_retrieval.ipynb)**: Self-RAG adaptive retrieval gating (`[Retrieve]`), groundedness verification (`[IsSup]`), and reflection tokens.


- 🔬 **[09_parent_document_retrieval_split_indexing.ipynb](17-advanced-rag-and-vector-search/09_parent_document_retrieval_split_indexing.ipynb)**: Advanced RAG: Hierarchical chunking, child vector indexing, and parent document resolution.
- 🔬 **[10_hypothetical_document_embeddings_hyde.ipynb](17-advanced-rag-and-vector-search/10_hypothetical_document_embeddings_hyde.ipynb)**: Zero-Shot Retrieval: Hypothetical Document Embeddings (HyDE) pseudo-passage generation.
- 🔬 **[11_contextual_compression_and_embedding_filtering.ipynb](17-advanced-rag-and-vector-search/11_contextual_compression_and_embedding_filtering.ipynb)**: RAG Noise Reduction: Contextual compression, cross-encoder re-ranking, and sentence relevance filtering.
- 🔬 **[12_agentic_rag_query_routing_and_decomposition.ipynb](17-advanced-rag-and-vector-search/12_agentic_rag_query_routing_and_decomposition.ipynb)**: Multi-Hop RAG: Sub-query decomposition, dynamic routing across SQL/Vector stores, and synthesis.
---

### 📍 Week 18: Modern Autonomous AI Systems & Multi-Agent Architectures
- 📓 **[01_planning_and_reasoning_tree_of_thoughts.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/01_planning_and_reasoning_tree_of_thoughts.ipynb)**: Tree of Thoughts heuristic search, state-space exploration, and BFS state pruning.
- 📓 **[02_multi_agent_collaboration_and_debate.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/02_multi_agent_collaboration_and_debate.ipynb)**: Society of Mind multi-agent debate, critique-refinement loops, and consensus scoring.
- 📓 **[03_memory_systems_episodic_semantic_working_memory.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/03_memory_systems_episodic_semantic_working_memory.ipynb)**: Short-term working memory, episodic vector retrieval, and exponential recency decay.
- 📓 **[04_code_generation_execution_and_sandboxing.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/04_code_generation_execution_and_sandboxing.ipynb)**: AST validation, isolated sandboxed execution, and automated error reflection.
- 📓 **[05_structured_outputs_json_grammar_constrained_sampling.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/05_structured_outputs_json_grammar_constrained_sampling.ipynb)**: Grammar-constrained decoding, pushdown automata, and logit masking for 100% valid JSON.
- 📓 **[06_ai_safety_guardrails_prompt_injection_defense.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/06_ai_safety_guardrails_prompt_injection_defense.ipynb)**: Defenses against direct and indirect prompt injection, canary token verification, and input-output boundaries.
- 📓 **[07_agent_benchmarking_and_swe_bench_evaluation.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/07_agent_benchmarking_and_swe_bench_evaluation.ipynb)**: Autonomous software agent evaluation (SWE-bench), unified git diff patches, and sandbox regression testing.
- 📓 **[08_langgraph_cyclic_agent_state_machines.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/08_langgraph_cyclic_agent_state_machines.ipynb)**: Cyclic agent state machines, state reducer functions, conditional edge routing, and human-in-the-loop checkpoints.
- 📓 **[09_reflexion_reinforcement_learning_verbal.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/09_reflexion_reinforcement_learning_verbal.ipynb)**: Reflexion verbal reinforcement learning, evaluator failure diagnosis, and episodic self-reflection memory loops.


- 🔬 **[10_dynamic_scratchpad_and_chain_of_code.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/10_dynamic_scratchpad_and_chain_of_code.ipynb)**: Program-Aided Language Models (PAL), Chain of Code (CoC), and safe AST sandboxed execution.
- 🔬 **[11_human_in_the_loop_approval_workflows.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/11_human_in_the_loop_approval_workflows.ipynb)**: Agent Governance: Human-In-The-Loop (HITL) approval gates, durable checkpoints, and rollback logs.
- 🔬 **[12_agent_eval_llm_as_a_judge_mechanics.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/12_agent_eval_llm_as_a_judge_mechanics.ipynb)**: Automated LLM Evaluation: G-Eval calibration, position/verbosity bias mitigation, and Cohen's Kappa.
- 🔬 **[13_swarm_orchestration_hierarchical_agents.ipynb](18-autonomous-ai-agents-and-multi-agent-systems/13_swarm_orchestration_hierarchical_agents.ipynb)**: Multi-Agent Swarms: Hierarchical orchestrator-worker architectures and decoupled message bus coordination.
---

### 📍 Week 19: Time-Series Deep Learning, State Space Models (SSMs) & Mamba
- 📓 **[01_time_series_decomposition_fourier_wavelets.ipynb](19-time-series-ssm-and-mamba/01_time_series_decomposition_fourier_wavelets.ipynb)**: Fourier transform, spectral time-series decomposition, and frequency-domain noise filtering from scratch.
- 📓 **[02_temporal_convolutional_networks_tcn.ipynb](19-time-series-ssm-and-mamba/02_temporal_convolutional_networks_tcn.ipynb)**: Temporal Convolutional Networks (TCN), causal dilated convolutions, and exponential receptive fields.
- 📓 **[03_neural_prophet_and_nbeats_forecasting.ipynb](19-time-series-ssm-and-mamba/03_neural_prophet_and_nbeats_forecasting.ipynb)**: Neural Basis Expansion (N-BEATS), interpretable trend/seasonality blocks, and backcast residual loops.
- 📓 **[04_state_space_models_s4_foundations.ipynb](19-time-series-ssm-and-mamba/04_state_space_models_s4_foundations.ipynb)**: Structured State Space Models (S4), continuous-time ODE discretization, and HiPPO memory initialization.
- 📓 **[05_mamba_selective_state_spaces_scratch.ipynb](19-time-series-ssm-and-mamba/05_mamba_selective_state_spaces_scratch.ipynb)**: Mamba Selective State Spaces, input-dependent parameters ($B_t, C_t, \Delta_t$), and linear-time inference.
- 📓 **[06_time_series_anomaly_detection_vae_flow.ipynb](19-time-series-ssm-and-mamba/06_time_series_anomaly_detection_vae_flow.ipynb)**: Multivariate time-series reconstruction error, PCA subspace projection, and rolling Z-score anomaly thresholds.
- 📓 **[07_patchtst_patching_channel_independence.ipynb](19-time-series-ssm-and-mamba/07_patchtst_patching_channel_independence.ipynb)**: PatchTST subseries patching, channel-independent Transformer backbones, and $O(S^2)$ attention memory reduction.
- 📓 **[08_crossformer_cross_dimension_attention.ipynb](19-time-series-ssm-and-mamba/08_crossformer_cross_dimension_attention.ipynb)**: Crossformer Two-Stage Attention (TSA) alternating Cross-Time and Cross-Dimension self-attention passes.


- 🔬 **[09_hippo_high_order_polynomial_projection.ipynb](19-time-series-ssm-and-mamba/09_hippo_high_order_polynomial_projection.ipynb)**: State Space Foundations: HiPPO orthogonal Legendre polynomial projection and continuous memory dynamics.
- 🔬 **[10_conformal_time_series_interval_forecasting.ipynb](19-time-series-ssm-and-mamba/10_conformal_time_series_interval_forecasting.ipynb)**: Non-Stationary Uncertainty: Adaptive Conformal Inference (ACI) and finite-sample prediction intervals.
- 🔬 **[11_transformer_vs_linear_dlinear_forecasting.ipynb](19-time-series-ssm-and-mamba/11_transformer_vs_linear_dlinear_forecasting.ipynb)**: Are Transformers Effective for Time Series? DLinear trend-seasonality decomposition vs temporal attention.
- 🔬 **[12_bidirectional_mamba_vision_and_dna.ipynb](19-time-series-ssm-and-mamba/12_bidirectional_mamba_vision_and_dna.ipynb)**: Non-Causal Sequence Modeling: Bidirectional Selective SSMs (Vim / BiMamba) for 2D images and genomics.
---

### 📍 Week 20: Advanced Computer Vision, 3D Vision & NeRFs
- 📓 **[01_object_detection_yolo_and_anchor_boxes.ipynb](20-computer-vision-and-nerfs/01_object_detection_yolo_and_anchor_boxes.ipynb)**: YOLO object detection mechanics, Intersection over Union (IoU), and Non-Maximum Suppression (NMS) from scratch.
- 📓 **[02_semantic_and_instance_segmentation_unet_maskrcnn.ipynb](20-computer-vision-and-nerfs/02_semantic_and_instance_segmentation_unet_maskrcnn.ipynb)**: U-Net architecture, skip connections, and Soft Dice Loss for class-imbalanced image segmentation.
- 📓 **[03_neural_radiance_fields_nerf_scratch.ipynb](20-computer-vision-and-nerfs/03_neural_radiance_fields_nerf_scratch.ipynb)**: Neural Radiance Fields (NeRF), continuous volumetric rendering equation, and ray marching from scratch.
- 📓 **[04_3d_gaussian_splatting_foundations.ipynb](20-computer-vision-and-nerfs/04_3d_gaussian_splatting_foundations.ipynb)**: 3D Gaussian Splatting, 3D to 2D covariance projection (EWA Splatting), and real-time rasterization.
- 📓 **[05_optical_flow_and_motion_estimation.ipynb](20-computer-vision-and-nerfs/05_optical_flow_and_motion_estimation.ipynb)**: Lucas-Kanade optical flow, brightness constancy constraint, and motion vector field estimation.
- 📓 **[06_depth_estimation_and_stereo_vision.ipynb](20-computer-vision-and-nerfs/06_depth_estimation_and_stereo_vision.ipynb)**: Stereo vision triangulation ($Z = f B / d$), epipolar geometry, and block-matching disparity estimation.
- 📓 **[07_segment_anything_sam_prompt_encoder.ipynb](20-computer-vision-and-nerfs/07_segment_anything_sam_prompt_encoder.ipynb)**: Segment Anything (SAM) architecture, Fourier coordinate prompt encoders, and two-way cross-attention mask decoders.
- 📓 **[08_depth_anything_monocular_depth.ipynb](20-computer-vision-and-nerfs/08_depth_anything_monocular_depth.ipynb)**: Depth Anything foundation models, Scale-and-Shift Invariant (SSI) depth loss, and large-scale unlabeled distillation.


- 🔬 **[09_feature_pyramid_networks_fpn_scratch.ipynb](20-computer-vision-and-nerfs/09_feature_pyramid_networks_fpn_scratch.ipynb)**: Multi-Scale Object Detection: Feature Pyramid Networks (FPN) top-down pathway and lateral connections.
- 🔬 **[10_panoptic_segmentation_mechanics.ipynb](20-computer-vision-and-nerfs/10_panoptic_segmentation_mechanics.ipynb)**: Unified Vision: Panoptic Quality (PQ) metric, Hungarian matching, and Stuff vs Thing unification.
- 🔬 **[11_nerf_positional_encoding_high_frequencies.ipynb](20-computer-vision-and-nerfs/11_nerf_positional_encoding_high_frequencies.ipynb)**: 3D Representations: Neural Radiance Fields (NeRF), volumetric rendering, and Fourier positional encoding.
- 🔬 **[12_dino_self_supervised_vision_transformers.ipynb](20-computer-vision-and-nerfs/12_dino_self_supervised_vision_transformers.ipynb)**: Emergent Vision Transformers: DINO self-distillation, centering, sharpening, and unsupervised segmentation.
---

### 📍 Week 21: High-Performance ML Inference, Compilers & Serving
- 📓 **[01_tensorrt_cuda_graphs_and_kernel_fusion.ipynb](21-high-performance-inference-and-compilers/01_tensorrt_cuda_graphs_and_kernel_fusion.ipynb)**: TensorRT operator fusion, CPU launch overhead elimination via CUDA Graphs, and latency profiling.
- 📓 **[02_vllm_paged_attention_from_scratch.ipynb](21-high-performance-inference-and-compilers/02_vllm_paged_attention_from_scratch.ipynb)**: vLLM PagedAttention, OS-style virtual memory paging for KV-cache, and fragmentation elimination.
- 📓 **[03_quantization_mechanics_gptq_awq_smoothquant.ipynb](21-high-performance-inference-and-compilers/03_quantization_mechanics_gptq_awq_smoothquant.ipynb)**: Activation-aware Weight Quantization (AWQ), activation channel outliers, and SmoothQuant transformation.
- 📓 **[04_continuous_batching_and_cellular_inference.ipynb](21-high-performance-inference-and-compilers/04_continuous_batching_and_cellular_inference.ipynb)**: Continuous (iteration-level) batching, dynamic request insertion, and zero idle GPU execution.
- 📓 **[05_triton_gpu_programming_fundamentals.ipynb](21-high-performance-inference-and-compilers/05_triton_gpu_programming_fundamentals.ipynb)**: OpenAI Triton block-level GPU programming model, SRAM memory tiling, and vector kernel execution.
- 📓 **[06_model_speculative_decoding_and_medusa.ipynb](21-high-performance-inference-and-compilers/06_model_speculative_decoding_and_medusa.ipynb)**: Medusa multi-head speculative decoding, tree-based attention verification, and multi-token acceleration.
- 📓 **[07_vllm_chunked_prefill_scheduling.ipynb](21-high-performance-inference-and-compilers/07_vllm_chunked_prefill_scheduling.ipynb)**: vLLM Chunked Prefill, mixed prefill/decode batching, and eliminating inter-token latency spikes.
- 📓 **[08_cuda_shared_memory_tiling_matmul.ipynb](21-high-performance-inference-and-compilers/08_cuda_shared_memory_tiling_matmul.ipynb)**: CUDA shared memory 2D block tiling, barrier synchronization, DRAM access reduction, and arithmetic intensity scaling.


- 🔬 **[09_speculative_decoding_tree_attention.ipynb](21-high-performance-inference-and-compilers/09_speculative_decoding_tree_attention.ipynb)**: Speculative Decoding: Tree Attention candidate branching and 2D causal ancestor masks in Medusa/Eagle.
- 🔬 **[10_prefix_caching_and_radix_tree_vllm.ipynb](21-high-performance-inference-and-compilers/10_prefix_caching_and_radix_tree_vllm.ipynb)**: Prefill Optimization: Radix Tree KV Cache prefix indexing and LRU eviction in vLLM/SGLang.
- 🔬 **[11_cuda_graph_replay_and_variable_shapes.ipynb](21-high-performance-inference-and-compilers/11_cuda_graph_replay_and_variable_shapes.ipynb)**: Latency Optimization: CUDA Graph execution replay, launch overhead elimination, and padding buckets.
- 🔬 **[12_torch_compile_inductor_code_generation.ipynb](21-high-performance-inference-and-compilers/12_torch_compile_inductor_code_generation.ipynb)**: PyTorch 2.0 Compilers: TorchInductor loop fusion, Triton kernel generation, and memory bus traffic reduction.
---

### 📍 Week 22: Multimodal Foundation Models & Vision-Language Architectures
- 📓 **[01_llava_visual_instruction_tuning.ipynb](22-multimodal-foundation-models/01_llava_visual_instruction_tuning.ipynb)**: LLaVA visual instruction tuning, projection projector bridging vision and language, and token alignment.
- 📓 **[02_cross_attention_in_diffusion_and_multimodal.ipynb](22-multimodal-foundation-models/02_cross_attention_in_diffusion_and_multimodal.ipynb)**: Cross-attention mechanics in text-to-image diffusion, latent conditioning, and prompt guidance.
- 📓 **[03_audio_transformers_whisper_scratch.ipynb](22-multimodal-foundation-models/03_audio_transformers_whisper_scratch.ipynb)**: Whisper speech transcription architecture, Log-mel spectrogram extraction, and audio transformer encoders.
- 📓 **[04_speech_language_models_speech_tokens.ipynb](22-multimodal-foundation-models/04_speech_language_models_speech_tokens.ipynb)**: Discrete speech tokens, Residual Vector Quantization (RVQ), and native audio language modeling.
- 📓 **[05_video_diffusion_and_temporal_attention.ipynb](22-multimodal-foundation-models/05_video_diffusion_and_temporal_attention.ipynb)**: Video diffusion models, factorized spatio-temporal attention, and cross-frame physical consistency.
- 📓 **[06_multimodal_rag_colpali_pdf_indexing.ipynb](22-multimodal-foundation-models/06_multimodal_rag_colpali_pdf_indexing.ipynb)**: ColPali OCR-free multimodal document retrieval, visual page screenshot embeddings, and late interaction MaxSim.

---

### 📍 Week 23: Next-Gen AI Reasoning, MCTS & Test-Time Compute
- 📓 **[01_monte_carlo_tree_search_mcts_scratch.ipynb](23-nextgen-reasoning-and-test-time-compute/01_monte_carlo_tree_search_mcts_scratch.ipynb)**: Monte Carlo Tree Search (MCTS), UCB1 exploration vs exploitation, and AlphaGo-style tree rollouts from scratch.
- 📓 **[02_process_supervision_prm_vs_outcome_supervision.ipynb](23-nextgen-reasoning-and-test-time-compute/02_process_supervision_prm_vs_outcome_supervision.ipynb)**: Process Reward Models (PRMs) scoring intermediate reasoning steps vs Outcome Reward Models (ORMs).
- 📓 **[03_self_consistency_and_majority_voting.ipynb](23-nextgen-reasoning-and-test-time-compute/03_self_consistency_and_majority_voting.ipynb)**: Self-Consistency with majority voting across diverse sampled chains of thought and entropy confidence.
- 📓 **[04_test_time_compute_scaling_laws.ipynb](23-nextgen-reasoning-and-test-time-compute/04_test_time_compute_scaling_laws.ipynb)**: Test-Time Compute scaling laws, internal thinking tokens, and Pareto trade-off frontiers (OpenAI o1 / DeepSeek-R1).
- 📓 **[05_self_correction_and_backtracking_agents.ipynb](23-nextgen-reasoning-and-test-time-compute/05_self_correction_and_backtracking_agents.ipynb)**: Automated reasoning reflection, state backtracking, and hypothesis pruning from scratch.
- 📓 **[06_synthetic_reasoning_data_generation_rejection_sampling.ipynb](23-nextgen-reasoning-and-test-time-compute/06_synthetic_reasoning_data_generation_rejection_sampling.ipynb)**: Synthetic reasoning data generation, deterministic verifier rejection sampling, and golden SFT curation.

---

## 🎯 Daily Cadence & Code Quality
- **Pure Jupyter Notebook Format (`.ipynb`)**: Directly viewable in your browser on GitHub.
- **Deep Explanations**: Theory, math derivations, line-by-line commentary, and interview Q&As.
- **Sequential Commits**: Each notebook is committed and pushed individually with clean conventional commit messages.

---

*Authored by Muhammad Zabiullah ([@mzb000](https://github.com/mzb000))*
