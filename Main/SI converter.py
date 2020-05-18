import tkinter as tk

myWindow = tk.Tk()
myWindow.geometry('400x300')
myWindow.title("SI converter")
background_image = tk.PhotoImage(file='/home/ramana/PycharmProjects/python/Main/Background1.png')
background_label = tk.Label(myWindow, image=background_image)
background_label.place(x=0, y=0)
myWindow.resizable(height=False, width=False)
# myWindow.configure(background = 'cyan')

unit1Dict = {'Meter': 1, 'Centi meter': 0.01, 'Kilo meter': 1000}
unit2Dict = {'Meter': 1, 'Centi meter': 100, 'Kilo meter': 0.001}

unit1 = tk.StringVar()
unit2 = tk.StringVar()

units = {'Meter', 'Centi meter', 'Kilo meter'}

menu1 = tk.OptionMenu(myWindow, unit1, *units)
menu2 = tk.OptionMenu(myWindow, unit2, *units)
menu1.place(x=30, y=40)
menu2.place(x=270, y=40)

n1 = tk.DoubleVar()

entry1 = tk.Entry(textvariable=n1, width=30, bg='#E4D0CA')

entry1.place(x=20, y=100)

ans = tk.Label(text='', fg='black', bg='#E4D0CA')
ans.place(x=120, y=190)


def calc():
    x = n1.get() * unit1Dict[unit1.get()]
    y = x * unit2Dict[unit2.get()]
    ans['text'] = y


calButton = tk.Button(text="calculate", command=calc, bg='#DE7A5D')
calButton.place(x=60, y=130)

myWindow.mainloop()
