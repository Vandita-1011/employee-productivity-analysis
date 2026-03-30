Employee Productivity & Work Hours Analysis

Why This Project?

In modern workplaces, employees often work extended hours with the assumption that more time leads to higher productivity. However, this may not always be true.

This project aims to critically evaluate whether longer working hours actually improve productivity, or if they lead to diminishing returns and inefficiency.

---
 Problem Statement

To analyze and determine:

- Does working overtime increase productivity?
- Is there a significant difference between normal and overtime workers?
- At what point do longer hours stop being effective?

---

Approach (How We Solved It)

1. Data Collection

- Dataset sourced from Kaggle
- Contains employee work hours, tasks completed, and performance ratings

---

2. Data Preprocessing

- Cleaned and standardized column names
- Removed inconsistencies
- Created derived features:
  - Overtime (Work_Hours > 40)
  - Productivity Index:
    Productivity = (Tasks_Completed × 0.5) + (Quality_Score × 0.5)

---

3. Exploratory Data Analysis

- Analyzed distribution of work hours
- Compared productivity between normal and overtime employees
- Identified trends and patterns using visualizations

---

4. Statistical Analysis

- Correlation analysis (Work Hours vs Productivity)
- Hypothesis testing (t-test)
- Variance analysis (ANOVA)

---

5. Insight Generation

- Interpreted results to understand real-world implications
- Evaluated whether overtime leads to meaningful productivity gains

---

 Project Structure

Employee_Productivity_Project/
│
├── data/
│   ├── employee_productivity.csv
│   └── cleaned_employee_data.csv
│
├── notebooks/
│   └── data_cleaning.py
│
├── reports/

---

 Technologies Used

- Python (Pandas)
- Git & GitHub
- Visual Studio Code

---

 Key Features

- Real-world dataset analysis
- Feature engineering (Overtime & Productivity Index)
- Statistical validation of results
- Modular team-based workflow

---

 Dataset

Processed dataset available at:

data/cleaned_employee_data.csv

---

 Team Contribution

- Member 1: Data preprocessing & feature engineering
- Member 2: Exploratory data analysis
- Member 3: Statistical testing
- Member 4: Insights & reporting

---

 Outcome

This project provides a data-driven understanding of how work hours influence productivity, helping organizations make informed decisions about workload and efficiency.

---

 Future Scope

- Incorporate machine learning models
- Include additional factors (stress, salary, job role)
- Develop interactive dashboards

---

 A structured analytical approach to understanding productivity beyond assumptions.
