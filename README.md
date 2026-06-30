# AI Credit Scoring System

An AI-powered Credit Scoring and Loan Decision Support System that evaluates borrower creditworthiness and predicts the Probability of Default (PD) using Machine Learning.

This project combines a complete credit scoring application with machine learning model development, providing an end-to-end solution for intelligent lending decision support.

---

## Project Overview

The repository consists of three major components:

### 📌 Credit Scoring System
A production-oriented application built with **Streamlit** and **FastAPI** for borrower assessment and loan decision support.

### 🤖 Model Development
A research environment for developing, training, evaluating, and comparing Machine Learning models, including:

- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning (Research)

### 🪪 National ID Verification
A FastAPI service integrated with the Cambodia voter database for borrower identity verification.

---

# Features

- National ID (NID) Verification
- Credit Assessment for New and Existing Borrowers
- Machine Learning-based Default Prediction
- Probability of Default (PD) Estimation
- Credit Score Generation
- Loan Decision Support
- Personalized Credit Improvement Recommendations
- Assessment History Dashboard
- Interactive Streamlit Web Application

---

# System Workflow

```text
Loan Application
        │
        ▼
National ID Verification
        │
        ▼
Data Validation
        │
        ▼
Redline Rules
        │
        ▼
Borrower Segmentation
(New / Existing Borrower)
        │
        ▼
Machine Learning Prediction
        │
        ▼
Probability of Default (PD)
        │
        ▼
Credit Score Generation
        │
        ▼
Loan Decision & Recommendation
```

---

# Repository Structure

```text
AI-Credit-Scoring-System/
│
├── check_nid/
│   FastAPI service for National ID verification
│
├── credit_scoring/
│   Main Streamlit application
│
├── model_development/
│   ├── supervised_learning/
│   ├── unsupervised_learning/
│   └── reinforcement_learning/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Module Description

## 1. Credit Scoring System

The main application responsible for borrower assessment and loan decision support.

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

### Responsibilities

- User Authentication
- Borrower Information Collection
- National ID Integration
- Feature Engineering
- Credit Score Calculation
- Default Prediction
- Decision Recommendation
- Assessment History

---

## 2. Model Development

Contains all experiments, notebooks, trained models, and evaluation results.

### Supervised Learning

Develops predictive models for borrower default prediction.

Contents include:

- Data preprocessing
- Feature engineering
- Model training
- Hyperparameter tuning
- Model evaluation
- Model comparison
- Trained models

Algorithms include:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Multi-Layer Perceptron (MLP)

---

### Unsupervised Learning

Explores borrower segmentation using clustering techniques.

Includes:

- Data preprocessing
- Feature transformation
- K-Means clustering
- Cluster analysis
- Cluster visualization
- Evaluation metrics

---

### Reinforcement Learning

Research module for intelligent credit policy optimization.

Current work includes:

- Reinforcement Learning fundamentals
- Q-Learning implementation
- Credit decision environment
- Reward function design
- Policy optimization

> **Note:** This module is currently under research and is not yet integrated into the production system.

---

## 3. National ID Verification

FastAPI service for verifying Cambodian National IDs using voter registration data.

Responsibilities:

- National ID verification
- Voter information retrieval
- Data validation
- MySQL caching
- REST API services

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

---

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

## Research

- Reinforcement Learning
- Q-Learning

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

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Running the Project

## 1. Start National ID Verification API

```bash
cd check_nid

uvicorn main:app --reload
```

API

```
http://127.0.0.1:8000
```

---

## 2. Start Credit Scoring System

```bash
cd credit_scoring

streamlit run app.py
```

Application

```
http://localhost:8501
```

---

# Future Development

- Explainable AI (XAI)
- Advanced Ensemble Models
- Graph-based Credit Scoring
- Reinforcement Learning Integration
- Dynamic Credit Limit Recommendation
- Real-time Risk Monitoring
- MLOps Deployment Pipeline
