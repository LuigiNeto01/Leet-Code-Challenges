class _SeriesILoc:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, idx):
        return self._data[idx]


class Series:
    def __init__(self, data):
        self._data = list(data)
        self.iloc = _SeriesILoc(self._data)

    def drop_duplicates(self):
        seen = set()
        result = []
        for value in self._data:
            if value not in seen:
                seen.add(value)
                result.append(value)
        return Series(result)

    def sort_values(self, ascending=True):
        return Series(sorted(self._data, reverse=not ascending))

    def __len__(self):
        return len(self._data)


class _Row:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]


class _DataFrameILoc:
    def __init__(self, df):
        self._df = df

    def __getitem__(self, idx):
        return _Row(self._df._rows[idx])


class DataFrame:
    def __init__(self, data=None, columns=None):
        self._rows = []
        if isinstance(data, dict):
            self.columns = list(data.keys())
            lengths = [len(v) for v in data.values()] if data else [0]
            size = lengths[0] if lengths else 0
            for i in range(size):
                row = {}
                for col in self.columns:
                    row[col] = data[col][i]
                self._rows.append(row)
        else:
            self.columns = list(columns or [])
            for row_values in data or []:
                row = {}
                for i, col in enumerate(self.columns):
                    row[col] = row_values[i]
                self._rows.append(row)
        self.iloc = _DataFrameILoc(self)

    def astype(self, _types):
        return self

    def __getitem__(self, key):
        return Series(row[key] for row in self._rows)

    def __len__(self):
        return len(self._rows)


class _MiniPandas:
    DataFrame = DataFrame

    @staticmethod
    def isna(value):
        return value is None


pd = _MiniPandas()


def second_highest_salary(employee):
    salaries = []
    seen = set()
    for row in employee._rows:
        salary = row["salary"]
        if salary not in seen:
            seen.add(salary)
            salaries.append(salary)

    if len(salaries) < 2:
        return pd.DataFrame({"SecondHighestSalary": [None]})

    salaries.sort(reverse=True)
    return pd.DataFrame({"SecondHighestSalary": [salaries[1]]})


class Solution:
    def secondHighestSalary(self, employee):
        return second_highest_salary(employee)

    def second_highest_salary(self, employee):
        return second_highest_salary(employee)