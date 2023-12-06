def solve():
    with open('day6/input6.txt') as f:
        lines = f.readlines()
    lines = [line.split(":")[1].strip().split() for line in lines]
    races = list(zip(*lines))
    result = 1
    for race in races:
        time, distance, count = int(race[0]), int(race[1]), 0
        for t in range(1, time):
            distanceTravelled = (time - t)* t
            count += 1 if distanceTravelled > distance else 0
        result *= count
    return result
print(solve())