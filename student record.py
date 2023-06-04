from tkinter import*
from tkinter import messagebox

def addr():
    global dc
    name=nm.get()
    mark=marks.get()
    address=adrs.get()
    i=count.get()
    i+=1
    count.set(i)
    d={'name':name,'marks':mark,'address':address}
    dc[i]=d
    
def clear():
    nm.set(' ')
    marks.set(' ')
    adrs.set(' ')

    
def showall():
    t1.insert(END,dc)
    
def first():
    nm.set(dc[1]['name'])
    marks.set(dc[1]['marks'])
    adrs.set(dc[1]['address'])
    current.set(1)

def last():
    i=count.get()
    nm.set(dc[i]['name'])
    marks.set(dc[i]['marks'])
    adrs.set(dc[i]['address'])
    current.set(i)
    
def next():
    i=current.get()+1
    if i<=count.get():
        nm.set(dc[i]['name'])
        marks.set(dc[i]['marks'])
        adrs.set(dc[i]['address'])
        current.set(i)
    else:
        messagebox.showinfo("Alert","This is last record")


def previous():
    i=current.get()-1
    if i>=1:
        nm.set(dc[i]['name'])
        marks.set(dc[i]['marks'])
        adrs.set(dc[i]['address'])
        current.set(i)
    else:
        messagebox.showinfo("Alert","This is first record")        
        
def delete():
    i=current.get()
    del dc[i]

def edit():
    global dc
    i=current.get()
    name=nm.get()
    mark=marks.get()
    address=adrs.get()
    dc[i]['name']=name
    dc[i]['marks']=mark
    dc[i]['address']=address
    messagebox.showinfo("Success","This record is edited successfully")        
            
    

root=Tk()
root.geometry("500x600")

nm=StringVar()
marks=StringVar()
adrs=StringVar()
nm.set(' ')
marks.set(' ')
adrs.set(' ')
count =IntVar()
count.set(0)
current =IntVar()
current.set
root.title("student record")

dc={}
l1= Label(root, text="Name:")
l1.pack()
E1 = Entry(root,textvariable=nm)
E1.pack()

l2= Label(root, text="Marks:")
l2.pack()
E2 = Entry(root,textvariable=marks)
E2.pack()

l3= Label(root, text="address:")
l3.pack()
E3 = Entry(root,textvariable=adrs)
E3.pack()

b0 = Button(root, text="clear", command=clear)
b0.place(x=500,y=10)

b1 = Button(root, text="add", command=addr)
b1.place(x=550,y=10)

b2 = Button(root, text="Delete",command=delete)
b2.place(x=600,y=10)

b3 = Button(root, text="Edit",command=edit)
b3.place(x=500,y=40)

b4 = Button(root, text="Exit",command=root.destroy)
b4.place(x=500,y=80)

b5 = Button(root, text="show all",command= showall)
b5.place(x=920,y=40)

b6 = Button(root, text="first",command=first)
b6.place(x=850,y=10)

b7 = Button(root, text="last",command=last)
b7.place(x=900,y=10)

b8 = Button(root, text="next",command=next)
b8.place(x=950,y=10)

b9 = Button(root, text="previous",command=previous)
b9.place(x=850,y=40)

t1 = Text(root)
t1.place(x=500,y=150)

root.mainloop()
