RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def solve():
    lines = open('day2/input2.txt', 'r')
    total = 0
    for line in lines:
        invalid = False
        gamesInfoOriginal, allGames = line.split(':')
        gamesId = int(gamesInfoOriginal.replace("Game ", ""))
        games = allGames.split(';')
        for game in games:
            game = game.split(",")
            #print(game)
            for cube in game:
                cube = cube.rstrip() and cube.lstrip()
                count, color = cube.split()
                 #print("count: ",count, "color: ",color)
                if color == 'red' and int(count) <= RED_MAX:
                    continue
                elif color == 'green' and int(count) <= GREEN_MAX:
                    continue
                elif color == 'blue' and int(count) <= BLUE_MAX:
                    continue
                else:
                    invalid = True
                    break
            if invalid:
                break
        total += int(gamesId) if not invalid else 0

    return total 

print(solve())