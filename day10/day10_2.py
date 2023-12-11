from collections import deque

grid = open("day10/input10.txt").read().strip().split("\n")
#determine what the S pipe is
aboveValid, belowValid, leftValid, rightValid, pipeS = False, False, False, False, None
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            start = (r, c)
            if r > 0 and grid[r-1][c] in "|7F":
                aboveValid = True
            if r < len(grid)-1 and grid[r+1][c] in "|JL":
                belowValid = True
            if c > 0 and grid[r][c-1] in "-J7":
                leftValid = True
            if c < len(grid[r])-1 and grid[r][c+1] in "-LF":
                rightValid = True

            if aboveValid and belowValid:
                pipeS = "|"
            elif leftValid and rightValid:
                pipeS = "-"
            elif aboveValid and rightValid:
                pipeS = "L"
            elif aboveValid and leftValid:
                pipeS = "J"
            elif belowValid and rightValid:
                pipeS = "F"
            elif belowValid and leftValid:
                pipeS = "7"

            break 


visited = {start}
queue = deque([start])

while queue:
    r, c = queue.popleft()
    currentChar = grid[r][c]
    #going up conditions
    if r > 0 and currentChar in "S|JL" and grid[r-1][c] in "|7FS" and (r-1, c) not in visited:
        queue.append((r-1, c))
        visited.add((r-1, c))

    #going down conditions
    if r < len(grid)-1 and currentChar in "S|F7" and grid[r+1][c] in "|JLS" and (r+1, c) not in visited:
        queue.append((r+1, c))
        visited.add((r+1, c))

    #going left conditions
    if c > 0 and currentChar in "S-7J" and grid[r][c-1] in "-FLS" and (r, c-1) not in visited:
        queue.append((r, c-1))
        visited.add((r, c-1))
    
    #going right conditions
    if c < len(grid[r])-1 and currentChar in "S-LF" and grid[r][c+1] in "-J7S" and (r, c+1) not in visited:
        queue.append((r, c+1))
        visited.add((r, c+1))

#assing the S pipe
grid[start[0]] = grid[start[0]][:start[1]] + pipeS + grid[start[0]][start[1] + 1:]

def countInversions(row, col):
    line = grid[row]
    count = 0
    for char in range(col):
        if (row, char) not in visited:
            continue
        count += 1 if line[char] in "|JL" else 0
    return count

result = 0
for i, line in enumerate(grid):
    for j in range(len(grid[0])):
        if (i,j) not in visited:
            numInversions = countInversions(i, j)
            if numInversions % 2 == 1:
                result += 1

print(result)