def factorial(a):
    f = 1
    for i in range(1, a + 1):
        f *= i
    return f


def noOccurances(b, a):
    pos = a.count(b)
    return pos
