from classes.Ninja import Ninja
from classes.Samurai import Samurai
import random

Andrew = Samurai('Andrew')
Andrew.show_stats()

print('-------------------VS-------------------')

Stefanie = Ninja('Stefanie')
Stefanie.show_stats()

print("Ninja attacks Samurai")
Stefanie.attack(Andrew)
print("Samurai's health is now: ", Andrew.health)

print(f'The Samurai {Andrew.name} approaches the ninja {Stefanie.name}!')


while Andrew.health > 0 and Stefanie.health > 0:
    player_input = ""
    while not player_input == "1" and not player_input == "2":
        player_input = input(
            "What to do?\n 1) Attack\n 2) Use skill\n <=========>")
        if player_input == "1":
            Stefanie.attack(Andrew)
        elif player_input == "2":
            Andrew.attack(Stefanie)
        else:
            print("Choose a valid option! (1 or 2)")

    coin_toss = random.randint(1, 2)
    if coin_toss == 1:
        Andrew.attack(Stefanie)
    else:
        Stefanie.eat_apple()
    if coin_toss == 2:
        Stefanie.attack(Andrew)

    else:
        Andrew.drink_rum()

    if Andrew.health > 0:
        print("You win!")
    elif Stefanie.health <= 0:
        print("Draw!")
    else:
        print("The Ninja Wins!")
