from constants import UNKNOWN_COMMAND
from new_game import NewGame


def test_is_valid_number_returns_true_for_integer_string() -> None:
    """
    Проверяет, что строка с целым числом считается валидной.
    """
    assert NewGame.is_valid_number('10') is True
    assert NewGame.is_valid_number('-5') is True


def test_is_valid_number_returns_false_for_invalid_value() -> None:
    """
    Проверяет, что некорректный ввод не считается числом.
    """
    assert NewGame.is_valid_number('abc') is False
    assert NewGame.is_valid_number('10.5') is False


def test_check_number_returns_true_for_correct_guess() -> None:
    """
    Проверяет, что метод возвращает True, если число угадано.
    """
    game = NewGame('User')

    assert game.check_number(50, 50) is True


def test_check_number_returns_false_for_wrong_guess() -> None:
    """
    Проверяет, что метод возвращает False, если число не угадано.
    """
    game = NewGame('User')

    assert game.check_number(40, 50) is False


def test_number_of_attempts_for_default_range() -> None:
    """
    Проверяет расчёт оптимального количества попыток.
    """
    assert NewGame.number_of_attempts(1, 100) == 7


def test_get_statistics_is_unavailable_for_regular_user(capsys) -> None:
    """
    Проверяет, что обычный пользователь не может вызвать статистику.
    """
    game = NewGame('User')

    game.get_statistics()

    captured = capsys.readouterr()

    assert UNKNOWN_COMMAND in captured.out
