import socket
import random

PATH = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))
server.listen(1)

print("Server is runing...")

conn, addr = server.accept()
print(f"Connect with: {addr}")



class PasswordGeberator(object):
  def __init__(self, length, text, chars):
    self.length = int(length)
    self.text = text
    self.chars = chars

  def generate_password(self):
        available_chars = ''

        if self.text and len(self.text) <= self.length:
            available_chars += self.text

        if self.chars and len(self.chars) <= self.length:
            available_chars += self.chars

        if available_chars:
            password = ''.join(random.choices(available_chars, k=self.length))
            return password
        else:
            return "Error: No characters to generate password!"
  



while True:

  try:

    data = conn.recv(1024)

    if not data:
      print("Server closing...")
      break

    decoding = data.decode()

    get_values = eval(decoding)

    print(f"Values on server: {get_values}")

    generator = PasswordGeberator(get_values[0], get_values[1], get_values[2])
    password = generator.generate_password()

    with open("password.txt", "a") as f:
        f.write(password + "\n")  

    with open("password.txt", "r") as f:
        print(f.readline()) 

    
    print(f"Password: {password}")

  except Exception as e:
    print(f"Error: {e}")

conn.close()
server.close()