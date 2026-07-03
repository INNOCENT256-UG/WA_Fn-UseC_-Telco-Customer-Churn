## 👋 Hi, I'm INNOCENT WATSALA

### 📊 Data Analyst | Business Intelligence | Python

I transform raw data into actionable business insights.

**🔭 Currently Working On:**
- Customer churn analysis and retention strategies
- Predictive modeling for business forecasting
- Data visualization and storytelling

**🌱 Learning:**
- Machine Learning (scikit-learn, XGBoost)
- SQL for data extraction
- Cloud platforms (AWS, GCP)

**💼 Projects:**
- [Telco Customer Churn Analysis](https://github.com/yourusername/telco-churn-analysis)- Identified $328K annual savings opportunity
- [CRM](https://github.com/INNOCENT256-UG/Managing-Employee-Data-with-Intergrity)
- [PK-Market-Price](https://github.com/INNOCENT256-UG/Analyzing-Paskistani-Food-Market-Prices-)
- [PK-Market-Price](https://github.com/INNOCENT256-UG/SFO-Air-Traffic-Cargo-Statistics-Data-Analysis-Project)
- [More projects coming soon...]

**📫 Connect:**
- LinkedIn: [Watsala.Digital](https://linkedin.com/in/Watsala.Digital)
- Email: Watsala.Digital@gmail.com



# 🎯 Telco Customer Churn Analysis

**A comprehensive data analysis project identifying at-risk customer segments and retention strategies for a telecommunications company, potentially saving $328K annually.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-green)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12%2B-orange)
![Status](https://img.shields.io/badge/Status-Complete-success)

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
![Churn Distribution](Graph/Customer%20Churn.png)
*Insight: Imbalanced dataset with 26.5% churn rate*

### 2. Numeric Feature Distributions
![Numeric Distributions](Graph/Monthly%20Charges%20Distribution.png)
*Insight: Bimodal tenure shows new vs loyal customer segments*

### 3. Correlation Heatmap
![Correlation Heatmap](Graph/Feature%20correlation%20Matrix.png)
*Insight: TotalCharges strongly correlated with tenure (0.83)*

### 4. Churn by Contract Type
![Churn by Contract](Graph/Churn%20Rate%20By%20Contract%20Type.png)
*Insight: Month-to-month contracts have 42% churn vs 11% for two-year*

### 5. Monthly Charges vs Churn
![Charges vs Churn](Graph/Churn%20Vs%20No%20Churn%20Monthly%20Charges.png)
*Insight: Higher monthly charges correlate with increased churn*

### 6. Churn by Internet Service
![Churn by Internet](Graph/Churn%20Rate%20By%20internet%20Service.png)
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

## 📝 Documentation

- **[Analysis Guide](notebooks/)** - Complete step-by-step analysis
- **[Portfolio Q&A](PORTFOLIO_QA.md)** - 27 interview questions & answers

---

## 🎯 Interview Preparation(GUIDE)

This project demonstrates:
1. **Technical proficiency** in Python data analysis
2. **Business acumen** - translated data into $328K savings
3. **Communication skills** - clear visualizations and recommendations
4. **Problem-solving** - systematic approach to complex problem
5. **Attention to detail** - caught hidden missing values

**Common Interview Questions:** See [PORTFOLIO_QA.md](PORTFOLIO_QA.md) for 27 detailed Q&A

---

## 🔄 My Future Enhancements Plan

- [ ] Buildding a predictive churn model (target: 80%+ accuracy)
- [ ] Implementing A/B testing framework
- [ ] Adding customer lifetime value (CLV) analysis
- [ ] Creating interactive dashboard with Plotly/Dash
- [ ] Analyzing temporal trends with historical data
- [ ] Deploying model as REST API

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**INNOCENT256**
- GitHub: [INNOCENT256-UG](https://github.com/INNOCENT256-UG)
- LinkedIn: [WatsalaDigital](https://linkedin.com/in/Watsala.Digital)
- Email: watsala.digital.com.com

---

## 🙏 Acknowledgments

- Dataset: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle
- Inspired by real-world customer retention challenges

---

## 📊 Project Stats


![GitHub stars](https://img.shields.io/github/stars/INNOCENT256-UG/telco-churn-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/INNOCENT256-UG/telco-churn-analysis?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/INNOCENT256-UG/telco-churn-analysis?style=social)
---

**⭐ If you found this project helpful, please give it a star!**

**📧 For questions or collaboration opportunities, feel free to reach out!**
```

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
