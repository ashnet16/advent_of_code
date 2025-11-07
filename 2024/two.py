def advent_two_one():
    with open('two.txt', 'r') as file:
        return sum(
            advent_two_one_helper(list(map(int, line.split())))
            for line in file
        )


def advent_two_two():
    with open('two.txt', 'r') as file:
        return sum(
            advent_two_one_helper(test) or advent_two_two_helper(test)
            for test in (list(map(int, line.split())) for line in file)
        )


def advent_two_one_helper(sequence: list) -> bool:
    if len(sequence) < 2:
        return True

    increase = None
    for i in range(len(sequence) - 1):
        diff = sequence[i + 1] - sequence[i]

        if abs(diff) > 3 or diff == 0:
            return False
        if increase is None:
            increase = diff > 0
        elif (diff > 0) != increase:
            return False
    return True


def advent_two_two_helper(sequence: list) -> bool:
    return any(
        advent_two_one_helper(sequence[:i] + sequence[i + 1:])
        for i in range(len(sequence))
    )


if __name__ == "__main__":
    print(advent_two_one())
    print(advent_two_two())
