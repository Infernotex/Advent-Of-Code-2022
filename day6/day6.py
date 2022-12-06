def main() -> None:
    f = open("input", "r")
    line: str = f.readline()
    f.close()
    packet_start: int = 0
    message_start: int = 0

    # Task 1
    i: int
    for i in range(len(line)):
        packet_buffer: str = line[i: i + 4]

        if len(set(packet_buffer)) == len(packet_buffer):
            packet_start = i + 4
            break

    # Task 2
    i: int
    for i in range(len(line)):
        message_buffer: str = line[i: i + 14]

        if len(set(message_buffer)) == len(message_buffer):
            message_start = i + 14
            break

    print(packet_start)
    print(message_start)


if __name__ == "__main__":
    main()
