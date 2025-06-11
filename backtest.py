import yfinance as yf

def backtest_strategy(ticker, strategy_func, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    results = []
    for S_T in data['Close']:
        pnl = strategy_func(S_T)
        results.append(pnl)
    return data.index, results