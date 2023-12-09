lines = open("day9/input9.txt").read().splitlines()
report = [list(map(int,line.split())) for line in lines]

def extrapolate(arr):
    if all(x==0 for x in arr):
        return 0
    deltas = [arr[idx+1] - arr[idx] for idx in range(len(arr)) if idx+1 < len(arr)]
    diff = extrapolate(deltas)
    return arr[0] - diff #we can just add the diff to the last number

total = 0
for line in report:
    total += extrapolate(line)
print(total)
