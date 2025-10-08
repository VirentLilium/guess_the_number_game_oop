from datetime import datetime as dt
from random import randint

from access_control import access_control
from constants import UNKNOWN_COMMAND


class NewGame:

    def __init__(self, username: str):
        self.username = username
        self.start_time = dt.now()
        self.total_games = 0

    @access_control
    def get_statistics(self) -> None:
        game_time = dt.now() - self.start_time
        print(
            f'Общее время игры: {game_time},\n'
            f'текущая игра - №{self.total_games}')

    @access_control
    def get_right_answer(self, number: int) -> None:
        print(f'Правильный ответ: {number}')

    def check_number(self, guess, number: int) -> bool:
        if guess == number:
            print(f'Отличная интуиция, {self.username}! Вы угадали число :)')
            return True
        if guess < number:
            print('Ваше число меньше того, что загадано.')
        else:
            print('Ваше число больше того, что загадано.')
        return False

    def game(self) -> None:
        number = randint(1, 100)
        print(
            '\nУгадайте число от 1 до 100.\n'
            'Для выхода из текущей игры введите команду "stop"'
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
                    try:
                        guess = int(user_input)
                    except ValueError:
                        print(UNKNOWN_COMMAND)
                        continue

                    if self.check_number(guess, number):
                        break

    def start(self):
        while True:
            self.total_games += 1
            self.game()
            play_again = input(
                '\nХотите сыграть ещё? (yes/no): ').strip().lower()
            if play_again not in ('y', 'yes', 'д', 'да', 'lf', 'l'):
                break
