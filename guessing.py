import random

random_number = random.randint(1,10) #numbers 1-10
guess = None

while guess != random_number:
    guess = input("pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("too low try again")
    elif guess > random_number:
        print("to high")
    else:
        print("you got this")





print(random_number)