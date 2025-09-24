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

print(tokenize(['"They had 16 rolls of duct tape, 2 bags of clothes pins,','130 hampsters from the cancer labs down the hall, and','at least 500 pounds of grape jello and unknown amounts of chopped liver"','said the source on a recent Geraldo interview.']))