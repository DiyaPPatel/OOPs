'''
File: Patdp003_A2.py
Description:
Author: Diya Patel
StudentID: 110399790
EmailID: patdp003@mymail.unisa.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.

'''

from abc import ABC, abstractmethod

class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []
        

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """Mix potion is added in the potion list."""
        self.name = name
        self.type = type
        self.stat = stat
        self.primaryIngredient = primaryIngredient
        self.secondaryIngredient = secondaryIngredient
        self.potions.append({"name":self.name,"type":self.type,"stat":self.stat,"primaryIngredient":self.primaryIngredient,"secondaryIngredient":self.secondaryIngredient})

    def addReagent(self,reagent, amount):
        """New reagent is added."""
        if type(reagent).__name__ == "Herb":
            self.herbs.append(reagent)
        elif type(reagent).__name__ == "Catalyst":
            self.catalysts.append(reagent)
        
        

class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, Laboratory):
        self.attack = attack
        self.strength = strength
        self.defence = defense
        self.magic = magic
        self.ranged = ranged
        self.necromancy = necromancy
        self.laboratory = Laboratory
        self.recipes = {}

    def getLaboratory():
        return Laboratory()

    def getRecipes(recipe):
        for x in recipe:
            print(x["name"], x["primaryIngredient"], x["secondaryIngredient"])
    
    def mixPotion(recipe):
        """Mix potion from Laboratory is called."""
        lab.mixPotion(recipe["name"],recipe["type"],recipe["stat"],recipe["primaryIngredient"],recipe["secondaryIngredient"])

    def drinkPotion(potion):
        pass

    def collectReagent(reagent, amount):
        """Reagents are collected."""
        lab.addReagent(reagent, amount)

    def refineReagent(self):
        pass

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.name = name
        self.stat = stat
        self.boost = boost

    @abstractmethod
    def calculateBoost(self):
        """This method is and abstractmethod."""
        pass

    def getName(self):
        return self.name
    
    def getStat(self):
        return self.stat

    def getBoost(self):
        return self.boost
    
    def setBoost(self):
        pass
        
class SuperPotion(Potion):
    def __init__(self, potionName, stat, boost, herb, catalyst):
        super().__init__(potionName, stat, boost)
        self.herb = herb
        self.catalyst = catalyst

    def calculateBoost(herb,catalyst):
        """Method is called from the parent class."""
        herbPotency = herb.getPotency()
        catalystPotency = catalyst.getPotency()
        catalystQuality = catalyst.getQuality()

        boost = herbPotency + (catalystPotency * catalystQuality) * 1.5
        return round(boost, 2)

    def getHerb(self):
        return self.herb.name
    
    def getCatalyst(self):
        return self.catalyst.name
    
class ExtremePotion(Potion):
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name,stat,boost)
        self.reagent = reagent
        self.potion = potion

    def calculateBoost(reagent,potion):
        """This method is called from the parent class."""
        reagentPotency = reagent.getPotency()
        superPotionBoost = potion.getBoost()

        boost = (reagentPotency * superPotionBoost) * 3.0
        return round(boost, 2)

    def getReagent(self):
        return self.reagent.name

    def getPotion(self):
        return self.potion.name

class Reagent(ABC):
    def __init__(self, name, potency):
        self.name = name
        self.potency = potency

    @abstractmethod
    def refine(self):
        """This is an abstract method for the Reagent class."""
        pass
    
    def getName(self):
        return self.name
    
    def getPotency(self):
        return self.potency

    def setPotency(self):
        pass

class Herb(Reagent):
    def __init__(self, name, potency,grimy):
        super().__init__(name, potency)
        self.grimy = grimy

    def refine(self):
        """This method is called from the oarent class."""
        if self.grimy != True:
            refinedHerb = self.potency * 2.5
            print("Refined herb = ", refinedHerb)
        else:
            print("Refined herb = ")

    def getGrimy(self):
        return self.grimy
    
    def setGrimy():
        return True 

class Catalyst(Reagent): 
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.quality = quality

    def refine(self):
        """This method is called from the parenr class."""
        if self.quality < 8.9:
            refinedQuality = self.__quality + 1.1
            print("Refined Catalyst Quality = ", refinedQuality)

        elif self.quality > 8.9:
            refinedQuality = 10
            print("Refined Quality = ", refinedQuality,"/nIt cannot be refined any further")

    def getQuality(self):
        return self.quality
score = {"attack": 0, "strength": 0, "defence": 0, "magic": 0, "ranged": 0, "necromancy": 0}

lab = Alchemist.getLaboratory()



#getting herb

grimy = Herb.setGrimy()
herb1 = Herb("Irit",1.0,grimy)
print("Added Herb")
herb2 = Herb("Avantoe",3.0,grimy)
print("Added Herb")

#getting catalyst
print("")
print("###################################################")
print("")

catalyst1 = Catalyst("Eye of Newt",4.3,1.0)
print("Added Catalyst")
#adding reagent
Alchemist.collectReagent(herb1,1)
Alchemist.collectReagent(herb2,1)
Alchemist.collectReagent(catalyst1,1)

# available content in laboratory
print("")
print("###################################################")
print("")
print("Available Herbs: ")
for herb in lab.herbs:
    print(herb.name,herb.potency,herb.grimy)
print("")
print("###################################################")
print("")

print("Available catalysts: ")
for catalyst in lab.catalysts:
    print(catalyst.name,catalyst.potency,catalyst.quality)

# mix super potion
print("")
print("###################################################")
print("")
boost1 = SuperPotion.calculateBoost(herb1,catalyst1)
score["attack"] = score["attack"] + boost1
potion1 = SuperPotion("Super Attack","Attack",boost1,herb1,catalyst1)
primaryIngredient = potion1.getHerb()
secondaryIngredient = potion1.getCatalyst()
recipes = {"name":"Super Attack","type":"Super", "stat":"Attack", "primaryIngredient":primaryIngredient , "secondaryIngredient":secondaryIngredient }
Alchemist.mixPotion(recipes)
print("Mixed super Potion")
print("Super Attack: " + primaryIngredient + " " + secondaryIngredient)
print("Available Potions: ")
for x in lab.potions:
    print(x["name"], x["type"], x["stat"], x["primaryIngredient"], x["secondaryIngredient"])
# boost for Alchemist
print("")
print("###################################################")
print("")
for key,value in score.items():
    print(f"{key}: {value}" )


# mix extreme potion
print("")
print("###################################################")
print("")
boost2 = ExtremePotion.calculateBoost(herb2,potion1)
score["attack"] = score["attack"] + boost2
potion2 = ExtremePotion("Extreme Attack","Extreme",boost2,herb2,potion1)
primaryIngredient = potion2.getReagent()
secondaryIngredient = potion2.getPotion()
recipes = {"name":"Extreme Attack","type":"Extreme", "stat":"Attack", "primaryIngredient":primaryIngredient , "secondaryIngredient":secondaryIngredient }
Alchemist.mixPotion(recipes)
print("Mixed Extreme Potion")
print("Extreme Attack: " + primaryIngredient + " " + secondaryIngredient)
# boost for Alchemist
print("")
print("###################################################")
print("")
for key,value in score.items():
    print(f"{key}: {value}" )

# get recipes
print("")
print("###################################################")
print("")
print("Available Recipes:")
Alchemist.getRecipes(lab.potions)







    


