import random


def canvas(word):
    wordLc = list(word)
    canvas = list('_' * len(word))
    noLetters = len(word) // 4
    for i in range(noLetters):
        char = random.choice(word)
        while wordLc.count(char) != 0:
            x = wordLc.index(char)
            canvas[x] = char
            wordLc[x] = ''
    return canvas


def guess(wordL, g):
    if g in wordL:
        return True
    else:
        return False


with open('/home/ramana/PycharmProjects/python/Main/wordList.txt') as f:
    r = f.read().splitlines()
try:
    randNum = random.randint(0, len(r))
    word = r.__getitem__(randNum)
except:
    print("Word not found")
    word = 'error'
wordL = list(word)
canvas = canvas(wordL)
print(*canvas)

for i in range(10):
    g = input("What is your guess ?")
    if guess(wordL, g):
        while wordL.count(g) != 0:
            x = wordL.index(g)
            canvas[x] = g
            wordL[x] = ''
        print(*canvas)
        print(9 - i, 'chances left')
    elif g == word:
        print("CORRECT")
        break
    else:
        print("INCORRECT")
        print(9 - i, 'chances left')
        print(*canvas)
    if canvas == list(word):
        print("Correct")
        break
else:
    print("The word is:-- ", word)
