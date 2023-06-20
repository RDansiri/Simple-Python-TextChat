import socket
import threading
import time
import datetime
import os
from PIL import Image

clear = False
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
    file_path = current_directory + "/" + file_name
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
    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s3.bind((ip, (portb + 1)))
    while True:
        s1.listen()
        print("WAITING FOR CLIENTS sockA")
        conna, addr = s1.accept()
        print("CLIENT ACCEPTED AT:", addr)
        print("Starting new RX thread") #RX = Receive
        threading.Thread(target=recv, args=(conna,)).start()
        print("Started new client thread")
        s2.listen()
        print("WAITING FOR CLIENTS sockB")
        connb, addr = s2.accept()
        print("CLIENT ACCEPTED AT:", addr)
        print("Starting new TX thread") #TX = Send
        threading.Thread(target=send, args=(connb,)).start()
        print("Started new client thread")
        s3.listen()
        print("WAITING FOR CLIENTS sockB")
        connc, addr = s3.accept()
        print("CLIENT ACCEPTED AT:", addr)
        print("Starting new IM thread") #IM = Image thread
        threading.Thread(target=IM, args=(connc,)).start()
        print("Started new client Image thread")

def IM(conn):
    folder_path = os.getcwd()  # Find the current directory
    print("IM")
    file_name = conn.recv(1024).decode()
    print(file_name)
    save_path = str(folder_path +'/'+ file_name)
    # Receive the image size as a 4-byte length prefix
    image_size_bytes = conn.recv(4)
    image_size = int.from_bytes(image_size_bytes, 'big')
    # Receive the image data
    print('image recieveing')
    received_data = b''
    while len(received_data) < image_size:
        data = conn.recv(image_size - len(received_data))
        received_data += data
    print('image recieved')
    with open(save_path, 'wb') as file:
        file.write(received_data)
    print("Image saved successfully:", file_name)
    while True:
        print('a')
        data = conn.recv(1024).decode()
        print(data)
        folder_path = os.getcwd()  # Find the current directory
        if data:
            file_path = os.path.join(folder_path, data)
            if os.path.exists(file_path):
                print(f"The file '{data}' exists in the folder.")
                Image_Send(conn,file_path)
            else:
                print(f"The file '{data}' does not exist in the folder.")
                file_path = os.path.join(folder_path, 'Unfound.png')
                Image_Send(conn,file_path)
        time.sleep(0.1)

def Image_Send(conn, file_path):
    with open(file_path, 'rb') as file:
        image_data = file.read()

    # Send the image size as a 4-byte length prefix
    image_size = len(image_data)
    conn.sendall(image_size.to_bytes(4, 'big'))

    # Send the image data
    conn.sendall(image_data)

    print("Image sent successfully")  # Add this line to indicate successful image transmission

def send(conn):
    global loaded
    global chat
    global clear
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
        if clear == True:
            time.sleep(0.4)
            lengthb = lengtha
        else:
            time.sleep(0.1)  # Add a small delay to avoid excessive CPU usage

def recv(conn):
    global chat
    global loaded
    global clear
    while True:
        data = conn.recv(1024).decode()
        if data == "admin -s":
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time_string = current_time.replace("-", "").replace(" ", "").replace(":", "")
            time_string = time_string + ".txt"
            chat.append("Saving chat history to a file")
            wltf(chat, time_string)
            chat.append("Save complete")
            save = str("File name is:" + time_string)
            chat.append(save)
        elif data[0:8] == "admin -l":
            print("loading")
            cut_index = data.index("-l ") + 3  # Find the index of the point where you want to cut
            filename = data[cut_index:]  # Cut out everything before the index
            llff(filename)
            loaded = True
            time.sleep(0.1)
            loaded = False
        elif data[0:8] == "admin -c":
            clear()
            clear = True
            time.sleep(0.1)
            clear = False
        else:
            if data != '':
                chat.append(data)
                print(chat)

acceptclients(ip)
