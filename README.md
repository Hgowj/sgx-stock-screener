# SGX Stock Screener Dashboard

A stock screening tool for Singapore Exchange (SGX) stocks. This application provides real-time technical analysis and investment recommendations for beginners and professionals.

![Dashboard Preview](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)

## 🎯 Project Overview

This project demonstrates practical application of:
- **Financial Data Analysis** using real-time market data
- **Technical Indicators** (RSI, Moving Averages, Momentum, Volume Analysis)
- **Risk Assessment** through volatility calculations
- **Interactive Dashboards** with Streamlit
- **Automated Scoring System** for investment opportunities

## 🚀 Features

### Core Functionality
- **Real-time SGX Stock Data** from Yahoo Finance API
- **Technical Analysis** with 5+ indicators
- **Automated Scoring System** (0-100 points)
- **Risk Assessment** based on annualized volatility
- **Interactive Dashboard** for investment beginners
- **Excel Report Generation** for professional use

### Technical Indicators
- **RSI (Relative Strength Index)** - Momentum oscillator
- **Moving Averages** (20-day, 50-day) - Trend analysis
- **Price Momentum** (5D, 20D, 50D) - Performance tracking
- **Volume Analysis** - Market interest measurement
- **Volatility Calculation** - Risk assessment

### Investment Recommendations
- **🟢 Strong Buy** - Score ≥80 with positive momentum
- **🟡 Consider** - Score 60-79 with decent signals
- **🟠 Weak** - Score 40-59 with mixed signals
- **🔴 Avoid** - Score <40 with poor indicators

## 📊 Dashboard Screenshots

### Main Dashboard
- Real-time stock analysis for 10+ major SGX stocks
- Interactive filtering and sorting capabilities
- Educational sidebar with indicator explanations

### Key Metrics Display
- Total stocks analyzed
- Strong opportunities count
- Uptrend percentage
- Individual stock breakdowns

## 🛠️ Installation & Setup

### Prerequisites
```bash
Python 3.10 or higher
pip (Python package manager)
```

### Quick Start
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/sgx-stock-screener.git
cd sgx-stock-screener
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Streamlit Dashboard**
```bash
streamlit run streamlit_dashboard.py
```

4. **Run the Command-line Screener**
```bash
python sgx_screener.py
```

### Alternative Installation
```bash
# Install packages individually if requirements.txt fails
pip install yfinance pandas numpy streamlit plotly openpyxl
```

## 🎮 Usage Guide

### Streamlit Dashboard
1. **Launch**: Run `streamlit run streamlit_dashboard.py`
2. **Access**: Open browser to `http://localhost:8501`
3. **Refresh Data**: Click "🔄 Refresh Data" for latest prices
4. **Filter Stocks**: Use sliders to filter by score and trend
5. **Learn**: Check sidebar for indicator explanations

### Command-line Tool
1. **Run**: Execute `python sgx_screener.py`
2. **Output**: Check generated Excel file with rankings
3. **Analysis**: Review top 5 stock recommendations in console

## 🏗️ Project Structure

```
sgx-stock-screener/
│
├── streamlit_dashboard.py    # Interactive web dashboard
├── sgx_screener.py          # Command-line stock screener
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── .gitignore             # Git ignore rules
│
├── output/                # Generated reports (auto-created)
│   └── SGX_Stock_Screen_YYYYMMDD.xlsx
│
└── .streamlit/           # Streamlit configuration (optional)
    └── config.toml
```

## 📈 Scoring Methodology

Our proprietary scoring system evaluates stocks on multiple criteria:

### Point Distribution (Total: 100 points)
- **Price vs 20-day MA** (+20 points) - Short-term trend
- **Price vs 50-day MA** (+20 points) - Long-term trend  
- **MA Momentum** (+15 points) - 20-day > 50-day average
- **Strong Returns** (+20 points) - >5% gain in 20 days
- **Modest Returns** (+10 points) - 0-5% gain in 20 days
- **Healthy RSI** (+15 points) - RSI between 30-70
- **High Volume** (+10 points) - Above average trading volume

### Interpretation
- **80-100**: Exceptional opportunities with multiple strong signals
- **60-79**: Good prospects with several positive indicators
- **40-59**: Fair options with some positive signals
- **20-39**: Weak choices with few positive indicators
- **0-19**: Poor options with minimal positive signals

## 🎯 Investment Philosophy

This tool implements **technical analysis** principles suitable for:
- **Beginner Investors** learning market analysis
- **Portfolio Managers** seeking systematic screening
- **Financial Analysts** requiring quick market overviews
- **Educational Purposes** in finance and data science

## ⚠️ Risk Disclaimer

**Important Investment Notice:**
- This tool provides **technical analysis only**
- **Past performance doesn't guarantee future results**
- Always conduct additional **fundamental analysis**
- **Never invest money you cannot afford to lose**
- Consider consulting a **qualified financial advisor**
- This is an **educational/demonstration project**

## 🔧 Technical Details

### Data Sources
- **Yahoo Finance API** via `yfinance` library
- **Real-time SGX stock prices** (15-minute delay)
- **3-month historical data** for technical calculations

### Libraries Used
- **yfinance** - Financial data retrieval
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **streamlit** - Web dashboard framework
- **plotly** - Interactive visualizations
- **openpyxl** - Excel file generation

### Performance
- **Analysis Time**: ~30 seconds for 10 stocks
- **Data Refresh**: Manual trigger or daily auto-refresh
- **Memory Usage**: ~50MB for typical dataset
- **Browser Support**: Chrome, Firefox, Safari, Edge

### Development Setup
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

*This project demonstrates practical application of financial analysis, data science, and software development skills in a real-world investment context.*
