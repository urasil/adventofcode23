import re
def solve():
    scratchCards = open('day4/input4.txt').readlines()
    cardCount = dict()
    for card in scratchCards:
        cardInfo, numbers = card.split(":")
        winningNumbers, yourNumbers = numbers.split("|")
        winningNumbers, yourNumbers = re.split(r'\s+', winningNumbers.strip()), re.split(r'\s+', yourNumbers.strip())
        #print("winning numbers: ",winningNumbers)
        #print("your numbers: ",yourNumbers)
        cardNum = int(re.search(r'\d+', cardInfo).group())
        multiplier = 1
        if cardNum not in cardCount:
            cardCount[cardNum] = 1
        else:
            multiplier = cardCount[cardNum]
        for number in yourNumbers:
            if number in winningNumbers:
                cardNum += 1
                cardCount[cardNum] = cardCount.get(cardNum, 1) + multiplier
    return sum(cardCount.values())

print(solve())