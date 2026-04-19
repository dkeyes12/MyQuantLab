# MyQuantLab

MyQuantLab is a collection of quantitative trading strategies implemented in Python. These strategies span across various methodologies, including options trading, statistical arbitrage, and trend following.

## Prerequisites

To run and backtest these strategies, you will need active accounts with the following platforms:
* **[Alpaca](https://alpaca.markets/)**: Used for the options strategies and API-based order execution (e.g., Covered Calls, Options Wheel).
* **[QuantConnect](https://www.quantconnect.com/)**: Used for backtesting and execution of the equity strategies (Mean Reversion, Pairs Trading, Trend Following).

## Strategies Included

### Covered Calls (`CoveredCalls.py`)
A script to execute a basic covered call strategy using the Alpaca Trading API. It demonstrates submitting a limit order to purchase an underlying asset (SPY) and subsequently selling a call option against the position.

### Mean Reversion (`MeanReversion.py`)
A QuantConnect algorithm implementing an RSI-based mean reversion strategy for SPY. It shorts the asset when the 14-period RSI exceeds 70 (overbought) and covers the short position when the RSI drops below 50.

### Pairs Trading (`PairsTrading.py`)
A statistical arbitrage strategy built for QuantConnect. It trades a pair of highly correlated assets (PEP and KO) by calculating the Z-score of their price spread. It shorts the outperforming asset and goes long the underperforming asset when the spread diverges significantly (Z-score > 2), and liquidates when the spread reverts to the mean.

### Trend Following (`TrendFollowing.py`)
A "Death Cross" short strategy implemented in QuantConnect. It utilizes 50-day and 200-day Simple Moving Averages (SMAs). It enters a short position when the fast SMA crosses below the slow SMA (downtrend confirmed) and covers the position when the trend reverses.

### Options Wheel Strategy (`options-wheel-strategy.ipynb` / `OptionsWheel.ipynb`)
Jupyter notebooks containing the research and implementation of the Options Wheel strategy using the `alpaca-py` library. This income-generating strategy involves systematically selling cash-secured puts to acquire stock, and then selling covered calls on the acquired stock.