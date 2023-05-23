# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки
from dataclasses import dataclass
from random import randint


@dataclass
class Status:
    status: bool
    message: str


@dataclass
class Data:
    less: Status
    more: Status
    equals: Status


class GuessingGame:
    def __init__(self, attempts: int):
        self._attempts = attempts
        self._number = self._think_of_a_number()

    @staticmethod
    def _get_default_data() -> Data:
        return Data(
            less=Status(status=False, message="Мое число меньше"),
            more=Status(status=False, message="Мое число больше"),
            equals=Status(status=False, message="Ты угадал!)")
        )

    @staticmethod
    def _think_of_a_number(left_border: int = 0, right_border: int = 10 ** 3):
        return randint(left_border, right_border)

    def _check(self, user_number: int) -> Data:
        data = self._get_default_data()

        if user_number > self._number:
            data.less.status = True
        elif user_number < self._number:
            data.more.status = True
        else:
            data.equals.status = True

        return data

    def _process_game(self, user_number: int) -> bool:
        result = False
        data = self._check(user_number)
        if data.less.status:
            msg = data.less.message
        elif data.more.status:
            msg = data.more.message
        else:
            msg = data.equals.message
            result = True
        print(msg)

        return result

    def run(self):
        print(self._number)
        user_attempts = 0
        print(f"Я загадал число от 0 до 1000. Попробуй угадать за {self._attempts} попыток))")
        while user_attempts < self._attempts:
            print(f"У тебя осталось {self._attempts - user_attempts} попыток")
            user_answer = input("Введи число: ")
            try:
                user_answer = int(user_answer)
                if not self._process_game(user_answer):
                    user_attempts += 1
                else:
                    print(f"Ты выйграл за {user_attempts} попыток")
                    break

            except ValueError:
                print(f"{user_answer} не является числом. Попробуй снова.")
        else:
            print("В следующий раз повезет!!!")


def start_task3():
    attempts = 10
    game = GuessingGame(attempts)
    game.run()
