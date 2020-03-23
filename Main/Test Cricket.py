import random
import time

while True:
    try:
        compScr = plrScr = m = 0
        OddOrEven = input("Odd or Even")
        comp = random.randint(0, 10)
        player = int(input("your chance"))
        print(player, comp, player + comp)
        if OddOrEven == "Odd":
            if (player + comp) % 2 == 0:
                t = False
                print("You are bowling")
                batter = "Computer"
                m = "Player"
            else:
                t = True
                print("You are batting")
                batter = "Player"
                m = "Computer"
        if OddOrEven == "Even":
            if (player + comp) % 2 == 0:
                t = True
                batter = "Player"
                m = "Computer"
                print("You are batting")
            else:
                t = False
                print("You are bowling")
                batter = "Computer"
                m = "Player"
        AI = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        while True:
            player = int(input("your chance"))
            if batter == "Player":
                AI.append(player)
                comp = random.choice(AI)
            else:
                comp = random.randint(0, 10)

            if player != comp:
                if t:
                    plrScr += player
                    batter = "Player"
                    bowler = "Computer"
                    m = plrScr
                else:
                    compScr += comp
                    batter = "Computer"
                    bowler = "Player"
                    m = compScr
            print(player, comp, plrScr, compScr, sep="\t")
            if plrScr == 0 or compScr == 0:
                if player == comp:
                    n = m
                    print(batter, "Out", bowler, "needs", m + 1, "runs to win")
                    time.sleep(2.5)
                    print('<-------------------------------->', "SECOND INNINGS START", sep='\n')
                    if t:
                        t = False
                    elif not t:
                        t = True

            elif player == comp or m > n:
                if plrScr > compScr:
                    result = "Player wins"
                elif compScr > plrScr:
                    result = "Computer wins"
                else:
                    result = "Draw"
                break
        print("Final scores:\n", "Player", "Computer", sep="\t")
        print("", plrScr, compScr, sep="\t\t")
        print("Result:", result)
        break
    except:
        print("excp")
