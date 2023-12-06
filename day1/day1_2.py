_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

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
                elif line[i:i+3] in _dict or line [i:i+4] in _dict or line[i:i+5] in _dict:
                    left = _dict.get(line[i:i+5]) or _dict.get(line[i:i+4]) or _dict.get(line[i:i+3])
                else: i+=1
            if not right:
                if line[j].isnumeric():
                    right = line[j]
                elif line[j-2:j+1] in _dict or line [j-3:j+1] in _dict or line[j-4:j+1] in _dict:
                    right = _dict.get(line[j-4:j+1]) or _dict.get(line[j-3:j+1]) or _dict.get(line[j-2:j+1])
                else: j-=1
        total += int(left)*10 + int(right)
    return total

print(solve())