def tokenize(lst: str):
    main_array = []

    for el in lst:
        array = []
        word = ""
        el = el.lower()

        for char in el:
            if char.isalpha():
                word += char
                continue

            if char.isdigit():
                word += char
                continue

            if char.isspace():
                char.replace(" ", "")

            array.append(word)

            if not char.isalpha() and not char.isdigit() and not char.isspace():
                array.append(char)

            word = ""

        main_array.extend(array)

        if "" in main_array:
            main_array.remove("")

    return main_array


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
