# MY GitHub Portfolio Setup Guide

## 📁 Complete Portfolio Structure

```
telco-churn-analysis/
│
├── README.md                          # Main portfolio README
├── requirements.txt                   # Python dependencies
├── LICENSE                            # MIT License
│
├── data/
│   ├── README.md                      # Data dictionary
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── telco_churn_analyzed.csv       # Cleaned dataset
│
├── notebooks/
│   ├── 01_data_exploration.ipynb      # Initial EDA
│   ├── 02_data_cleaning.ipynb         # Data quality checks
│   ├── 03_feature_engineering.ipynb   # Feature creation
│   └── 04_business_insights.ipynb     # Analysis & insights
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py                 # Data loading functions
│   ├── data_cleaner.py                # Cleaning functions
│   ├── feature_engineering.py         # Feature creation
│   ├── visualization.py               # Plotting functions
│   └── analysis.py                    # Analysis functions
│
├── visualizations/
│   ├── 01_churn_distribution.png
│   ├── 02_numeric_distributions.png
│   ├── 03_correlation_heatmap.png
│   ├── 04_churn_by_contract.png
│   ├── 05_charges_vs_churn.png
│   └── 06_churn_by_internet_service.png
│
├── reports/
│   ├── executive_summary.pdf          # One-page summary
│   ├── detailed_report.pdf            # Full analysis report
│   └── presentation.pptx              # Slide deck
│
└── tests/
    └── test_analysis.py               # Unit tests
```
---

## 📊 Project Overview

This project analyzes **7,043 customer records** from a telecommunications company to understand customer churn patterns and identify actionable retention strategies. Through systematic data analysis, I uncovered high-risk customer segments and provided data-driven recommendations that could reduce churn by 20%, saving **$328,130 annually**.

### 🎯 Key Metrics

- **Dataset Size:** 7,043 customers × 21 features
- **Churn Rate:** 26.5% (1,865 customers lost)
- **Monthly Revenue Loss:** $136,721
- **Potential Annual Savings:** $328,130
- **High-Risk Segments Identified:** 4 segments with 40%+ churn

---

## 🔍 Key Findings

### 1. **Contract Type is Critical**
- Month-to-month customers: **42% churn rate**
- Two-year contract customers: **11% churn rate**
- **Impact:** 2,876 month-to-month customers at high risk

### 2. **Payment Method Matters**
- Electronic check users: **45.3% churn** (highest!)
- Automatic payment users: **15.3% churn**
- **Impact:** 2,361 customers using high-risk payment method

### 3. **Internet Service Type**
- Fiber optic customers: **41.9% churn**
- DSL customers: **19% churn**
- **Impact:** Premium service customers actually churn more

### 4. **Service Adoption**
- 0-2 addon services: **35-40% churn**
- 4+ addon services: **15% churn**
- **Impact:** Customers with fewer services are 2.5x more likely to leave

---

## 💼 Business Impact

### Financial Analysis

| Metric | Value |
|--------|-------|
| Current Monthly Revenue Loss | $136,721 |
| Annual Revenue Loss | $1,640,652 |
| Potential Savings (20% churn reduction) | $328,130/year |
| Implementation Cost | $200K-400K |
| **First Year ROI** | **82-164%** |

### Recommended Actions (Prioritized)

**Priority 1: Payment Optimization** ⭐
- Incentivize automatic payments with 10% discount
- Expected impact: 5-7% churn reduction
- ROI: Immediate positive return

**Priority 2: Contract Conversion**
- Offer 20% discount for annual contracts
- Expected impact: 15-20% churn reduction
- Target: 2,876 month-to-month customers

**Priority 3: Service Bundling**
- Bundle Tech Support + Online Security
- Expected impact: 8-10% churn reduction
- Target: 2,088 customers without support

**Priority 4: Senior Citizen Program**
- Dedicated support line, simplified billing
- Expected impact: 5-8% churn reduction
- Target: 1,142 senior customers

---

## 🛠️ Technologies Used

### Core Libraries
- **Python 3.8+** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualization
- **Scipy** - Statistical analysis

### Development Tools
- **Jupyter Notebook** - Interactive analysis
- **Git** - Version control
- **VS Code** - Code editor

---

## 📁 Project Structure

```
├── notebooks/           # Jupyter notebooks for each analysis phase
├── src/                 # Modular Python code
├── visualizations/      # Saved charts and graphs
├── data/               # Dataset files
├── reports/            # PDF reports and presentations
└── tests/              # Unit tests
```


---

## 📈 Analysis Workflow

### Phase 1: Data Exploration & Cleaning
- ✅ Loaded and inspected 7,043 customer records
- ✅ Identified 11 missing values in TotalCharges
- ✅ Validated data types and consistency
- ✅ Detected outliers using IQR and Z-score methods

### Phase 2: Exploratory Data Analysis
- ✅ Analyzed distributions of numeric and categorical variables
- ✅ Created 6 key visualizations
- ✅ Identified correlations between features
- ✅ Discovered bimodal tenure pattern (new vs loyal customers)

### Phase 3: Feature Engineering
- ✅ Created 6 new features:
  - `tenure_group` - Customer lifecycle stage
  - `avg_monthly_spend` - Normalized spending
  - `has_internet` - Binary internet flag
  - `num_addon_services` - Service adoption level
  - `uses_auto_payment` - Payment behavior
  - `contract_months` - Contract commitment

### Phase 4: Business Insights
- ✅ Identified 4 high-risk segments (40%+ churn)
- ✅ Quantified financial impact ($136K/month loss)
- ✅ Developed prioritized recommendations
- ✅ Calculated ROI (82-164% first year)

---

## 📊 Visualizations

### 1. Churn Distribution
![Churn Distribution](visualizations/01_churn_distribution.png)
*Insight: Imbalanced dataset with 26.5% churn rate*

### 2. Numeric Feature Distributions
![Numeric Distributions](visualizations/02_numeric_distributions.png)
*Insight: Bimodal tenure shows new vs loyal customer segments*

### 3. Correlation Heatmap
![Correlation Heatmap](visualizations/03_correlation_heatmap.png)
*Insight: TotalCharges strongly correlated with tenure (0.83)*

### 4. Churn by Contract Type
![Churn by Contract](visualizations/04_churn_by_contract.png)
*Insight: Month-to-month contracts have 42% churn vs 11% for two-year*

### 5. Monthly Charges vs Churn
![Charges vs Churn](visualizations/05_charges_vs_churn.png)
*Insight: Higher monthly charges correlate with increased churn*

### 6. Churn by Internet Service
![Churn by Internet](visualizations/06_churn_by_internet_service.png)
*Insight: Fiber optic customers churn at 41.9%*

---

## 🎓 Skills Demonstrated

### Technical Skills
- ✅ Data cleaning and preprocessing
- ✅ Exploratory data analysis (EDA)
- ✅ Statistical analysis (correlation, hypothesis testing)
- ✅ Outlier detection (IQR, Z-score)
- ✅ Feature engineering (6 techniques)
- ✅ Data visualization (6 professional charts)
- ✅ Business intelligence and segmentation
- ✅ Financial impact calculation

### Business Skills
- ✅ Problem definition and scoping
- ✅ Customer segmentation
- ✅ ROI calculation and business case development
- ✅ Actionable recommendation formulation
- ✅ Stakeholder communication

### Tools & Technologies
- ✅ Python (Pandas, NumPy, Matplotlib, Seaborn, Scipy)
- ✅ Jupyter Notebooks
- ✅ Git version control
- ✅ Statistical analysis
- ✅ Data storytelling

---

## 🎯 Interview Preparation

This project demonstrates:
1. **Technical proficiency** in Python data analysis
2. **Business acumen** - translated data into $328K savings
3. **Communication skills** - clear visualizations and recommendations
4. **Problem-solving** - systematic approach to complex problem
5. **Attention to detail** - caught hidden missing values

**Common Interview Questions:** See [PORTFOLIO_QA.md](PORTFOLIO_QA.md) for 27 detailed Q&A


---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


## 🙏 Acknowledgments

- Dataset: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle
- Inspired by real-world customer retention challenges

---

---

**⭐ If you found this project helpful, please give it a star!**

**📧 For questions or collaboration opportunities, feel free to reach out!**
```

---

## 📋 requirements.txt

Create this file for easy dependency installation:

```txt
# Data manipulation
pandas==1.5.3
numpy==1.23.5

# Visualization
matplotlib==3.6.2
seaborn==0.12.2
plotly==5.13.0

# Statistical analysis
scipy==1.9.3
statsmodels==0.13.5

# Machine learning (for future enhancements)
scikit-learn==1.2.0
xgboost==1.7.5
imbalanced-learn==0.10.1

# Jupyter
jupyter==1.0.0
jupyterlab==3.5.3
notebook==6.5.2

# Utilities
python-dotenv==0.21.0
tqdm==4.64.1

# Testing
pytest==7.2.1

# Code quality
black==23.1.0
flake8==6.0.0
pylint==2.17.2
```

---

## 📄 LICENSE (MIT License)

```
MIT License

Copyright (c) 2024 INNOCENT WATSALA

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎨 Visualizations Script

Create `src/generate_visualizations.py`:

```python
"""
Generate all visualizations for the portfolio
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Create output directory
os.makedirs('../visualizations', exist_ok=True)

# Load data
df = pd.read_csv('../data/telco_churn_analyzed.csv')

# Color scheme
colors = {'No Churn': '#3498db', 'Churn': '#e74c3c'}

# 1. Churn Distribution
fig, ax = plt.subplots(figsize=(8, 6))
churn_counts = df['Churn'].value_counts()
ax.pie(churn_counts, labels=churn_counts.index, autopct='%1.1f%%', 
       colors=[colors['No Churn'], colors['Churn']], startangle=90)
ax.set_title('Customer Churn Distribution\n(26.5% Churn Rate)', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../visualizations/01_churn_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Numeric Distributions
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for idx, col in enumerate(['tenure', 'MonthlyCharges', 'TotalCharges']):
    axes[idx].hist(df[col].dropna(), bins=30, color='steelblue', edgecolor='black')
    axes[idx].set_title(f'{col} Distribution', fontweight='bold')
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('../visualizations/02_numeric_distributions.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Correlation Heatmap
numeric_df = df[['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']].copy()
numeric_df['Churn'] = (df['Churn'] == 'Yes').astype(int)
correlation_matrix = numeric_df.corr()
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, ax=ax, fmt='.2f')
ax.set_title('Feature Correlation Matrix', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('../visualizations/03_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Churn by Contract Type
contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index') * 100
fig, ax = plt.subplots(figsize=(10, 6))
contract_churn.plot(kind='bar', ax=ax, color=[colors['No Churn'], colors['Churn']])
ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Contract Type')
ax.legend(title='Churn')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('../visualizations/04_churn_by_contract.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Monthly Charges vs Churn
fig, ax = plt.subplots(figsize=(10, 6))
df[df['Churn']=='No']['MonthlyCharges'].hist(ax=ax, alpha=0.6, 
                                              label='No Churn', bins=30, color=colors['No Churn'])
df[df['Churn']=='Yes']['MonthlyCharges'].hist(ax=ax, alpha=0.6, 
                                               label='Churn', bins=30, color=colors['Churn'])
ax.set_title('Monthly Charges Distribution by Churn Status', 
             fontsize=14, fontweight='bold')
ax.set_xlabel('Monthly Charges ($)')
ax.set_ylabel('Frequency')
ax.legend()
plt.tight_layout()
plt.savefig('../visualizations/05_charges_vs_churn.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Churn by Internet Service
internet_churn = pd.crosstab(df['InternetService'], df['Churn'], normalize='index') * 100
fig, ax = plt.subplots(figsize=(10, 6))
internet_churn.plot(kind='bar', ax=ax, color=[colors['No Churn'], colors['Churn']])
ax.set_title('Churn Rate by Internet Service Type', fontsize=14, fontweight='bold')
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Internet Service')
ax.legend(title='Churn')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('../visualizations/06_churn_by_internet_service.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ All visualizations generated successfully!")
print(f"   Saved to: visualizations/")
print(f"   Total: 6 PNG files (300 DPI)")
```

---

## 🚀 Deployment Steps

### Step 1: Prepare Your Repository

```bash
# Create project directory
mkdir telco-churn-analysis
cd telco-churn-analysis

# Initialize git
git init

# Create folder structure
mkdir -p data notebooks src visualizations reports tests
```

### Step 2: Copy Files

```bash
# Copy your analysis files
cp DATA_ANALYSIS_GUIDE.py src/
cp telco_churn_analyzed.csv data/
cp WA_Fn-UseC_-Telco-Customer-Churn.csv data/

# Copy documentation
cp README_DATA_ANALYSIS.md .
cp PORTFOLIO_QA.md .
cp GITHUB_PORTFOLIO_SETUP.md .
```

### Step 3: Generate Visualizations

```bash
# Install dependencies
pip install -r requirements.txt

# Generate visualizations
python src/generate_visualizations.py
```

### Step 4: Create Main README

```bash
# Copy the README template above
# Customize with your information
# Save as README.md
```
```

---

## ✅ Final Checklist

Before making your portfolio public:

- [ ] All code is well-commented
- [ ] README is complete and professional
- [ ] Visualizations are high quality (300 DPI)
- [ ] requirements.txt is accurate
- [ ] No sensitive data exposed
- [ ] All files are organized
- [ ] Git history is clean
- [ ] License file included
- [ ] Portfolio Q&A is ready for interviews
- [ ] Demo video recorded (optional but recommended)
- [ ] Blog post written (optional but recommended)

---

## 🎯 Next Steps

1. **Today:** Create repository and push code
2. **This Week:** Record demo video, write blog post
3. **This Month:** Share on LinkedIn, apply for jobs
4. **Ongoing:** Add more projects, contribute to open source

---

**Your portfolio is now ready to showcase your data analysis skills to the world! 🚀**