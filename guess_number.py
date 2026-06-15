"Модуль запуска игры."

from constants import ADMIN_USERNAME
from new_game import NewGame


def get_username() -> str:
    """
    Запрашивает имя пользователя.

    Для администратора выводит информацию о доступных командах.

    :return: Имя пользователя.
    """
    username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()

    if username == ADMIN_USERNAME:
        print(
            '\nДобро пожаловать, создатель! '
            'Во время игры вам доступны команды "stat", "answer".'
        )
    else:
        print(f'\n{username}, добро пожаловать в игру!')

    return username


def main() -> None:
    """
    Запускает консольную игру.
    """
    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C.'
    )

    username = get_username()
    new_game = NewGame(username)
    new_game.start()


if __name__ == '__main__':
    main()
