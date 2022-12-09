# TODO make general
def main() -> None:
    with open("input", "r") as f:
        top_crates: str = ""
        stack_matrix: list[list[str]] = [[],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         [],
                                         []]

        # Gives the correct order, but .pop() removes last element in list
        i: int
        for i in range(8):
            line: str = f.readline()
            for j in range(1, len(line), 4):
                char: str = line[j]
                if char != " ":
                    stack_matrix[(j-1) // 4].append(char)

        # Reverses so .pop() works
        i: int
        for i in range(len(stack_matrix)):
            stack_matrix[i].reverse()

        f.readline()
        f.readline()

        instruction: str
        for instruction in f:
            instruction: list[str] = instruction.split()
            iterations: int = int(instruction[1])
            target: int = int(instruction[3]) - 1
            destination: int = int(instruction[5]) - 1

            crates: list[str] = []

            i: int
            for i in range(iterations):
                # Task 1
                # stack_matrix[destination].append(stack_matrix[target].pop())

                # Task 2
                crates.append(stack_matrix[target].pop())

            # Task 2
            crates.reverse()
            stack_matrix[destination].extend(crates)

        i: int
        for i in range(len(stack_matrix)):
            top_crates += stack_matrix[i][-1]

        print(top_crates)


if __name__ == "__main__":
    main()
