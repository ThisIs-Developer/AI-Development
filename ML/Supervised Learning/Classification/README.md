# Supervised Learning: Classification

## Introduction
Classification tasks aim to assign a category to an input based on its features. For instance, an email can be classified as "spam" or "not spam", or a tumor can be classified as "malignant" or "benign". Supervised learning algorithms build a model that makes these classifications based on examples in the training data.

<img src="https://cdn.educba.com/academy/wp-content/uploads/2019/09/Explain-Classification-Algorithms-in-Detail.png" height="300">

## Table of Contents
 -  [Types of Classification](#types-of-classification)
 -  [Common Algorithms](#common-algorithms)
 -  [Performance Metrics](#performance-metrics)
 -  [Applications](#applications)


## Types of Classification
- **Binary Classification**: Classifies inputs into two distinct classes (e.g., spam or not spam).
- **Multiclass Classification**: Classifies inputs into one of three or more classes (e.g., categorizing types of animals).
- **Multilabel Classification**: Each input can belong to multiple classes simultaneously (e.g., tagging a photo with multiple labels like "beach", "sunset", "vacation").

## Common Algorithms
- **Logistic Regression**: A statistical model that uses a logistic function to model a binary dependent variable.  
<img src="https://assets-global.website-files.com/5ced99a4fd5e3ae5e159181c/61a79d95128eb3d804b7ff74_KYdeWR91QVfwv1rRiTj3Yq87_5_mdKRYmfz7GigdVCw2cHyChluQ0g0GQbuyBXUbRdfDcIeXiwSiaHJYvNTO6KrB-4-VEnA1bF0bX-IYBYTLQA--TY8bzmv5plfglQ4b7-f1VLOI.png" height=400>

- **Decision Trees**: A flowchart-like structure where an internal node represents a feature, the branch represents a decision rule, and each leaf represents an outcome.
<img src="https://assets-global.website-files.com/5ced99a4fd5e3ae5e159181c/61a79d958aa2147980a4e5ba_ysXw_BoPMEz7s_Y2sFhYoKwt_h4jmYYQOLbH10ittWAiW32cZkyTf-GoH84Uzy8EgmcFStgYaAEJ9WVvlHPySowrEIoxWkbsPjteBfQQ5aznjLmqg14VX1sTDquq5BzDNPP3oilp.png" height=400>

- **Random Forest**: An ensemble of decision trees, generally trained with the bagging method.
<img src="https://miro.medium.com/v2/resize:fit:1400/1*hmtbIgxoflflJqMJ_UHwXw.jpeg" height=400>

- **Support Vector Machines (SVM)**: A classifier that finds the hyperplane that best separates the classes in the feature space.    
<img src="https://assets-global.website-files.com/5ced99a4fd5e3ae5e159181c/61a79d95e1b9565f171db7cc_o2lFCv5i57fqv_jvJHUexY1yvo0IzUn2ckq5WBx4J2mj1XrAuRHsCJuDRZ4hwqGadG7t2OgYCOwKxLdZHzBJybzeSLkCB-s8MydcmfHy6Apk5ekhzN_DRw1pFRJ6MP5EyRtlElBf.png" height=400>

- **k-Nearest Neighbors (k-NN)**: Classifies a data point based on how its neighbors are classified.
<img src="https://assets-global.website-files.com/5ced99a4fd5e3ae5e159181c/61a79d95db8073623e1430a4_XjsuvXUtXYqTinwu3RPayQ0bIn84XQwR2wShJZElx9_vh9oPky-qX4L_VWgh-rcvsbfux2qaWMCr-4jxgQlKtsS6jwyE1na_vir7N39TggeZi38_tUV1u5Xv2GLzPRhevOTMykaP.png" height=400>

- **Naive Bayes**: A probabilistic classifier based on Bayes' theorem with strong independence assumptions.

- **Neural Networks**: Consist of layers of neurons that can learn complex patterns in data.

## Performance Metrics
- **Accuracy**: The ratio of correctly predicted instances to the total instances.
- **Precision**: The ratio of true positive predictions to the total positive predictions.
- **Recall (Sensitivity)**: The ratio of true positive predictions to the actual positives.
- **F1 Score**: The harmonic mean of precision and recall.
- **ROC-AUC**: The area under the receiver operating characteristic curve, a measure of the model's ability to distinguish between classes.

## Applications
- **Spam Detection**: Classifying emails as spam or not.
- **Image Recognition**: Identifying objects or features in images.
- **Medical Diagnosis**: Classifying medical images or symptoms to diagnose diseases.
- **Sentiment Analysis**: Determining the sentiment of a piece of text.
- **Fraud Detection**: Identifying fraudulent transactions or activities.
