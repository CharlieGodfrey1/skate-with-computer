import random

def dice_roll():
    diceroll = random.randint(1, 6)
    return diceroll

def getTrick():
    print("1. Ollie\n2. Kick Flip")
    trick = input("Enter trick number: ")
    return trick

def getYesNo():
    while True:
        answer = input("Did you land? (y/n): ")
        if answer=="y":
            return True
        elif answer=="n":
            return False

def computerAttempt(trick):
    possibleTricks = [1, 3, 5]
    if trick in possibleTricks:
        print("i can o that")
        return True
    else:
        print("bail")
        return False


def playRound(player1, player2):
    #player1 enter trick
    trick = getTrick()

    #player enters if they have landed
    landed = getYesNo()

    #if player1 lands the trick
    if landed:
        #computer attempts trick
        computerLandedTrick = computerAttempt()

        #if computer lands trick
        if computerLandedTrick:
            #computer doesnt get letter
            continue

        #else computer didint land the trick
        else:
            #computer gets letter
            player2

    #if player 1 doesnt land the trick
        #computers go


#establish players
class player:
    def __init__(self, name):
        self.name = name
        self.currentLetter = 0

human = player("human")
computer = player("computer")


#pick random number to chose first player 1
print("Rolling dice")
roll = dice_roll()
print("dice was " + str(roll))
if roll > 3:
    currentPlayer = human
else:
    currentPlayer = computer


while ((human.currentLetter < 6) and (computer.currentLetter < 6)):
    #if player 1 first 
    if currentPlayer.name == "human":
        print("humans go")
        playRound(human, computer)
    #else computer first
    else:
        print("computers go")
        playRound(computer, human)

print(human.name + "scored: " + human.currentLetter)
print(computer.name + "scored: " + computer.currentLetter)