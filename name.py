import tkinter as tk

def calculate_length():
    name = name_entry.get()
    length = len(name)
    length_label.config(text="Length of name: {}".format(length))

root = tk.Tk()
root.title("Name Length Calculator")

# Create a Label and Entry for the user to input their name
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Create a Button that calls the calculate_length function when clicked
calculate_button = tk.Button(root, text="Calculate", command=calculate_length)
calculate_button.pack()

# Create a Label to display the length of the name
length_label = tk.Label(root)
length_label.pack()

root.mainloop()
