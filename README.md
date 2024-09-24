# Сортировка данных
## Логирование
Логирование, на данном этапе осуществляется только у некоторых функций,
запись логов осуществляется в `logs.log` файл в корне проекта.
Логирование происходит в формате: [дата и время] [модуль] [функция] 
[уровень логирования] - [сообщение]

## Описание основных функций
### Функции для сортировки данных
Данное прилоение сортирует данные, такие как state и date.
Может выполнить сортировку по state, 
проверить, соответствует ли эти данный требуемым

```filter_by_state
def filter_by_state(data, state='EXECUTED'):
    pass
    
data = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

И сотртровать по date(дате) по возростанию или по убыванию

```sort_by_date
def sort_by_date(data, sort_by=False):
    pass

data = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]
>>> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

### Функции для маскировки данных по картам
Предоставленные функции призваны для маскировки 
части номера карты:

```get_mask_card_number
def get_mask_card_number(card_number):
    pass

card_number = "7000792289606361"
>>> "7000 79** **** 6361"
```
Или счёта:

```get_mask_account
def get_mask_account(card_number):
    pass
    
card_number = "73654108430135874305"
>>> "**4305"
```

### Функции выводящие замаскированные данные карты пользователя
С помощью уже имеющихся функций для маскировки номера карт,
а так же выводим данные к какому типу карта или счёт принадлежит

```mask_account_card
def mask_account_card(bank_card):
    pass
    
bank_card = "Visa Platinum 7000792289606361"
>>> "Visa Platinum 7000 79** **** 6361"
```

Функция возвращающая "ДД.ММ.ГГГГ" из строки
такого образца "2024-03-11T02:26:18.671407"

```get_date
def get_date(dat):
    pass
    
dat = "2024-03-11T02:26:18.671407"
>>> "11.03.2024"
```

### Фнкция фильтрует транзакции по заданной валюте

```
def filter_by_currency(list_transactions, currency):
    pass
    
list_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }, ...]
    
 currency = "USD"
 
>>> {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
```

### Функция выводящяя банковские операции

```
def transaction_descriptions(list_transactions):
    pass

list_transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }, ...]
    
>>> Перевод организации
```

### """Функция сгенерирующая номера карт в заданном диапазоне

Функция может сгенерировать номера карт в заданном диапазоне 
от 0000 0000 0000 0001 до 9999 9999 9999 9999

```card_number_generator
def card_number_generator(start, stop):
    pass
    
start = "0000 0000 0000 0001"
stop = "0000 0000 0000 0002"

>>>"0000 0000 0000 0001"
```

## Декораторы

### Декоратор `log`

Декоратор `log` фиксирует выполнение кода, 
в командную строку если не указан файл для 
сохранения данных, выводит информацию об ошибках, если они есть
и исподьзуемых переменных
Простой пример использования:


```@log()
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)

>>> "my_function ok"
```

## Тестирование
К каждой функции добавленны тесты с использованием 
фикстуры и параметризации

### `test_masks`
Пример теста к маскировке даннных по карте:

```test_masks
def test_masks():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    with pytest.raises(TypeError):
        assert get_mask_card_number() == ""
```

### `test_filter_by_state`
Тест сортировки данных в виде списка словарей по ключу "state"

```test_filter_by_state
@pytest.mark.parametrize(
    "data, state, expected_output", [...])
def test_filter_by_state(data, state, expected_output):
    assert filter_by_state(data, state) == expected_output
```
### `test_sort_by_date`
тест сортировки данных в виде списка словарей по дате,
с указанием по возростанию или по убыванию 

```test_sort_by_date
@pytest.mark.parametrize(
    "data, sort_by, expected_output", [...]
def test_sort_by_date(data, sort_by, expected_output):
    assert sort_by_date(data, sort_by) == expected_output
```

### `test_widget_mask_account_card`
Тест маскировки данных карты и счёта
```
def test_widget_mask_account_card():
    assert (
        mask_account_card("Visa Platinum 7000792289606361")
        == "Visa Platinum 7000 79** **** 6361"
    )
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card(700079223) == ""
```

### `test_widget_get_date`
Тест вывода даты 

```test_widget_get_date
def test_widget_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == ""
    assert get_date("11-03-2024") == "11.03.2024"
```

### `@log()`
Тестирование логирования, если `filename=None` не указан,
логи выводятся на консоль 

```@log()
@log()
def my_function(x, y):
    return int(x) + int(y)

my_function(3, 2)
def test_log_none(capsys):
    log(my_function(3, 2))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
```
А с указанием `filename="mylog.txt"`,
данные записываются в указанных вайл

```@log(filename="mylog.txt")
@log(filename="mylog.txt")
def my_function(x, y):
    return int(x) + int(y)

my_function(1, 2)

def test_log(capsys):
    log(my_function(1, 2))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
```
