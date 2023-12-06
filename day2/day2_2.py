def solve():
    lines = open('day2/input2.txt', 'r')
    total = 0
    for line in lines:
        invalid = False
        gamesInfoOriginal, allGames = line.split(':')
        games = allGames.split(';')
        maxRed, maxGreen, maxBlue = 0,0,0
        for game in games:
            game = game.split(",")
            #print(game)
            for cube in game:
                cube = cube.rstrip() and cube.lstrip()
                count, color = cube.split()
                 #print("count: ",count, "color: ",color)
                if color == 'red':
                    maxRed = max(maxRed, int(count))
                elif color == 'green':
                    maxGreen = max(maxGreen, int(count))
                elif color == 'blue':
                    maxBlue = max(maxBlue, int(count))
        print(maxRed, maxGreen, maxBlue)
        total += (maxRed * maxGreen * maxBlue)

    return total 

print(solve())