# EDA to OOP

## Overview

This directory demonstrates how to transition from exploratory data analysis (EDA) scripts to an object-oriented programming (OOP) approach in Python. Using the **Loan Approval** dataset, we encapsulate each EDA task into reusable functions and organize them into classes, promoting modularity and maintainability.

## Dataset

- **Filename:** `loan_approval_dataset.csv`
- **Description:** Contains  loan application records with features such as:
  - `loan_id`: Unique identifier for each application
  - `no_of_dependents`: Number of dependents of the applicant
  - `education`: Educational status (`Graduate`/`Not Graduate`)
  - `self_employed`: Self-employment status (`Yes`/`No`)
  - `income_annum`: Annual income (in local currency)
  - `loan_amount`: Requested loan amount
  - `loan_term`: Term of the loan (in years)
  - `cibil_score`: Credit score of the applicant
  - Asset values: `residential_assets_value`, `commercial_assets_value`, `luxury_assets_value`, `bank_asset_value`
  - `loan_status`: Outcome (`Approved`/`Rejected`)

## Objectives

1. **Explore Key EDA Questions**: Answer 10 analytical questions related to loan approval, including income impact, debt-to-income ratio, credit scores, and asset correlations.
2. **Modularize EDA**: Convert individual analysis steps into standalone functions.
3. **OOP Structuring**: Group related EDA functions into two classes (`EDA_Part1` and `EDA_Part2`), each exposing five methods corresponding to the questions.
4. **Reusability & Clarity**: Demonstrate how OOP enhances code readability, reusability, and ease of maintenance in data science workflows.

### The 6 Key EDA Questions from the loan Dataset

1. **Income & Approval**  
   - How does annual income (`income_annum`) differ between approved and rejected loans?

2. **Debt-to-Income Ratio**  
   - If you define a new feature `loan_amount / income_annum`, how does its distribution vary by approval status?

3. **Dependents Impact**  
   - Does the number of dependents (`no_of_dependents`) affect the likelihood of loan approval?

4. **Creditworthiness**  
   - What’s the relationship between CIBIL score (`cibil_score`) and loan approval? Is there a clear cutoff?

5. **Employment Status**  
   - Are self‑employed applicants (`self_employed`) more or less likely to get approved than salaried ones?

6. **Education Effect**  
   - Does being a graduate (`education`) improve chances of approval, and by how much?


## Structure

```
EDA_to_OOP Conlusion/
├── loan_approval_dataset.csv             # Loan application dataset
├── EDA.ipynb                             # EDA notebook
├── EDA to Functions and Class.ipynb      # EDA to Function definitions classes
├── eda_test.ipynb                        # EDA classe test
├── eda.py                                # EDA classe module
└── README.md                             # This documentation
```

## Key Takeaways

- **OOP for EDA**: Encapsulating EDA tasks in classes promotes organized and maintainable code.
- **Function Reusability**: Standalone functions can be easily tested and reused across projects.
- **Extendability**: New analysis methods can be added by extending the existing classes or creating new ones.

*Developed as part of a methodical approach to teaching data scientists how to implement object-oriented principles in exploratory data analysis workflows.*

