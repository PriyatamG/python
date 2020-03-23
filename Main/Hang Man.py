import random
from random_word import RandomWords
r = RandomWords()
word = r.get_random_word(hasDictionaryDef="true")
print(word)
wordL = list(word)
def canvas(word):
    wordLc = list(word)
    canvas = list('_'* len(wordLc))
    noLetters = len(word)//4
    for i in range(noLetters):
        char = random.choice(wordLc)
        x = wordLc.index(char)
        canvas[x] = char
        wordLc.remove(char)
    return canvas
canvas = canvas(wordL)
print(*canvas)

def guess(wordL,g):
    if g in wordL:
        return True
    else:
        return False

for i in range(10):
    g = input("What is your guess ?")
    if guess(wordL,g):
        canvas[wordL.index(g)] = g
        print(*canvas)
    elif g == word or canvas == wordL:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
