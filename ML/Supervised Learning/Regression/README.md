# Supervised Learning: Regression

## Introduction
Regression tasks aim to predict a continuous output based on input features. For example, predicting the price of a house based on its characteristics, or forecasting sales based on historical data. Supervised learning algorithms build a model that makes these predictions based on examples in the training data.

<img src="https://fastercapital.com/i/Regression-analysis--Utilizing-Regression-Analysis-in-Consensus-Estimates--Types-of-Regression-Analysis.webp" height="300">

## Table of Contents
 -  [Types of Regression](#types-of-regression)
 -  [Common Algorithms](#common-algorithms)
 -  [Performance Metrics](#performance-metrics)
 -  [Applications](#applications)


## Types of Regression
- **Linear Regression**: Predicts the output by fitting a linear relationship between the input features and the output.
- **Polynomial Regression**: A type of linear regression where the relationship between the input features and the output is modeled as an nth degree polynomial.
- **Ridge Regression**: A type of linear regression that includes a regularization term to prevent overfitting.
- **Lasso Regression**: Similar to ridge regression, but uses L1 regularization which can shrink some coefficients to zero, effectively selecting features.
- **Elastic Net**: Combines the penalties of ridge and lasso regression.
- **Logistic Regression**: Though commonly used for classification, it can also be used for regression problems where the outcome is binary.

## Common Algorithms
- **Simple Linear Regression**: Models the relationship between two variables by fitting a linear equation.
- **Multiple Linear Regression**: Extends simple linear regression to include multiple input features.
- **Polynomial Regression**: Fits a polynomial equation to the data.
- **Ridge Regression**: Adds a regularization term to the linear regression loss function to reduce overfitting.
- **Lasso Regression**: Similar to ridge regression, but can shrink some coefficients to zero.
- **Elastic Net**: A combination of ridge and lasso regression.
- **Support Vector Regression (SVR)**: Uses support vector machines to perform regression.
- **Decision Trees**: Splits the data into regions and fits a simple model in each region.
- **Random Forest**: An ensemble of decision trees, generally trained with the bagging method.
- **Gradient Boosting Machines (GBM)**: An ensemble technique that builds models sequentially to correct the errors of previous models.
- **Neural Networks**: Consist of layers of neurons that can learn complex patterns in data.

## Performance Metrics
- **Mean Absolute Error (MAE)**: The average of absolute differences between predicted and actual values.
- **Mean Squared Error (MSE)**: The average of the squared differences between predicted and actual values.
- **Root Mean Squared Error (RMSE)**: The square root of the average of the squared differences between predicted and actual values.
- **R-squared (R²)**: The proportion of the variance in the dependent variable that is predictable from the independent variables.

## Applications
- **House Price Prediction**: Estimating the price of a house based on its features.
- **Stock Price Forecasting**: Predicting the future price of stocks.
- **Sales Forecasting**: Estimating future sales based on historical data.
- **Weather Prediction**: Forecasting temperatures and other weather conditions.
- **Medical Diagnosis**: Predicting the progression of diseases based on patient data.
