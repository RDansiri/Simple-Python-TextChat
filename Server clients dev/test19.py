import socket
import threading as Thread
host = '10.201.1.66'
port = 49153
dummy = 0

def send(dummy):
    print("se")
    while(True):
        data = "hey - client"
        client_socket.send((data.encode()))

def rcv(dummy):
    print("rc")
    while(True):
        print(conn.recv(1024).decode())
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("IcA Connected to",host)
    Thread._start_new_thread(send(dummy))
    Thread._start_new_thread(rcv(dummy))


