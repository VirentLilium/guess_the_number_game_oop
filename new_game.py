"Модуль с логикой игры."

import math
from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import MAX_NUMBER, MIN_NUMBER, UNKNOWN_COMMAND


class NewGame:
    """
    Консольная игра "Угадай число".

    Класс хранит состояние игры: имя пользователя, время начала
    и количество сыгранных партий.
    """

    def __init__(self, username: str) -> None:
        """
        Инициализирует новую игру.

        :param username: Имя пользователя.
        """
        self.username = username
        self.start_time = dt.now()
        self.total_games = 0

    @staticmethod
    def number_of_attempts(left: int, right: int) -> int:
        """
        Рассчитывает оптимальное количество попыток для угадывания числа.

        :param left: Левая граница диапазона.
        :param right: Правая граница диапазона.
        :return: Оптимальное количество попыток.
        """
        numbers_count = abs(right - left) + 1
        return math.ceil(math.log2(numbers_count))

    @staticmethod
    def is_valid_number(value: str) -> bool:
        """
        Проверяет, что строка содержит целое число.

        :param value: Строка для проверки.
        :return: True, если строку можно преобразовать в целое число.
        """
        try:
            int(value)
            return True
        except ValueError:
            return False

    @access_control
    def get_statistics(self) -> None:
        """
        Выводит статистику игры для администратора.
        """
        game_time = dt.now() - self.start_time
        print(
            f'Общее время игры: {game_time},\n'
            f'текущая игра - №{self.total_games}'
        )

    @access_control
    def get_right_answer(self, number: int) -> None:
        """
        Выводит правильный ответ для администратора.

        :param number: Загаданное число.
        """
        print(f'Правильный ответ: {number}')

    def check_number(self, guess: int, number: int) -> bool:
        """
        Сравнивает число пользователя с загаданным числом.

        :param guess: Число пользователя.
        :param number: Загаданное число.
        :return: True, если число угадано.
        """
        if guess == number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            return True

        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')

        return False

    def game(self) -> None:
        """
        Запускает одну партию игры.
        """
        number = randint(MIN_NUMBER, MAX_NUMBER)
        attempts = self.number_of_attempts(MIN_NUMBER, MAX_NUMBER)

        print(
            f'\nУгадайте число от {MIN_NUMBER} до {MAX_NUMBER}.\n'
            f'Оптимальное количество попыток: {attempts}.\n'
            'Для выхода из текущей игры введите команду "stop".'
        )

        while True:
            user_input = input('Введите число или команду: ').strip().lower()

            match user_input:
                case 'stop':
                    break
                case 'stat':
                    self.get_statistics()
                case 'answer':
                    self.get_right_answer(number)
                case _:
                    if not self.is_valid_number(user_input):
                        print(UNKNOWN_COMMAND)
                        continue

                    guess = int(user_input)

                    if self.check_number(guess, number):
                        break

    def start(self) -> None:
        """
        Запускает игру и предлагает сыграть повторно после каждой партии.
        """
        while True:
            self.total_games += 1
            self.game()

            play_again = input(
                '\nХотите сыграть ещё? (yes/no): '
            ).strip().lower()

            if play_again not in ('y', 'yes', 'д', 'да', 'lf', 'l'):
                break
