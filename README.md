# AI Credit Scoring System

## Overview

AI Credit Scoring System is an intelligent loan decision support system that evaluates borrower creditworthiness and predicts the probability of default using Machine Learning techniques.

The system integrates:

* National ID (NID) Verification
* Credit Risk Assessment
* Default Prediction Models
* Credit Scoring
* Recommendation System
* Assessment History Dashboard

The project aims to assist financial institutions and microfinance organizations in making faster, more accurate, and data-driven lending decisions, especially for borrowers with limited or no credit history.

---

# Features

*  National ID (NID) verification using Cambodia voter database.
*  Credit assessment for both new and existing borrowers.
*  Machine Learning-based default prediction.
*  Probability of Default (PD) estimation.
*  Credit score generation.
*  Loan decision support (Approve, Review, Reject).
*  Personalized recommendations to improve creditworthiness.
*  Assessment history management.
*  Interactive dashboard using Streamlit.

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

# Technology Stack

### Programming Language

* Python 3

### Machine Learning

* Scikit-learn
* Random Forest
* Logistic Regression
* Support Vector Machine (SVM)
* Multi-Layer Perceptron (MLP)

### Web Framework

* Streamlit
* FastAPI

### Database

* MySQL

### Libraries

* Pandas
* NumPy
* SQLAlchemy
* Selenium
* Joblib

---

# Project Structure

```text
AI-Credit-Scoring-System/
│
├── check_nid/              # FastAPI service for National ID verification and voter data retrieval.
│
├── credit_scoring/         # Main Streamlit application for credit assessment and default prediction.
│
├── ML/                     # Machine learning development notebooks and model training experiments.
│
├── README.md               # Project documentation and setup instructions.
│
├── requirements.txt        # Python dependencies required to run the project.
│
└── .gitignore              # Files and folders excluded from Git tracking.
```

---

# Credit Scoring Module Structure

```text
credit_scoring/
│
├── app.py                  # Entry point of the Streamlit application.
│
├── src/
│   ├── config/             # Application configurations and constants.
│   ├── database/           # Database connection and SQL scripts.
│   ├── prediction/         # Machine learning prediction logic.
│   ├── scoring/            # Credit scoring and risk calculation.
│   ├── ui/                 # Streamlit pages and user interface components.
│   └── utils/              # Utility and helper functions.
│
├── model/                  # Models of Machine learning that already train
│
├── preprocessor/           # Saved preprocessing pipelines and encoders.
│
└── data/                   # Input datasets and generated data files.
```

---

# National ID Verification Module

```text
check_nid/
│
└── main.py                 # FastAPI application and Selenium scraper.
```

### Responsibilities

* Verify Cambodian National ID (NID).
* Retrieve voter information from the Cambodia voter database.
* Cache voter information in MySQL.
* Provide API endpoints for the credit scoring application.

---

# Machine Learning Models

## New User Model

Predicts default risk for borrowers without repayment history using:

* Repayment Capacity
* Debt Exposure
* Stability & Life Structure
* Credit Seeking Behavior
* Financial Resilience
* Identity & Fraud Risk

## Existing User Model

Predicts default risk for borrowers with historical repayment records using:

* Repayment Behavior
* Current Debt & Exposure
* Financial Trend
* Credit Activity & Engagement
* Stability & Tenure

---

# Installation

## Clone Repository

```bash
git clone https://github.com/SopheaktraDLT/AI-Credit-Scoring-System.git
cd AI-Credit-Scoring-System
```

---

# Install Dependencies

## Credit Scoring System

```bash
cd credit_scoring
pip install -r requirements.txt
```

---

# Running the Project

## Step 1: Start NID Verification API

```bash
cd check_nid
uvicorn main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

---

## Step 2: Start Credit Scoring System

```bash
cd credit_scoring
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# Main Functionalities

### Identity Verification

Verify borrower information using Cambodia National ID.

### Credit Assessment

Collect borrower information and calculate financial features.

### Default Prediction

Predict the probability of borrower default using machine learning models.

### Credit Scoring

Generate borrower credit scores and determine risk levels.

### Decision Support

Classify applications into:

* Approve
* Manual Review
* Reject

### Recommendation System

Provide recommendations to improve borrower creditworthiness and reduce default risk.

---

# Author

**Yoeung Sopheaktra**

