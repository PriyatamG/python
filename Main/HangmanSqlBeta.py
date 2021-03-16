import mysql.connector as sql
import random

database = sql.connect(host = "localhost", user = "root", passwd = "", database = "world")
if database.is_connected():
	print("Succesfully connected")

cursor = database.cursor()



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


randint = random.randint(1,2000)
query = "SELECT Name, District FROM city WHERE ID = " + str(randint)

cursor.execute(query)

lol = cursor.fetchall()
dataset = lol[0]
print(dataset)

word = dataset[0]
place = dataset[1]


wordL = list(word)
canvas = canvas(wordL)
print(*canvas)
print("District:",place)
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
