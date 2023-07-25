import socket

HOST = "192.168.1.78"
PORT = 9091

username = "Doge"

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

while True:
    message = input("You: ")

    # socket.send("Hello world!".encode("utf-8"))
    socket.send(message.encode("utf-8"))
    print("Cheems", socket.recv(1024).decode("utf-8"))
