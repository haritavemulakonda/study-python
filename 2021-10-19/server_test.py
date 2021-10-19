import socket

soc = socket.socket()
host = socket.gethostname()
port = 5000
soc.bind((host, port))
soc.listen(1)
connection, address = soc.accept()
print(f"Established a connection with:{address}")

while True:
    data_received = connection.recv(1024).decode()
    if not data_received:
        break
    print(f"Data from client:{str(data_received)}")
    data_to_sent = input("---")
    connection.send(data_to_sent.encode())
connection.close()
