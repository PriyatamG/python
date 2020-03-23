import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.7', 6969))
while True:
    msg = s.recv(1024).decode('utf-8')
    print(msg)
    message = input('Enter your message:')
    s.send(bytes(message, 'utf-8'))
    if message == 'Bye' or message == 'bye':
        s.close()
        break
