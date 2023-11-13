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
        self.__laboratory = Laboratory

    def getRecipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe):

    def drinkPotion():
        pass


class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagent(reagent, amount):
        pass


class Potion:

class SuperPotion(Potion):

class ExtremePotion(Potion):

class Reagent:

class Herb(Reagent):

class Catalyst(Reagent):      
        
