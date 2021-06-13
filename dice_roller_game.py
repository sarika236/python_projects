import random

def Main():
    harry = 0
    harry_wins = 0
    harmione = 0
    harmione_wins = 0
    rounds = 1

    while rounds != 4:
        print("Round " + str(rounds))
        harry = dice_roll()
        harmione = dice_roll()
        print("harry roll: " + str(harry))
        print("harmione roll: " + str(harmione))

        if harry == harmione:
            print("Draw!\n")
        elif harry > harmione:
            harry_wins = harry_wins + 1
            print("harry is Winner\n")
        else:
            harmione_wins = harmione_wins + 1
            print("harmione is the winner\n")

        rounds = rounds + 1

    if harry_wins == harmione_wins:
        print("Draw!")
    elif harry_wins > harmione_wins:
        print("harry is the winner - Rounds Won: " + str(harry_wins))
    else:
        print("harmione is the winner - Rounds Won: " + str(harmione_wins))

def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

Main()