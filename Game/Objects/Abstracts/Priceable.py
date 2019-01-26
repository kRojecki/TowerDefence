class Priceable:

    _price = 0

    def get_price(self):
        return self._price

    def get_sell_price(self):
        return int(self._price/2)
