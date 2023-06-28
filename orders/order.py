import cookies.types


class Order:
    def __init__(self, order_ID: str, order: list[cookies.types.Cookie]):
        self.order_ID = order_ID
        self.order = order

    def order_price(self):
        price = 0
        for cookie in self.order:
            price += cookie.price
        return f"Вашата поръчка е на стойност {price} лв."
