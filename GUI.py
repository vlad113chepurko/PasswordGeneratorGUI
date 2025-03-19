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
  
    if not client:
        print("Client is not connected!")
        return

    VALUES = []

    length = length_entry.get()
    text = text_entry.get()
    chars = chars_entry.get()

    try:
        length = int(length)
        if length > 10:
            VALUES.append(length)
        else:
            print("Length must be more than 10!")
            return
    except ValueError:
        print("Invalid!")
        return

    
    if len(text) > 1:
        VALUES.append(text.lower())
    else:
        print("Text must be more than 1 character!")
        return

    
    if len(chars) > 1:
        VALUES.append(chars)
    else:
        print("Chars must be more than 1 character!")
        return

    try:
       
        client.send(str(VALUES).encode())
        print(f"Sent: {VALUES}")

    except Exception as e:
        print(f"Error: {e}")


# Entry and Labels:

length_label = Label(text="Enter length: ", font="Arial", background="#3d3d3d", fg="white")
length_label.grid(column=0, row=0, pady=10)

length_entry = Entry()
length_entry.grid(column=1, row=0, pady=10)

text_label = Label(text="Enter text: ", font="Arial", background="#3d3d3d", fg="white")
text_label.grid(column=0, row=2, pady=10)

text_entry = Entry()
text_entry.grid(column=1, row=2, pady=10)

chars_label = Label(text="Enter chars: ", font="Arial", background="#3d3d3d", fg="white")
chars_label.grid(column=0, row=3, pady=10)

chars_entry = Entry()
chars_entry.grid(column=1, row=3, pady=10)

# Else:

submit = Button(text="Generate Password", command=get_values)
submit.grid(column=1, row=4, pady=10)

root.mainloop()

client.close()