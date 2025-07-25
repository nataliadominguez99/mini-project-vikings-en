import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        #set the initial annotation. 
        self.health = health 
        self.strength = strength
    
    def attack(self):
        return self.strength #attack method returns the strength property of the Soldier.

    def receiveDamage(self, damage):
        self.health -=  damage #removes damage from the health property. 
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage" 
        else: 
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage" 
        else: 
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append (viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append (saxon)
        
    def vikingAttack(self): #selecting random viking and saxon.
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        #inflict damage.
        result = random_saxon.receiveDamage(random_viking.strength) 

        #removing defeated saxons.
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)

    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        #inflict damage.
        result = random_viking.receiveDamage(random_saxon.strength) 

        #removing defeated saxons.
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)

    def showStatus(self):
        if not self.saxonArmy:
            return "Viking have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons hav fought for their lives and survive another day..."
        else: 
            return "Vikings and Saxons are still in the thick of battle."