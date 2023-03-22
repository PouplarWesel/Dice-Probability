import random

def boxExp(diceAmount, boxXAmount, boxYAmount, trialNum):
    # open a file for writing the results
    with open("experiment_results.txt", "w") as f:
        # write the headers to the file
        f.write("Data Table — Equilibrium Trial 1\n")
        f.write("{:>10s}{:>20s}{:>35s}{:>20s}{:>40s}\n".format("",
            "Reactants (Successful Forward = 1)", "", "Products (Successful Reverse = 6)", ""))
        f.write("{:>10s}{:>20s}{:>35s}{:>20s}{:>40s}\n".format("Throw", "Starting Dice",
            "Number of Successful Forward Reactions", "Starting Dice",
            "Number of Successful Reverse Reactions"))
        f.write("\n")

        # initialize variables
        boxXCount = diceAmount
        boxYCount = 0

        # do the trials and write the results to the file
        for throw in range(1, trialNum+1):
            backUp = ("The amount of dice in each box is {} and {} respectively.".format(boxXCount, boxYCount))
            # roll the dice for X box
            diceListX = [random.randint(1, 6) for i in range(boxXCount)]
            # count the number of successful forward reactions
            forwardCount = sum(1 for d in diceListX if d <= boxXAmount)

            # roll the dice for Y box
            diceListY = [random.randint(1, 6) for i in range(boxYCount)]
            # count the number of successful reverse reactions
            reverseCount = sum(1 for d in diceListY if d <= boxYAmount)

            # write the results to the file
            f.write("{:>10d}{:>20d}{:>35d}{:>20d}{:>40d}\n".format(throw, boxXCount,
                forwardCount, boxYCount, reverseCount))

            # update the counts for next trial
            boxXCount -= forwardCount
            boxYCount += forwardCount
            boxYCount -= reverseCount
            boxXCount += reverseCount
            
        # write the final box counts to the file
        f.write("\n")
        f.write(backUp)

# run the experiment with given parameters
boxExp(100, 1, 1, 1000)
