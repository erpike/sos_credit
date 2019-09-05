from datetime import date


def is_numeric(value):
    return isinstance(value, float) or isinstance(value, int)


# ==== Task #1 ==== #
def swap_1(var1, var2):
    """
    swaps two variables
    :param var1: any
    :param var2: any
    :return: var2, var1

    >>> swap_1(23, 32)
    (32, 23)
    """
    return var2, var1


def swap_2(var1, var2):
    """
    swaps two variables
    :param var1: any
    :param var2: any
    :return: var1, var2

    >>> swap_2('23', 32)
    (32, '23')
    """
    var1, var2 = var2, var1
    return var1, var2


def swap_3(var1, var2):
    """
    swaps two variables
    :param var1: (int or float)
    :param var2: (int or float)
    :return: var1, var2

    >>> swap_3(23, 32.0)
    (32.0, 23.0)

    >>> swap_3(23, '32.0')
    Traceback (most recent call last):
    ValueError: Args should be numeric
    """
    if is_numeric(var1) and is_numeric(var2):
        var1 = var1 + var2
        var2 = var1 - var2
        var1 = var1 - var2
        return var1, var2
    raise ValueError('Args should be numeric')


def swap_4(var1, var2):
    """
    swaps two variables
    :param var1: (int or float)
    :param var2: (int or float)
    :return: var1, var2

    >>> swap_4(23, 32.0)
    (32.0, 23.0)
    """
    if is_numeric(var1) and is_numeric(var2):
        var1 = var1 * var2
        var2 = var1 / var2
        var1 = var1 / var2
        return var1, var2
    raise ValueError('Args should be numeric')


def swap_5(var1, var2):
    """
    swaps two variables
    :param var1: int
    :param var2: int
    :return: var1, var2

    >>> swap_5(23, 32)
    (32, 23)

    >>> swap_5('23', 32)
    Traceback (most recent call last):
    ValueError: Args should be int
    """
    if isinstance(var1, int) and isinstance(var2, int):
        var1 = var1 ^ var2  # 011 XOR 101 -> 110
        var2 = var1 ^ var2  # 110 XOR 101 -> 011
        var1 = var1 ^ var2  # 110 XOR 011 -> 101
        return var1, var2
    raise ValueError('Args should be int')
# ==== Task #1 ==== #


# ==== Task #2 ==== #
def is_palindrom(string: str) -> bool:
    """
    defines if string is palindrom
    :param string1: str
    :param string2: str
    :return: bool

    >>> is_palindrom('abba')
    True
    >>> is_palindrom('abbas')
    False
    """
    return string == string[::-1]
# ==== Task #2 ==== #


# ==== Task #3 ==== #
def string_collapse(string):
    """
    collapses string to specific format
    :param string:
    :return:
    >>> string_collapse('abc')
    'abc'
    >>> string_collapse('aabbc')
    'aabbc'
    >>> string_collapse('aabbcc')
    'a2b2c2'
    >>> string_collapse('aaabccc')
    'a3b1c3'
    """
    if not isinstance(string, str):
        raise ValueError('arg must be a str')
    collapse = []
    counter = 1
    for i in range(len(string)):
        if i == len(string) - 1:
            if string[i - 1] == string[i]:
                collapse.append(f'{string[i]}{counter}')
                continue
            collapse.append(f'{string[i]}1')
        if i < len(string) - 1:
            if string[i] == string[i + 1]:
                counter += 1
                continue
            collapse.append(f'{string[i]}{counter}')
            counter = 1
    collapse = ''.join(collapse)
    return collapse if len(collapse) <= len(string) else string
# ==== Task #3 ==== #


# ==== Task #4 ==== #
def validate_date(year, month, day):
    """
    checks if date exists
    :param year: int
    :param month: int
    :param day: int
    :return: bool

    >>> validate_date(2003, '12', 4)
    Traceback (most recent call last):
    ValueError: all params should be int

    >>> validate_date(2003, 12, 4)
    True

    >>> validate_date(2003, 12, 40)
    False
    """
    if isinstance(year, int) and (isinstance(month, int)) and isinstance(day, int):
        try:
            date(year, month, day)
        except ValueError:
            return False
        return True
    raise ValueError('all params should be int')
# ==== Task #4 ==== #


# ==== Task #6 ==== #
def get_dict(list1, list2):
    """
    generates dict form input lists
    :param list1: list
    :param list2: list
    :return: dict
    >>> get_dict(['k1', 'k2', 'k3'], ['v1', 'v2', 'v3', 'v4'])
    {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    >>> get_dict(['k1', 'k2', 'k3'], ['v1', 'v2', 'v3',])
    {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    >>> get_dict(['k1', 'k2', 'k3'], ['v1', 'v2',])
    {'k1': 'v1', 'k2': 'v2', 'k3': None}
    """
    if len(list1) > len(list2):
        list2.extend([None] * (len(list1) - len(list2)))
    return {k: v for k, v in zip(list1[:len(list2)], list2)}
# ==== Task #6 ==== #


if __name__ == '__main__':
    import doctest
    doctest.testmod()
