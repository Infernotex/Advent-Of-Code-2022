def obscured_above(forest: list[str], tree: int, row: int, col: int) -> bool:
    i: int
    for i in range(row):
        if int(forest[i][col]) >= tree:
            return True
    return False


def obscured_below(forest: list[str], tree: int, row: int, col: int) -> bool:
    i: int
    for i in range(row + 1, len(forest)):
        if int(forest[i][col]) >= tree:
            return True
    return False


def obscured_left(forest: list[str], tree: int, row: int, col: int) -> bool:
    i: int
    for i in range(col):
        if int(forest[row][i]) >= tree:
            return True
    return False


def obscured_right(forest: list[str], tree: int, row: int, col: int) -> bool:
    i: int
    for i in range(col + 1, len(forest)):
        if int(forest[row][i]) >= tree:
            return True
    return False


def hidden(forest: list[str], row: int, col: int) -> bool:
    tree: int = int(forest[row][col])
    x_axis: bool = obscured_left(forest, tree, row, col) and obscured_right(forest, tree, row, col)
    y_axis: bool = obscured_above(forest, tree, row, col) and obscured_below(forest, tree, row, col)

    return x_axis and y_axis


def distance_above(forest: list[str], tree: int, row: int, col: int) -> int:
    distance: int = 0

    i: int
    for i in range(row - 1, -1, -1):
        distance += 1
        if int(forest[i][col]) >= tree:
            break

    return distance


def distance_below(forest: list[str], tree: int, row: int, col: int) -> int:
    distance: int = 0

    i: int
    for i in range(row + 1, len(forest)):
        distance += 1
        if int(forest[i][col]) >= tree:
            break

    return distance


def distance_left(forest: list[str], tree: int, row: int, col: int) -> int:
    distance: int = 0

    i: int
    for i in range(col - 1, -1, -1):
        distance += 1
        if int(forest[row][i]) >= tree:
            break

    return distance


def distance_right(forest: list[str], tree: int, row: int, col: int) -> int:
    distance: int = 0

    i: int
    for i in range(col + 1, len(forest)):
        distance += 1
        if int(forest[row][i]) >= tree:
            break

    return distance


def scenic_score(forest: list[str], row: int, col: int) -> int:
    tree: int = int(forest[row][col])
    above_score: int = distance_above(forest, tree, row, col)
    below_score: int = distance_below(forest, tree, row, col)
    left_score: int = distance_left(forest, tree, row, col)
    right_score: int = distance_right(forest, tree, row, col)

    return above_score * below_score * left_score * right_score


def main() -> None:
    with open("input", "r") as f:
        visible_trees: int = 0
        best_score: int = 0

        forest: list[str] = [line.strip() for line in f]

        row: int
        for row in range(len(forest)):
            col: int
            for col in range(len(forest)):
                if not hidden(forest, row, col):
                    visible_trees += 1

                tree_score: int = scenic_score(forest, row, col)
                if tree_score > best_score:
                    best_score = tree_score

        print(visible_trees)
        print(best_score)


if __name__ == "__main__":
    main()
