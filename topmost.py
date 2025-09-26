import sys
from wordfreq import tokenize, countWords, printTopMost


def main():
    stop_words_path = sys.argv[1]
    words_path = sys.argv[2]
    max_words_to_print = int(sys.argv[3])

    with open(stop_words_path, encoding="utf-8") as file:
        stop_words = file.read()

    with open(words_path, encoding="utf-8") as file:
        input_lines = file.readlines()

    words = tokenize(input_lines)
    word_counts = countWords(words, stop_words)

    printTopMost(word_counts, max_words_to_print)


if __name__ == "__main__":
    main()
