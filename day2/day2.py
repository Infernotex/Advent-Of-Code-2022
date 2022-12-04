def shape_to_value(shape: str) -> int:
    if shape == "A" or shape == "X":
        return 1
    elif shape == "B" or shape == "Y":
        return 2
    else:
        return 3


def rpc(hand1: int, hand2: int) -> int:
    if hand1 == 1:
        if hand2 == 1:
            return 3
        elif hand2 == 2:
            return 6
        else:
            return 0

    elif hand1 == 2:
        if hand2 == 1:
            return 0
        elif hand2 == 2:
            return 3
        else:
            return 6

    else:
        if hand2 == 1:
            return 6
        elif hand2 == 2:
            return 0
        else:
            return 3


def outcome_to_hand(hand1: int, outcome: int) -> int:
    if outcome == 1:
        if hand1 == 1:
            return 3
        elif hand1 == 2:
            return 1
        else:
            return 2

    elif outcome == 2:
        return hand1

    else:
        if hand1 == 1:
            return 2
        elif hand1 == 2:
            return 3
        else:
            return 1


def main() -> None:
    f = open("input", "r")
    score1: int = 0
    score2: int = 0

    row: str
    for row in f:
        hand1: int = shape_to_value(row[0])
        hand2: int = shape_to_value(row[2])
        score1 += rpc(hand1, hand2) + hand2

        hand2 = outcome_to_hand(hand1, hand2)
        score2 += rpc(hand1, hand2) + hand2

    f.close()

    print(score1)
    print(score2)


if __name__ == "__main__":
    main()
