#gettind rid of the unnecessary solve function
#getting help from hyperneutrino
letterMap = {'T':'A', 'J':'B', 'Q':'C', 'K':'D', 'A':'E'}


def classify(hand):
    counts = [hand.count(card) for card in hand]
    if 5 in counts:
        return 6
    elif 4 in counts:
        return 5
    elif 3 in counts and 2 in counts:
        return 4
    elif 3 in counts:
        return 3
    elif counts.count(2) == 4:
        return 2
    elif 2 in counts:
        return 1
    return 0 #high card

def strength(hand):
    return (classify(hand), [letterMap.get(card, card) for card in hand])

plays = []
for line in open('day7\\input7.txt'):
    hand, value = line.split()
    plays.append((hand, int(value)))
plays.sort(key=lambda x: strength(x[0]))

total = 0
for rank, (hand, value) in enumerate(plays, 1):
    total += (rank * value)

print(total)