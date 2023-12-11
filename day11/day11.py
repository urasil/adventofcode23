#solution from HyperNeutrino
#my original solution was too slow for part 2 and I fixed it by implementing HyperNueutrino's scale-trick solution
with open("day11\input11.txt") as f:
    lines = f.read().splitlines()

emptyRows = [r for r, row in enumerate(lines) if all(ch == "." for ch in row)]
emptyCols = [c for c in range(len(lines[0])) if all(row[c] == "." for row in lines)]

points = [(r,c) for r, row in enumerate(lines) for c, ch in enumerate(row) if ch == "#"]

total = 0
scale = 1000000

for i, (r1,c1) in enumerate(points):
    for (r2,c2) in points[:i]:
        for r in range(min(r1,r2), max(r1,r2)):
            total += scale if r in emptyRows else 1
        for c in range(min(c1,c2), max(c1,c2)):
            total += scale if c in emptyCols else 1
print(total)
            
                            