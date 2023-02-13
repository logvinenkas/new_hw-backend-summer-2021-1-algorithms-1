__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    # raise NotImplementedError

    if number < 2:
        return False

    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True
