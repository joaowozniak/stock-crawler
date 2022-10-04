from utils.Constants import Constants
from services.StockPriceService import StockPriceService
from services.CSVService import CSVService


def main():
    sps = StockPriceService()
    csv = CSVService()
    print("Calculating most volatile stock price...")
    csv.write_to_csv(sps.get_most_volatile_stock(Constants.TECH_STOCKS))
    print("Program finished OK!")


if __name__ == "__main__":
    main()
