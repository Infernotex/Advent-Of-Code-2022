def main() -> None:
    with open("input", "r") as f:
        x: int = 1
        current_cycle: int = 1
        signal_strengths: dict[int, int] = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}

        line: str
        for line in f:
            instructions: list[str] = line.split()

            if instructions[0] == "addx":
                iterations: int = 2
            else:
                iterations: int = 1

            for i in range(iterations):
                current_pixel: int = (current_cycle - 1) % 40

                if current_pixel == 0:
                    print("")

                if (x - 1) <= current_pixel <= (x + 1):
                    print("#", end="")
                else:
                    print(".", end="")

                current_cycle += 1

                if i == 1:
                    x += int(instructions[1])

                if current_cycle in signal_strengths:
                    signal_strengths[current_cycle] = current_cycle * x

        print("\n")
        print(sum(signal_strengths.values()))


if __name__ == "__main__":
    main()
