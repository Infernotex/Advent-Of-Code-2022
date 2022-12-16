def move_knot(tail: complex, head: complex) -> complex:
    def direction(position: float) -> int:
        return (position > 0) - (position < 0)

    tail += direction(head.real - tail.real)
    tail += direction(head.imag - tail.imag) * 1j

    return tail


def main() -> None:
    with open("input", "r") as f:
        # Inspiration from Reza
        instruction_table: dict[str, int] = {"L": -1, "R": 1, "U": 1j, "D": -1j}

        head_pos: complex = (0 + 0j)
        tail_pos: complex = (0 + 0j)
        tail_visited_coordinates: set[complex] = {0}

        knots: list[complex] = [(0 + 0j) for _ in range(10)]
        knots_visited_coordinates: set[complex] = {0}

        line: str
        for line in f:
            instructions = line.strip().split()
            direction: int = instruction_table.get(instructions[0])
            iterations: int = int(instructions[-1])

            for _ in range(iterations):
                head_last_pos: complex = head_pos
                head_pos += direction

                # Task 1
                # sqrt(2) ≈ 1.414 ≈ 1.5
                if abs(head_pos - tail_pos) > 1.5:
                    tail_pos = head_last_pos
                    tail_visited_coordinates.add(tail_pos)

                # Task 2 (I KEEP F****** MAKING SNAKES 🤬🤬🤬)
                knots[0] = head_pos

                for i in range(1, len(knots)):
                    if abs(knots[i] - knots[i - 1]) > 1.5:
                        knots[i] = move_knot(knots[i], knots[i - 1])

                knots_visited_coordinates.add(knots[-1])

        print(len(tail_visited_coordinates))
        print(len(knots_visited_coordinates))


if __name__ == "__main__":
    main()
