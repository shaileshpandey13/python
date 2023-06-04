from tkinter import*
root=Tk()
root.geometry("500x600")

def addpress(): 
    global expression 
    expression = "" 
    input_text.set("")
def shop(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)    
    



ar =Button(root, text="Click to Remove \r Item", bg="green", fg="white", font='Calibri 18 bold', width=15,
                      height=5, command=lambda: [addpress()])
ar.grid(row=3, column=5)

exit = Button(root, text="Exit", fg="white", bg="blue", font='Calibri 18 bold',
                         command=root.master.destroy, width=15, height=5)
exit.grid(row=4, column=5)

root.master.title("Evanz Shopping Store ||"
                          " \r Location: Brgy. Enclaro, Binalbagan, Negros Occidental || "
                          "\r Number: 09121234567")


asus = Button(root, command=lambda:[shop("Asus-P25,000"),press()])
image = ImageTk.PhotoImage(file="asus.gif")
asus.config(image=image, width=200, height=200, bg="green")
asus.image = image
asus.grid(row=2, column=1)

dell = Button(root, command=lambda:[shop("Dell-P30,000"),press()])
image = ImageTk.PhotoImage(file="dell-touchscreen.gif")
dell.config(image=image, width=200, height=200, bg="green")
dell.image = image
dell.grid(row=2, column=2)

headseat = Button(root, command=lambda: [shop("Headseat-P500"),press()])
image = ImageTk.PhotoImage(file="headseat.gif")
headseat.config(image=image, width=200, height=200, bg="green")
headseat.image = image
headseat.grid(row=2, column=3)

hp = tk.Button(root, command=lambda:[shop("HP-P45,000"),press()])
image = ImageTk.PhotoImage(file="hp.gif")
hp.config(image=image, width=200, height=200, bg="green")
hp.image = image
hp.grid(row=2, column=4)

longsleeve = Button(root, command=lambda: [shop("Long Sleeve-P5,000"), press()])
image = ImageTk.PhotoImage(file="longsleeve.gif")
longsleeve.config(image=image, width=200, height=200, bg="green")
longsleeve.image = image
longsleeve.grid(row=3, column=1)

pants =Button(root, command=lambda: [shop("Pants-P4,500"), press()])
image = ImageTk.PhotoImage(file="pants.gif")
pants.config(image=image, width=200, height=200, bg="green")
pants.image = image
pants.grid(row=3, column=2)

samsung = tk.Button(root, command=lambda: [shop("Samsung-P15,000"), press()])
image = ImageTk.PhotoImage(file="samsung.gif")
samsung.config(image=image, width=200, height=200, bg="green")
samsung.image = image
samsung.grid(row=3, column=3)

luxuryshoes = tk.Button(root, command=lambda: [shop("Luxury Shoes-P15,000"), press()])
image = ImageTk.PhotoImage(file="shoes1.gif")
luxuryshoes.config(image=image, width=200, height=200, bg="green")
luxuryshoes.image = image
luxuryshoes.grid(row=3, column=4)

cheapshoes = tk.Button(root, command=lambda: [shop("Cheap Shoes-P1,500"), press()])
image = ImageTk.PhotoImage(file="shoes2.gif")
cheapshoes.config(image=image, width=200, height=200, bg="green")
cheapshoes.image = image
cheapshoes.grid(row=4, column=1)

vivo = Button(root, command=lambda: [shop("Vivo-P16,000"), press()])
image = ImageTk.PhotoImage(file="vivo.gif")
vivo.config(image=image, width=200, height=200, bg="green")
vivo.image = image
vivo.grid(row=4, column=2)

rolex = Button(root, command=lambda: [shop("Rolex Watch-P12,000"), press()])
image = ImageTk.PhotoImage(file="watch1.gif")
rolex.config(image=image, width=200, height=200, bg="green")
rolex.image = image
rolex.grid(row=4, column=3)

applewatch = Button(root, command=lambda: [shop("Apple Watch-P10,000"), press()])
image = ImageTk.PhotoImage(file="watch2.gif")
applewatch.config(image=image, width=200, height=200, bg="green")
applewatch.image = image
applewatch.grid(row=4, column=4)

root.mainloop()
