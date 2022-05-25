
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

    wordList = []

    guessList = []

    for char in word:
        wordList += char

    for char in guess:
        guessList += char

    for i in range(len(guessList)):
        if guessList[i] == wordList[i]:
            displayedWord[i] = wordList[i]
            wordList[i] = "nada"
            guessList[i] = "nadie"

    for i in range(len(guessList)):
        if guessList[i] in wordList:
            idx = wordList.index(guessList[i])
            displayedWord[i] =  "<" + guessList[i] + ">"
            wordList[idx] = "nada"
            guessList[i] = "nadie"

    return displayedWord

def getGuess(wordList):

    guess = input("Enter a 7 letter word: ")
    while True:
        if len(guess) == 7 and guess.isalpha() == True and guess in wordList:
            return(guess)
        else:
            guess = input("illegal choice; enter a 7 letter word: ")

def main():

    guess = ""
    guesses = 0
    wordList = getWords()
    word = pickWord(wordList)

    displayedWord = ["_", "_", "_", "_", "_", "_", "_"]
    print(displayedWord)

    while guesses < 7:

        guess = getGuess(wordList)

        displayedWord = displayWord(word, guess)
        print(displayedWord)

        if guess == word:
            print("die")
            return

        guesses += 1

    if guess != word:
        print("the word was " + word + "\nGod ur stoopid")



main()
