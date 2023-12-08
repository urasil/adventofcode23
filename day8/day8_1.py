steps, _, *rest = open("day8\\input8.txt").read().splitlines()

mapping = {}
for line in rest:
    position, targets = line.split(" = ")
    mapping[position] = targets[1:-1].split(", ")

stepsCount = 0
currentStep = "AAA"
while currentStep != "ZZZ":
    stepsCount += 1
    if steps[0] == "L":
        currentStep = mapping[currentStep][0]
    else:
        currentStep = mapping[currentStep][1]
    steps = steps[1:] + steps[0]
print(stepsCount)