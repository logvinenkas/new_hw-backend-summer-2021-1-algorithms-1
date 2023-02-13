from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    # raise NotImplementedError

    word_list: list = sorted([[len(x), x] for x in text.split()])
    if len(word_list) < 2:
        return None, None
    return word_list[0][1], word_list[-1][1]
