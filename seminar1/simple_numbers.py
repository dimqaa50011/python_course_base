# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
from math import sqrt
from typing import Union


def is_simple(number: int) -> Union[bool, None]:
    result = True
    if number == 1:
        return None

    for digit in range(2, round(sqrt(number))):
        if number % digit == 0:
            result = False
            break

    return result


def check_number(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError(f"{number} не является числом")

    if number < 0 or number > 10 ** 5 - 1:
        raise ValueError(f"число {number} должно быть положительным и меньше 100 тысяч")

    return True


def print_result(number: int):
    if check_number(number):
        result = is_simple(number)
        if result:
            answer = "Число простое"
        elif result is None:
            answer = "Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1."
        else:
            answer = "Число составное"
    else:
        answer = "Число должно быть положительным, но меньше 100000"
    print(answer)


def get_int_number(number: str):
    try:
        number = int(number)
        return number
    except ValueError:
        raise ValueError(f"{number} не является чилом")


def start_task2():
    repeat = True
    while repeat:
        user_answer = input("Введите целое число: ").strip()
        try:
            user_answer = get_int_number(user_answer)
            print_result(user_answer)
            repeat = False
        except ValueError as ex:
            print(ex)
