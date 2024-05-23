# A classic game of Snake Water Gun (a spin-off of Rock Paper Scissors)

import random


def gameWin(comp, user):
    # If two values are equal, declare a tie
    if comp == user:
        return None

    # Check for all possibilities when computer chose 's' (Snake)
    elif comp == 's':
        if user == 'w':
            return False
        elif user == 'g':
            return True

    # Check for all possibilities when computer chose 'w' (Water)
    elif comp == 'w':
        if user == 'g':
            return False
        elif user == 's':
            return True

    # Check for all possibilities when computer chose 'g' (Gun)
    elif comp == 'g':
        if user == 's':
            return False
        elif user == 'w':
            return True


def fin_result(abbreviation):
    if abbreviation == 's':
        return 'Snake'
    elif abbreviation == 'w':
        return 'Water'
    elif abbreviation == 'g':
        return 'Gun'


print("Computer's Turn- SNAKE(s) WATER(w) GUN(g) ?")
randNum = random.randint(1, 3)
if randNum == 1:
    comp = 's'
elif randNum == 2:
    comp = 'w'
elif randNum == 3:
    comp = 'g'


user = input("Your Turn: Snake(s) Water(w) or Gun(g)? : ")

# Determine the result of the game
a = gameWin(comp, user)


print(f"Computer chose {fin_result(comp)}")
print(f"You chose {fin_result(user)}")

# Display the result
if a == None:
    print('The game is a TIE')
elif a:
    print('You WIN')
else:
    print('You LOSE')
