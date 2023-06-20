import socket
ip = '127.0.0.1'
port = 49153

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip,port))
    s.listen()
    conn, addr = s.accept()
    print("Connected by",addr)
    print('client accepted')
    while True:
        data = conn.recv(1024)
        print(data)
        message = 'hello'
        conn.send(message.encode())