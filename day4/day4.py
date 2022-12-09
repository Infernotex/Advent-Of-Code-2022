def main() -> None:
    with open("input", "r") as f:
        subsets: int = 0
        intersections: int = 0

        line: str
        for line in f:
            pair: list[str] = line.split(",")

            left: str = pair[0]
            first: list[str] = left.split("-")
            f_start: int = int(first[0])
            f_end: int = int(first[1])

            right: str = pair[1]
            second: list[str] = right.split("-")
            s_start: int = int(second[0])
            s_end: int = int(second[1])

            if f_start <= s_start and f_end >= s_end or s_start <= f_start and s_end >= f_end:
                subsets += 1

            if f_start <= s_end and s_start <= f_end:
                intersections += 1

        print(subsets)
        print(intersections)


if __name__ == "__main__":
    main()
