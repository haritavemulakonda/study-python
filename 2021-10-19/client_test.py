import socket

soc = socket.socket()
host = socket.gethostname()
port = 5000

soc.connect( (host, port) )
message_sent = input("---")
while message_sent.lower().strip() != "bye":
    soc.send(message_sent.encode())
    message_received = soc.recv(1024).decode()
    print(f"Message from server:{str(message_received)}")
    message_sent = input("---")
soc.close()