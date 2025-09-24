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
                word += char
                word = word[:-1]
                array.append(char)

            word = ""
            
        if ("") in array:
            array.remove("")

        main_array.extend(array)

    return main_array
