import argparse
import math

from typing import Any, List


def main(args: Any) -> None:
    """
    Main method.

    Parameters
    ----------
    args : Any
        Command line arguments.
    """
    max_value: int = args.integer
    if max_value <= 0:
        raise ValueError('The first argument must be a positive number.')

    ret: List[bool] = [True] * max_value
    ret[0] = False

    src_index: int = 0
    while src_index + 1 < math.sqrt(max_value):
        if ret[src_index]:
            dst_index = ((src_index + 1) ** 2) - 1
            for i in range(((dst_index - 1) // src_index + 1) * src_index, max_value, src_index + 1):
                ret[i] = False
        src_index += 1

    print([i + 1 for i, x in enumerate(ret) if x])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='List all primzahlen less than or equal to the specified integer.')
    _ = parser.add_argument('integer', type=int, help='max number')
    args = parser.parse_args()
    main(args)
