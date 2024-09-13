from src.home_11_2.decorators import log


@log(filename="mylog.txt")
def my_function(x, y):
    return int(x) + int(y)


my_function(1, 2)


def test_log(capsys):
    log(my_function(1, 2))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


@log()
def my_function(x, y):
    return int(x) + int(y)


my_function(3, 2)


def test_log_none(capsys):
    log(my_function(3, 2))
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
