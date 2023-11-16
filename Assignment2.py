from abc import ABC, abstractmethod

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        self.name = name
        self.type = type
        self.stat = stat
        self.primaryIngredient = primaryIngredient
        self.secondaryIngredient = secondaryIngredient
        pass

    def addReagent(self,reagent, amount):
        self.reagent = reagent
        self.amount = amount
        pass

class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, Laboratory):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory
        self.__recipes = {}

    def getLaboratory(self, Laboratory):
        return self.laboratory

    def getRecipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe):
        pass

    def drinkPotion(self):
        pass

    def collectReagent(self):
        pass

    def refineReagent(self):
        pass

class Potion(ABC, Laboratory):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost
    
    def setBoost(self):
        pass
        
class SuperPotion(Potion):
    def __init__(self, potionName, stat, boost, herb, catalyst):
        super().__init__(potionName, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        self.__boost = Herb.self.__potency + (Catalyst.self.__potency * Catalyst.self.__quality) * 1.5
        return self.__boost

    def getHerb(self):
        return self.__herb
    
    def getCatalyst(self):
        return self.__catalyst
    
class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name,stat,boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        Reagent.self.__potency * 3

    def getReady(self):
        pass

    def getPotion(self):
        pass

class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name
    
    def getPotency(self):
        return self.__potency

    def setPotency(self):
        pass

class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True

    def refine(self):
        if self.__grimy != True:
            refinedHerb = self.___potency * 2.5
            print("Refined herb = ", refinedHerb)
        else:
            print("Refined herb = ")

    def getGrimy(self):
        return self.__grimy
    
    def setGrimy(self):
        pass

class Catalyst(Reagent): 
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        if self.__quality < 8.9:
            refinedQuality = self.__quality + 1.1
            print("Refined Catalyst Quality = ", refinedQuality)

        elif self.__quality > 8.9:
            refinedQuality = 10
            print("Refined Quality = ", refinedQuality,"/nIt cannot be refined any further")


    def getQuality(self):
        return self.__quality     
        
