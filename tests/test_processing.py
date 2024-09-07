import pytest
from src.home_10_1.processing import filter_by_state, sort_by_date

@pytest.mark.parametrize("data, state, expected_output", [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 615064552, 'state': 'canceled', 'date': '2018-10-14T08:21:33.4194452'},
            {'id': 615064552, 'state': 'executed', 'date': '2018-10-14T08:21:33.419452'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'},
            {'state': 'EXECUTED'},
            {}
        ],
        "EXECUTED",
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'state': 'EXECUTED'}
        ]
    ),
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 615064552, 'state': 'canceled', 'date': '2018-10-14T08:21:33.4194452'},
            {'id': 615064552, 'state': 'executed', 'date': '2018-10-14T08:21:33.419452'},
            {'id': 615064591, 'date': '2018-10-14T08:21:33.419441'},
            {}
        ],
        "CANCELED",
        [
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]
    )
])
def test_filter_by_state(data, state, expected_output):
    assert filter_by_state(data, state) == expected_output


@pytest.mark.parametrize("data, sort_by, expected_output", [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2015-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2016-07-03T18:35:29.512364'},
            {'id': 615064552, 'state': 'canceled', 'date': '2017-07-03T18:35:29.512364'},
            {'id': 615064552, 'state': 'executed', 'date': '2014-07-03T18:35:29.512364'},
            {'date': '2012-07-03', 'id': 939718560, 'state': 'EXECUTED'},
            {'id': 615064591, 'date': '2013-07-03T18:35:29.512364'},
            {'state': 'EXECUTED'},
            {}
        ],
        False,
        [
            {'date': '2012-07-03', 'id': 939718560, 'state': 'EXECUTED'},
            {'date': '2013-07-03T18:35:29.512364', 'id': 615064591},
            {'date': '2014-07-03T18:35:29.512364', 'id': 615064552, 'state': 'executed'},
            {'date': '2015-07-03T18:35:29.512364', 'id': 594226727, 'state': 'CANCELED'},
            {'date': '2016-07-03T18:35:29.512364', 'id': 615064591, 'state': 'CANCELED'},
            {'date': '2017-07-03T18:35:29.512364', 'id': 615064552, 'state': 'canceled'},
            {'date': '2018-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
            {'date': '2019-07-03T18:35:29.512364', 'id': 939719570, 'state': 'EXECUTED'}
        ]
    ),
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2018-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2015-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2016-07-03T18:35:29.512364'},
            {'id': 615064552, 'state': 'canceled', 'date': '2017-07-03T18:35:29.512364'},
            {'id': 615064552, 'state': 'executed', 'date': '2014-07-03T18:35:29.512364'},
            {'id': 615064591, 'date': '2013-07-03T18:35:29.512364'},
            {'state': 'EXECUTED'},
            {'id': 939718560, 'state': 'EXECUTED', 'date': '2012-07-03'},
            {}
        ],
        True,
        [
            {'date': '2019-07-03T18:35:29.512364', 'id': 939719570, 'state': 'EXECUTED'},
            {'date': '2018-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
            {'date': '2017-07-03T18:35:29.512364', 'id': 615064552, 'state': 'canceled'},
            {'date': '2016-07-03T18:35:29.512364', 'id': 615064591, 'state': 'CANCELED'},
            {'date': '2015-07-03T18:35:29.512364', 'id': 594226727, 'state': 'CANCELED'},
            {'date': '2014-07-03T18:35:29.512364', 'id': 615064552, 'state': 'executed'},
            {'date': '2013-07-03T18:35:29.512364', 'id': 615064591},
            {'date': '2012-07-03', 'id': 939718560, 'state': 'EXECUTED'}
        ]
    )
])
def test_sort_by_date(data, sort_by, expected_output):
    assert sort_by_date(data, sort_by) == expected_output
