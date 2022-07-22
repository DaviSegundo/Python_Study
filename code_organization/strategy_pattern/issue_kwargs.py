"""
Simple module that simulates an exchange.
"""

from abc import ABC, abstractmethod
import statistics
from typing import List


class ExchangeConnectionError(Exception):
    """Custom error that is raised when an exchange is not connected."""


class Exchange:
    """Basic exchange simulator."""

    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> None:
        """Connect to the exchange."""
        print("Connecting to Crypto exchange...")
        self.connected = True

    def check_connection(self) -> None:
        """Check if the exchange is connected."""
        if not self.connected:
            raise ExchangeConnectionError()

    def get_market_data(self, symbol: str) -> List[float]:
        self.check_connection()

        price_data = {
            "BTC/USD" : [35842.0, 34069.0, 33871.0, 34209.0],
            "ETH/USD" : [2381.0, 2233.0, 2300.0, 2342.0],
        }

        return price_data[symbol]

    def buy(self, symbol: str, amount: float) -> None:
        """Simulate buying an amount of a given symbol at the current price."""
        self.check_connection()
        print(f"Buying amount {amount} in market {symbol}.")

    def sell(self, symbol: str, amount: float) -> None:
        """Simulate selling an amount of a given symbol at the current price."""
        self.check_connection()
        print(f"Selling amount {amount} in market {symbol}.")


class TradingStrategy(ABC):
    """Trading strategy that decides whether to buy or sell, given a list of prices."""

    @abstractmethod
    def should_buy(self, prices: List[float], **kwargs: float) -> bool:
        """Whether you should buy this coin, given the prices."""

    @abstractmethod
    def should_sell(self, prices: List[float], **kwargs: float) -> bool:
        """Whether you should sell this coin, given the prices."""


class AverageTradingStrategy(TradingStrategy):
    """Trading strategy based on price averages."""

    def should_buy(self, prices: List[float], **kwargs: float) -> bool:
        window_size = kwargs.get("window_size", 3.0)
        list_window = prices[-window_size:]
        return prices[-1] < statistics.mean(list_window)
    
    def should_sell(self, prices: List[float], **kwargs: float) -> bool:
        window_size = kwargs.get("window_size", 3.0)
        list_window = prices[-window_size:]
        return prices[-1] > statistics.mean(list_window)


class MinMaxTradingStrategy(TradingStrategy):
    """Trading strategy based on price minima and maxima."""

    def should_buy(self, prices: List[float], **kwargs: float) -> bool:
        return prices[-1] < kwargs.get("min_price", 32000.0)
    
    def should_sell(self, prices: List[float], **kwargs: float) -> bool:
        return prices[-1] > kwargs.get("max_price", 33000.0)


class TradingBot:
    """Trading bot that connects to a crypto exchange and performs trades."""

    def __init__(self, exchange: Exchange, trading_strategy: TradingStrategy) -> None:
        self.exchange = exchange
        self.trading_strategy = trading_strategy

    def run(self, symbol: str) -> None:
        """Run the trading bot once for a particular symbol, with a given strategy."""
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)
        if should_buy:
            self.exchange.buy(symbol, 4)
        elif should_sell:
            self.exchange.sell(symbol, 4)
        else:
            print(f"No action needed for {symbol}.")


def main():
    """
    Create an exchange and a trading bot with a strategy.
    Run the stategy once on a particular symbol.
    """

    # create the exchange and connect to it
    exchange = Exchange()
    exchange.connect()

    # create the trading strategy
    trading_strategy = MinMaxTradingStrategy()

    # create the trading bot and run the bot once
    bot = TradingBot(exchange, trading_strategy)
    bot.run("BTC/USD")


if __name__ == '__main__':
    main()