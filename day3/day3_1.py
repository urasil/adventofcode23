def solve():
    lines = list(open('day3/input3.txt'))
    lines = [line.strip() for line in lines]
    i, total = 0, 0

    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            num = 0
            if lines[i][j].isnumeric():
                start = j
                while j < len(lines[i]) and lines[i][j].isnumeric():
                    num = num * 10 + int(lines[i][j])
                    j += 1
                if hasSpecialNeighboor(lines, i, start, j):
                    total += num
            else:
                j += 1
        i += 1
    return total


def hasSpecialNeighboor(grid, row, colStart, colEnd):
    for i in range(row - 1, row + 2):
        if i >= 0 and i < len(grid):
            for j in range(colStart - 1, colEnd + 1):
                if j >= 0 and j < len(grid[i]):
                    if grid[i][j] != '.' and grid[i][j] not in "0123456789":
                        return True
    return False

print(solve())