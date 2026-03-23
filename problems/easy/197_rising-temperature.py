from datetime import datetime, timedelta


class Series:
    def __init__(self, data):
        self._data = list(data)

    def tolist(self):
        return list(self._data)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class DataFrame:
    def __init__(self, rows=None, columns=None):
        self.columns = list(columns or [])
        self._data = {col: [] for col in self.columns}
        if rows:
            for row in rows:
                for col, value in zip(self.columns, row):
                    self._data[col].append(value)

    def __getitem__(self, key):
        if isinstance(key, str):
            return Series(self._data[key])
        if isinstance(key, list):
            rows = []
            size = len(self)
            for i in range(size):
                rows.append([self._data[col][i] for col in key])
            return DataFrame(rows, key)
        raise TypeError("Unsupported key type")

    def __setitem__(self, key, value):
        if isinstance(value, Series):
            value = value.tolist()
        self._data[key] = list(value)
        if key not in self.columns:
            self.columns.append(key)

    def __len__(self):
        if not self.columns:
            return 0
        return len(self._data[self.columns[0]])


class MiniPandas:
    @staticmethod
    def DataFrame(rows=None, columns=None):
        return DataFrame(rows, columns)

    @staticmethod
    def to_datetime(values):
        result = []
        for value in values:
            if isinstance(value, datetime):
                result.append(value.date())
            elif hasattr(value, "year") and hasattr(value, "month") and hasattr(value, "day"):
                result.append(value)
            else:
                result.append(datetime.strptime(value, "%Y-%m-%d").date())
        return result


pd = MiniPandas()


class Solution:
    def risingTemperature(self, weather):
        records = []
        n = len(weather)
        for i in range(n):
            records.append(
                {
                    "id": weather._data["id"][i],
                    "recordDate": weather._data["recordDate"][i],
                    "temperature": weather._data["temperature"][i],
                }
            )

        temp_by_date = {row["recordDate"]: row["temperature"] for row in records}
        result_rows = []

        for row in records:
            prev_date = row["recordDate"] - timedelta(days=1)
            if prev_date in temp_by_date and row["temperature"] > temp_by_date[prev_date]:
                result_rows.append([row["id"]])

        return DataFrame(result_rows, ["id"])

    def rising_temperature(self, weather):
        return self.risingTemperature(weather)