import random


class Warrior:
    health = 100

    @staticmethod
    def attack(enemy, v):
        enemy.health -= v
        print(f'{enemy.name} was attacked, his health is {enemy.health}')

    def set_name(self, name):
        self.name = name


class Battle:
    def battle(self, u_1, u_2):
        while u_1.health > 0 and u_2.health > 0:
            if random.randint(1, 2) == 1:
                Warrior.attack(u_2, 20)
            else:
                u_2.attack(u_1, 20)

        if u_1.health == 0:
            self.result = f'\n{u_2.name} has won!'
        else:
            self.result = f'\n{u_1.name} has won!'

    def who_won(self):
        print(self.result)
