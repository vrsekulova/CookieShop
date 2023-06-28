import employee


class Waiter(employee.Employee):
    def __init__(self, name, ID, start_date):
        super().__init__(name, ID, start_date)
