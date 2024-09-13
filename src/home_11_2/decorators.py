def log(filename=None):
    """
    Декоратор фиксирует выполнение кода, в командную
    строку если не указан файл для сохранения данных,
    выводит информацию об ошибках и исподьзуемых переменных
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename:
                try:
                    with open("mylog.txt", "a") as file_1:
                        file_1.write(f"{func.__name__} ok\n")
                        print(result)
                except Exception as e:
                    with open("mylog.txt", "a") as file_2:
                        file_2.write(f"{func.__name__} error: "
                                     f"{type(e).__name__}. "
                                     f"Inputs: {args}, {kwargs}")
            else:
                try:
                    print(f"{func.__name__} ok")
                except Exception as e:
                    print(f"{func.__name__} error: {type(e).__name__}. "
                          f"Inputs: {args}, {kwargs}")
                return result
        return wrapper
    return decorator
