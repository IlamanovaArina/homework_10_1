from unittest.mock import mock_open, patch

from src.home_13_1.reading_tabular import (reading_tables_csv,
                                           reading_tables_xlsx)

file_path_csv_ = (
    r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
    r"\homework_10_1\data\transactions.csv"
)
file_path_xlsx_ = (
    r"C:\Users\minac.DESKTOP-L51PJSH\PycharmProjects"
    r"\homework_10_1\data\transactions_excel.xlsx"
)


@patch("csv.DictReader")
def test_tabular_csv(example_csv_reader):
    """Тест на tabular_csv"""

    example_csv_reader.return_value = [{
        "column1": "value1",
        "column2": "value2"
    }]

    with patch("builtins.open", mock_open()) as file_mock_open:
        assert reading_tables_csv("random_test_file.csv") == [
            {"column1": "value1", "column2": "value2"}
        ]

        file_mock_open.assert_called()
        example_csv_reader.assert_called_with(file_mock_open(), delimiter=";")

        # example_csv_reader = < MagicMock name = 'DictReader'
        # id = '2144005849552' >


@patch("pandas.read_excel")
def test_reading_tables_xlsx(mock_read_excel):
    file_path_xlsx = "test.xlsx"
    expected_result = [{"c1": "v1", "c2": "v2"}, {"c1": "v3", "c2": "v4"}]

    # Моделируем чтение файла Excel и имитируем результат
    mock_read_excel.return_value.to_dict.return_value = expected_result

    assert reading_tables_xlsx(file_path_xlsx) == expected_result
    mock_read_excel.assert_called_with(file_path_xlsx)

    # mock_read_excel = < MagicMock name = 'read_excel' id = '1517065600800' >
