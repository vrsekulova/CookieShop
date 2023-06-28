import orders.order


class Customer:
    def __init__(self, table_number: int, order: orders.order.Order):
        self.table_number = table_number
        self.order = order
        self.price = order.order_price()
