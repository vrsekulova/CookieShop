import employee


class Waiter(employee.Employee):
    def __init__(self, name: str, ID: str, start_date: str, tables: list[int]):
        super().__init__(name, ID, start_date)
        self.tables = tables
