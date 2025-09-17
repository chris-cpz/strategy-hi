#!/usr/bin/env python3
"""
hi - Momentum, trend_following, breakout Trading Strategy

Strategy Type: momentum, trend_following, breakout
Description: hihi
Created: 2025-09-17T07:17:59.797Z

WARNING: This is a template implementation. Thoroughly backtest before live trading.
"""

import os
import sys
import logging
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('strategy.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class hiStrategy:
    """
    hi Implementation
    
    Strategy Type: momentum, trend_following, breakout
    Risk Level: Monitor drawdowns and position sizes carefully
    """
    
    def __init__(self, config=None):
        self.config = config or self.get_default_config()
        self.positions = {}
        self.performance_metrics = {}
        logger.info(f"Initialized hi strategy")
        
    def get_default_config(self):
        """Default configuration parameters"""
        return {
            'max_position_size': 0.05,  # 5% max position size
            'stop_loss_pct': 0.05,      # 5% stop loss
            'lookback_period': 20,       # 20-day lookback
            'rebalance_freq': 'daily',   # Rebalancing frequency
            'transaction_costs': 0.001,  # 0.1% transaction costs
        }
    
    def load_data(self, symbols, start_date, end_date):
        """Load market data for analysis"""
        try:
            import yfinance as yf
            data = yf.download(symbols, start=start_date, end=end_date)
            logger.info(f"Loaded data for {len(symbols)} symbols")
            return data
        except Exception as e:
            logger.error(f"Error loading data: {e}")
            return None

# =============================================================================
# USER'S STRATEGY IMPLEMENTATION
# =============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TradingStrategy:
    def __init__(self, data, short_window=20, long_window=50, risk_per_trade=0.01):
        self.data = data
        self.short_window = short_window
        self.long_window = long_window
        self.risk_per_trade = risk_per_trade
        self.signals = pd.DataFrame(index=self.data.index)
        self.position = None

    def generate_signals(self):
        self.signals['short_mavg'] = self.data['Close'].rolling(window=self.short_window, min_periods=1).mean()
        self.signals['long_mavg'] = self.data['Close'].rolling(window=self.long_window, min_periods=1).mean()
        self.signals['signal'] = 0
        self.signals['signal'][self.short_window:] = np.where(self.signals['short_mavg'][self.short_window:] > self.signals['long_mavg'][self.short_window:], 1, 0)
        self.signals['positions'] = self.signals['signal'].diff()

    def risk_management(self, current_price):
        if self.position is None:
            self.position = self.risk_per_trade * 10000 / current_price

    def backtest(self):
        self.generate_signals()
        self.data['Portfolio_Value'] = 10000
        for i in range(1, len(self.data)):
            if self.signals['positions'].iloc[i] == 1:
                self.risk_management(self.data['Close'].iloc[i])
                self.data['Portfolio_Value'].iloc[i] = self.data['Portfolio_Value'].iloc[i-1] + (self.position * (self.data['Close'].iloc[i] - self.data['Close'].iloc[i-1]))
            elif self.signals['positions'].iloc[i] == -1:
                self.data['Portfolio_Value'].iloc[i] = self.data['Portfolio_Value'].iloc[i-1] - (self.position * (self.data['Close'].iloc[i] - self.data['Close'].iloc[i-1]))
            else:
                self.data['Portfolio_Value'].iloc[i] = self.data['Portfolio_Value'].iloc[i-1]

    def calculate_performance_metrics(self):
        returns = self.data['Portfolio_Value'].pct_change()
        sharpe_ratio = np.mean(returns) / np.std(returns) * np.sqrt(252)
        max_drawdown = (self.data['Portfolio_Value'].cummax() - self.data['Portfolio_Value']).max()
        return sharpe_ratio, max_drawdown

def generate_sample_data():
    dates = pd.date_range(start='2020-01-01', end='2020-12-31', freq='B')
    prices = np.random.normal(loc=100, scale=10, size=len(dates)).cumsum()
    return pd.DataFrame(data={'Close': prices}, index=dates)

if __name__ == "__main__":
    try:
        sample_data = generate_sample_data()
        strategy = TradingStrategy(data=sample_data)
        strategy.backtest()
        sharpe_ratio, max_drawdown = strategy.calculate_performance_metrics()
        print("Sharpe Ratio: %s" % sharpe_ratio)
        print("Max Drawdown: %s" % max_drawdown)
        plt.plot(strategy.data['Portfolio_Value'])
        plt.title('Portfolio Value Over Time')
        plt.show()
    except Exception as e:
        print("Error: %s" % str(e))

# =============================================================================
# STRATEGY EXECUTION AND TESTING
# =============================================================================

if __name__ == "__main__":
    # Example usage and testing
    strategy = hiStrategy()
    print(f"Strategy '{strategyName}' initialized successfully!")
    
    # Example data loading
    symbols = ['SPY', 'QQQ', 'IWM']
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    
    print(f"Loading data for symbols: {symbols}")
    data = strategy.load_data(symbols, start_date, end_date)
    
    if data is not None:
        print(f"Data loaded successfully. Shape: {data.shape}")
        print("Strategy ready for backtesting!")
    else:
        print("Failed to load data. Check your internet connection.")
