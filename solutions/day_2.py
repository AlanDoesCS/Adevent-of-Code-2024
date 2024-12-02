import heapq

input_path: str = r"../input/day_2.txt"

# Part 1
n_safe: int = 0

file = open(input_path, "r")
for columns in ( raw.strip().split() for raw in file ):
    columns = [int(x) for x in columns]
    left: int = columns[0]
    right: int = columns[1]
    delta: int = right - left

    if delta == 0:
        continue
    elif abs(delta) > 3:
        continue

    direction: int = int(delta/abs(delta))
    row_is_safe: bool = True
    left = right
    for right in columns[2:]:
        right = int(right)
        delta = right - left

        if delta == 0:
            row_is_safe = False
            break
        elif (int(delta/abs(delta)) != direction) or (abs(delta) > 3):
            row_is_safe = False
            break

        left = right

    if row_is_safe:
        n_safe += 1

print("Part 1:", n_safe)

# Part 2
n_safe_2: int = 0

file = open(input_path, "r")
for columns in (raw.strip().split() for raw in file):
    columns = [int(x) for x in columns]
    n = len(columns)
    safe_found = False

    for i in range(n):
        if i == n:
            test_columns = columns
        else:
            test_columns = columns[:i] + columns[i+1:]

        left = test_columns[0]
        right = test_columns[1]
        delta = right - left

        if delta == 0 or abs(delta) > 3:
            continue
        direction = int(delta / abs(delta))

        row_is_safe = True
        left = right
        for right in test_columns[2:]:
            delta = right - left
            if delta == 0 or abs(delta) > 3 or int(delta / abs(delta)) != direction:
                row_is_safe = False
                break
            left = right

        if row_is_safe:
            n_safe_2 += 1
            safe_found = True
            break

    if not safe_found and n == 2:
        delta = columns[1] - columns[0]
        if delta != 0 and abs(delta) <= 3:
            n_safe_2 += 1

print("Part 2:", n_safe_2)
