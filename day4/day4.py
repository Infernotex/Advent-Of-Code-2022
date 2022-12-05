def find_comma(pair: str) -> int:
    for i in range(len(pair)):
        if pair[i] == ",":
            return i


def find_dash(pair: str) -> int:
    for i in range(len(pair)):
        if pair[i] == "-":
            return i


# TODO use split
def main() -> None:
    f = open("input", "r")
    subsets: int = 0
    intersections: int = 0

    pair: str
    for pair in f:
        comma_index: int = find_comma(pair)

        # first_index is 0
        first_dash: int = find_dash(pair)
        first_start: int = int(pair[:first_dash])
        first_end: int = int(pair[first_dash + 1: comma_index])
        first: set[int] = set(range(first_start, first_end + 1))

        second_index: int = comma_index + 1
        second_dash: int = second_index + find_dash(pair[second_index:])
        second_start: int = int(pair[second_index:second_dash])
        second_end: int = int(pair[second_dash + 1: -1])
        second: set[int] = set(range(second_start, second_end + 1))

        if first.issubset(second) or second.issubset(first):
            subsets += 1

        if first.intersection(second) != set():
            intersections += 1

    f.close()

    print(subsets)
    print(intersections)


if __name__ == "__main__":
    main()
