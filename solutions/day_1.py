import heapq

input_path: str = r"../input/day_1.txt"

# Part 1
left: list = []
right: list = []

file = open(input_path, "r")
for columns in ( raw.strip().split() for raw in file ):
    left.append(int(columns[0]))
    right.append(int(columns[1]))

left_copy: list = list(left) # for part 2
right_copy: list = list(right) # for part 2

heapq.heapify(left)
heapq.heapify(right)

length: int = len(left)
distance: int = 0

for i in range(length):
    distance += abs(heapq.heappop(left) - heapq.heappop(right))

print("Part 1:", distance)

# Part 2
right_frequency: dict = {}
similarity_score: int = 0

for i in range(length):
    current: int = right_copy[i]
    if current not in right_frequency:
        right_frequency[current] = 1
    else:
        right_frequency[current] += 1

for i in range(length):
    current: int = left_copy[i]
    if current not in right_frequency:
        similarity_score += 0
    else:
        similarity_score += current * right_frequency[current]

print("Part 2:", similarity_score)
