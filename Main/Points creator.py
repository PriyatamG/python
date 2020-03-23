def Points(string):
    s = ''
    for i in range(len(string)):
        if string[i - 1] == '.' or i == 0:
            s += '\n'
            s += string[i].upper()
        else:
            s += string[i]
    return s

#i = open('.//home/ramana/Documents/Manas_Abhilash_Gundapuneni_MNNIT_Allahabad.pdf')

print(Points(input("Start writing !\n")))
