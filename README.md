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

### 📍 Week 7: Deep Learning Foundations & Neural Networks
- 📓 **[01_single_layer_perceptron_scratch.ipynb](07-deep-learning-foundations/01_single_layer_perceptron_scratch.ipynb)**: Artificial neuron, threshold activation, boolean logic gates, and the XOR problem.
- 📓 **[02_activation_functions_relu_sigmoid_tanh_gelu.ipynb](07-deep-learning-foundations/02_activation_functions_relu_sigmoid_tanh_gelu.ipynb)**: Vanishing gradients, dying ReLU, and modern GELU activations.
- 📓 **[03_feedforward_neural_network_numpy_scratch.ipynb](07-deep-learning-foundations/03_feedforward_neural_network_numpy_scratch.ipynb)**: Multi-Layer Perceptron (MLP) forward pass, matrix shapes, and cross-entropy in pure NumPy.
- 📓 **[04_backpropagation_calculus_chain_rule.ipynb](07-deep-learning-foundations/04_backpropagation_calculus_chain_rule.ipynb)**: Calculus chain rule, partial derivatives, and complete XOR training loop.
- 📓 **[05_pytorch_tensor_fundamentals_and_autograd.ipynb](07-deep-learning-foundations/05_pytorch_tensor_fundamentals_and_autograd.ipynb)**: PyTorch tensors, GPU acceleration, automatic differentiation, and `nn.Module`.
- 📓 **[06_optimizers_sgd_momentum_rmsprop_adam.ipynb](07-deep-learning-foundations/06_optimizers_sgd_momentum_rmsprop_adam.ipynb)**: SGD with momentum, RMSProp adaptive rates, and Adam optimizer implementation.
- 📓 **[07_regularization_dropout_batchnorm_weight_decay.ipynb](07-deep-learning-foundations/07_regularization_dropout_batchnorm_weight_decay.ipynb)**: Inverted dropout from scratch, batch normalization, and weight decay.
- 📓 **[08_convolutional_neural_networks_cnn_basics.ipynb](07-deep-learning-foundations/08_convolutional_neural_networks_cnn_basics.ipynb)**: 2D convolution from scratch, Sobel edge filter kernels, stride, padding, and pooling.

---

### 📍 Week 8: Natural Language Processing (NLP) & Text Embeddings
- 📓 **[01_text_preprocessing_tokenization_lemmatization.ipynb](08-nlp-and-text-embeddings/01_text_preprocessing_tokenization_lemmatization.ipynb)**: Regex cleaning, tokenization, stop word filtering, and stemming vs lemmatization.
- 📓 **[02_bag_of_words_and_tfidf_from_scratch.ipynb](08-nlp-and-text-embeddings/02_bag_of_words_and_tfidf_from_scratch.ipynb)**: Term frequency, inverse document frequency, and L2 normalization from scratch.
- 📓 **[03_word_embeddings_word2vec_cosine_similarity.ipynb](08-nlp-and-text-embeddings/03_word_embeddings_word2vec_cosine_similarity.ipynb)**: Dense semantic vectors, Word2Vec skip-gram intuition, and vector arithmetic (King - Man + Woman = Queen).
- 📓 **[04_sentiment_analysis_naive_bayes_nlp.ipynb](08-nlp-and-text-embeddings/04_sentiment_analysis_naive_bayes_nlp.ipynb)**: Bayes theorem, Laplace smoothing, and multinomial spam classification.
- 📓 **[05_recurrent_neural_networks_rnn_and_lstm.ipynb](08-nlp-and-text-embeddings/05_recurrent_neural_networks_rnn_and_lstm.ipynb)**: Sequence memory, hidden state propagation, and LSTM gating mechanics.

---

### 📍 Week 9: Transformers, Attention & Large Language Models (LLMs)
- 📓 **[01_self_attention_mechanism_from_scratch.ipynb](09-transformers-and-llms/01_self_attention_mechanism_from_scratch.ipynb)**: Queries ($Q$), Keys ($K$), Values ($V$), and Scaled Dot-Product Attention in NumPy.
- 📓 **[02_multi_head_attention_and_positional_encoding.ipynb](09-transformers-and-llms/02_multi_head_attention_and_positional_encoding.ipynb)**: Multi-Head attention splitting and sinusoidal positional encodings.
- 📓 **[03_transformer_encoder_decoder_architecture.ipynb](09-transformers-and-llms/03_transformer_encoder_decoder_architecture.ipynb)**: Encoder (BERT) vs Decoder (GPT), LayerNorm, and Residual skip connections.
- 📓 **[04_tokenization_bpe_byte_pair_encoding.ipynb](09-transformers-and-llms/04_tokenization_bpe_byte_pair_encoding.ipynb)**: Subword tokenization and Byte-Pair Encoding (BPE) algorithm from scratch.
- 📓 **[05_prompt_engineering_and_rag_foundations.ipynb](09-transformers-and-llms/05_prompt_engineering_and_rag_foundations.ipynb)**: Chain-of-Thought prompting, vector database retrieval, and RAG architecture.

---

### 📍 Week 10: Model Evaluation, Explainable AI (XAI) & MLOps
- 📓 **[01_cross_validation_stratified_kfold_time_series.ipynb](10-mlops-and-explainable-ai/01_cross_validation_stratified_kfold_time_series.ipynb)**: Stratified K-Fold and TimeSeriesSplit to prevent lookahead leakage.
- 📓 **[02_roc_curves_auc_and_precision_recall_curves.ipynb](10-mlops-and-explainable-ai/02_roc_curves_auc_and_precision_recall_curves.ipynb)**: ROC-AUC vs PR-AUC curves, threshold calibration, and business cost matrices.
- 📓 **[03_shap_and_lime_explainable_ai.ipynb](10-mlops-and-explainable-ai/03_shap_and_lime_explainable_ai.ipynb)**: Shapley values from cooperative game theory and feature attributions.
- 📓 **[04_data_drift_and_concept_drift_detection.ipynb](10-mlops-and-explainable-ai/04_data_drift_and_concept_drift_detection.ipynb)**: Covariate shift, Kolmogorov-Smirnov test, and Population Stability Index (PSI).
- 📓 **[05_model_serialization_onnx_and_fastapi_serving.ipynb](10-mlops-and-explainable-ai/05_model_serialization_onnx_and_fastapi_serving.ipynb)**: ONNX runtime export and low-latency FastAPI REST microservice schemas.

---

### 📍 Week 11: Specialized Topics & Advanced Machine Learning
- 📓 **[01_imbalanced_data_smote_and_class_weights.ipynb](11-advanced-specialized-ml/01_imbalanced_data_smote_and_class_weights.ipynb)**: SMOTE synthetic interpolation and cost-sensitive balanced class weighting.
- 📓 **[02_feature_selection_rfe_lasso_boruta.ipynb](11-advanced-specialized-ml/02_feature_selection_rfe_lasso_boruta.ipynb)**: Recursive Feature Elimination (RFE) and Boruta random shadow feature testing.
- 📓 **[03_anomaly_detection_isolation_forest.ipynb](11-advanced-specialized-ml/03_anomaly_detection_isolation_forest.ipynb)**: Isolation Forest average path length and unsupervised outlier scoring.
- 📓 **[04_recommender_systems_collaborative_filtering.ipynb](11-advanced-specialized-ml/04_recommender_systems_collaborative_filtering.ipynb)**: User-Item interaction matrix, Collaborative Filtering, and Cosine similarity.
- 📓 **[05_time_series_forecasting_arima_and_seasonality.ipynb](11-advanced-specialized-ml/05_time_series_forecasting_arima_and_seasonality.ipynb)**: Stationarity testing, differencing, and ARIMA $(p, d, q)$ parameters.

---

### 📍 Week 12: Generative AI, Multimodal Architectures & Diffusion
- 📓 **[01_autoencoders_and_variational_autoencoders_vae.ipynb](12-generative-ai-and-diffusion/01_autoencoders_and_variational_autoencoders_vae.ipynb)**: Latent bottleneck compression, reparameterization trick, and KL-divergence loss from scratch.
- 📓 **[02_generative_adversarial_networks_gan_from_scratch.ipynb](12-generative-ai-and-diffusion/02_generative_adversarial_networks_gan_from_scratch.ipynb)**: Min-max zero-sum game, Generator vs. Discriminator adversarial loss, and mode collapse.
- 📓 **[03_diffusion_models_ddpm_and_denoising_math.ipynb](12-generative-ai-and-diffusion/03_diffusion_models_ddpm_and_denoising_math.ipynb)**: Forward Markov noise schedule, reverse score denoising, and U-Net epsilon prediction math.
- 📓 **[04_vision_transformers_vit_patch_projection.ipynb](12-generative-ai-and-diffusion/04_vision_transformers_vit_patch_projection.ipynb)**: Image patch flattening, linear projection, [CLS] token classification, and self-attention in CV.
- 📓 **[05_clip_and_multimodal_contrastive_learning.ipynb](12-generative-ai-and-diffusion/05_clip_and_multimodal_contrastive_learning.ipynb)**: OpenAI CLIP dual-encoders, cross-modal cosine similarity, and zero-shot image classification.

---

### 📍 Week 13: Reinforcement Learning (RL) & Human Alignment (RLHF)
- 📓 **[01_reinforcement_learning_markov_decision_process_mdp.ipynb](13-reinforcement-learning-and-rlhf/01_reinforcement_learning_markov_decision_process_mdp.ipynb)**: Markov Decision Processes (MDP), Bellman optimality equations, and state-value iteration.
- 📓 **[02_q_learning_and_temporal_difference_from_scratch.ipynb](13-reinforcement-learning-and-rlhf/02_q_learning_and_temporal_difference_from_scratch.ipynb)**: Model-free tabular Q-learning, Temporal Difference (TD) updates, and epsilon-greedy exploration.
- 📓 **[03_deep_q_networks_dqn_experience_replay.ipynb](13-reinforcement-learning-and-rlhf/03_deep_q_networks_dqn_experience_replay.ipynb)**: Deep Q-Networks, experience replay memory buffers, and frozen target networks.
- 📓 **[04_policy_gradients_reinforce_and_actor_critic.ipynb](13-reinforcement-learning-and-rlhf/04_policy_gradients_reinforce_and_actor_critic.ipynb)**: REINFORCE policy gradient theorem, log-derivative trick, and Advantage Actor-Critic (A2C).
- 📓 **[05_rlhf_reinforcement_learning_human_feedback.ipynb](13-reinforcement-learning-and-rlhf/05_rlhf_reinforcement_learning_human_feedback.ipynb)**: 3-step RLHF pipeline: SFT, Bradley-Terry reward modeling, and PPO alignment with KL penalties.

---

### 📍 Week 14: LLM Fine-Tuning (PEFT), Quantization & AI Agents
- 📓 **[01_lora_low_rank_adaptation_from_scratch.ipynb](14-llm-finetuning-and-peft/01_lora_low_rank_adaptation_from_scratch.ipynb)**: Low-Rank Adaptation (LoRA) weight decomposition $W + B \cdot A$, rank $r$ bottleneck, and parameter savings.
- 📓 **[02_qlora_and_4bit_quantization_nf4.ipynb](14-llm-finetuning-and-peft/02_qlora_and_4bit_quantization_nf4.ipynb)**: 4-bit NormalFloat (NF4) quantization, double quantization, and paged optimizers for consumer GPUs.
- 📓 **[03_direct_preference_optimization_dpo.ipynb](14-llm-finetuning-and-peft/03_direct_preference_optimization_dpo.ipynb)**: Direct Preference Optimization (DPO) mathematical derivation, closed-form objective, and bypassing separate reward models.
- 📓 **[04_speculative_decoding_and_kv_cache.ipynb](14-llm-finetuning-and-peft/04_speculative_decoding_and_kv_cache.ipynb)**: KV-Cache memory mechanics, memory bandwidth bottlenecks, and Speculative Decoding draft verification.
- 📓 **[05_ai_agents_function_calling_and_tool_use.ipynb](14-llm-finetuning-and-peft/05_ai_agents_function_calling_and_tool_use.ipynb)**: ReAct (Reason + Act) loop, JSON tool schemas, multi-step tool execution, and error handling.

---

## 🎯 Daily Cadence & Code Quality
- **Pure Jupyter Notebook Format (`.ipynb`)**: Directly viewable in your browser on GitHub.
- **Deep Explanations**: Theory, math derivations, line-by-line commentary, and interview Q&As.
- **Sequential Commits**: Each notebook is committed and pushed individually with clean conventional commit messages.

---

*Authored by Muhammad Zabiullah ([@mzb000](https://github.com/mzb000))*
