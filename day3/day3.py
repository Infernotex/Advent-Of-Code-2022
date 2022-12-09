def letter_to_value(letter: str) -> int:
    value = ord(letter)
    # ASCII values:
    # A-Z: 65-90
    # a-z: 97-122
    if value <= 90:
        return value - 38
    else:
        return value - 96


def main() -> None:
    with open("input", "r") as f:
        rucksacks: list[str] = []
        priority_sum: int = 0
        badge_sum: int = 0

        rucksack: str
        for rucksack in f:
            rucksacks.append(rucksack.strip())

            cutoff_index: int = (len(rucksack) - 1) // 2

            i: int
            for i in range(cutoff_index):
                if rucksack[i] in rucksack[cutoff_index:]:
                    priority_sum += letter_to_value(rucksack[i])
                    break

        i: int
        for i in range(2, len(rucksacks), 3):
            j: int = i - 1
            k: int = i - 2

            for letter in rucksacks[i]:
                if letter in rucksacks[j] and letter in rucksacks[k]:
                    badge_sum += letter_to_value(letter)
                    break

        print(priority_sum)
        print(badge_sum)


if __name__ == "__main__":
    main()
