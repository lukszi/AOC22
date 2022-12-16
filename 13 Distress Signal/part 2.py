from typing import List, Tuple

RIGHT_ORDER = 1
UNDECIDED = 2
WRONG_ORDER = 3


def check_list_order(left: List, right: List) -> int:
    for l, r in zip(left, right):
        order = check_order(l, r)
        if order == WRONG_ORDER:
            return WRONG_ORDER
        elif order == RIGHT_ORDER:
            return RIGHT_ORDER
    if len(left) < len(right):
        return RIGHT_ORDER
    elif len(left) > len(right):
        return WRONG_ORDER
    else:
        return UNDECIDED


def check_int_order(left: int, right: int) -> int:
    if left < right:
        return RIGHT_ORDER
    elif left == right:
        return UNDECIDED
    else:
        return WRONG_ORDER


def check_order(left: List | int, right: List | int) -> int:
    if isinstance(left, int) and isinstance(right, int):
        return check_int_order(left, right)
    if isinstance(left, List) and isinstance(right, List):
        return check_list_order(left, right)
    elif isinstance(left, int):
        return check_order([left], right)
    elif isinstance(right, int):
        return check_order(left, [right])


class Packet:
    data: List

    def __init__(self, data: List):
        self.data = data
    def __cmp__(self, other):
        return check_order(self.data, other.data) - UNDECIDED

    def __eq__(self, other):
        return self.__cmp__(other) == UNDECIDED

    def __ne__(self, other):
        return self.__cmp__(other) != UNDECIDED

    def __lt__(self, other):
        return self.__cmp__(other) == RIGHT_ORDER

    def __gt__(self, other):
        return self.__cmp__(other) == WRONG_ORDER

    def __le__(self, other):
        return self.__cmp__(other) <= UNDECIDED

    def __ge__(self, other):
        return self.__cmp__(other) >= UNDECIDED

    def __repr__(self):
        return str(self.data)


def main():
    dividers = [Packet([[2]]), Packet([[6]])]
    pairs: List[Packet] = []
    pairs.extend(dividers)
    with open("signal.txt", "r") as f:
        signal = f.read().splitlines()
    for i in range(0, len(signal), 3):
        packet_pair = tuple([Packet(eval(packet)) for packet in signal[i:i+2]])
        pairs.extend(packet_pair)

    pairs.sort(reverse=True)
    print(pairs)
    print((pairs.index(dividers[0]) + 1) * (pairs.index(dividers[1]) + 1))

if __name__ == '__main__':
    main()