class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        for i in range(len(names)):
            self.tables[names[i]] = {
                "columns": columns[i],
                "data": {},
                "next_id": 1
            }

    def insertRow(self, name: str, row: List[str]) -> None:
        table = self.tables[name]
        row_id = table["next_id"]
        table["data"][row_id] = row
        table["next_id"] += 1

    def deleteRow(self, name: str, rowId: int) -> None:
        table = self.tables[name]
        if rowId in table["data"]:
            del table["data"][rowId]

    def selectRow(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables[name]
        return table["data"][rowId][columnId - 1]