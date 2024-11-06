import random


def numberGuess():
    winningNumber = random.randint(0,100)
    # print(f"the winning number is: {winningNumber}")
    inputNum = 0
    inputStr = ""
    while inputStr != "e" and inputStr != "h":
        inputStr = input("Select difficulty: (e)asy: 10 guesses or (h)ard: 5 guesses: " ).lower()
        if inputStr == "e":
            numOfGuesses = int(10)
        if inputStr == "h":
            numOfGuesses = int(5)
    while (inputNum != winningNumber and numOfGuesses > 0):    
        inputNum = input(f"guess the number. You have {numOfGuesses} guesses left: ")
        inputNum = int(inputNum)
        print(f"you guessed: {inputNum}")
        if (inputNum != winningNumber):
            numOfGuesses = numOfGuesses-1
            if(inputNum > winningNumber):
                print("guess lower")
            if(inputNum < winningNumber):
                print("guess higher")
        else:
            return print(f"you guessed the number ({winningNumber}) with {numOfGuesses} guesses remaining!")
    print(f"game over. The number was {winningNumber}")

if __name__ == '__main__':
    main()
    