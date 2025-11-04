import json
import numpy as np

class CardVectoriser:
    
    def __init__(self):
        cardNameIndex = []
        cardMatrix = []

    # A function to vectorise a card
    # Takes in a card as an array of values pulled from the cards .json file

    """
    Vector format:
    - Colour Identity
    - Colours
    - Mana Value
    - Mana Cost < Addlater
    - Is Game Changer
    -
    - All the Keywords 
    -
    - Card Layout < Addlater
    - Power
    - Toughness
    -
    - Subtypes
    -
    -
    - Supertypes
    -
    -
    - Types
    -
    - Effect <- Addlater
    """

    def vectoriseCard(self, card):
        

        # Ability words
        abilityWords = ["Adamant", "Addendum", "Alliance", "Battalion", "Bloodrush", "Celebration", "Channel", "Chroma", "Cohort", "Constellation", "Converge", "Corrupted", "Council's dilemma", "Coven", "Delirium", "Descend", "Domain", "Eerie", "Eminence", "Enrage", "Fateful hour", "Fathomless descent", "Ferocious", "Flurry", "Formidable", "Grandeur", "Hellbent", "Hero's Reward", "Heroic", "Imprint", "Inspired", "Join forces", "Kinfall", "Kinship", "Landfall", "Landship", "Legacy", "Lieutenant", "Magecraft", "Metalcraft", "Morbid", "Pack tactics", "Paradox", "Parley", "Radiance", "Raid", "Rally", "Renew", "Revolt", "Secret council", "Spell mastery", "Start your engines!", "Strive", "Survival", "Sweep", "Teamwork", "Tempting offer", "Threshold", "Underdog", "Undergrowth", "Valiant", "Void", "Will of the Planeswalkers", "Will of the council"]
        # Keyword Abilties
        keywordAbilities = ["Absorb", "Affinity", "Afflict", "Afterlife", "Aftermath", "Amplify", "Annihilator", "Ascend", "Assist", "Augment", "Aura Swap", "Awaken", "Backup", "Banding", "Bargain", "Basic landcycling", "Battle Cry", "Bestow", "Blitz", "Bloodthirst", "Boast", "Bushido", "Buyback", "Cascade", "Casualty", "Champion", "Changeling", "Choose a background", "Cipher", "Cleave", "Commander ninjutsu", "Companion", "Compleated", "Conspire", "Convoke", "Craft", "Crew", "Cumulative upkeep", "Cycling", "Dash", "Daybound", "Deathtouch", "Decayed", "Defender", "Delve", "Demonstrate", "Desertwalk", "Dethrone", "Devoid", "Devour", "Disguise", "Disturb", "Doctor's companion", "Double agenda", "Double strike", "Double team", "Dredge", "Echo", "Embalm", "Emerge", "Enchant", "Encore", "Enlist", "Entwine", "Epic", "Equip", "Escalate", "Escape", "Eternalize", "Evoke", "Evolve", "Exalted", "Exhaust", "Exploit", "Extort", "Fabricate", "Fading", "Fear", "First strike", "Flanking", "Flash", "Flashback", "Flying", "For Mirrodin!", "Forecast", "Forestcycling", "Forestwalk", "Foretell", "Fortify", "Freerunning", "Frenzy", "Friends forever", "Fuse", "Gift", "Graft", "Gravestorm", "Harmonize", "Haste", "Haunt", "Hexproof", "Hexproof from", "Hidden agenda", "Hideaway", "Horsemanship", "Impending", "Improvise", "Indestructible", "Infect", "Ingest", "Intensity", "Intimidate", "Islandcycling", "Islandwalk", "Job select", "Jump-start", "Kicker", "Landcycling", "Landwalk", "Legendary landwalk", "Level Up", "Lifelink", "Living metal", "Living weapon", "Madness", "Max speed", "Mayhem", "Megamorph", "Melee", "Menace", "Mentor", "Miracle", "Mobilize", "Modular", "More Than Meets the Eye", "Morph", "Mountaincycling", "Mountainwalk", "Multikicker", "Mutate", "Myriad", "Nightbound", "Ninjutsu", "Nonbasic landwalk", "Offering", "Offspring", "Outlast", "Overload", "Partner", "Partner with", "Persist", "Phasing", "Plainscycling", "Plainswalk", "Poisonous", "Protection", "Prototype", "Provoke", "Prowess", "Prowl", "Rampage", "Ravenous", "Reach", "Read Ahead", "Rebound", "Reconfigure", "Recover", "Reinforce", "Renown", "Replicate", "Retrace", "Riot", "Ripple", "Saddle", "Scavenge", "Shadow", "Shroud", "Skulk", "Slivercycling", "Soulbond", "Soulshift", "Specialize", "Spectacle", "Splice", "Split second", "Spree", "Squad", "Station", "Storm", "Sunburst", "Surge", "Suspend", "Swampcycling", "Swampwalk", "Toxic", "Training", "Trample", "Transfigure", "Transmute", "Tribute", "Typecycling", "Umbra armor", "Undaunted", "Undying", "Unearth", "Unleash", "Vanishing", "Vigilance", "Ward", "Warp", "Web-slinging", "Wither", "Wizardcycling"]
        # Keyword Actions
        keywordActions = ["Abandon", "Activate", "Adapt", "Amass", "Assemble", "Attach", "Behold", "Bolster", "Cast", "Clash", "Cloak", "Collect evidence", "Conjure", "Connive", "Convert", "Counter", "Create", "Destroy", "Detain", "Discard", "Discover", "Double", "Endure", "Exchange", "Exert", "Exile", "Explore", "Fateseal", "Fight", "Food", "Forage", "Goad", "Heist", "Incubate", "Investigate", "Learn", "Manifest", "Manifest dread", "Meld", "Mill", "Monstrosity", "Open an Attraction", "Planeswalk", "Play", "Plot", "Populate", "Proliferate", "Regenerate", "Reveal", "Role token", "Roll to Visit Your Attractions", "Sacrifice", "Scry", "Seek", "Set in motion", "Shuffle", "Support", "Surveil", "Suspect", "Tap", "Time Travel", "Transform", "Treasure", "Untap", "Venture into the dungeon", "Vote"]

        # Subtypes
        subtypes = ["Abian", "Adventure", "Advisor", "Aetherborn", "Ajani", "Alara", "Alfava Metraxis", "Alicorn", "Alien", "Ally", "Aminatou", "Amonkhet", "Amsterdam", "Androzani Minor", "Angel", "Angrath", "Antausia", "Antelope", "Apalapucia", "Ape", "Arcane", "Arcavios", "Archer", "Archon", "Arkhos", "Arlinn", "Armadillo", "Armored", "Army", "Art", "Artifact", "Artificer", "Artist", "Ashiok", "Assassin", "Assembly-Worker", "Astartes", "Athlete", "Atog", "Attraction", "Aura", "Aurochs", "Autobot", "Automaton", "Avatar", "Avishkar", "Azgol", "Azra", "B.O.B.", "Background", "Baddest,", "Badger", "Bahamut", "Balloon", "Barbarian", "Bard", "Barnyard", "Basilisk", "Basri", "Bat", "Bear", "Beast", "Beaver", "Beeble", "Beholder", "Belenon", "Berserker", "Biggest,", "Bird", "Bison", "Blind Eternities", "Blood", "Bloomburrow", "Boar", "Bobblehead", "Bolas", "Bolas's Meditation Realm", "Boxer", "Brainiac", "Bringer", "Brushwagg", "Bureaucrat", "Byode", "C'tan", "Calix", "Camel", "Capenna", "Capybara", "Carrier", "Cartouche", "Case", "Cat", "Cave", "Centaur", "Cephalid", "Chameleon", "Champion", "Chandra", "Chef", "Chicago", "Chicken", "Child", "Chimera", "Chorus", "Citizen", "Clamfolk", "Clamhattan", "Class", "Cleric", "Cloud", "Clown", "Clue", "Cockatrice", "Comet", "Construct", "Contraption", "Control", "Cow", "Coward", "Coyote", "Crab", "Cridhe", "Crocodile", "Curse", "Custodes", "Cyberman", "Cyborg", "Cyclops", "Dack", "Dakkon", "Dalek", "Daretti", "Darillium", "Dauthi", "Davriel", "Deb", "Deer", "Demigod", "Demon", "Desert", "Designer", "Detective", "Devil", "Dihada", "Dinosaur", "Djinn", "Doctor", "Dog", "Dominaria", "Domri", "Donkey", "Dovin", "Dragon", "Drake", "Dreadnought", "Drix", "Drone", "Druid", "Dryad", "Duck", "Dungeon", "Duskmourn", "Dwarf", "Earth", "Echidna", "Echoir", "Efreet", "Egg", "Elder", "Eldraine", "Eldrazi", "Elemental", "Elemental?", "Elephant", "Elf", "Elk", "Ellywick", "Elminster", "Elspeth", "Elves", "Employee", "Equilor", "Equipment", "Ergamon", "Ersta", "Estrid", "Etiquette", "Eye", "Fabacin", "Faerie", "Ferret", "Fiora", "Fire", "Fish", "Flagbearer", "Foldaria", "Food", "Forest", "Fortification", "Foundations", "Fox", "Fractal", "Freyalise", "Frog", "Fungus", "Gallifrey", "Gamer", "Gargantikar", "Gargoyle", "Garruk", "Gate", "Germ", "Giant", "Gideon", "Gith", "Glimmer", "Gnoll", "Gnome", "Goat", "Gobakhan", "Goblin", "God", "Gold", "Golem", "Gorgon", "Grandchild", "Graveborn", "Gremlin", "Griffin", "Grist", "Guest", "Guff", "Gus", "Hag", "Halfling", "Hamster", "Harpy", "Hatificer", "Hawk", "Head", "Hedgehog", "Hell", "Hellion", "Hero", "Hippo", "Hippogriff", "Homarid", "Homunculus", "Horror", "Horse", "Horsehead Nebula", "Huatli", "Human", "Human?", "Hydra", "Hyena", "Igpay", "Ikoria", "Illusion", "Imp", "Incarnation", "Incubator", "Infinity", "Inkling", "Innistrad", "Inquisitor", "Insect", "Inzerva", "Iquatana", "Ir", "Island", "Ixalan", "Jace", "Jackal", "Jared", "Jaya", "Jellyfish", "Jeska", "Judge", "Juggernaut", "Junk", "Kaito", "Kaldheim", "Kamigawa", "Kandoka", "Kangaroo", "Karn", "Karsus", "Kasmina", "Kavu", "Kaya", "Kephalai", "Key", "Killbot", "Kinshala", "Kiora", "Kirin", "Kithkin", "Knight", "Kobold", "Kolbahan", "Kor", "Koth", "Kraken", "Kylem", "Kyneth", "LaIR", "Lady", "Lair", "Lamia", "Lammasu", "Lander", "Las Vegas", "Leech", "Lemur", "Lesson", "Leviathan", "Lhurgoyf", "Licid", "Liliana", "Lizard", "Lobster", "Locus", "Lolth", "Lorwyn", "Lukka", "Luvion", "Luxior", "MagicCon", "Mammoth", "Manticore", "Map", "Mars", "Master", "Masticore", "Mercadia", "Mercenary", "Merfolk", "Metathran", "Mime", "Mine", "Minion", "Minotaur", "Minsc", "Mirrodin", "Mission", "Mite", "Moag", "Mole", "Monger", "Mongoose", "Mongseng", "Monk", "Monkey", "Moogle", "Moon", "Moonfolk", "Mordenkainen", "Mount", "Mountain", "Mouse", "Mummy", "Muraganda", "Mutagen", "Mutant", "Myr", "Mystic", "Naga", "Nahiri", "Narset", "Nastiest,", "Nautilus", "Necron", "Necros", "Nephilim", "New Earth", "New Phyrexia", "Nightmare", "Nightstalker", "Niko", "Ninja", "Nissa", "Nixilis", "Noble", "Noggle", "Nomad", "Nymph", "Octopus", "Ogre", "Oko", "Omen", "Omenpath", "Ooze", "Orc", "Orgg", "Otter", "Ouphe", "Outside Mutter's Spiral", "Ox", "Oyster", "Pangolin", "Paratrooper", "Peasant", "Pegasus", "Penguin", "Pentavite", "Performer", "Pest", "Phelddagrif", "Phoenix", "Phyrexia", "Phyrexian", "Pilot", "Pirate", "Plains", "Planet", "Plant", "Point", "Pony", "Porcupine", "Possum", "Power-Plant", "Powerstone", "Praetor", "Primarch", "Processor", "Proper", "Pyrulea", "Qu", "Quest", "Quintorius", "Rabbit", "Rabiah", "Raccoon", "Ral", "Ranger", "Rat", "Rath", "Ravnica", "Realm", "Rebel", "Reflection", "Regatha", "Reveler", "Rhino", "Rigger", "Robot", "Rogue", "Role", "Room", "Rowan", "Rukh", "Rune", "Sable", "Saga", "Saheeli", "Salamander", "Samurai", "Samut", "Sand", "Saproling", "Sarkhan", "Satyr", "Scarecrow", "Scientist", "Scion", "Scorpion", "Scout", "Sculpture", "Seal", "Secret", "Secret Lair", "Segovia", "Serf", "Serpent", "Serra", "Serra’s Realm", "Servo", "Shade", "Shadowmoor", "Shaman", "Shandalar", "Shapeshifter", "Shard", "Shark", "Sheep", "Shenmeng", "Ship", "Shrine", "Siege", "Siren", "Sivitri", "Skaro", "Skeleton", "Skunk", "Slith", "Sliver", "Sloth", "Slug", "Snail", "Snake", "Soldier", "Soltari", "Sorcerer", "Sorin", "Spacecraft", "Spawn", "Specter", "Spellshaper", "Sphere", "Sphinx", "Spider", "Spike", "Spirit", "Splinter", "Sponge", "Spuzzem", "Spy", "Squid", "Squirrel", "Starfish", "Stone", "Surrakar", "Survivor", "Svega", "Swamp", "Symbiote", "Synth", "Szat", "Tamiyo", "Tarkir", "Tasha", "Teddy", "Teferi", "Tentacle", "Teyo", "Tezzeret", "Thalakos", "The", "The Abyss", "The Dalek Asylum", "The Library", "Theros", "Thopter", "Thrull", "Thunder Junction", "Tibalt", "Tiefling", "Time", "Time Lord", "Tower", "Town", "Townsfolk", "Toy", "Trap", "Treasure", "Tree", "Treefolk", "Trenzalore", "Trilobite", "Triskelavite", "Troll", "Turtle", "Tyranid", "Tyvar", "Ugin", "Ulamog's", "Ulgrotha", "Undercity", "Unicorn", "Universia Beyondia", "Unknown Planet", "Urza", "Urza's", "Urzan", "Utrom", "Valla", "Vampire", "Vampyre", "Varmint", "Vedalken", "Vehicle", "Venser", "Villain", "Vivien", "Volver", "Vraska", "Vronos", "Vryn", "Waiter", "Wall", "Walrus", "Wanderer", "Warlock", "Warrior", "Weasel", "Weird", "Werewolf", "Whale", "Wildfire", "Will", "Windgrace", "Wizard", "Wolf", "Wolverine", "Wombat", "Worm", "Wraith", "Wrenn", "Wrestler", "Wurm", "Xenagos", "Xerex", "Yanggu", "Yanling", "Yeti", "You", "Zariel", "Zendikar", "Zhalfir", "Zombie", "Zonian", "Zubera", "and/or", "of", "sECreT"]
        # Supertypes
        supertypes = ["Basic", "Host", "Legendary", "Ongoing", "Snow", "World"]
        # Types
        types = ["Artifact", "Battle", "Boss", "Card", "Conspiracy", "Creature", "Dragon", "Dungeon", "Eaturecray", "Elemental", "Elite", "Emblem", "Enchantment", "Ever", "Goblin", "Hero", "Instant", "Jaguar", "Kindred", "Knights", "Land", "Legend", "Licid", "Phenome-nom", "Phenomenon", "Plane", "Planeswalker", "Poly", "Scariest", "Scheme", "See", "Sorcery", "Stickers", "Summon", "Token", "Tolkien", "Tribal", "Universewalker", "Vanguard", "Wolf", "You'll", "instant", "pLAnE"]

        
        # Vector size
        vectorSize = 14 + len(abilityWords) + len(keywordAbilities) + len(keywordActions) + len(subtypes) + len(supertypes) + len(types)
        card = card[0]
        cardVector = np.zeros((vectorSize, ))
        
        
        # Sets the colour idenity values
        # Is White
        cardVector[0] = 1 if "W" in card["colors"] else 0
        # Is Blue
        cardVector[1] = 1 if "U" in card["colors"] else 0
        # Is Black
        cardVector[2] = 1 if "B" in card["colors"] else 0
        # Is Red
        cardVector[3] = 1 if "R" in card["colors"] else 0
        # Is Green
        cardVector[4] = 1 if "G" in card["colors"] else 0


        # Sets the colour values
        # Is White
        cardVector[5] = 1 if "W" in card["colors"] else 0
        # Is Blue
        cardVector[6] = 1 if "U" in card["colors"] else 0
        # Is Black
        cardVector[7] = 1 if "B" in card["colors"] else 0
        # Is Red
        cardVector[8] = 1 if "R" in card["colors"] else 0
        # Is Green
        cardVector[9] = 1 if "G" in card["colors"] else 0

        # Mana value is just mana value
        if "manaValue" in card:
            cardVector[10] = card["manaValue"]

        # 0 or 1 if the card is a game changer
        if "isGameChanger" in card:
            cardVector[11] = card["isGameChanger"]

        # Loops for each ability word and sets wether it exists or not
        position = 11
        for i in range(len(abilityWords)):
            position += 1
            if "keywords" in card:
                if abilityWords[i] in card["keywords"]:
                    cardVector[position] = 1

        # Loops for each keyword and sets wether it exists or not
        for i in range(len(abilityWords)):
            position += 1
            if "keywords" in card:
                if keywordAbilities[i] in card["keywords"]:
                    cardVector[position] = 1

        # Loops for each keyword action and sets wether it exists or not
        for i in range(len(abilityWords)):
            position += 1
            if "keywords" in card:
                if keywordActions[i] in card["keywords"]:
                    cardVector[position] = 1

        # Power and Toughness
        if "power" in card:
            try:
                cardVector[position + 1] = int(card["power"])
            except:
                pass
        if "toughness" in card:
            try:
                cardVector[position + 2] = int(card["toughness"])
            except:
                pass
        position += 2

        # Loops for each supertype and sets wether it exists or not
        for i in range(len(supertypes)):
            position += 1
            if supertypes[i] in card["supertypes"]:
                cardVector[position] = 1

        # Loops for each type and sets wether it exists or not
        for i in range(len(types)):
            position += 1
            if types[i] in card["types"]:
                cardVector[position] = 1

        # Loops for each subtype and sets wether it exists or not
        for i in range(len(subtypes)):
            position += 1
            if subtypes[i] in card["subtypes"]:
                cardVector[position] = 1

        return cardVector

    # Takes in a file and vectorises the values
    def vectoriseDataSet(self, filename):
        f = open(f"{filename}.json", "r", encoding='utf-8')
        cards = f.read()
        cards = json.loads(cards)
        cards = cards["data"]

        cardNameIndex = []
        cardMatrix = []

        # Iterates through all the cards
        for card in cards:
            cardNameIndex.append(card)
            cardMatrix.append(self.vectoriseCard(cards[card]))
        
        self.cardNameIndex = np.array(cardNameIndex)
        self.cardMatrix = np.array(cardMatrix)


    # Gets the vector for a card
    def getVector(self, cardname):
        return self.cardMatrix[self.cardNameIndex.searchsorted(cardname)]
    
    # Finds the n cards that are closest to the sum of two cards
    def sumCards(self, cardName1, cardName2, n=1):
        card1 = self.getVector(cardName1)
        card2 = self.getVector(cardName2)

        # Finds the closest match using the l2 norm
        newCard = card1 + card2
        closestMatch = self.cardNameIndex[np.argsort(np.linalg.norm(self.cardMatrix - newCard, 1, 1))][:n]

        return closestMatch
    
    # Finds the n cards that are closest to the differents of two cards
    def diffCards(self, cardName1, cardName2, n=1):
        card1 = self.getVector(cardName1)
        card2 = self.getVector(cardName2)

        # Finds the closest match using the l2 norm
        newCard = card1 - card2
        closestMatch = self.cardNameIndex[np.argsort(np.linalg.norm(self.cardMatrix - newCard, 1, 1))][:n]

        return closestMatch
    
    # Finds the n cards most similar to a card
    def simCards(self, cardName, n=1):
        card = self.getVector(cardName)

        # Finds the closest matchs using the l2 norm
        closestMatch = self.cardNameIndex[np.argsort(np.linalg.norm(self.cardMatrix - card, 1, 1))][:n]

        return closestMatch
    
    # Finds the n cards most similar the mean of two cards
    def midCards(self, cardName1, cardName2, n=1):
        card1 = self.getVector(cardName1)
        card2 = self.getVector(cardName2)

        card = np.mean(np.array([card1, card2]), axis=0)

        # Finds the closest matchs using the l2 norm
        closestMatch = self.cardNameIndex[np.argsort(np.linalg.norm(self.cardMatrix - card, 1, 1))][:n]

        return closestMatch