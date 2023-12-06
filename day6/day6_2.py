def solve():
    with open('day6/input6.txt') as f:
        lines = f.readlines()
    lines = ["".join(line.split(":")[1].strip().split()) for line in lines]
    time, distance, count, result = int(lines[0]), int(lines[1]), 0, 1
    for t in range(1, time):
        distanceTravelled = (time - t)* t
        count += 1 if distanceTravelled > distance else 0
    result *= count
    return result
print(solve())