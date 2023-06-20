import socket
import threading as Thread
ip = '10.201.1.66'
port = 49153
dummy = 0

def send(dummy):
    while(True):
        data = "hey - server"
        conn.send((data.encode()))

def rcv(dummy):
    while(True):
        print(conn.recv(1024).decode())

print("ska")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip,port))
    s.listen()
    print("Listening")
    conn, addr = s.accept()
    print("Connected by",addr)
    print('client accepted')
    Thread._start_new_thread(send(dummy))
    Thread._start_new_thread(rcv(dummy))



#a = 1
#Thread._start_new_thread(SkA(a))
