#Calculator Application Using Tkinter

#Modules 

from tkinter import *


#Functions


def button_click (value) :
    current_value = entry_box.get()

    entry_box.delete(0, END)
    entry_box.insert(0, str(current_value) + str(value))

def clear () :
    entry_box.delete(0, END)

def add () :
    first_value = entry_box.get()

    entry_box.delete(0, END)

    global first_number
    first_number = int(first_value)


def equal () :
    second_number = int(entry_box.get())

    entry_box.delete(0, END)

    entry_box.insert(0, first_number + second_number)



def calculator () :

    window = Tk()

    window.title("Calculator")

    #Entry Box
    global entry_box
    entry_box = Entry(window, width=35, borderwidth=5)
    entry_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    #Button Creation
    button_0 = Button(window, text="0", padx=40, pady=20, command=lambda : button_click(0))
    button_1 = Button(window, text="1", padx=40, pady=20, command=lambda : button_click(1))
    button_2 = Button(window, text="2", padx=40, pady=20, command=lambda : button_click(2))
    button_3 = Button(window, text="3", padx=40, pady=20, command=lambda : button_click(3))
    button_4 = Button(window, text="4", padx=40, pady=20, command=lambda : button_click(4))
    button_5 = Button(window, text="5", padx=40, pady=20, command=lambda : button_click(5))
    button_6 = Button(window, text="6", padx=40, pady=20, command=lambda : button_click(6))
    button_7 = Button(window, text="7", padx=40, pady=20, command=lambda : button_click(7))
    button_8 = Button(window, text="8", padx=40, pady=20, command=lambda : button_click(8))
    button_9 = Button(window, text="9", padx=40, pady=20, command=lambda : button_click(9))

    button_additon = Button(window, text="+", padx=39, pady=20, command=add)
    button_clear = Button(window, text="Clear", padx=84, pady=20, command=clear)
    button_equal = Button(window, text="=", padx=95, pady=20, command=equal)



    #Button Placement
    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
    button_additon.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)


    window.mainloop()


#__main__
calculator()