from math import floor, log

def int2nary(number: int, base: int, length: int=0) -> tuple[int]:
    """与えられた整数をn進数へ変換する

    Args:
        number (int): 変換する整数
        base (int): 底n
        length (int, optional): 変換後の桁数. Defaults to 0.

    Returns:
        tuple[int]: n進数のタプル表現
    """
    return tuple(
            [
                (number // (base ** (i-1))) % base
                for i in range(max(length, floor(log(number, base))+1), 0, -1)
            ]
            if number else [0]*max(length, 1)
        )


def nary2int(nary: tuple[int], base: int) -> int:
    """n進数のタプル表現を10進数へ変換する

    Args:
        nary (tuple[int]): n進数のタプル表現
        base (int): 底n

    Returns:
        int: n進数の10進数表現
    """
    return sum(entry * (base ** (len(nary)-digit-1)) for digit, entry in enumerate(nary))


def xor(x_bin: tuple[int], y_bin: tuple[int]) -> tuple[int]:
    """要素ごとの排他的論理和を計算する

    Args:
        x_bin (tuple[int]): バイナリのタプル表現
        y_bin (tuple[int]): バイナリのタプル表現

    Returns:
        tuple[int]: 与えられた2引数の要素ごとの排他的論理和のタプル表現
    """
    return tuple([xi ^ yi for (xi, yi) in zip(x_bin, y_bin)])
