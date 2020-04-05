import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('117.98.141.209', 6969))
try:
    while True:
        msg = s.recv(1024).decode('utf-8')
        print(msg)
        message = input('Enter your message:')
        s.send(bytes(message, 'utf-8'))
        if message == 'Bye' or message == 'bye':
            s.close()
            break
except:
    s.close()
