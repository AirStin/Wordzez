
import random

def getWords():
    wordsFile = open("sevenLetterWords.txt", 'r')
    wordList = []

    for word in wordsFile:
        word = word.strip()
        wordList.append(word)

    return wordList

def pickWord(wordList):
    word = random.choice(wordList)
    return word

def displayWord(word, guess):

    displayedWord = []
    for letter in word:
        displayedWord += "_"

    guessList = []

    wordList = []

    for char in guess:
        guessList += char

    for char in word:
        wordList += char

    for i in range(len(guess)):
        if guessList[i] == wordList[i]:
            displayedWord[i] = guess[i]
            guessList.pop(i)
            guessList.insert(i, "nothing")
            wordList.pop(i)
            wordList.insert(i, "nada")
        else:
            #wordCount = 0
            #guessCount = 0
            for j in range(len(word)):
                #for wordList[j] in wordList:
                    #wordCount += 1
                #for wordList[j] in guessList:
                    #guessCount += 1
                if guess[i] == wordList[j]:
                    if guess[j] == wordList[j]: #and guessCount <= wordCount:
                        break
                    else:
                        displayedWord[i] = "<" + guess[i] + ">"
                        guessList.pop(i)
                        guessList.insert(i, "nothing")
                        wordList.pop(j)
                        wordList.insert(j, "nada")
                        print(wordList)
                        break


    return displayedWord

def getGuess():

    guess = input("Enter a 7 letter word: ")
    while True:
        if len(guess) == 7 and guess.isalpha() == True:
            return(guess)
        else:
            guess = input("illegal choice; enter a 7 letter word: ")

def main():

    guess = ""
    guesses = 0
    wordList = getWords()
    word = pickWord(wordList)
    print(word)

    displayedWord = ["_", "_", "_", "_", "_", "_", "_"]
    print(displayedWord)

    while guesses < 7:

        guess = getGuess()

        displayedWord = displayWord(word, guess)
        print(displayedWord)

        if guess == word:
            print("die")
            return

        guesses += 1



main()
