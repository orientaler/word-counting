def tokenize(lst:str):
    main_array = []
    
    for el in lst:
        array = []
        word = ""
        el = el.lower()
        
        for char in el:
            if char.isalpha():
                word += char
                continue

            elif char.isdigit():
                word += char
                continue
            
            elif char.isspace():
                char.replace(" ", "") 

            array.append(word)
            
            if not char.isalpha() and not char.isdigit() and not char.isspace():
                array.append(char)

            word = ""
            
        main_array.extend(array)

        if ("") in main_array:
            main_array.remove("")


    return main_array


def countWords(words, stopWords):
    wordCount = {}
    for word in words:
        if word not in stopWords:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount.setdefault(word, 1)
    
    
    return wordCount

def printTopMost(frequencies, n):
    sorted_frequencies =  sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    
    for i in range(min(n, len(sorted_frequencies))):
        print(f"{sorted_frequencies[i][0].ljust(20)}{str(sorted_frequencies[i][1]).rjust(5)}")
