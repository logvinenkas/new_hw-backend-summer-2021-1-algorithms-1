__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    # raise NotImplementedError

    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)

    hours = seconds // 3600
    seconds %= 3600

    minutes = seconds // 60
    seconds %= 60

    result = ('%02dd' % days) if days > 0 else ''
    result += ('%02dh' % hours) if hours > 0 or result != '' else result
    result += ('%02dm' % minutes) if minutes > 0 or result != '' else result
    result += ('%02ds' % seconds)

    return result



