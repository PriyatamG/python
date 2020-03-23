lst = eval(input(">?"))
for i in range(1,len(lst)):
    key = lst[i]
    j = i-1
    while j>=0 and lst[j] > key:
        lst[j+1] = lst[j]
        j-=1
    else:
        lst[j+1] = key
print(lst)