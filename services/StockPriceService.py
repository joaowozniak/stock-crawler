from math import inf
from utils.Utils import Utils
from utils.Constants import Constants
from models.Quote import Quote


class StockPriceService:

    def get_most_volatile_stock(self, stocks: list) -> Quote:
        print("Requesting stock prices...")
        most_volatile_stock = Quote("", 0, -inf, -inf, 0, 0, 0, 0)
        for stock in stocks:
            current_stock = self.__get_latest_price(stock)
            print("Stock price of: ", stock, " - ", current_stock.pc_change)

            if current_stock.pc_change > most_volatile_stock.pc_change:
                most_volatile_stock = current_stock
                print("Updating most volatile stock to: ", stock)

        return most_volatile_stock

    @staticmethod
    def __get_latest_price(ticker: str) -> Quote:
        response = Utils.execute_get_request(Constants.FINNHUB_BASE_URL + Constants.STOCK_ENDPOINT + ticker).json()
        if response:
            return Quote(ticker, response["c"], response["d"], response["dp"], response["h"], response["l"],
                         response["o"], response["pc"])
