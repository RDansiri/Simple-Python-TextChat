import socket
import threading as Thread
import time
ip = '192.168.1.43'
port = 49153
fileout = []
fileoutn = 0
rts = 0
clients = 0
def clientthread(conn,addr):
    global fileout
    global fileoutn
    global rts
    global clients
    while True:
        lrts = rts
        rts = 0
        lu = 0
        lm = 0
        data = conn.recv(1024).decode()
        if(data == '-u'):
            print("Updating Client at:",addr)
            lm = fileoutn - lu
            fileoutin = fileoutn - lm
            if(fileoutin < 0):
                fileoutin = 0
            print(fileoutn)
            while(fileoutin != fileoutn):
                data = conn.recv(1024).decode()
                if(data == "-n"):
                    print(fileoutin)
                    data = fileout[fileoutin]
                    data = data.encode()
                    conn.send(data)
                    fileoutin = fileoutin + 1
            conn.send('-u'.encode())
            lu = fileoutn
        elif(data == '-c'):
            print("Sending amount of clients to:",addr)
            data = str(clients)
            data = data.encode()   
            conn.send(data)
        elif(data == "-n"):
            print("-n reject")
        elif(data == "-t"):
            print("-t")
            clients = clients - 1
            break
        else:
            print(data)
            fileout.append(data)
            fileoutn = fileoutn + 1
            rts = 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip,port))
    while True:
        s.listen()
        print("WAITING FOR CLIENTS")
        conn, addr = s.accept()
        clients = clients + 1
        print("CLIENT ACCEPTED AT:",addr)
        print("Now at",clients,"Client/s")   
        print("Starting new thread")
        Thread._start_new_thread(clientthread,(conn,addr))
