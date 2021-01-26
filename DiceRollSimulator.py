from random import randrange

while True:
    try:
        userInput = input("Input Roll to roll the dice! ").lower()
        if userInput == "roll":
            print(randrange(1,7))
        else:
            print("Please enter Roll!")
    except ValueError:
        continue