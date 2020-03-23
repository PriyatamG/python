l = eval(input(">?"))
x = len(l)
for j in range(1, x):
    for i in range(x-1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]
print(l)
