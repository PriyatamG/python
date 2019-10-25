"""
Program that takes a string and checks the rank of the word among the different
permutations of the string arranged alphabetically as in a dictionary.
"""

import tools  # Additional program containing factorial() and noOccurances()

word = input("Enter the word")  # input the word
# Lists
letters = []  # List of the letters of word
Set = []  # Set of the letters

# Splitting letters
for i in word:
    letters.append(i)

# Sorting lists
letters.sort()
Set = set(letters)

# Variables
wlen = (len(word))
a = b = c = rank = pos = 0

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
            pos = tools.noOccurances(x, letters)
            q *= tools.factorial(pos)
        b = tools.factorial(wlen)
        rank += (b * a) / q
    letters.remove(letter)
# print(b, a, q, rank, sep="\t") - for debugging
print("rank:", rank)
