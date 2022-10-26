import requests
from Utils.dateUtils import DateUtils
import Loading_data


class Stock:
    def __init__(self):
        data, interval = Loading_data.input_ticker(4)
        self.ticker = self.get_ticker(data)
        self.last_refresh_date_time = self.get_last_refresh_date_time(data)
        self.historical_prices = self.get_historical_prices(data, interval)
        self.current_price = self.get_current_price()
        self.purchase_date_time = self.parse_purchase_date_time()
        self.purchase_price = self.get_purchase_price()
        self.profit = self.get_profit()


    def get_ticker(self, data):
        return data['Meta Data']['2. Symbol']
    # @staticmethod
    # def get_stock_data(ticker, interval=60):
    #     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=' + str(
    #         interval) + 'min&apikey=X266B0IXMXQ7IN5J'
    #     r = requests.get(url)
    #     data = r.json()
    #     return data

    def get_last_refresh_date_time(self, stock_data_last_refresh):
        self.last_refresh_date_time = stock_data_last_refresh['Meta Data']['3. Last Refreshed']
        return self.last_refresh_date_time

    def get_historical_prices(self, data, interval):
        self.historical_prices = data[f'Time Series ({interval}min)']
        return self.historical_prices

    def get_current_price(self):
        price_for_date_time = self.historical_prices[self.last_refresh_date_time]
        self.current_price = float(price_for_date_time['4. close'])
        return self.current_price

    def parse_purchase_date_time(self):
        current_date = DateUtils.get_current_date()

        purchase_date_time_adjusted = min(self.historical_prices.keys(),
                                          key=lambda x: abs(current_date - DateUtils.convert_string_to_date_time(x)))
        return purchase_date_time_adjusted

    def get_purchase_price(self):
        purchase_price = float(self.historical_prices[self.purchase_date_time]['4. close'])
        return purchase_price

    def get_profit(self):
        self.profit = self.current_price - self.purchase_price
        return self.profit

    def __str__(self):
        return f'{self.ticker}'

    def __repr__(self):
        return f'{self.ticker}'
