import random

def boxExp(diceAmount, boxXAmount, boxYAmount, trialNum):
    #create a list of numbers in ranoage of 1 to 6, and the amount of numbers in the list is the dice amount
    diceListX = []
    diceListY = []
    boxXCount = diceAmount
    boxYCount = 0
    for x in range(trialNum):
        diceListX = []
        for x in range(boxXCount):
            diceListX.append(random.randint(1, 6))
        #count how many numbers are equal to or less than the boxXAmount
        for x in diceListX:
            if x <= boxXAmount:
                boxYCount += 1
                boxXCount -= 1
        #now do the same with Y
        diceListY = []
        for x in range(boxYCount):
            diceListY.append(random.randint(1, 6))
        for x in diceListY:
            if x <= boxYAmount:
                boxXCount += 1
                boxYCount -= 1
    print("The amount of dice in each box is " + str(boxXCount) + " and " + str(boxYCount) + " respectively.")


    
boxExp(1000, 1, 5, 1000)
