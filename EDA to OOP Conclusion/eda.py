import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class EDA:
    def __init__(self, df):
        # Make a copy so we don’t modify the original passed-in DataFrame
        self.df = df.copy()
        # Strip whitespace on the copy’s column names
        self.df.columns = self.df.columns.str.strip()

    def plot_income_by_status(self):
        """Q1: How does annual income differ between approved and rejected loans?"""
        plt.figure(figsize=(6,4))
        sns.boxplot(x="loan_status", y="income_annum", data=self.df)
        plt.title("Income by Loan Status")
        plt.show()

    def plot_dti_ratio(self):
        """Q2: Debt-to-Income Ratio distribution by status."""
        self.df["dti_ratio"] = self.df["loan_amount"] / self.df["income_annum"]
        plt.figure(figsize=(6,4))
        sns.histplot(data=self.df, x="dti_ratio", hue="loan_status", element="step", stat="density")
        plt.title("Debt-to-Income Ratio by Loan Status")
        plt.show()

    def plot_dependents_impact(self):
        """Q3: Approval % by number of dependents."""
        dep_ct = pd.crosstab(self.df["no_of_dependents"], self.df["loan_status"], normalize="index") * 100
        dep_ct.plot(kind="bar", stacked=True, figsize=(6,4))
        plt.title("% Approval by Number of Dependents")
        plt.show()

    def plot_cibil_vs_income(self):
        """Q4: CIBIL Score distribution by loan status."""
        plt.figure(figsize=(6,4))
        sns.kdeplot(data=self.df, x="cibil_score", hue="loan_status", fill=True)
        plt.title("CIBIL Score Distribution by Loan Status")
        plt.show()

    def plot_self_employed_approval(self):
        """Q5: Approval % by self-employed status."""
        se_ct = pd.crosstab(self.df["self_employed"], self.df["loan_status"], normalize="index") * 100
        se_ct.plot(kind="bar", figsize=(6,4))
        plt.title("Approval % by Self-Employed Status")
        plt.show()

    def plot_education_approval(self):
        """Q6: Approval % by education level."""
        edu_ct = pd.crosstab(self.df["education"], self.df["loan_status"], normalize="index") * 100
        edu_ct.plot(kind="bar", figsize=(6,4))
        plt.title("Approval % by Education Level")
        plt.show()