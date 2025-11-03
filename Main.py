import CardVectoriser

vectoriser = CardVectoriser.CardVectoriser()

cardVecs = vectoriser.vectoriseDataSet("AtomicCards")

print(cardVecs["Counterspell"])