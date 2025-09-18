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

        if char.isdigit():
            word += char
            continue
        
            
        word += char
        
        array.append(word)
        print(array)
        word = ""
    return array

tokenize('12 cider is not grey, but it can be almost grey.')





#insert(array)



# def tokenize(lines):
#     words = []
#     for line in lines:
#         start = 0
#         while start < len(line):
#             print(line[start])
#             start = start+1
#             print(line.split())
    

# print()" , ".join(input.lower().split(", ").split(". ")).split())