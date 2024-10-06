def log(filename=None):
    """
    Декоратор фиксирует выполнение кода, в командную
    строку если не указан файл для сохранения данных,
    выводит информацию об ошибках и исподьзуемых переменных
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename:
                try:
                    with open("mylog.txt", "a") as file:
                        result = func(*args, **kwargs)
                        file.write(f"{func.__name__} ok\n")
                        return result
                except Exception as e:
                    with open("mylog.txt", "a") as file:
                        file.write(
                            f"{func.__name__} error: "
                            f"{type(e).__name__}. "
                            f"Inputs: {args}, {kwargs}\n"
                        )
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func.__name__} ok\n")
                    return result, "1"
                except Exception as e:
                    print(
                        f"{func.__name__} error: {type(e).__name__}. "
                        f"Inputs: {args}, {kwargs}\n"
                    )

        return wrapper

    return decorator
