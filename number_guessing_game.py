import random

random_number = random.randint(1, 100)
while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess > random_number:
        print("Too high")
    elif user_guess < random_number:
        print("Too low")
    else:
        print("You got it!")
        break