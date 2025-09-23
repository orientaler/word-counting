def printTopMost(frequencies, n):
    sorted_frequencies =  sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    
    for i in range(min(n, len(sorted_frequencies))):
        print(f"{sorted_frequencies[i][0].ljust(20)}{str(sorted_frequencies[i][1]).rjust(5)}")
