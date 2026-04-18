from AlgorithmImports import *

class RSIMeanReversionShort(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        
        # Subscribe to SPY data at a daily resolution
        self.symbol = self.AddEquity("SPY", Resolution.Daily).Symbol
        
        # Initialize a 14-period RSI
        self.rsi = self.RSI(self.symbol, 14, MovingAverageType.Simple, Resolution.Daily)
        
        # Warm up the engine to pre-calculate the RSI
        self.SetWarmUp(14)

    def OnData(self, data):
        # Ensure we have data and the indicator is ready
        if not self.rsi.IsReady or not data.ContainsKey(self.symbol):
            return

        current_rsi = self.rsi.Current.Value

        # Entry logic: If RSI > 70 and we are not already short
        if current_rsi > 70 and not self.Portfolio[self.symbol].IsShort:
            self.SetHoldings(self.symbol, -1) # Allocate 100% of portfolio to short SPY
            self.Debug(f"Shorting SPY at RSI: {current_rsi}")

        # Exit logic: If RSI drops back below 50, buy to cover
        elif current_rsi < 50 and self.Portfolio[self.symbol].IsShort:
            self.Liquidate(self.symbol)
            self.Debug(f"Covering SPY at RSI: {current_rsi}")