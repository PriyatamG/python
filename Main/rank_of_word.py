"""
Program that takes a string and checks the rank of the word among the different
permutations of the string arranged alphabetically as in a dictionary.
"""
import math

def noOccurances(b, a):
    pos = a.count(b)
    return pos

while True:
    word = input("Enter the word")  # input the word
    # Lists
    word = word.lower()
    letters = list(word)  # List of the letters of word
    letters.sort()  # Sorting lists
    Set = set(letters)  # Set of letters

    # Variables
    wlen = (len(word))
    a = b = c = rank = pos = 0
    count = 0
    # Main loop
    for letter in word:
        a = letters.index(letter)
        wlen -= 1
        if wlen == 0:
            wlen = 1
            a = 1
        q = 1
        if a != 0:
            for x in Set:  # Loop for duplicates
                pos = noOccurances(x, letters)
                q *= math.factorial(pos)
                count += 1
            b = math.factorial(wlen)
            rank += (b * a) / q
        letters.remove(letter)

       # print(b, a, q, rank, sep="\t") # for debugging
    print("rank:", rank)
    print(count)
