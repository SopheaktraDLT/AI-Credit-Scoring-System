# AI Credit Scoring System

An AI-powered Credit Scoring and Loan Decision Support System designed to evaluate borrower creditworthiness and predict the probability of default using Machine Learning.

The project combines a complete credit scoring application with machine learning model development, enabling financial institutions and microfinance organizations to make faster, more consistent, and data-driven lending decisions.

---

## Project Components

This repository consists of two main modules:

### Credit Scoring System
A production-oriented application built with Streamlit and FastAPI that performs:

- National ID (NID) Verification
- Credit Assessment
- Probability of Default (PD) Prediction
- Credit Score Generation
- Loan Decision Support
- Personalized Recommendations
- Assessment History Dashboard

### Model Development
A research and experimentation environment containing the complete machine learning pipeline, including:

- Data Preprocessing
- Feature Engineering
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning (Research)
- Hyperparameter Tuning
- Model Evaluation
- Model Comparison

---

# Features

- National ID (NID) verification using Cambodia voter database
- Credit assessment for new and existing borrowers
- Machine learning-based default prediction
- Probability of Default (PD) estimation
- Credit score generation
- Loan decision support (Approve / Review / Reject)
- Personalized recommendations
- Assessment history management
- Interactive Streamlit dashboard

---

# System Workflow

```text
Loan Application
        ↓
National ID Verification
        ↓
Data Validation
        ↓
Redline Rules
        ↓
Borrower Segmentation
(New User / Existing User)
        ↓
Machine Learning Prediction
        ↓
Probability of Default
        ↓
Credit Score
        ↓
Decision & Recommendation
```

---

# Repository Structure

```text
AI-Credit-Scoring-System/
│
├── check_nid/                    # FastAPI service for National ID verification
│
├── credit_scoring/               # Main credit scoring application
│
├── model_development/            # Machine learning development
│   │
│   ├── supervised_learning/
│   │
│   ├── unsupervised_learning/
│   │
│   └── reinforcement_learning/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Credit Scoring System

The **credit_scoring** module contains the deployable application.

### Main Components

```text
credit_scoring/
│
├── app.py
│
├── src/
│   ├── config/
│   ├── database/
│   ├── prediction/
│   ├── scoring/
│   ├── ui/
│   └── utils/
│
├── model/
├── preprocessor/
└── data/
```

---

# Model Development

The **model_development** module contains all machine learning research and experimentation.

```text
model_development/
│
├── supervised_learning/
│   ├── Data preprocessing
│   ├── Feature engineering
│   ├── Model training
│   ├── Hyperparameter tuning
│   ├── Model evaluation
│   └── Model comparison
│
├── unsupervised_learning/
│   ├── Data preprocessing
│   ├── K-Means clustering
│   ├── Cluster analysis
│   └── Results
│
└── reinforcement_learning/
    ├── Reinforcement learning experiments
    └── Q-Learning research
```

---

# Machine Learning Models

## New Borrower Model

Predicts default risk for applicants without repayment history using:

- Repayment Capacity
- Debt Exposure
- Stability & Life Structure
- Credit Seeking Behavior
- Financial Profile & Resilience
- Identity & Fraud Risk

## Existing Borrower Model

Predicts default risk for borrowers with historical repayment records using:

- Repayment Behavior
- Current Debt & Exposure
- Financial Trend
- Credit Activity & Engagement
- Stability & Tenure

---

# Technology Stack

## Programming Language

- Python

## Machine Learning

- Scikit-learn
- Random Forest
- Logistic Regression
- Support Vector Machine (SVM)
- Multi-Layer Perceptron (MLP)

## Web Framework

- Streamlit
- FastAPI

## Database

- MySQL

## Libraries

- Pandas
- NumPy
- SQLAlchemy
- Selenium
- Joblib

---

# Installation

Clone the repository.

```bash
git clone https://github.com/SopheaktraDLT/AI-Credit-Scoring-System.git
cd AI-Credit-Scoring-System
```

Install the required dependencies.

```bash
cd credit_scoring
pip install -r requirements.txt
```

---

# Running the Project

### Start the National ID Verification API

```bash
cd check_nid
uvicorn main:app --reload
```

API:

```
http://127.0.0.1:8000
```

---

### Start the Credit Scoring System

```bash
cd credit_scoring
streamlit run app.py
```

Application:

```
http://localhost:8501
```

---

# Future Development

- Advanced ensemble models
- Explainable AI (XAI)
- Reinforcement Learning for credit policy optimization
- Alternative data integration
- Dynamic scorecard optimization
- Real-time risk monitoring
