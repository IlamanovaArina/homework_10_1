from unittest.mock import mock_open, patch

from src.home_12_1.utils import change_json_file


@patch("os.path.exists")
@patch("json.load")
def test_get_transactions_valid_json(mocked_load, mock_os_path_exists):
    """
    Мок метод os.path.exists и функцию open()
    Проверяет, что если файл существует и содержит валидный JSON,
    возвращается список словарей с данными об операциях.
    """
    mock_os_path_exists.return_value = True  # задаём фальшивому
    # .exists что он возвращает True

    # тут вызываем встроенную в unittest функцию mock_open - она
    # вернёт то же, что и обычная open(), но
    # с фиксированным содержимым, которое мы задаём в read_data=
    m = mock_open()
    # мокаем встроенную функцию open() и передаём прошлый объект,
    # таким образом добиваемся того, что вся функция
    # работает со значениями в read_data
    with patch("builtins.open", m) as mocked_open:
        # в контексте мок объекта open вызываем тестируемую
        # функцию. json.dump уже мокать не нужно, так как
        # она уже будет работать с read_data
        mocked_load.return_value = [
            {"amount": "100", "currency": "RUB"},
            {"amount": "200", "currency": "USD"},
        ]
        assert change_json_file("operations.json") == [
            {"amount": "100", "currency": "RUB"},
            {"amount": "200", "currency": "USD"},
        ]
        # проверяем что мок функция open() была вызвана
        # с нужными параметрами и не была вызвана реальная
        mocked_open.assert_called_with("operations.json", "r",
                                       encoding="utf-8")
