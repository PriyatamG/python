lst = []
for a in range(0, 9):
    lst.append(str(a))
x = 'abcdefghijklmnoprqstuvwxyz'
y = x.upper()
for a in x:
    lst.append(a)
for a in y:
    lst.append(a)
for a in '!@#$%^&*()_+-=?':
    lst.append(a)
print(lst)
