import socket

HOST = 'localhost'
PORT = 4000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    connection, address = s.accept()

    with connection:
        print(f"Connected by {address}")

        while True:
            data = connection.recv(1024)
            print(data)
            connection.sendall(data)
            if not data:
                break