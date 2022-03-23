from string import punctuation

def readFile(dictionary, sevenletter):
    """
    Purpose: Reads in the input file that contains the full text of a book,
             checking validity of each word in each line, before adding it to a
             list of lists, with the [word, number of appearances]
    Paramters: filename(str)
    Return Val: list of lists, with the [word, number of appearances]
    """
    readDict = open(dictionary, 'r')
    writeDict = open(sevenletter, 'w')
    punx = punctuation
    sevenLetter = ["word"]

    for line in readDict:
        line = line.lower()                 # line with no upper case characters
        line = line.split(',')                 # line with each word seperate
        word = line[0]
        frequency = int(line[1])
        numchars = len(word)
        if numchars == 7 and frequency > 4:
            writeDict.write(word + "\n")

    readDict.close()
    writeDict.close()
#------------------------------------------------------------------------------#
def main():
    sevenletter = readFile("wordCountsWordzzle.txt", "sevenletter.txt")


main()
