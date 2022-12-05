def main() -> None:
    f = open("input", "r")
    subsets: int = 0
    intersections: int = 0

    line: str
    for line in f:
        pair: list[str] = line.split(",")

        left: str = pair[0]
        first: list[str] = left.split("-")
        first_start: int = int(first[0])
        first_end: int = int(first[1])
        first_set: set[int] = set(range(first_start, first_end + 1))

        right: str = pair[1]
        second: list[str] = right.split("-")
        second_start: int = int(second[0])
        second_end: int = int(second[1])
        second_set: set[int] = set(range(second_start, second_end + 1))

        if first_set.issubset(second_set) or second_set.issubset(first_set):
            subsets += 1

        if first_set.intersection(second_set) != set():
            intersections += 1

    f.close()

    print(subsets)
    print(intersections)


if __name__ == "__main__":
    main()
