from src.home_11_2.decorators import log
import pytest


@log(filename="mylog.txt")
def my_function(x, y):
    return int(x) + int(y)


def test_log():
    result = my_function(1, 2)
    assert result == 3

    with open("mylog.txt", "r") as file:
        open_file = file.read()
        assert "my_function ok" in open_file

    my_function("a")

    with open("mylog.txt", "r") as file:
        open_file = file.read()
        assert "my_function error: TypeError" in open_file

