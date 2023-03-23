import statistics
from typing import List, Protocol
from exchange import Exchange


class TradingStrategy(Protocol):
    """Trading strategy that decides whether to buy or sell, given a list of prices."""

    def should_buy(self, prices: List[int]) -> bool:
        raise NotImplementedError()

    def should_sell(self, prices: List[int]) -> bool:
        raise NotImplementedError()


class AverageTradingStrategy:
    """Trading strategy based on price averages."""

    def should_buy(self, prices: List[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: List[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)