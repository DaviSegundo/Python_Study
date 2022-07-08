class Application:
    trading_strategy: str

    def __init__(self, trading_strategy) -> None:
        self.trading_strategy = trading_strategy

    def __connect(self):
        print(f"Connecting to Crypto exchange")

    def get_market_data(self, coin):
        return [10, 12, 18, 14]

    def list_average(self, l):
        return sum(l) / len(l)

    def should_buy(self, prices):
        if self.trading_strategy == 'minmax':
            return prices[-1] == min(prices)
        else:
            return prices[-1] < self.list_average(prices)

    def should_sell(self, prices):
        if self.trading_strategy == 'minmax':
            return prices[-1] == max(prices)
        else:
            return prices[-1] > self.list_average(prices)

    def check_prices(self, coin):
        self.__connect()
        prices = self.get_market_data(coin=coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")


if __name__ == '__main__':
    app = Application("average")
    app.check_prices("BTC/USD")
