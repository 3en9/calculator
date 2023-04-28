from tkinter import *


def calculate(exp: str):
    try:
        return eval(exp)
    except SyntaxError:
        return 'Error'


def add(s):
    val = txt_var.get()
    txt_var.set(val+s)


def clear():
    txt_var.set('')


def erase():
    txt_var.set(txt_var.get()[:-1])


def calc():
    txt_var.set(str(calculate(txt_var.get())))


window = Tk()
window.title("Calculator")
window.geometry('250x330')
window.resizable(False, False)
txt_var = StringVar()
txt = Entry(window, font=40, justify=LEFT, bg='white', textvariable=txt_var, state='readonly')
txt.place(x=0, y=0, width=330, height=35)

btn1 = Button(window, text='1', command=lambda: add('1'), font=25)
btn1.place(x=10, y=100, width=50, height=50)
btn2 = Button(window, text='2', command=lambda: add('2'), font=25)
btn2.place(x=62, y=100, width=50, height=50)
btn3 = Button(window, text='3', command=lambda: add('3'), font=25)
btn3.place(x=114, y=100, width=50, height=50)

btn4 = Button(window, text='4', command=lambda: add('4'), font=25)
btn4.place(x=10, y=152, width=50, height=50)
btn5 = Button(window, text='5', command=lambda: add('5'), font=25)
btn5.place(x=62, y=152, width=50, height=50)
btn6 = Button(window, text='6', command=lambda: add('6'), font=25)
btn6.place(x=114, y=152, width=50, height=50)

btn7 = Button(window, text='7', command=lambda: add('7'), font=25)
btn7.place(x=10, y=204, width=50, height=50)
btn8 = Button(window, text='8', command=lambda: add('8'), font=25)
btn8.place(x=62, y=204, width=50, height=50)
btn9 = Button(window, text='9', command=lambda: add('9'), font=25)
btn9.place(x=114, y=204, width=50, height=50)

btn0 = Button(window, text='0', command=lambda: add('0'), font=25)
btn0.place(x=62, y=256, width=50, height=50)

btnp = Button(window, text='+', command=lambda: add('+'), font=25)
btnp.place(x=168, y=100, width=50, height=50)
btnm = Button(window, text='-', command=lambda: add('-'), font=25)
btnm.place(x=168, y=152, width=50, height=50)
btnu = Button(window, text='*', command=lambda: add('*'), font=25)
btnu.place(x=168, y=204, width=50, height=50)
btnd = Button(window, text='/', command=lambda: add('/'), font=25)
btnd.place(x=168, y=256, width=50, height=50)
btnr = Button(window, text='=', command=lambda: calc(), font=25)
btnr.place(x=114, y=256, width=50, height=50)

btnso = Button(window, text='(', command=lambda: add('('), font=25)
btnso.place(x=10, y=42, width=50, height=50)
btnsz = Button(window, text=')', command=lambda: add(')'), font=25)
btnsz.place(x=62, y=42, width=50, height=50)

btnsc = Button(window, text='C', command=lambda: clear(), font=25)
btnsc.place(x=114, y=42, width=50, height=50)

btne = Button(window, text='<--', command=lambda: erase(), font=25)
btne.place(x=168, y=42, width=50, height=50)

btnt = Button(window, text='.', command=lambda: add('.'), font=25)
btnt.place(x=10, y=256, width=50, height=50)
window.mainloop()
