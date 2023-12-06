def solve():
    inputs, *blocks = open("day5/input5.txt").read().split("\n\n")
    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = [(inputs[idx], inputs[idx] + inputs[idx+1]) for idx in range(0, len(inputs), 2)]

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            s, e = seeds.pop()
            for destStart, sourceStart, rangeLen in ranges:
                overlapStart = max(s, sourceStart)
                overlapEnd = min(e, sourceStart + rangeLen)
                # If an overlap exists for the conversion, tranform the range to the new range
                if overlapStart < overlapEnd:
                    new.append((overlapStart + destStart - sourceStart, overlapEnd + destStart - sourceStart))
                    if overlapStart > s:
                        seeds.append((s, overlapStart))
                    if overlapEnd < e:
                        seeds.append((overlapEnd, e))
                    break
            #If no overlap exists, we can just add the range to the new list
            else:
                new.append((s, e))
        seeds = new
    return sorted(seeds)[0][0]

print(solve())