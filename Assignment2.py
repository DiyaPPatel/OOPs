class Laboratory:
    def __init__(self):
        self.potions = []
        self.herbs = []
        self.catalysts = []

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
        self.attack = attack
        self.strength = strength
        self.defence = defense
        self.magic = magic
        self.ranged = ranged
        self.necromancy = necromancy
        self.laboratory = Laboratory
        self.recipes = {}

    def getLaboratory(self, Laboratory):
        self.laboratory = Laboratory

    def getRecipes(self):
        pass
    
    def mixPotion(self, recipe):
        self.recipe = recipe

    def drinkPotion():
        pass

class Potion(Laboratory):

    def __init__(self, name, stat, boost):
        

class SuperPotion(Potion):
    def 

class ExtremePotion(Potion):

class Reagent:

class Herb(Reagent):
    def

class Catalyst(Reagent):      
        
