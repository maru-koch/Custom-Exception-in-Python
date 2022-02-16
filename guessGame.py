
from random import randint

game = True
life = 0
random_number = randint(1, 10)

class NumberTooLarge(Exception):
    pass

class NumberTooSmall(Exception):
    pass

while game:
    if life >= 4:
        print("Game Over. You lost!")
        break
    try:
        user_guess = int(input('Guess a number: '))
        if user_guess > random_number:
            raise NumberTooLarge
     
        if   user_guess < random_number:
            raise NumberTooSmall
    except ValueError:
        print("Invalid value")
    
    except NumberTooSmall:
        print(f"{user_guess} is too small")
    except NumberTooLarge:
        print(f"{user_guess} is too large")
    else:
        print("Correct!, you won")
        game = False 
    finally:
        life += 1