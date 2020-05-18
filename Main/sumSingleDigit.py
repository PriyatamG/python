n = int(input("Enter the number"))


def Sum(no):
    s = 0
    while no > 0:
        x = no % 10
        s += x
        no //= 10
    return s


while n >= 10:
    n = Sum(n)
else:
    print(n)
