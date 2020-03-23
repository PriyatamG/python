import socket

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server.bind(('192.168.0.7', 6969))
Server.listen(10)
msg, addr = Server.accept()
print("Connection established to", addr)
try:
    while True:
        msg.send(bytes(input("Enter message"), 'utf-8'))
        message = msg.recv(1024).decode('utf-8')
        print(message)
        if msg == 'Bye':
            Server.close()
            break
except:
    Server.close()