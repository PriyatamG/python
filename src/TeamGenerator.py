import random
from builtins import print
from typing import List

def enterNames():
    students = []
    while True:
        name = input("Enter the name")
        students.append(name)
        q1 = input("Do you want to add or continue? [y/n]")
        if q1 == "n" or q1 == "N" or q1 == "No":
            return students
            break
        else:
            continue


def rollNo():
    n = int(input("Enter the class strength"))
    students = [[i] for i in range(1, n + 1)]
    return students

while True:

    while True:
        q2 = input("Do you want to add names or roll numbers ? [N/R]")
        if q2 == "N":
            students = enterNames()
            break
        elif q2 == "R":
            students = rollNo()
            break
        else:
            continue

    x = len(students)
    tNum = 0

    # Number of teams
    print('The possible number of teams are')
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

    y = int(input("Enter the no of teams"))
    z = int(x / y)

    # Loop
    while x > 0:
        if x % z == 0:
            print("Team", tNum + 1)
            tNum += 1
        choice = random.choice(students)
        students.remove(choice)
        x = len(students)
        print(choice)

    q3 = input("Do you want to close or continue ? [y/n]")

    if q3 == "y":
        continue
    else:
        break
