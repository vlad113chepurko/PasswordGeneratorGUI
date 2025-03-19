from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Password Generator")
root.config(bg="#3d3d3d")


length_label = Label(text="Enter length: ", font="Arial", background="#3d3d3d", fg="white")
length_label.grid(column=0, row=0, pady=10)

length_entry = Entry()
length_entry.grid(column=1, row=0, pady=10)

letters_label = Label(text="Enter letters: ", font="Arial", background="#3d3d3d", fg="white")
letters_label.grid(column=0, row=2, pady=10)

letters_entry = Entry()
letters_entry.grid(column=1, row=2, pady=10)

numbers_label = Label(text="Enter numbers: ", font="Arial", background="#3d3d3d", fg="white")
numbers_label.grid(column=0, row=3, pady=10)

numbers_entry = Entry()
numbers_entry.grid(column=1, row=3, pady=10)

submit = Button(text="Generate Password")
submit.grid(column=1, row=4, pady=10)


root.mainloop()