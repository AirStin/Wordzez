
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
    """
    for i in range(len(guess)):
        if guess[i] == word[i]:
            displayedWord[i] = word[i]

    wordLetterCount = 0
    guessLetterCount = 0

    for i in range(len(guess)):
        if guess[i] in word and guess[i] != word[i]:
            for j in range(len(word)):
                if guess[i] == word[j]:
                    wordLetterCount += 1

            for j in range(len(displayedWord)):
                if guess[i] == displayedWord[j] or "<" + guess[i] + ">" == displayedWord[j]:
                    guessLetterCount += 1

            if guessLetterCount < wordLetterCount:
                displayedWord[i] = "<" + guess[i] + ">"
    """
    for i in range(len(word),-1):
        if word[i] == guess[i]:
            displayedWord[i] = guess[i]
            word.remove(i)
            guess.remove(i)

    for i in range(len(word), -1):
        for j in range(len(guess)):
            if word[i] == guess[j]:
                displayedWord[j] = "<" + guess[j] + ">"
                word.remove(i)


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
