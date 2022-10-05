from unittest import TestCase
from unittest.mock import patch
from models.Quote import Quote
from services.StockPriceService import StockPriceService


class TestStockPriceService(TestCase):

    @patch('services.StockPriceService.StockPriceService.get_most_volatile_stock',
           return_value=Quote("TEST1", 1, 1, 1, 1, 1, 1, 1))
    def test_get_most_volatile_stock(self, mock_get_most_volatile_stock):
        sps = StockPriceService()
        self.assertEqual(sps.get_most_volatile_stock(["TEST1", "TEST2"]).symbol, "TEST1")
