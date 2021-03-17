import mysql.connector as sql
import random



def canvas1(word):
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




database = sql.connect(host = "localhost", user = "root", passwd = "", database = "world")
databaseLeader = sql.connect(host = "localhost", user="root", passwd= "", database = "autos")

if database.is_connected():
    print("Succesfully connected")

cursor = database.cursor()
cursorLeader = databaseLeader.cursor()

Name = input("Enter your name")

streak = True
score = 0
while streak == True:

    randint = random.randint(1,2000)
    query = "SELECT Name, District FROM city WHERE ID = " + str(randint)

    cursor.execute(query)

    lol = cursor.fetchall()
    dataset = lol[0]
    print(dataset)

    word = dataset[0]
    place = dataset[1]


    wordL = list(word)
    canvas = canvas1(wordL)
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
            score+=1
            break
        else:
            print("INCORRECT")
            print(9 - i, 'chances left')
            print(*canvas)
        if canvas == list(word):
            print("Correct")
            score += 1
            break
    else:
        print("The word is:-- ", word)
        print("Your score is", score)
        streak = False


query2 = "INSERT INTO bois (Name, Total, Best, Worst) values('"+ Name+"'," +str(score)+",0,0)"
cursorLeader.execute(query2)
databaseLeader.commit()

query3 = "select * from bois order by Total DESC"
cursorLeader.execute(query3)

lol = cursorLeader.fetchall()

print("\t 𝙇𝙚𝙖𝙙𝙚𝙧𝙗𝙤𝙖𝙧𝙙")
rank = 1
for i in lol:
    print(rank,i[0],"\t", i[1])
    rank+=1

cursor.close()
cursorLeader.close()
