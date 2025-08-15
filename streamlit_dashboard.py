# SGX Stock Screening Dashboard for Investment Beginners
# Run with: streamlit run streamlit_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time

# Configure page
st.set_page_config(
    page_title="SGX Stock Screener - Investment Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
.metric-card {
    background-color: #f0f2f6;
    padding: 10px;
    border-radius: 10px;
    margin: 5px 0;
}
.good-score {
    color: #28a745;
    font-weight: bold;
}
.neutral-score {
    color: #ffc107;
    font-weight: bold;
}
.poor-score {
    color: #dc3545;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Helper Functions
@st.cache_data(ttl=None, show_spinner=False)  # Cache until manually cleared or date changes
def load_stock_data():
    """Load the latest stock screening data"""
    # Check if we need to refresh based on date
    today = datetime.now().strftime("%Y-%m-%d")
    
    # SGX stocks dictionary
    sgx_stocks = {
        'DBS Group Holdings': 'D05.SI',
        'OCBC Bank': 'O39.SI',
        'United Overseas Bank': 'U11.SI',
        'Singapore Airlines': 'C6L.SI',
        'Singtel': 'Z74.SI',
        'CapitaLand Investment': '9CI.SI',
        'Wilmar International': 'F34.SI',
        'Genting Singapore': 'G13.SI',
        'City Developments': 'C09.SI',
        'Keppel Corp': 'BN4.SI'
    }
    
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Track the actual data date range
    data_start_date = None
    data_end_date = None
    
    for i, (name, symbol) in enumerate(sgx_stocks.items()):
        status_text.text(f'Loading {name}...')
        try:
            stock = yf.download(symbol, period="3mo", progress=False)
            if not stock.empty and len(stock) >= 20:
                
                # Track actual data dates
                if data_start_date is None:
                    data_start_date = stock.index[0].strftime("%Y-%m-%d")
                    data_end_date = stock.index[-1].strftime("%Y-%m-%d")
                
                # Simple calculations
                current_price = float(stock['Close'].iloc[-1])
                ma20 = float(stock['Close'].rolling(20).mean().iloc[-1])
                ma50 = float(stock['Close'].rolling(50).mean().iloc[-1])
                
                # Momentum calculations
                mom_5d = ((current_price / float(stock['Close'].iloc[-5])) - 1) * 100 if len(stock) >= 5 else 0
                mom_20d = ((current_price / float(stock['Close'].iloc[-20])) - 1) * 100 if len(stock) >= 20 else 0
                
                # Calculate volatility (for risk assessment)
                daily_returns = stock['Close'].pct_change().dropna()
                volatility = daily_returns.std() * np.sqrt(252) * 100  # Annualized volatility %
                
                # RSI calculation
                delta = stock['Close'].diff()
                gain = delta.where(delta > 0, 0).rolling(14).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
                rs = gain / loss
                rsi = float((100 - (100 / (1 + rs))).iloc[-1])
                
                # Volume analysis
                avg_volume = float(stock['Volume'].rolling(20).mean().iloc[-1])
                current_volume = float(stock['Volume'].iloc[-1])
                volume_ratio = current_volume / avg_volume if avg_volume > 0 else 1
                
                # Better scoring system - start from 0
                score = 0  # No base score - earn points only for positive signals
                if current_price > ma20: score += 20  # Strong signal
                if current_price > ma50: score += 20  # Strong signal  
                if ma20 > ma50: score += 15  # Building momentum
                if mom_20d > 5: score += 20  # Strong recent gains
                elif mom_20d > 0: score += 10  # Modest gains
                if 30 <= rsi <= 70: score += 15  # Healthy RSI
                if volume_ratio > 1.2: score += 10  # Above average interest
                
                results.append({
                    'Company': name,
                    'Symbol': symbol,
                    'Price': current_price,
                    'Score': min(score, 100),
                    'RSI': rsi,
                    'Momentum_5D': mom_5d,
                    'Momentum_20D': mom_20d,
                    'MA20': ma20,
                    'MA50': ma50,
                    'Above_MA20': current_price > ma20,
                    'Above_MA50': current_price > ma50,
                    'Volume_Ratio': volume_ratio,
                    'Volatility': volatility,  # Add volatility for risk calculation
                    'Trend': 'Uptrend' if (current_price > ma20 and ma20 > ma50) else 'Downtrend',
                    'Data_Start': data_start_date,
                    'Data_End': data_end_date
                })
        except:
            pass
        
        progress_bar.progress((i + 1) / len(sgx_stocks))
    
    status_text.text('Data loaded successfully!')
    progress_bar.empty()
    status_text.empty()
    
    df = pd.DataFrame(results)
    return df.sort_values('Score', ascending=False) if not df.empty else pd.DataFrame()

def get_score_color(score):
    """Return color based on score"""
    if score >= 75:
        return "good-score"
    elif score >= 60:
        return "neutral-score"
    else:
        return "poor-score"

def explain_indicator(indicator_name):
    """Provide simple explanations for indicators"""
    explanations = {
        'RSI': """
        **RSI (Relative Strength Index)**
        - Measures if a stock is overbought or oversold
        - Range: 0-100
        - 30-70: Healthy range
        - Below 30: Potentially undervalued (might go up)
        - Above 70: Potentially overvalued (might go down)
        """,
        'Momentum': """
        **Momentum**
        - Shows how much the stock price has changed
        - Positive %: Price went up
        - Negative %: Price went down
        - Higher positive momentum = stronger upward trend
        """,
        'Moving Average': """
        **Moving Average (MA)**
        - Average price over the last 20 or 50 days
        - If current price > MA: Stock is trending up
        - If current price < MA: Stock is trending down
        - MA20 > MA50: Short-term trend is stronger than long-term
        """,
        'Volume Ratio': """
        **Volume Ratio**
        - Compares today's trading volume to average
        - Ratio > 1.5: High interest (many people buying/selling)
        - Ratio < 0.5: Low interest
        - High volume + positive momentum = strong buy signal
        """,
        'Risk Level': """
        **Risk Level Calculation**
        - Based on **annualized volatility** (how much the stock price fluctuates)
        - **Low Risk (<15% volatility):** Stable, predictable price movements
        - **Medium Risk (15-25%):** Moderate price swings
        - **High Risk (>25%):** Large, unpredictable price movements
        
        *Formula: Standard deviation of daily returns × √252 trading days*
        """
    }
    return explanations.get(indicator_name, "No explanation available.")

# Main Dashboard
def main():
    st.title("📈 SGX Stock Screening Dashboard")
    st.markdown("## Investment Analysis Made Simple - Perfect for Beginners!")
    
    st.markdown("""
    This dashboard analyzes Singapore Exchange (SGX) stocks using technical indicators to help identify potential investment opportunities.
    All data is **real-time** from Yahoo Finance!
    """)
    
    # Load data
    st.markdown("---")
    
    if st.button("🔄 Refresh Data", type="primary"):
        st.cache_data.clear()
    
    with st.spinner("Loading latest stock data..."):
        df = load_stock_data()
    
    if df.empty:
        st.error("Unable to load stock data. Please check your internet connection and try again.")
        return
    
    # Display data date information
    if not df.empty:
        data_info = df.iloc[0]
        st.info(f"""
        📅 **Data Coverage:** {data_info['Data_Start']} to {data_info['Data_End']} 
        📊 **Analysis Date:** {datetime.now().strftime("%Y-%m-%d %H:%M")} SGT
        📈 **Data Source:** Yahoo Finance (Real-time SGX prices)
        """)
    
    st.success(f"✅ Successfully loaded data for {len(df)} stocks!")
    
    # Sidebar with explanations
    with st.sidebar:
        st.header("📚 Learn the Basics")
        
        st.markdown("### What is Stock Screening?")
        st.info("""
        Stock screening helps investors filter through hundreds of stocks to find the most promising ones based on specific criteria like price trends, momentum, and trading volume.
        """)
        
        indicator = st.selectbox(
            "Learn about indicators:",
            ['RSI', 'Momentum', 'Moving Average', 'Volume Ratio', 'Risk Level']
        )
        st.markdown(explain_indicator(indicator))
    
    # Main content area
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total Stocks Analyzed",
            value=len(df)
        )
    
    with col2:
        top_performers = len(df[df['Score'] >= 80])
        st.metric(
            label="Strong Opportunities",
            value=f"{top_performers} stocks",
            delta=f"Score ≥ 80"
        )
    
    with col3:
        uptrend_stocks = len(df[df['Trend'] == 'Uptrend'])
        st.metric(
            label="Stocks in Uptrend",
            value=f"{uptrend_stocks} stocks",
            delta=f"{uptrend_stocks/len(df)*100:.1f}%"
        )
    
    # Top Opportunities Section
    st.markdown("---")
    st.header("🏆 Top Investment Opportunities")
    
    top_5 = df.head(5)
    
    for i, (_, stock) in enumerate(top_5.iterrows()):
        with st.expander(f"#{i+1} {stock['Company']} - Score: {stock['Score']}/100", expanded=(i==0)):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Current Price", f"${stock['Price']:.2f}")
                st.metric("Trend", stock['Trend'])
            
            with col2:
                momentum_color = "🟢" if stock['Momentum_20D'] > 0 else "🔴"
                st.metric("20-Day Return", f"{stock['Momentum_20D']:.1f}%", delta=momentum_color)
                st.metric("5-Day Return", f"{stock['Momentum_5D']:.1f}%")
            
            with col3:
                rsi_status = "Neutral" if 30 <= stock['RSI'] <= 70 else ("Overbought" if stock['RSI'] > 70 else "Oversold")
                st.metric("RSI", f"{stock['RSI']:.1f}", delta=rsi_status)
                st.metric("Volume Activity", f"{stock['Volume_Ratio']:.1f}x")
            
            with col4:
                # Simple buy/hold/avoid recommendation
                if stock['Score'] >= 80 and stock['Momentum_20D'] > 0:
                    recommendation = "🟢 Strong Buy"
                elif stock['Score'] >= 60:
                    recommendation = "🟡 Consider"
                elif stock['Score'] >= 40:
                    recommendation = "🟠 Weak"
                else:
                    recommendation = "🔴 Avoid"
                
                st.metric("Recommendation", recommendation)
                
                # Risk level based on volatility (annualized %)
                volatility = float(stock['Volatility'])
                if volatility < 15:
                    risk = "🟢 Low Risk"
                    risk_explanation = f"({volatility:.1f}% annual volatility)"
                elif volatility < 25:
                    risk = "🟡 Medium Risk"
                    risk_explanation = f"({volatility:.1f}% annual volatility)"
                else:
                    risk = "🔴 High Risk"
                    risk_explanation = f"({volatility:.1f}% annual volatility)"
                    
                st.metric("Risk Level", risk)
                st.caption(risk_explanation)
    
    # Detailed Analysis Section
    st.markdown("---")
    st.header("📊 Detailed Stock Analysis")
    
    # Interactive filters
    col1, col2 = st.columns(2)
    with col1:
        min_score = st.slider("Minimum Score", 0, 100, 50)
    with col2:
        trend_filter = st.selectbox("Trend Filter", ["All", "Uptrend", "Downtrend"])
    
    # Filter data
    filtered_df = df[df['Score'] >= min_score]
    if trend_filter != "All":
        filtered_df = filtered_df[filtered_df['Trend'] == trend_filter]
    
    # Display filtered data
    if not filtered_df.empty:
        st.subheader(f"Showing {len(filtered_df)} stocks matching your criteria:")
        
        # Create display dataframe
        display_df = filtered_df[['Company', 'Price', 'Score', 'Momentum_20D', 'RSI', 'Trend']].copy()
        display_df.columns = ['Company', 'Price (SGD)', 'Score', '20D Return (%)', 'RSI', 'Trend']
        display_df['Price (SGD)'] = display_df['Price (SGD)'].round(2)
        display_df['20D Return (%)'] = display_df['20D Return (%)'].round(1)
        display_df['RSI'] = display_df['RSI'].round(1)
        
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("No stocks match your criteria. Try adjusting the filters.")
    
    # How Scoring Works Section
    st.markdown("---")
    st.header("🎯 How We Score Stocks")
    
    st.info(f"""
    **Our scoring system (0-100 points) - Updated {datetime.now().strftime("%Y-%m-%d")}:**
    
    📊 **No Base Score** - Stocks must earn every point!
    
    📈 **How Points Are Earned:**
    - **+20 points:** Price above 20-day average (short-term uptrend)
    - **+20 points:** Price above 50-day average (long-term uptrend)
    - **+15 points:** 20-day average > 50-day average (building momentum)
    - **+20 points:** Strong gains (>5% in 20 days)
    - **+10 points:** Modest gains (0-5% in 20 days)
    - **+15 points:** Healthy RSI (30-70 range)
    - **+10 points:** High trading volume (above average interest)
    
    **Score Interpretation:**
    - **80-100:** Exceptional - Multiple strong signals
    - **60-79:** Good - Several positive indicators
    - **40-59:** Fair - Some positive signals
    - **20-39:** Weak - Few positive indicators  
    - **0-19:** Poor - Very few or no positive signals
    """)
    
    # Show example calculation
    if not df.empty:
        example_stock = df.iloc[0]
        with st.expander("📋 Example: How we calculated the score for " + example_stock['Company']):
            score_breakdown = []
            total_score = 0
            
            if example_stock['Above_MA20']:
                score_breakdown.append("✅ +20 points: Price above 20-day average")
                total_score += 20
            else:
                score_breakdown.append("❌ +0 points: Price below 20-day average")
                
            if example_stock['Above_MA50']:
                score_breakdown.append("✅ +20 points: Price above 50-day average")
                total_score += 20
            else:
                score_breakdown.append("❌ +0 points: Price below 50-day average")
                
            if example_stock['MA20'] > example_stock['MA50']:
                score_breakdown.append("✅ +15 points: 20-day MA > 50-day MA")
                total_score += 15
            else:
                score_breakdown.append("❌ +0 points: 20-day MA < 50-day MA")
                
            if example_stock['Momentum_20D'] > 5:
                score_breakdown.append("✅ +20 points: Strong 20-day gains (>5%)")
                total_score += 20
            elif example_stock['Momentum_20D'] > 0:
                score_breakdown.append("✅ +10 points: Modest 20-day gains (0-5%)")
                total_score += 10
            else:
                score_breakdown.append("❌ +0 points: Negative 20-day momentum")
                
            if 30 <= example_stock['RSI'] <= 70:
                score_breakdown.append("✅ +15 points: Healthy RSI")
                total_score += 15
            else:
                score_breakdown.append("❌ +0 points: RSI outside healthy range")
                
            if example_stock['Volume_Ratio'] > 1.2:
                score_breakdown.append("✅ +10 points: High trading volume")
                total_score += 10
            else:
                score_breakdown.append("❌ +0 points: Normal/low trading volume")
            
            for item in score_breakdown:
                st.write(item)
            
            st.write(f"**Calculated Total: {total_score}/100**")
            st.write(f"**Actual Score: {example_stock['Score']}/100**")
    
    # Educational Footer
    st.markdown("---")
    st.markdown("### 💡 Investment Tips for Beginners")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **Before You Invest:**
        - Always do your own research
        - Never invest money you can't afford to lose
        - Consider your risk tolerance
        - Diversify your portfolio
        """)
    
    with col2:
        st.warning("""
        **Remember:**
        - This tool provides technical analysis only
        - Past performance doesn't guarantee future results
        - Consider fundamental analysis too
        - Consult a financial advisor for major decisions
        """)
    
    st.markdown("---")
    st.caption("Data source: Yahoo Finance")

if __name__ == "__main__":
    main()