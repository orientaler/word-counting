def tokenize(txt:str):
    array = []
    word = ""
    print(word)
    txt = txt.lower()
    print(txt)
    for char in txt:
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
            word += char
            word = word[:-1]
            array.append(char)

        word = ""
            

    array.remove("")
    return array


print(tokenize('12 cider is not grey, but it can be almost grey.'))
