#Imports
import sys

#Welcome message
print("Welcome to Hangman!")
    
#Remainder of attempts left
tries = 6

#The word needing to be matched and the answer the user is giving.
#Also prints out the currently already guessed letters
question = ["t", "h", "e", "d", "e", "p", "a", "r", "t", "e", "d"]

answer = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

guessedLetters = []

#Check if the user has completed the game checking if there are any underscores left in the answer array. 
#If there are then the game continues, if not the game ends.
def isGameOver():
    j = 0
    for n, i in enumerate(answer):
        if i == "_":
            j += 1
    if j > 0:
        return False
    else:
        return True

#Main functionaility asking the user to guess and then checking through the question array if there is a match.
#If there is a match the letter is added to the answer array and printed out
#If there is no match the user is deducted a try
#If the letters are guessed correct the game finishes congratulatig the user
#If tries run out the player loses and the game is over
while True:
    try:
        if tries > 0 and isGameOver() == False:
            x = input("Please enter a letter to guess: ")
            userInput = x.strip()
            if userInput.isalnum() == True and len(userInput) < 2:
                j = 0
                for n, i in enumerate(question):
                    if i == userInput:
                        answer[n] = i
                        j += 1
                if j == 0:
                    tries -= 1
                print("You have " + str(tries) + " tries left")
                guessedLetters.append(userInput)
                print(answer)
                print("Already guessed letters are: ")
                print(guessedLetters)
            else:
                print("Please enter a single valid letter or number")
        elif isGameOver() == True and tries > 0:
            print("You have guessed correctly! Congratulations!")
            sys.exit()
        elif tries <= 0:
            print("You have ran out of tries. GAME OVER!")
            sys.exit()
    except ValueError:
        continue