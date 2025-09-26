def tokenize(lines: list[str]):
    tokens = []

    for line in lines:
        words = []
        word = ""
        word_type = None
        line = line.lower()

        for char in line:
            if char.isalpha() and word_type != "number":
                word += char
                word_type = "word"
                continue

            if char.isdigit() and word_type != "word":
                word += char
                word_type = "number"
                continue

            if word:
                words.append(word)

            if not char.isspace():
                if char.isalpha() or char.isdigit():
                    word = char
                    word_type = "word" if char.isalpha() else "number"
                    continue

                words.append(char)

            word = ""
            word_type = None

        if word:
            words.append(word)

        tokens.extend(words)

        if "" in tokens:
            tokens.remove("")

    return tokens


def countWords(words, stop_words):
    word_count = {}
    for word in words:
        if word not in stop_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count.setdefault(word, 1)

    return word_count


def printTopMost(frequencies, max_words_to_print):
    sorted_frequencies = sorted(
        frequencies.items(), key=lambda item: item[1], reverse=True
    )

    for i in range(min(max_words_to_print, len(sorted_frequencies))):
        print(
            f"{sorted_frequencies[i][0].ljust(20)}{str(sorted_frequencies[i][1]).rjust(5)}"
        )
