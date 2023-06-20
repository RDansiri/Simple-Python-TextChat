import socket

def client_program():
    host = '192.168.1.53'
    port = 49153  # socket server port number
    message = "a"
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    while message != 'bye':
        message = input(" -> ")  # again take input
        client_socket.send(message.encode())  # send message
        if(message == "-u"):
            client_socket.send("-n".encode())
            data = "e"
            while(data != "-u"):
                data = client_socket.recv(1024).decode()  # receive response
                if(data != "-u"):
                    print('Received from server: ' + data)  # show in terminal
                client_socket.send("-n".encode())
        elif(message == "-c"):
            data = client_socket.recv(1024).decode()
            print("There are",data,"users on this network")

    client_socket.close()  # close the connection


client_program()
