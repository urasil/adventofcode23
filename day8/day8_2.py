import math

steps, _, *rest = open("day8\\input8.txt").read().splitlines()

mapping = {}
for line in rest:
    position, targets = line.split(" = ")
    mapping[position] = targets[1:-1].split(", ")

currentSteps = {k:v for k, v in mapping.items() if k[-1] == "A"}
stepsToReachFirstZ = []

#because time taken to reach each Z is equal = there is only one Z in each path for a each ghost
#otherwise we would have had to calculate the number of steps to reach each Z for a each ghost
#and taken the lcm of all possibilities 
for currentStep, value in currentSteps.items():
    stepsCount = 0
    #time taken for each step to reach Z
    while currentStep[-1] != "Z":
        stepsCount += 1
        if steps[0] == "L":
            currentStep = mapping[currentStep][0]
        else:
            currentStep = mapping[currentStep][1]
        steps = steps[1:] + steps[0]
    stepsToReachFirstZ.append(stepsCount)

result = math.lcm(*stepsToReachFirstZ)
print(result)




