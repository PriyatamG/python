l = eval(input("Enter the list"))
x = len(l)
f =[]
for i in range(x):
    e = l[i]
    for j in e:
        f.append(j.upper())
print(f)