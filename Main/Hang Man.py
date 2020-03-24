import random
from random_word import RandomWords

def canvas(word):
    wordLc = list(word)
    canvas = list('_'* len(word))
    noLetters = len(word)//4
    for i in range(noLetters):
        char = random.choice(word)
        while wordLc.count(char) != 0:
            x = wordLc.index(char)
            canvas[x] = char
            wordLc[x] = ''
    return canvas


def guess(wordL,g):
    if g in wordL:
        return True
    else:
        return False


r = RandomWords()
word = r.get_random_word()
wordL = list(word)
canvas = canvas(wordL)
print(*canvas)

for i in range(10):
    g = input("What is your guess ?")
    if guess(wordL,g):
        while wordL.count(g) != 0:
            x = wordL.index(g)
            canvas[x] = g
            wordL[x] = ''
        print(*canvas)
        print(9 - i, 'chances left')
    elif g == word :
        print("CORRECT")
        break
    else:
        print("INCORRECT")
        print(9-i,'chances left')
    if canvas == list(word):
        print("Correct")
        break
else:
    print("The word is:-- ",word)