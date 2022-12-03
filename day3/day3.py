def letter_to_value(letter: str) -> int:
    value = ord(letter)
    if value <= 90:
        return value - 38
    else:
        return value - 96


def main():
    f = open("input", "r")
    rucksacks: list[str] = []
    priority_sum: int = 0

    rucksack: str
    for rucksack in f:
        rucksacks.append(rucksack[:-1])

        item_found: bool = False
        cutoff_index: int = (len(rucksack) - 1) // 2

        for i in range(cutoff_index):
            if item_found:
                break
            else:
                for j in range(cutoff_index):
                    if rucksack[i] == rucksack[j + cutoff_index]:
                        # ASCII values:
                        # A-Z: 65-90
                        # a-z: 97-122
                        priority_sum += letter_to_value(rucksack[i])
                        item_found = True
                        break

    f.close()

    badge_sum: int = 0
    i: int
    for i in range(2, len(rucksacks), 3):
        j: int = i - 1
        k: int = i - 2
        item_found: bool = False

        for a in rucksacks[i]:
            for b in rucksacks[j]:
                if item_found:
                    break
                else:
                    for c in rucksacks[k]:
                        if a == b == c:
                            badge_sum += letter_to_value(a)
                            item_found = True
                            break

    print(priority_sum)
    print(badge_sum)


if __name__ == "__main__":
    main()
