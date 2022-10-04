class Quote:
    def __init__(self, symbol, current_price, change, pc_change, high_price_day, low_price_day, open_price,
                 close_price):
        self.symbol = symbol
        self.current_price = current_price
        self.change = change
        self.pc_change = pc_change
        self.high_price_day = high_price_day
        self.low_price_day = low_price_day
        self.open_price = open_price
        self.close_price = close_price
