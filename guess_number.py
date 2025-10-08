from constants import ADMIN_USERNAME
from new_game import NewGame


def get_username() -> str:
    username = input('Представьтесь, пожалуйста, как Вас зовут?\n').strip()
    if username == ADMIN_USERNAME:
        print(
            '\nДобро пожаловать, создатель! '
            'Во время игры вам доступны команды "stat", "answer"'
        )
    else:
        print(f'\n{username}, добро пожаловать в игру!')
    return username


if __name__ == '__main__':

    print(
        'Вас приветствует игра "Угадай число"!\n'
        'Для выхода нажмите Ctrl+C'
    )

    username = get_username()
    new_game = NewGame(username)
    new_game.start()
