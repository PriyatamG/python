lst = eval(input())
for i in range(0,len(lst)):
    x = lst[i]-1
    if lst[x] < 0:
        print(lst[i])
    else:
        lst[x] = lst[x]*-1
