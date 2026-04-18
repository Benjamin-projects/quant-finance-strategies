import numpy as np

TRADING_DAYS = 252

def calculate_returns(data):
    data = data.copy()
    data["Returns"] = np.log(data["Close"]).diff()
    return data

def volatility(returns, annualize=True):
    # Calculate the volatility of returns
    returns = returns.dropna()
    vol = returns.std()
    if annualize:
        vol *= np.sqrt(TRADING_DAYS)
    return vol

def sharpe_ratio(returns, risk_free_rate = 0.0, annualize=True):
    # Calculate the Sharpe Ratio
    returns = returns.dropna()
    daily_rf = risk_free_rate / TRADING_DAYS
    sharpe = (returns.mean() - daily_rf) / returns.std()
    if annualize:
        sharpe *= np.sqrt(TRADING_DAYS)
    return sharpe

def sortino_ratio(returns, risk_free_rate = 0.0, annualize=True):
    # Calculate the Sortino Ratio
    returns = returns.dropna()
    daily_rf = risk_free_rate / TRADING_DAYS
    downside_returns = returns[returns < daily_rf]
    downside_deviation = downside_returns.std()

    if downside_deviation == 0 or np.isnan(downside_deviation):
        return np.nan

    sortino = (returns.mean() - daily_rf) / downside_deviation
    if annualize:
        sortino *= np.sqrt(TRADING_DAYS)
    return sortino

def display_annualized_ratios(returns, risk_free_rate = 0.0):
    print("Annualized Ratios:")
    print(f"Volatility: {volatility(returns, annualize=True):.4f}")
    print(f"Sharpe Ratio: {sharpe_ratio(returns, risk_free_rate, annualize=True):.4f}")
    print(f"Sortino Ratio: {sortino_ratio(returns, risk_free_rate, annualize=True):.4f}")

def display_daily_ratios(returns, risk_free_rate = 0.0):
    print("Daily Ratios:")
    print(f"Volatility: {volatility(returns, annualize=False):.4f}")
    print(f"Sharpe Ratio: {sharpe_ratio(returns, risk_free_rate, annualize=False):.4f}")
    print(f"Sortino Ratio: {sortino_ratio(returns, risk_free_rate, annualize=False):.4f}")

def drawdown(returns):
    pass

def max_drawdown(returns):
    pass


