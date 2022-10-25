import requests
from Utils.dateUtils import DateUtils


@staticmethod
def get_stock_data(stock_ticker, interval=60):
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock_ticker + '&interval=' + str(
        interval) + 'min&apikey=X266B0IXMXQ7IN5J'
    r = requests.get(url)
    data = r.json()
    return data


stock_data = get_stock_data('Goog', interval=60)


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker
        self.last_refresh_date_time = self.get_last_refresh_date_time(stock_data)
        self.historical_prices = self.get_historical_prices(stock_data)
        self.current_price = self.get_current_price(self.last_refresh_date_time, self.historical_prices)
        self.purchase_date_time = self.get_purchase_date_time(self.historical_prices)
        self.purchase_price = self.get_purchase_price(self.historical_prices, self.purchase_date_time)
        self.profit = self.get_profit(self.purchase_price, self.current_price)

    @staticmethod
    def get_last_refresh_date_time(stock_data_last_refresh):
        last_refresh_date_time = stock_data_last_refresh['Meta Data']['3. Last Refreshed']
        return last_refresh_date_time

    @staticmethod
    def get_historical_prices(data):
        historical_prices = data['Time Series (60min)']
        return historical_prices

    @staticmethod
    def get_current_price(last_refresh_date_time, historical_prices):
        price_for_date_time = historical_prices[last_refresh_date_time]
        current_price = float(price_for_date_time['4. close'])
        return current_price

    @staticmethod
    def get_purchase_date_time(historical_prices):
        current_date = DateUtils.get_current_date()

        purchase_date_time = min(historical_prices.keys(),
                                 key=lambda x: abs(current_date - DateUtils.convert_string_to_date_time(x)))
        return purchase_date_time

    @staticmethod
    def get_purchase_price(historical_prices, purchase_date_time):
        purchase_price = float(historical_prices[purchase_date_time]['4. close'])
        return purchase_price

    @staticmethod
    def get_profit(purchase_price, current_price):
        return purchase_price - current_price
