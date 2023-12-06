def solve():
    seeds, *blocks = open("day5/input5.txt").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        for seed in seeds:
            for destStart, sourceStart, rangeLen in ranges:
                if sourceStart <= seed < sourceStart + rangeLen:
                    new.append(seed-sourceStart + destStart)
                    break
            else: #statement only ran if for loop didn't break, we could have identified the break with a flag instead of this
                new.append(seed)
        seeds = new
    return min(seeds)

print(solve())