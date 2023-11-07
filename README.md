# Predicting Smartphone Addiction

This repository contains code and resources for predicting smartphone addiction in college students. 

## Dataset Description

The dataset consists of 688 undergraduate students at Notre Dame University (NDU), Lebanon, who participated in a cross-sectional study on depression, anxiety, and smartphone addiction. The dataset includes various features related to participants' demographics, personality traits, smartphone usage, and mental health scores. The `TotAddiction_Score` serves as the target variable, representing the total addiction score calculated from the other columns. The dataset includes the following columns:

- `ID`: Participant ID
- `AGE`: Age of the participant
- `Gender`: Gender of the participant (0 for male, 1 for female)
- `WrkHrs_Wk`: Weekly work hours (categorized)
- `Prsnlty_type`: Personality type (0 for Type A, 1 for Type B)
- `Smoking`: Smoking habits (0 for No, 1 for Yes)
- `Alcohol_drnk`: Alcohol consumption (0 for No, 1 for Yes)
- `AgeStrt_useSmrtPhne`: Age at which the participant started using a smartphone
- `HrsSmrtPhnUse_Wkday`: Average hours of smartphone use on weekdays (categorized)
- `Compulsive_Behavior`: Compulsive behavior related to smartphone use
- `Functional_Impairment`: Functional impairment due to smartphone use
- `Withdrawal`: Withdrawal symptoms when not using a smartphone
- `Tolerance`: Tolerance to smartphone use
- `Depression_score`: Score related to depression
- `Anxiety_score`: Score related to anxiety
- `TotAddiction_Score`: Total addiction score

Link to the study: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0182239

The project is divided into two modules:

## Module 1: Exploratory Data Analysis 

In this module, we perform an exploratory data analysis (EDA) on the dataset to gain insights into the factors contributing to smartphone addiction.

### Steps in Module 1

1. Data Loading and Preprocessing
2. Data Exploration and Visualization
3. Correlation Analysis
4. Feature Selection

## Module 2: Model Building and Evaluation

In Module 2, we build a predictive model for smartphone addiction based on the insights gained in Module 1.

### Additional Steps in Module 2

5. Model Training
6. Metrics Calculation (e.g., MSE, RMSE, MAE, R-squared)
7. Model Comparison
