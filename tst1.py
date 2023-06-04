import tkinter as tk
from tkinter import messagebox

def calculate_length():
    name = name_entry.get()
    length = len(name)
    messagebox.showinfo("name length", "length of name: {}".format(length))

def calculate_vowels():
    name = name_entry.get()
    num_vowels = sum(1 for c in name if c.lower() in 'aeiou')
    messagebox.showinfo("vowel count", "number of vowels: {}".format(num_vowels))

def reverse_name():
    name = name_entry.get()
    reversed_name = name[::-1]
    messagebox.showinfo("reversed name", "your name in reverse: {}".format(reversed_name))

root = tk.Tk()
root.title("Name Analysis")

name_label = tk.Label(root, text="enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

length_button = tk.Button(root, text="calculate name length", command=calculate_length)
length_button.pack()

vowel_button = tk.Button(root, text="calculate number of vowels", command=calculate_vowels)
vowel_button.pack()

reverse_button = tk.Button(root, text="reverse name", command=reverse_name)
reverse_button.pack()

root.mainloop()
