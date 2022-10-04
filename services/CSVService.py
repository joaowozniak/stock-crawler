import csv
import os
from datetime import datetime
from models.Quote import Quote
from utils.Constants import Constants


class CSVService:

    def write_to_csv(self, stock_data_obj: Quote) -> None:
        stock_data_list = [stock_data_obj.symbol, stock_data_obj.pc_change, stock_data_obj.current_price,
                           stock_data_obj.close_price]

        path = self.__get_output_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)

        print("Writing most volatile stock to CSV: ", path)

        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(Constants.CSV_HEADERS)
            writer.writerow(stock_data_list)

    @staticmethod
    def __get_output_path():
        folder = "stock_data/"
        csv_filename = f"most_volatile_stock_{datetime.timestamp(datetime.now())}.csv"
        path = folder + csv_filename

        return path
