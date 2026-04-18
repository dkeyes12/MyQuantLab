from AlgorithmImports import *
import numpy as np

class PairsTradingShortStatArb(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 1, 1)
        self.SetCash(100000)
        
        # Two highly correlated assets
        self.asset1 = self.AddEquity("PEP", Resolution.Daily).Symbol
        self.asset2 = self.AddEquity("KO", Resolution.Daily).Symbol
        
        self.lookback = 21
        self.z_threshold = 2.0

    def OnData(self, data):
        # Ensure we have data for both assets today
        if not data.ContainsKey(self.asset1) or not data.ContainsKey(self.asset2):
            return

        # Fetch the last 21 days of historical close prices for both assets
        history = self.History([self.asset1, self.asset2], self.lookback, Resolution.Daily)
        
        if history.empty or len(history.unstack(level=0)) < self.lookback:
            return

        # Unstack the dataframe to easily access 'close' prices
        closes = history['close'].unstack(level=0)
        
        # Calculate the spread (Asset1 - Asset2)
        spread = closes[self.asset1] - closes[self.asset2]
        
        # Calculate Mean, Standard Deviation, and current Z-Score
        spread_mean = np.mean(spread)
        spread_std = np.std(spread)
        current_spread = spread.iloc[-1]
        
        z_score = (current_spread - spread_mean) / spread_std

        # Entry: If Z-score > 2, PEP has diverged higher than KO. 
        # We short PEP and go long KO.
        if z_score > self.z_threshold and not self.Portfolio[self.asset1].IsShort:
            # Allocate 50% short to PEP, 50% long to KO to remain market neutral
            self.SetHoldings(self.asset1, -0.5) 
            self.SetHoldings(self.asset2, 0.5)
            self.Debug(f"Spread diverged (Z: {z_score:.2f}). Short PEP, Long KO.")

        # Exit: Reversion to the mean. Close all positions if Z-score drops back to 0 or below.
        elif z_score <= 0 and self.Portfolio[self.asset1].IsShort:
            self.Liquidate()
            self.Debug(f"Spread reverted (Z: {z_score:.2f}). Liquidating positions.")