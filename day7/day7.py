def main() -> None:
    f = open("input", "r")
    directory_stack: list[str] = []
    directories: dict[str, int] = {}
    directory_sum: int = 0

    line: str
    for line in f:
        instructions: list[str] = line.strip().split()

        if instructions[-1] == "/":
            directory_stack.append("/")
        elif instructions[-1] == "..":
            if len(directory_stack) > 1:
                directory_stack.pop()
        elif instructions[1] == "cd":
            directory_stack.append(instructions[-1])

        elif instructions[0].isdigit():
            file_size = int(instructions[0])
            current_directory = ""

            for directory in directory_stack:
                current_directory += directory

                if current_directory not in directories:
                    directories[current_directory] = 0

                directories[current_directory] += file_size

    f.close()

    # Task 1
    for directory in directories:
        directory_size: int = directories[directory]
        if directory_size <= 100000:
            directory_sum += directory_size

    # Task 2
    total_space: int = 70000000
    required_space: int = 30000000
    used_space: int = directories["/"]
    eligible_directories: list[int] = []

    for directory in directories:
        directory_size: int = directories[directory]
        if used_space - directory_size < total_space - required_space:
            eligible_directories.append(directory_size)

    print(directory_sum)
    print(min(eligible_directories))


if __name__ == "__main__":
    main()
