def countWords(words, stopWords):
    wordCount = {}
    for word in words:
        if word not in stopWords:
            if word in wordCount:
                wordCount[word] += 1
            else:
                wordCount.setdefault(word, 1)
    
    
    return wordCount


# w = [
#     "apple", "banana", "cherry", "apple", "date",
#     "banana", "apple", "fig", "grape", "banana",
#     "cherry", "apple", "fig", "honeydew", "grape"
# ]

# sw = ["fig", "honeydew"]

# print(countWords(w, sw)) # => {'apple': 4, 'banana': 3, 'cherry': 2, 'date': 1, 'grape': 2}
            
