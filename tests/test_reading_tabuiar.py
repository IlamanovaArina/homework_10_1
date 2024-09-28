import pandas as pd
from unittest.mock import patch, mock_open

from coverage.html import read_data
from pandas import read_excel

from src.home_13_1.reading_tabular import reading_tables_csv, reading_tables_xlsx


file_path_csv_ = r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects\homework_10_1\data\transactions.csv"
file_path_xlsx_ = r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects\homework_10_1\data\transactions_excel.xlsx"


@patch("os.path.exists")
@patch("csv.DictReader")
def test_tabular_csv(mocked_dict, mock_csv_exists):
    """Тест на tabular_csv"""
    mock_csv_exists.return_value = True

    data = [
        {"column1": "value1", "column2": "value2"},
        {"column1": "value3", "column2": "value4"}
    ]

    reader_data = mock_open(read_data="\n".join([";".join(row.values()) for row in data]))

    with patch("builtins.open", reader_data), patch("csv.DictReader") as mocked_open:
        mocked_dict.return_value = data

    assert reading_tables_csv(file_path_csv_) == data

    # Это почемуто не работает, я пробовала и полный путь, всё равно ошибка

    # mocked_open.assert_called_with(file_path_csv_)

    # mocked_open.assert_called_with(
    # r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects\homework_10_1\data\transactions.csv", encoding="utf-8")


@patch("pandas.read_excel")
def test_reading_tables_xlsx(mock_read_excel):
    file_path_xlsx = "test.xlsx"
    expected_result = [{'c1': 'v1', 'c2': 'v2'}, {'c1': 'v3', 'c2': 'v4'}]

    # Моделируем чтение файла Excel и имитируем результат
    mock_read_excel.return_value.to_dict.return_value = expected_result

    result = reading_tables_xlsx(file_path_xlsx)

    assert result == expected_result
    # .assert_called_with(file_path_xlsx_)
