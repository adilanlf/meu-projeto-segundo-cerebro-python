# RPG Characters – Inheritance and Methods

# Base class for RPG characters
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name              # Character name
        self.health = health          # HP
        self.attack = attack          # Attack power
        self.defense = defense        # Defense level

    def hit(self, target):          # Method to attack another character
        damage = self.attack - target.defense      # Calculate damage
        damage = max(damage, 0)                     # Ensure no negative damage
        target.health -= damage                    # Subtract from target's health
        print(f"{self.name} hits {target.name} for {damage} damage.")

# Subclass Warrior with predefined attributes
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20, 10)

# Subclass Mage with different attributes
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 30, 5)

# Create characters
warrior = Warrior("Thor")
mage = Mage("Merlin")

# Characters attack each other
warrior.hit(mage)   # Thor attacks Merlin
mage.hit(warrior)   # Merlin attacks Thor

# Output:
# Thor hits Merlin for 15 damage.
# Merlin hits Thor for 20 damage.