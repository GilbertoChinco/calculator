from tkinter import *
#
root = Tk()
root.configure(background="#333333")
root.geometry("75x150")
root.title("Calculator")
#
#   Functions
#
equation = StringVar()
#
def press(num):
    equation.set(equation.get() + str(num))
#   
def equal_press():
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except:
        equation.set("error")

def clear():
    equation.set("")
#
#   Grid Layout
#
expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, columnspan=4, sticky="nswe")
#
btn_7 = Button(root, text=" 7 ", fg="#fff", bg="#666", command=lambda: press(7))
btn_7.grid(row=1, column=0, sticky="nswe")
#
btn_8 = Button(root, text=" 8 ", fg="#fff", bg="#666", command=lambda: press(8))
btn_8.grid(row=1, column=1, sticky="nswe")
#
btn_9 = Button(root, text=" 9 ", fg="#fff", bg="#666", command=lambda: press(9))
btn_9.grid(row=1, column=2, sticky="nswe")
#
btn_4 = Button(root, text=" 4 ", fg="#fff", bg="#666", command=lambda: press(4))
btn_4.grid(row=2, column=0, sticky="nswe")
#
btn_5 = Button(root, text=" 5 ", fg="#fff", bg="#666", command=lambda: press(5))
btn_5.grid(row=2, column=1, sticky="nswe")
#
btn_6 = Button(root, text=" 6 ", fg="#fff", bg="#666", command=lambda: press(6))
btn_6.grid(row=2, column=2, sticky="nswe")
#
btn_1 = Button(root, text=" 1 ", fg="#fff", bg="#666", command=lambda: press(1))
btn_1.grid(row=3, column=0, sticky="nswe")
#
btn_2 = Button(root, text=" 2 ", fg="#fff", bg="#666", command=lambda: press(2))
btn_2.grid(row=3, column=1, sticky="nswe")
#
btn_3 = Button(root, text=" 3 ", fg="#fff", bg="#666", command=lambda: press(3))
btn_3.grid(row=3, column=2, sticky="nswe")
#
btn_0 = Button(root, text=" 0 ", fg="#fff", bg="#666", command=lambda: press(0))
btn_0.grid(row=4, column = 0, columnspan=2, sticky="nswe")
#
btn_decimal = Button(root, text=" . ", fg="#fff", bg="#666", command=lambda: press("."))
btn_decimal.grid(row=4, column=2, sticky="nswe")
#
plus = Button(root, text=" + ", fg="#fff", bg="#fe9727", command=lambda: press("+"))
plus.grid(row=1, column=3, sticky="nswe")
#
minus = Button(root, text=" - ", fg="#fff", bg="#fe9727", command=lambda: press("-"))
minus.grid(row=2, column=3, sticky="nswe")
#
multiply = Button(root, text=" * ", fg="#fff", bg="#fe9727", command=lambda: press("*"))
multiply.grid(row=3, column=3, sticky="nswe")
#
divide = Button(root, text=" / ", fg="#fff", bg="#fe9727", command=lambda: press("/"))
divide.grid(row=4, column=3, sticky="nswe")
#
equal = Button(root, text=" = ", fg="#fff", bg="#fe9727", command=equal_press)
equal.grid(row=5, column=3, sticky="nswe")
#
clear = Button(root, text=" clear ", fg="#fff", bg="#999", command=clear)
clear.grid(row=5, column=2, sticky="nswe")
#
root.mainloop()