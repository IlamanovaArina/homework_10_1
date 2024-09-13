# Сортировка данных
## Описание
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

```def filter_by_currency(list_transactions, currency):
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

```def transaction_descriptions(list_transactions):
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

```def card_number_generator(start, stop):
    pass
    
start = "0000 0000 0000 0001"
stop = "0000 0000 0000 0002"

>>>"0000 0000 0000 0001"
```


## Тестирование
К каждой функции добавленны тесты с использованием 
фикстуры и параметризации

Пример теста к маскировке даннных по карте:

```test_masks
def test_masks():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("7000") == "7000"
    assert get_mask_card_number("7000123456789123456789") == "7000 12** **** 9123 4567 89"
    assert get_mask_card_number("пробуем буквы") == ""
    assert get_mask_card_number("") == ""
    assert get_mask_card_number(7000792289606361) == ""
    with pytest.raises(TypeError):
        assert get_mask_card_number() == ""
```
