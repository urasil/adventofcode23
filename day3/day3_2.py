def solve():
    lines = list(open('day3/input3.txt'))
    lines = [line.strip() for line in lines]
    i, total = 0, 0

    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            if lines[i][j] == "*":
                numbers = exactlyTwoAsterix(lines, i, j)
                if exactlyTwoAsterix(lines, i, j):
                    total += numbers[0]*numbers[1]
                    
            j += 1
        i += 1
    return total


def exactlyTwoAsterix(grid, row, col):
    numbers = []
    i,j = row-1, col-1
    while i <= row+1:
        j = col-1
        if i >= 0:
            while j <= col+1:
                if j >= 0:
                    if grid[i][j] in "0123456789":
                        num = 0
                        #Go to the starting point of the number
                        while j >= 0 and grid[i][j-1] in "0123456789":
                            if j == 0:
                                break
                            j -= 1
                        #Get the number
                        while j < len(grid[i]) and grid[i][j] in "0123456789":
                            num = num*10 + int(grid[i][j])
                            j += 1
                        numbers.append(num)
                    else:
                        j += 1
            i += 1
                        
    return numbers if len(numbers) == 2 else None


print(solve())