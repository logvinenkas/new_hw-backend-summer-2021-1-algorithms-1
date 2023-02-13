from typing import Any

__all__ = (
    'cartesian_product',
)


def cartesian_product(arr1: list[Any], arr2: list[Any]) -> list:
    """
    Должна возвращать все пары элементы двух массивов:
    cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    # raise NotImplementedError

    result: list = []
    if arr1 is None or arr2 is None:
        return []
    for a in arr1:
        for b in arr2:
            result.append((a, b))
    return result
