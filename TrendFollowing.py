from AlgorithmImports import *

class DeathCrossShort(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        
        # Initialize 50-day and 200-day SMAs
        self.fast_sma = self.SMA(self.symbol, 50, Resolution.Daily)
        self.slow_sma = self.SMA(self.symbol, 200, Resolution.Daily)
        
        # Warm up for the longest indicator
        self.SetWarmUp(200)

    def OnData(self, data):
        if not self.slow_sma.IsReady or not data.ContainsKey(self.symbol):
            return

        fast = self.fast_sma.Current.Value
        slow = self.slow_sma.Current.Value

        # Entry: Fast SMA crosses below Slow SMA (Downtrend confirmed)
        if fast < slow and not self.Portfolio[self.symbol].IsShort:
            self.SetHoldings(self.symbol, -1)
            self.Debug("Death Cross triggered. Going Short.")

        # Exit: Fast SMA crosses back above Slow SMA (Downtrend over)
        elif fast > slow and self.Portfolio[self.symbol].IsShort:
            self.Liquidate(self.symbol)
            self.Debug("Trend reversed. Covering Short.")