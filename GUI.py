from tkinter import *
import socket

PATH = '127.0.0.1'
PORT = 12345

root = Tk()
root.geometry("400x400")
root.title("Password Generator")
root.config(bg="#3d3d3d")


  
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((PATH, PORT))

def get_values():
    
    # Append Values in VALUES:

    if not client:
        print("Client is not!")

    VALUES = []

    length = length_entry.get()
    VALUES.append(length)
    letters = letters_entry.get()
    VALUES.append(letters)
    numbers = numbers_entry.get()
    VALUES.append(numbers)
    chars = chars_entry.get()
    VALUES.append(chars)

    try:
        client.send(str(VALUES).encode())
        print(f"Sends: {VALUES}")
    except Exception as e:
        print(f"Error: {e}")
    
    
# Entry and Labels:

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

chars_label = Label(text="Enter chars: ", font="Arial", background="#3d3d3d", fg="white")
chars_label.grid(column=0, row=4, pady=10)

chars_entry = Entry()
chars_entry.grid(column=1, row=4, pady=10)

# Else:

submit = Button(text="Generate Password", command=get_values)
submit.grid(column=1, row=5, pady=10)

root.mainloop()
client.close()