from collections import deque

grid = open("day10/input10.txt").read().strip().split("\n")

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            start = (r, c)
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

"""
halfway point of the loop is going to be the furthest point from the starting position
"""

print(len(visited) // 2)
