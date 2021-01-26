from random import randrange

i = 0

while i == 0:
    a = randrange(11)
    b = str(a)
    guess = input("Please guess a number between 0-10: ")
    if guess != "":
        if guess == b:
            print("You have guessed correctly")
            i += 1
        elif guess != b:
            print("That is wrong, please guess again...")
    else:
        print("You didn't enter a number!")
