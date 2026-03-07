import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_address = ('localhost', 12345)
client_socket.connect(socket_address)

# Отправляем сообщение серверу
message = "Привет!"
client_socket.send(message.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()
print(response)

client_socket.close()
