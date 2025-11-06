import CardVectoriser
import numpy as np

import pickle
import os

vectoriser = CardVectoriser.CardVectoriser()

# To avoid having to revectorise the dataset it gets save externally
if not os.path.exists("cardVectors.pkl"):
    vectoriser.vectoriseDataSet("AtomicCards")
    f = open(r"cardVectors.pkl", "wb")
    pickle.dump(vectoriser, f)
    f.close()
else:
    f = open(r"cardVectors.pkl", "rb")
    vectoriser = pickle.load(f)
    f.close()

# Creates a vector representing a white pip
whitePipVector = np.zeros((vectoriser.vectorSize, ))
whitePipVector[0] = 1
whitePipVector[5] = 1
whitePipVector[10] = 1



# Creates a vector representing a red pip
redPipVector = np.zeros((vectoriser.vectorSize, ))
redPipVector[3] = 1
redPipVector[8] = 1
redPipVector[10] = 1


print(vectoriser.sumCards("Arc-Slogger", "Giant Growth", 10))





