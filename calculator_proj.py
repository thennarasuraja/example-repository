from tkinter import*
                              #   using tkinster library 

exp=""


def press(number):
    global exp
    exp+=str(number)
    equation.set(exp)


def equalpress():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        expression=""
    except:
        equation.set("syntex error")
        exp=""


def clear():
    global exp
    exp=""
    equation.set("")


object=Tk()
object.configure(background="grey")
object.title("calcultor by codewithcurious.com")
object.geometry("300x250")

equation=StringVar()


Text_Entry_box=Entry(object,textvariable=equation,width=6)
Text_Entry_box.grid(columnspan=8,ipadx=100)

button1=Button(object, text="1", fg="black",bg="#8f8f8f",command=lambda: press(1), height=2,width=7)
button1.grid(row=2,column=0)

button2=Button(object, text="2", fg="black",bg="#8f8f8f",command=lambda: press(2), height=2,width=7)
button2.grid(row=2,column=1)

button3=Button(object, text="3", fg="black",bg="#8f8f8f",command=lambda: press(3), height=2,width=7)
button3.grid(row=2,column=2)

button4=Button(object, text="4", fg="black",bg="#8f8f8f",command=lambda: press(4), height=2,width=7)
button4.grid(row=3,column=0)

button5=Button(object, text="5", fg="black",bg="#8f8f8f",command=lambda: press(5), height=2,width=7)
button5.grid(row=3,column=1)

button6=Button(object, text="6", fg="black",bg="#8f8f8f",command=lambda: press(6), height=2,width=7)
button6.grid(row=3,column=2)

button7=Button(object, text="7", fg="black",bg="#8f8f8f",command=lambda: press(7), height=2,width=7)
button7.grid(row=4,column=0)

button8=Button(object, text="8", fg="black",bg="#8f8f8f",command=lambda: press(8), height=2,width=7)
button8.grid(row=4,column=1)

button9=Button(object, text="9", fg="black",bg="#8f8f8f",command=lambda: press(9), height=2,width=7)
button9.grid(row=4,column=2)

button0=Button(object, text="0", fg="black",bg="#8f8f8f",command=lambda: press(0), height=2,width=7)
button0.grid(row=5,column=0)

plus=Button(object, text="+", fg="black",bg="#8f8f8f",command=lambda: press("+"), height=2,width=7)
plus.grid(row=2,column=3)

minus=Button(object, text="-", fg="black",bg="#8f8f8f",command=lambda: press("-"), height=2,width=7)
minus.grid(row=3,column=3)

multiply=Button(object, text="*", fg="black",bg="#8f8f8f",command=lambda: press("*"), height=2,width=7)
multiply.grid(row=4,column=3)

divide=Button(object, text="/", fg="black",bg="#8f8f8f",command=lambda: press("/"), height=2,width=7)
divide.grid(row=5,column=3)

equal=Button(object, text="=", fg="black",bg="#8f8f8f",command=equalpress, height=2,width=7)
equal.grid(row=5,column=2)

clear=Button(object, text="clear", fg="black",bg="#8f8f8f",command=clear, height=2,width=7)
clear.grid(row=5,column=1)

object.mainloop()



