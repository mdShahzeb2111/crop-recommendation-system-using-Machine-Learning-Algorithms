# Crop Recommendation System

This project is a machine learning-based crop recommendation system that suggests the most suitable crop to grow based on soil and environmental conditions. The system uses various machine learning models to predict the crop based on input parameters such as nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall.

## Features
- Predicts the best crop to grow based on soil and environmental conditions.
- Utilizes multiple machine learning models, including:
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)
  - Logistic Regression
  - Naive Bayes
- Provides high accuracy predictions with pre-trained models.

## Dataset
The dataset used for training the models is stored in [`crop_recommendation.csv`](crop_recommendation.csv). It contains the following columns:
- `N`: Nitrogen content in the soil
- `P`: Phosphorus content in the soil
- `K`: Potassium content in the soil
- `temperature`: Temperature in degrees Celsius
- `humidity`: Humidity percentage
- `ph`: pH value of the soil
- `rainfall`: Rainfall in mm
- `label`: Crop name

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

