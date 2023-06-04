from tkinter import *

def add():
    a1=int(a.get())
    b1=int(b.get())
    c1=a1+b1
    c.set(str(c1))
def sub():
    a1=int(a.get())
    b1=int(b.get())
    c1=a1-b1
    c.set(str(c1))    
def mul():
    a1=int(a.get())
    b1=int(b.get())
    c1=a1*b1
    c.set(str(c1))
def div():
    a1=int(a.get())
    b1=int(b.get())
    c1=a1/b1
    c.set(str(c1))    
root = Tk()
root.title("calculation")
root.geometry("500x600")
a=StringVar()
a.set(" ")
b=StringVar()
b.set(" ")



l1 = Label(root, text="Num1:")
l1.pack()
E1 =Entry(root, textvariable=a)
E1.pack()
l2 = Label(root, text="Num2:")
l2.pack()
E2 =Entry(root, textvariable=b)
E2.pack()
c=StringVar()
c.set(" ")


b1 = Button(root, text="add", command=add)
b1.pack()
b2 = Button(root, text="substraction", command=sub)
b2.pack()
b3 = Button(root, text="multiplication", command=mul)
b3.pack()
b4 = Button(root, text="division", command=div)
b4.pack()

root.mainloop()
