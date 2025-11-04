import CardVectoriser

vectoriser = CardVectoriser.CardVectoriser()

vectoriser.vectoriseDataSet("AtomicCards")

print(vectoriser.sumCards("Mountain", "Swamp", 2))

print(vectoriser.sumCards("Boros Swiftblade", "Vigilance", 10))

print(vectoriser.diffCards("Badlands", "Swamp", 2))

print(vectoriser.diffCards("Ulamog, the Infinite Gyre", "Chatterfang, Squirrel General", 10))

print(vectoriser.sumCards("Anti-Venom, Horrifying Healer", "Venom, Eddie Brock", 10))

print(vectoriser.simCards("Opt", 10))



