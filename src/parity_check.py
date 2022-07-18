from functools import reduce

def parity_check(board: list[list[int]]) -> int:
    """与えられた盤面からパリティを計算する.

    Args:
        board (list[list[int]]): 0か1からなるリストのリスト．

    Returns:
        int: パリティの整数表現
    """
    return hamming_syndrome(reduce(lambda x, y: x + y, board))


def hamming_syndrome(bits: list[int]) -> int:
    """与えられたビット列からハミングシンドロームを計算する

    Args:
        bits (list[int]): ビット列

    Returns:
        int: ハミングシンドローム
    """
    return reduce(
        lambda x, y: x ^ y,
        [idx for (idx, bit) in enumerate(bits) if bit]
    )