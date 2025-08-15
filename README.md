# SGX Stock Screener Dashboard

A professional stock screening tool for Singapore Exchange (SGX) stocks, designed for investment analysis and educational purposes. Features real-time technical analysis, automated scoring, and an interactive dashboard perfect for both beginners and professionals.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## 📷 Dashboard Preview

### Main Dashboard Interface
![Main Dashboard](screenshots/main_dashboard.png)
*Interactive dashboard showing real-time SGX stock analysis with scoring system*
<img width="1917" height="1054" alt="image" src="https://github.com/user-attachments/assets/9b16785c-3519-4e6f-b2a6-ecb1ceb7fb33" />


### Stock Analysis Details
![Stock Analysis](screenshots/stock_analysis.png)
*Detailed breakdown of individual stock metrics and recommendations*
<img width="1539" height="709" alt="image" src="https://github.com/user-attachments/assets/a40c515f-514f-4f64-900c-edf8c0b17d6d" />


### Educational Sidebar
![Educational Features](screenshots/educational_sidebar.png)
*Built-in learning tools explaining technical indicators for beginners*
<img width="535" height="613" alt="image" src="https://github.com/user-attachments/assets/581c5625-acc1-410e-b74b-258c47f6e8d1" />


## 🎯 Project Overview

This project demonstrates practical application of:
- **Financial Data Analysis** using real-time market data
- **Technical Indicators** (RSI, Moving Averages, Momentum, Volume Analysis)
- **Risk Assessment** through volatility calculations
- **Interactive Web Dashboards** with Streamlit
- **Automated Investment Scoring** system
- **Professional Documentation** and code structure

## 🚀 Key Features

### 📊 Real-Time Analysis
- Live SGX stock data from Yahoo Finance API
- 10+ major Singapore stocks analyzed simultaneously
- Automatic data refresh capabilities
- 3-month historical data for trend analysis

### 🎯 Automated Scoring System
- **0-100 point scoring** based on multiple technical indicators
- **Color-coded recommendations**: Strong Buy, Consider, Weak, Avoid
- **Transparent methodology** with detailed explanations
- **Risk assessment** using annualized volatility

### 📈 Technical Indicators
- **RSI (Relative Strength Index)** - Momentum oscillator (14-period)
- **Moving Averages** - 20-day and 50-day trend analysis
- **Price Momentum** - 5D, 20D, and 50D performance tracking
- **Volume Analysis** - Trading interest measurement
- **Volatility Calculation** - Annualized risk assessment

## 📊 Sample Output

### Excel Report Format
The tool generates professional Excel reports with this structure:

| Company | Symbol | Price (SGD) | Score | RSI | 20D Momentum (%) | Risk Level | Recommendation |
|---------|--------|-------------|-------|-----|------------------|------------|----------------|
| DBS Group Holdings | D05.SI | $49.84 | 90 | 66.6 | 7.0% | Low Risk | 🟢 Strong Buy |
| OCBC Bank | O39.SI | $16.52 | 85 | 50.0 | 0.8% | Low Risk | 🟢 Strong Buy |
| Singtel | Z74.SI | $4.07 | 80 | 50.0 | 2.3% | Medium Risk | 🟡 Consider |

### Dashboard Metrics
- **Total Stocks Analyzed**: 10 stocks
- **Strong Opportunities**: 5 stocks (Score ≥ 80)
- **Stocks in Uptrend**: 6 stocks (60.0%)
- **Analysis Date**: Real-time with data timestamps

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Internet connection for real-time data

### Quick Start
```bash
# 1. Clone the repository
git clone https://github.com/yourusername/sgx-stock-screener.git
cd sgx-stock-screener

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit Dashboard
streamlit run streamlit_dashboard.py

# 4. Or run the command-line version
python sgx_screener.py
```

### Alternative Installation
```bash
# Install packages individually if requirements.txt fails
pip install yfinance pandas numpy streamlit plotly openpyxl
```

## 🎮 Usage Guide

### 🌐 Streamlit Dashboard
1. **Launch**: Run `streamlit run streamlit_dashboard.py`
2. **Access**: Browser automatically opens to `http://localhost:8501`
3. **Refresh Data**: Click "🔄 Refresh Data" for latest stock prices
4. **Filter Results**: Use sliders to filter by score and trend
5. **Learn**: Explore sidebar for detailed indicator explanations
6. **Analyze**: Click on individual stocks for detailed breakdowns

### 💻 Command-Line Tool
1. **Execute**: Run `python sgx_screener.py`
2. **Wait**: Analysis takes ~30 seconds for all stocks
3. **Review**: Check console output for top 5 recommendations
4. **Export**: Find generated Excel file in project directory

## 🏗️ Project Structure

```
sgx-stock-screener/
│
├── 📊 Core Application
│   ├── streamlit_dashboard.py    # Interactive web dashboard
│   └── sgx_screener.py          # Command-line stock screener
│
├── 📁 Configuration
│   ├── requirements.txt         # Python dependencies
│   ├── .gitignore              # Git ignore rules
│   └── .streamlit/
│       └── config.toml         # Streamlit configuration
│
├── 📖 Documentation
│   ├── README.md               # This file
│   └── screenshots/            # Dashboard images
│
└── 📈 Generated Output (excluded from Git)
    └── SGX_Stock_Screen_YYYYMMDD.xlsx
```

## 📈 Scoring Methodology

### Point Distribution System (Total: 100 points)
Our proprietary algorithm evaluates stocks across multiple technical dimensions:

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Price > 20-day MA** | +20 | Short-term uptrend confirmation |
| **Price > 50-day MA** | +20 | Long-term trend strength |
| **20-day > 50-day MA** | +15 | Building momentum signal |
| **Strong Returns (>5%)** | +20 | Exceptional 20-day performance |
| **Modest Returns (0-5%)** | +10 | Positive 20-day performance |
| **Healthy RSI (30-70)** | +15 | Balanced momentum indicator |
| **High Volume (>1.2x avg)** | +10 | Above-average market interest |

### Score Interpretation
- **🟢 80-100**: Exceptional opportunities with multiple strong signals
- **🟡 60-79**: Good prospects with several positive indicators  
- **🟠 40-59**: Fair options with some positive signals
- **🔴 20-39**: Weak choices with few positive indicators
- **⚫ 0-19**: Poor options with minimal positive signals

### Risk Assessment
Risk levels based on annualized volatility:
- **🟢 Low Risk**: <15% volatility (stable blue-chips)
- **🟡 Medium Risk**: 15-25% volatility (moderate growth)
- **🔴 High Risk**: >25% volatility (high growth/speculative)

## 🎯 Investment Philosophy & Use Cases

### Target Users
- **👨‍🎓 Student Investors** learning technical analysis
- **👩‍💼 Portfolio Managers** needing systematic screening tools
- **📊 Financial Analysts** requiring quick market overviews
- **🏫 Educators** teaching finance and data science concepts

### Analysis Approach
This tool implements **technical analysis** principles focusing on:
- **Trend identification** through moving averages
- **Momentum measurement** via RSI and price changes  
- **Volume confirmation** for signal validation
- **Risk quantification** through volatility metrics

## ⚠️ Important Disclaimers

**Investment Risk Notice:**
- 📊 This tool provides **technical analysis only**
- 📈 **Past performance does not guarantee future results**
- 🔍 Always conduct additional **fundamental analysis**
- 💰 **Never invest money you cannot afford to lose**
- 👨‍💼 Consider consulting a **qualified financial advisor**
- 🎓 This is an **educational/demonstration project**

**Data Limitations:**
- 15-minute delayed data from Yahoo Finance
- Technical analysis has inherent limitations
- Market conditions can change rapidly
- External factors not considered in scoring

## 🔧 Technical Implementation

### Data Pipeline
```
Yahoo Finance API → yfinance → pandas → Technical Indicators → Scoring Algorithm → Streamlit Dashboard
```

### Key Libraries
- **yfinance** (0.2.18+) - Financial data retrieval
- **pandas** (2.0.0+) - Data manipulation and analysis
- **numpy** (1.24.0+) - Numerical computations
- **streamlit** (1.28.0+) - Web dashboard framework
- **plotly** (5.15.0+) - Interactive visualizations
- **openpyxl** (3.1.0+) - Excel file generation

### Performance Metrics
- **Analysis Time**: ~30 seconds for 10 stocks
- **Memory Usage**: ~50MB for complete dataset
- **Update Frequency**: Manual refresh or daily auto-update
- **Browser Support**: Chrome, Firefox, Safari, Edge
