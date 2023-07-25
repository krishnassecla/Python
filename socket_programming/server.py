import socket

HOST = "192.168.1.78"
PORT = 9091

username = "Cheems"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode("utf-8")
    print(f"Doge: {message}")
    my_message = input("You:")
    communication_socket.send(my_message.encode("utf-8"))
    # communication_socket.close()
    # print(f"Connection with {address} ended.")
