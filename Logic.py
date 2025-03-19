import socket

PATH = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((PATH, PORT))
server.listen(1)

print("Server is runing...")

conn, addr = server.accept()
print(f"Connect with: {addr}")



# class PasswordGeberator(object):
#   def __init__(self, length, letters, numbers, chars):
#     self.length = length
#     self.letters = letters
#     self.numbers = numbers
#     self.chars = chars

#   # def generate_password(self, password):

while True:
  try:
    data = conn.recv(1024)
    if not data:
      print("Server closing...")
    decoding = data.decode()
    print(f"Decod: {decoding}")
  except Exception as e:
    print(f"Error: {e}")

conn.close()
server.close()