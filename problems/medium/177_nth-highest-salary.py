class _ScalarWrapper:
    def __init__(self, value):
        self._value = value

    def item(self):
        return self._value


class _ILocAccessor:
    def __init__(self, df):
        self._df = df

    def __getitem__(self, key):
        row_idx, col_idx = key
        return _ScalarWrapper(self._df._rows[row_idx][col_idx])


class DataFrame:
    def __init__(self, data=None, columns=None):
        self.columns = list(columns) if columns is not None else []
        self._rows = []

        if data is None:
            return

        if isinstance(data, dict):
            self.columns = list(data.keys())
            values = [data[col] for col in self.columns]
            row_count = len(values[0]) if values else 0
            for i in range(row_count):
                self._rows.append([values[j][i] for j in range(len(self.columns))])
        else:
            if columns is None:
                raise ValueError("columns must be provided for row-based data")
            for row in data:
                self._rows.append(list(row))

    def __len__(self):
        return len(self._rows)

    @property
    def iloc(self):
        return _ILocAccessor(self)


class _PandasCompat:
    DataFrame = DataFrame

    @staticmethod
    def isna(value):
        return value is None


pd = _PandasCompat()


def nth_highest_salary(employee: DataFrame, N: int) -> DataFrame:
    col = f"getNthHighestSalary({N})"
    if N <= 0:
        return pd.DataFrame({col: [None]})

    salary_idx = employee.columns.index("Salary")
    distinct_salaries = sorted({row[salary_idx] for row in employee._rows}, reverse=True)

    if len(distinct_salaries) < N:
        return pd.DataFrame({col: [None]})

    return pd.DataFrame({col: [distinct_salaries[N - 1]]})


class Solution:
    def nth_highest_salary(self, employee: DataFrame, N: int) -> DataFrame:
        return nth_highest_salary(employee, N)

    def getNthHighestSalary(self, employee: DataFrame, N: int) -> DataFrame:
        return nth_highest_salary(employee, N)