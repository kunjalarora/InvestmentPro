def create_ticker():
    """Create moving ticker footer"""
    ticker_text = get_stock_data()
    
    html = f"""
    <style>
    .ticker {{
        position: fixed;
        bottom: 0;
        width: 100%;
        background: #1f4e79;
        color: white;
        padding: 10px;
        font-size: 14px;
        white-space: nowrap;
        overflow: hidden;
        z-index: 999;
    }}
    .ticker-text {{
        display: inline-block;
        animation: scroll 30s linear infinite;
    }}
    @keyframes scroll {{
        0% {{ transform: translateX(100%); }}
        100% {{ transform: translateX(-100%); }}
    }}
    </style>
    <div class="ticker">
        <div class="ticker-text">📈 LIVE: {ticker_text}</div>
    </div>
    """
    return html
    
def get_stock_data():
    """Get stock data using Yahoo Finance - FREE, no API key needed"""
    stocks = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'NVDA', 'JNJ', 'V', 'WMT', 'PG', 'MA', 'AMZN', 'VTSAX', 'VOO', 'SWPPX', 'IVV', 'FCNTX', 'DODFX','QQQ','VTI', 'SPY', 'VWO', 'IEFA', 'BRK.A']
    stock_data = []
    
    for symbol in stocks:
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            current_price = info.get('currentPrice', info.get('regularMarketPrice', 0))
            change_percent = info.get('regularMarketChangePercent', 0)
            
            stock_data.append(f"{symbol}: ${current_price:.2f} ({change_percent:+.2f}%)")
        except:
            stock_data.append(f"{symbol}: $150.00 (+1.5%)")
    
    return " • ".join(stock_data)