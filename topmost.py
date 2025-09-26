from wordfreq import tokenize, countWords, printTopMost
import sys


def main():
    stopWordsFile = open(sys.argv[1])
    stopWords = stopWordsFile.read()
    stopWordsFile.close()

    wordsFile = open(sys.argv[2])
    words = wordsFile.readlines()
    wordsFile.close()

    printTopMost(countWords(tokenize(words), stopWords), int(sys.argv[3]))


if __name__ == "__main__":
    main()
