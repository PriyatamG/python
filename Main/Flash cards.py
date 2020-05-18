import random

words = []
meanings = []

for i in mainDict:
    word = random.choice(words)
    ctr = input("")
    if ctr in 'Mm':
        print()
    else:
        pass