
def solve():
    inp = open('day1/input1.txt', 'r')
    total = 0
    for line in inp:
        i, j = 0, len(line)-1
        left, right = None, None
        while i <= j:
            if left and right:
                break
            if not left:
                if line[i].isnumeric():
                    left = line[i]
                else: i+=1
            if not right:
                if line[j].isnumeric():
                    right = line[j]
                else: j-=1
        total += int(left)*10 + int(right)
    return total
print(solve())

