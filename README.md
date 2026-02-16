# FinZen AI - Personal Financial Advisor for Gen-Z

 **FinZen AI** is an intelligent personal financial advisor designed specifically for Gen-Z users. This single-file Streamlit application provides comprehensive financial analytics, predictive insights, goal planning, and AI-powered recommendations based on transaction data.

![FinZen AI](https://img.shields.io/badge/FinZen-AI-blue?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?style=flat-square&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

##  Features

###  **Comprehensive Dashboard**
- **Financial Health Score** (0-100) with detailed breakdown
- **Credit Score** (300-900) based on transaction patterns
- Real-time metrics: Income, Savings, Expenses, Savings Rate
- Interactive charts and visualizations

###  **Transaction Analysis**
- 12-month spending breakdown by category
- Benchmarking against ideal spending ratios
- Savings trend analysis with volatility metrics
- Expense radar charts

### **Predictive Analytics**
- AI-powered savings forecasting (3-5 year projections)
- Risk assessment based on savings consistency
- Linear regression models for trend analysis

###  **Goal Planning**
- Custom savings goals with progress tracking
- SIP (Systematic Investment Plan) recommendations
- Emergency fund calculations
- Goal prioritization

###  **What-If Simulator**
- Interactive scenario planning
- Impact analysis of spending changes
- SIP growth projections with CAGR calculations

###  **AI Financial Advisor**
- Multilingual support (English, Hindi, Marathi)
- Personalized recommendations
- Conversational interface
- Smart responses based on user data

##  Tech Stack

- **Frontend**: Streamlit with custom CSS (Dark neon-green theme)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly (interactive charts)
- **AI/ML**: Custom algorithms for scoring and predictions
- **Deployment**: Single-file Python application

##  Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository** (if applicable) or download `app.py`

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install streamlit pandas numpy plotly
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the app**:
   - Open your browser to `http://localhost:8501`
   - Login with any of the demo accounts below

##  Demo User Accounts

The app includes 15 demo user accounts with realistic financial data:

| Name | Email | Password | Role | City | Income Range |
|------|-------|----------|------|------|--------------|
| Arjun Sharma | arjun.sharma@email.com | arjun123 | Software Engineer | Pune | ₹55k-70k |
| Priya Desai | priya.desai@email.com | priya123 | Product Manager | Mumbai | ₹80k-100k |
| Sneha Kulkarni | sneha.kulkarni@email.com | sneha123 | Junior Analyst | Nagpur | ₹35k-45k |
| Rahul Verma | rahul.verma@email.com | rahul123 | UX Designer | Delhi | ₹50k |
| Ananya Singh | ananya.singh@email.com | ananya123 | Doctor | Bangalore | ₹80k-92k |
| Vikram Patel | vikram.patel@email.com | vikram123 | Teacher | Ahmedabad | ₹40k-48k |
| Kavya Rao | kavya.rao@email.com | kavya123 | Researcher | Hyderabad | ₹60k-72k |
| Amit Kumar | amit.kumar@email.com | amit123 | Business Analyst | Chennai | ₹55k-66k |
| Meera Joshi | meera.joshi@email.com | meera123 | Content Creator | Jaipur | ₹45k-52k |
| Sandeep Gupta | sandeep.gupta@email.com | sandeep123 | Data Scientist | Kolkata | ₹70k-84k |
| Riya Agarwal | riya.agarwal@email.com | riya123 | Frontend Developer | Pune | ₹50k-60k |
| Karan Mehta | karan.mehta@email.com | karan123 | Lawyer | Surat | ₹65k-78k |
| Pooja Nair | pooja.nair@email.com | pooja123 | Chef | Kochi | ₹35k-42k |
| Rohit Sharma | rohit.sharma@email.com | rohit123 | Sports Coach | Indore | ₹40k-48k |
| Yuvraj Pawar | yuvraj.pawar@email.com | yuvraj123 | Graphic Designer | Pune | ₹45k-54k |

##  Usage Guide

### 1. **Login**
- Enter your email and password
- Click "Login" to access your dashboard

### 2. **Dashboard**
- View your Financial Health Score and Credit Score
- Monitor key metrics and trends
- Review personalized recommendations

### 3. **Analysis**
- Deep dive into spending patterns
- Compare against ideal benchmarks
- Identify areas for improvement

### 4. **Predictions**
- See 5-year savings forecasts
- Understand risk levels
- Plan for future financial goals

### 5. **Goals**
- Set and track savings goals
- Calculate required SIP amounts
- Monitor progress with visual indicators

### 6. **What-If Simulator**
- Experiment with different spending scenarios
- See impact on savings and investments
- Plan lifestyle changes

### 7. **AI Advisor**
- Ask questions about your finances
- Get personalized advice
- Switch between languages

##  UI Features

- **Dark Theme**: Modern neon-green aesthetic
- **Responsive Design**: Works on desktop and mobile
- **Interactive Charts**: Hover effects and detailed tooltips
- **Multilingual Support**: English, Hindi, Marathi
- **Real-time Updates**: Dynamic calculations and visualizations

##  Scoring Methodology

### Financial Health Score (0-100)
- **Savings Rate** (40 pts): Monthly savings as % of income
- **Investment Habit** (25 pts): Investment spending ratio
- **Expense Control** (20 pts): Control over discretionary spending
- **Consistency** (15 pts): Stability of savings over time

### Credit Score (300-900)
- **Payment History** (35 pts): Consistency of debt payments
- **Credit Utilization** (30 pts): Debt-to-income ratio
- **Credit History** (15 pts): Length and stability of financial history
- **New Credit** (10 pts): Stability of borrowing patterns
- **Credit Mix** (10 pts): Diversity of financial activities

##  Customization

### Adding New Users
Edit the `USERS` dictionary in `app.py`:
```python
USERS["user16"] = {
    "name": "New User",
    "email": "new.user@email.com",
    "password": "password123",
    "role": "Profession",
    "city": "City",
    "emoji": "👤"
}
```

### Adding Transaction Data
Append to the `RAW_DATA` string in CSV format:
```
user16,1,2024,50000,6500,12000,2000,2400,1600,4000,800,400,3200,1400
```

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


##  Acknowledgments

- Built for Gen-Z financial empowerment
- Inspired by modern fintech applications
- Uses open-source libraries: Streamlit, Pandas, Plotly


**FinZen AI** - Your AI-powered financial companion for a brighter financial future! 🚀</content>
<parameter name="filePath">README.md
