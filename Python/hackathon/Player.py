# HitPoints (hp), strength, defense(armor), mana(mp), currency
# Generic Super Base Class

class Player:
    def __init__(self):
        self.name = "Player"
        self.hp = 100
        self.strength = 15
        self.defense = 10


    def attack(self, target):
        print(f'{self.name} is attacking {target.name}!')
        target.defend(self.strength)

    def defend(self, dmg):
        dmg -= self.defense
        self.hp -= dmg
        print(f'{self.name} takes {dmg} and now has {self.hp}!')