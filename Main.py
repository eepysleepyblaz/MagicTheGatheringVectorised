import CardVectoriser
import numpy as np

vectoriser = CardVectoriser.CardVectoriser()

vectoriser.vectoriseDataSet("AtomicCards")

# Creates a vector representing a white pip
whitePipVector = np.zeros((vectoriser.vectorSize, ))
whitePipVector[0] = 1
whitePipVector[5] = 1
whitePipVector[10] = 1

print(vectoriser.sumCardVec("Raging Goblin", whitePipVector, 10))


# Creates a vector representing a red pip
redPipVector = np.zeros((vectoriser.vectorSize, ))
redPipVector[3] = 1
redPipVector[8] = 1
redPipVector[10] = 1


print(vectoriser.diffCardVec("Goblin Rally", redPipVector, 10))


print(vectoriser.simCards("Spark Reaper", 10))




