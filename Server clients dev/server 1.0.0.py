import socket
import threading
import time
import datetime
import os

chat = ['---EMM---'] * 10
print(chat)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
porta = 49153
portb = 49154
loaded = False
Juststart = True
print(ip)

def clear():
    global chat
    length = len(chat)
    chat = chat[(length-10):length]

def llff(file_name): #Load list from file
    global chat
    current_directory = os.getcwd()
    file_path = current_directory+"/"+file_name
    print(file_path)
    with open(file_path, 'r') as file:
        chat = file.read().replace('\n', '\n\n').split('\n')
    chat = [line for line in chat if line.strip()]
    print(chat)

        
def wltf(lst, filename): #save chat history to text file
    with open(filename, 'w') as file:
        file.write('\n'.join(lst))

def acceptclients(ip): # Receive
    global portb
    global porta
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind((ip, porta))
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind((ip, portb))
    while True:
        s1.listen()
        print("WAITING FOR CLIENTS sockA")
        conna, addr = s1.accept()
        print("CLIENT ACCEPTED AT:", addr)
        print("Starting new RX thread") #RX = Recieve
        threading.Thread(target=recv, args=(conna,)).start()
        print("Starting new client thread")
        s2.listen()
        print("WAITING FOR CLIENTS sockB")
        connb, addr = s2.accept()
        print("CLIENT ACCEPTED AT:", addr)
        print("Starting new TX thread") #TX = Send
        threading.Thread(target=send, args=(connb,)).start()

# def send(conn):
#     global loaded
#     global chat
#     lengthb = 0
#     while True:
#         lengtha = len(chat)
#         if lengthb < lengtha:
#             new_message = chat[-1]  # Get the last message from the chat list
#             conn.send(new_message.encode())
#             lengthb = lengtha
#         if loaded == True:
#             lengthb = 0
#             time.sleep(0.3)
#         time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage

def send(conn):
    global loaded
    global chat
    lengthb = 0
    while True:
        lengtha = len(chat)
        if lengthb < lengtha:
            new_message = chat[-1]  # Get the last message from the chat list
            conn.send(new_message.encode())
            lengthb = lengtha
        if loaded:
            time.sleep(0.3) 
            rep = -10
            while rep <= -1:
                mts = chat[rep]  # Split each line into separate elements
                print(mts)
                conn.send(mts.encode())
                rep = rep + 1
                time.sleep(0.1)
            lengthb = lengtha
        else:
            time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage

def recv(conn):
    global chat
    global loaded
    while True:
        data = conn.recv(1024).decode()
        if data == "admin -s":
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_string = current_time.replace("-", "").replace(" ", "").replace(":", "")
            time_string = time_string+".txt"
            chat.append("Saving chat history to a file")
            wltf(chat,time_string)
            chat.append("Save complete")
            save = str("File name is:"+time_string)
            chat.append(save)
        elif data[0:8] == "admin -l":
            print("loading")
            cut_index = (data.index("-l "))+3  # Find the index of the point where you want to cut
            filename = data[cut_index:]  # Cut out everything before the index
            llff(filename)
            loaded = True
            time.sleep(0.1)
            loaded = False
        elif data[0:8] == "admin -c":
            clear()
        else:
            if(data != ''):
                chat.append(data)
                print(chat) 
        
acceptclients(ip)
