from collections.abc import Callable
from functools import wraps
from typing import Any

from constants import ADMIN_USERNAME, UNKNOWN_COMMAND


def access_control(func: Callable[..., None]) -> Callable[..., None]:
    """
    Ограничивает доступ к методу только для администратора.

    :param func: Метод, доступный только администратору.
    :return: Обёрнутый метод с проверкой прав доступа.
    """
    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> None:
        if self.username == ADMIN_USERNAME:
            func(self, *args, **kwargs)
            return

        print(UNKNOWN_COMMAND)

    return wrapper
