import tkinter as tk
import socket
import time
import threading as Thread
from PIL import ImageTk, Image
import os

recv = False
stop = 0
name = ''
porta = 49153
portb = 49154
host = ''
connected = False
Debug = False
WinTex = ['---ERR---'] * 10
folder_path = os.getcwd()  # Find the current directory
image_path = os.path.join(folder_path, "Unfound.png")  # Replace with the path to your image
if Debug == True:
    print(image_path)
image1 = Image.open(image_path)
image1 = image1.resize((20, 20))
im9 = image1
im8 = image1
im7 = image1
im6 = image1
im5 = image1
im4 = image1
im3 = image1
im2 = image1
im1 = image1
im0 = image1
root = tk.Tk()
root.title('Text Chat By: Pon')
def notstop():
    global root2
    time.sleep(3)
    root2.destroy()
    
def notification():
    global root2
    global name
    global WinTex
    global Debug
    if(Debug == True):
        print("NOTIF")
    root2 = tk.Tk()
    w = 200 # width for the Tk root
    h = 45 # height for the Tk root
    ws = root2.winfo_screenwidth() # width of the screen
    hs = root2.winfo_screenheight() # height of the screen
    x = ws - 200
    y = hs - 120
    root2.geometry('%dx%d+%d+%d' % (w, h, x, y))
    if(WinTex[9] != '-'):
        inpt = WinTex[9]
    elif(WinTex[8] != '-'):
        inpt = WinTex[8]
    elif(WinTex[7] != '-'):
        inpt = WinTex[7]
    elif(WinTex[6] != '-'):
        inpt = WinTex[6]
    elif(WinTex[5] != '-'):
        inpt = WinTex[5]
    elif(WinTex[4] != '-'):
        inpt = WinTex[4]
    elif(WinTex[3] != '-'):
        inpt = WinTex[3]
    elif(WinTex[2] != '-'):
        inpt = WinTex[2]
    elif(WinTex[1] != '-'):
        inpt = WinTex[1]
    elif(WinTex[0] != '-'):
        inpt = WinTex[0]

    nl = len(name)
    name2 = name + ':'
    rep = 0
    mat = 1
    while(rep <= nl):
        if(inpt[rep] == name2[rep]):
            if(Debug == True):
                print("mat")
        else:
            mat = 0
            if(Debug == True):
                print("nomat")
        rep = rep + 1
        
    if(mat == 0):
        inptl = len(inpt)
        outln1 = []
        outln2 = []
        if(Debug == True):
            print(inptl)
        rep = 34
        if(inptl > 34):
            t = 0
            inpos = 34
            while(t == 0):
                inptte = inpt[inpos]
                if(inptte == ' '):
                    if(Debug == True):
                        print("YES")
                    while(rep < inptl):
                        outln2.append(inpt[(rep)])
                        rep = rep + 1
                        if(Debug == True):
                            print(rep)
                    t = 1
                else:
                    inpos = inpos - 1
                    if(Debug == True):
                        print("NO")
                        print(inpos)
                    rep = inpos
            rep = inpos + 1
            while(rep != 0):
                outln1.append(inpt[(rep-1)])
                rep = rep - 1
            a = (''.join(reversed(outln1)))
            if(Debug == True):
                print(len(a))
                print(a)
            if(outln2[0] == ' '):
                outln2.pop(0)
            b = (''.join(outln2))
            if(Debug == True):
                print(b)
        else:
            a = inpt
            b = ''
            
        canvas2 = tk.Canvas(root2, width = 200, height = 45)
        canvas2.pack()
        label10 = tk.Label(root2, text= a)
        canvas2.create_window(0,10,window = label10,anchor = 'w')
        label11 = tk.Label(root2, text= b)
        canvas2.create_window(0,30,window = label11,anchor = 'w')
        Thread._start_new_thread(notstop,())
        root2.mainloop()
    
def Send():
    global entry1
    global msgo
    global cs1
    global Debug
    inpt = entry1.get()
    msgo = str(inpt)
    if(Debug == True):
        print(msgo)
        print(msgo[0:8])
    if(msgo[0:7] == "admin -"):
        msgo = str(name + msgo)
        cs1.send((msgo).encode())
    elif(msgo[0:6] == "/Debug"):
        if Debug == False:
            Debug = True
        elif Debug == True:
            Debug = False
    else:
        cs1.send((msgo).encode())

def Send2(t):
    global entry1
    global msgo
    global cs1
    global Debug
    inpt = entry1.get()
    msgo = str(inpt)
    if(Debug == True):
        print(msgo)
    if(msgo[0:7] == "admin -"):
        cs1.send((msgo).encode())
    elif(msgo[0:6] == "/Debug"):
        if Debug == False:
            Debug = True
        elif Debug == True:
            Debug = False
    else:
        msgo = str(name + msgo)
        cs1.send((msgo).encode())
    
def updateimage(image_path):
    global ima0, ima1, ima2, ima3, ima4, ima5, ima6, ima7, ima8, ima9
    global im9, im8, im7, im6, im5, im4, im3, im2, im1, im0

    im9 = im8
    im8 = im7
    im7 = im6
    im6 = im5
    im5 = im4
    im4 = im3
    im3 = im2
    im2 = im1
    im1 = im0

    im0 = Image.open(image_path)  # Open the image
    im0 = im0.resize((20, 20))  # Resize the image

    ia0 = ImageTk.PhotoImage(im0)
    ima0.configure(image=ia0)
    ima0.image = ia0

    # Update the rest of the image labels
    ia1 = ImageTk.PhotoImage(im1)
    ima1.configure(image=ia1)
    ima1.image = ia1
    ia2 = ImageTk.PhotoImage(im2)
    ima2.configure(image=ia2)
    ima2.image = ia2
    ia3 = ImageTk.PhotoImage(im3)
    ima3.configure(image=ia3)
    ima3.image = ia3
    ia4 = ImageTk.PhotoImage(im4)
    ima4.configure(image=ia4)
    ima4.image = ia4
    ia5 = ImageTk.PhotoImage(im5)
    ima5.configure(image=ia5)
    ima5.image = ia5
    ia6 = ImageTk.PhotoImage(im6)
    ima6.configure(image=ia6)
    ima6.image = ia6
    ia7 = ImageTk.PhotoImage(im7)
    ima7.configure(image=ia7)
    ima7.image = ia7
    ia8 = ImageTk.PhotoImage(im8)
    ima8.configure(image=ia8)
    ima8.image = ia8
    ia9 = ImageTk.PhotoImage(im9)
    ima9.configure(image=ia9)
    ima9.image = ia9
    if Debug == True:
        print('Update complete')

def sk():
    global ima0
    global ima1
    global ima2
    global ima3
    global ima4
    global ima5
    global ima6
    global ima7
    global ima8
    global ima9
    global label0
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global client_socket
    global root
    global canvas1
    global entry1
    global WinTex
    global entry2
    global entry3
    global entry4

    canvas1 = tk.Canvas(root, width=600, height=300)
    canvas1.pack()
    canvas1.create_line(180, 0, 180, 300)
    canvas1.create_line(180, 230, 600, 230)

    folder_path = os.getcwd()  # Find the current directory
    if Debug == True:
        print(folder_path)

    image_path = os.path.join(folder_path, "Unfound.png")  # Replace with the path to your image
    if Debug == True:
        print(image_path)
    image1 = Image.open(image_path)
    image1 = image1.resize((20, 20))
    test = ImageTk.PhotoImage(image1)
    ima0 = tk.Label(image=test)
    ima0.image = test
    # Position image
    ima0.place(x=185, y=200)
    ima1 = tk.Label(image=test)
    ima1.image = test
    # Position image
    ima1.place(x=185, y=180)
    ima2 = tk.Label(image=test)
    ima2.image = test
    # Position image
    ima2.place(x=185, y=160)
    ima3 = tk.Label(image=test)
    ima3.image = test
    # Position image
    ima3.place(x=185, y=140)
    ima4 = tk.Label(image=test)
    ima4.image = test
    # Position image
    ima4.place(x=185, y=120)
    ima5 = tk.Label(image=test)
    ima5.image = test
    # Position image
    ima5.place(x=185, y=100)
    ima6 = tk.Label(image=test)
    ima6.image = test
    # Position image
    ima6.place(x=185, y=80)
    ima7 = tk.Label(image=test)
    ima7.image = test
    # Position image
    ima7.place(x=185, y=60)
    ima8 = tk.Label(image=test)
    ima8.image = test
    # Position image
    ima8.place(x=185, y=40)
    ima9 = tk.Label(image=test)
    ima9.image = test
    # Position image
    ima9.place(x=185, y=20)
    entry1 = tk.Entry(root, width=50)
    canvas1.create_window(350, 270, window=entry1)
    entry2 = tk.Entry(root, width=20)
    canvas1.create_window(90, 50, window=entry2)
    text1 = tk.Label(root, text="host ip address")  ##Bottom
    canvas1.create_window(30, 25, window=text1, anchor='w')
    entry3 = tk.Entry(root, width=20)
    canvas1.create_window(90, 100, window=entry3)
    text2 = tk.Label(root, text="port")  ##Bottom
    canvas1.create_window(30, 75, window=text2, anchor='w')
    entry4 = tk.Entry(root, width=20)
    canvas1.create_window(90, 150, window=entry4)
    text3 = tk.Label(root, text="name")  ##Bottom
    canvas1.create_window(30, 125, window=text3, anchor='w')
    button1 = tk.Button(text='Apply and join', command=start)
    canvas1.create_window(70, 200, window=button1)
    canvas1.create_line(180, 0, 180, 300)
    canvas1.create_line(180, 230, 600, 230)
    label0 = tk.Label(root, text=WinTex[9])  ##Bottom
    canvas1.create_window(210, 210, window=label0, anchor='w')
    label1 = tk.Label(root, text=WinTex[8])
    canvas1.create_window(210, 190, window=label1, anchor='w')
    label2 = tk.Label(root, text=WinTex[7])
    canvas1.create_window(210, 170, window=label2, anchor='w')
    label3 = tk.Label(root, text=WinTex[6])
    canvas1.create_window(210, 150, window=label3, anchor='w')
    label4 = tk.Label(root, text=WinTex[5])
    canvas1.create_window(210, 130, window=label4, anchor='w')
    label5 = tk.Label(root, text=WinTex[4])
    canvas1.create_window(210, 110, window=label5, anchor='w')
    label6 = tk.Label(root, text=WinTex[3])
    canvas1.create_window(210, 90, window=label6, anchor='w')
    label7 = tk.Label(root, text=WinTex[2])
    canvas1.create_window(210, 70, window=label7, anchor='w')
    label8 = tk.Label(root, text=WinTex[1])
    canvas1.create_window(210, 50, window=label8, anchor='w')
    label9 = tk.Label(root, text=WinTex[0])
    canvas1.create_window(210, 30, window=label9, anchor='w')
    entry1.focus()
    root.bind('<Return>',Send2)

def update():
    global label0
    global label1
    global label2
    global label3
    global label4
    global label5
    global label6
    global label7
    global label8
    global label9
    global WinTex
    global Debug
    if(Debug == True):
        print(WinTex)
    label0.config(text = WinTex[9])
    label1.config(text = WinTex[8])
    label2.config(text = WinTex[7])
    label3.config(text = WinTex[6])
    label4.config(text = WinTex[5])
    label5.config(text = WinTex[4])
    label6.config(text = WinTex[3])
    label7.config(text = WinTex[2])
    label8.config(text = WinTex[1])
    label9.config(text = WinTex[0])

def start():
    global host
    global entry2
    global entry3
    global entry4
    global porta
    global portb
    global name
    global connected
    if(connected == False):
        host = str(entry2.get())
        porta = int(entry3.get())
        portb = porta + 1
        name = str(entry4.get())
        Thread._start_new_thread(socka, (host, porta))

def IM(host,port):
    global WinTex
    global recv
    global nocolname
    global Debug
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    folder_path = os.getcwd() #find current directory
    file_name = 'my_image.png'
    image_path = os.path.join(folder_path, file_name)
    pername = str(nocolname+".png")
    time.sleep(0.1)
    s.send((pername).encode())
    #file_path= 'C:/Users/racha/Desktop/ict/Out of Lesson/Server clients/my_image.png'
    with open(image_path, 'rb') as file:
        image_data = file.read()
    #image_data = image_data.resize((256, 256))  # Resize the image to 256x256 if needed
    image_size = len(image_data)
    s.sendall(image_size.to_bytes(4, 'big'))
    s.sendall(image_data)
    if Debug == True:
        print(pername)
    while True:
        if recv == True:
            imname = str((etbc(WinTex[9]))+".png")  
            if Debug == True:
                print(imname)
            file_path = str(folder_path+'/'+ imname)
            if Debug == True:
                print(file_path)
            if os.path.exists(file_path):
                if Debug == True:
                    print(f"The file '{imname}' exists in the folder.")
                updateimage(file_path)
                recv = False
            else:
                if Debug == True:
                    print(f"The file '{imname}' does not exist in the folder.")
                if (imname == "Console.png") or (imname == "File name is.png") or (imname == "---EMM---.png"): 
                    file_path = str(folder_path+'/'+ 'Cons.png')
                    updateimage(file_path)
                    recv = False
                else:
                    if Debug == True:
                        print('sending request')
                    s.send(imname.encode())
                    image_size_bytes = s.recv(4)
                    image_size = int.from_bytes(image_size_bytes, 'big')
                    # Receive the image data
                    received_data = b''
                    while len(received_data) < image_size:
                        data = s.recv(image_size - len(received_data))
                        # if not data:
                        #     break
                        received_data += data
                    # Save the received image
                    received_image_path = os.path.join(folder_path, imname)
                    if Debug == True:
                        print("saving")
                    with open(received_image_path, 'wb') as file:
                        file.write(received_data)
        time.sleep(0.1)

def etbc(text): #extract_text_before_colon
    colon_index = text.find(':')
    if colon_index != -1:
        extracted_text = text[:colon_index]
        return extracted_text
    else:
        return text

def socka(host, port):
    global cs1
    global msgo
    global name
    global portb
    global Debug
    global connected
    global nocolname
    connected = True
    if(Debug == True):
        print("SockA")
    cs1 = socket.socket()
    cs1.connect((host, port))
    if(Debug == True):
        print("SockA connect")
    Thread._start_new_thread(sockb, (host, portb))
    nocolname = name
    name = name + ": "
    msgo = str(name + " has joined the chat")
    cs1.send((msgo).encode())

def sockb(host, port):
    global WinTex 
    global Debug
    global recv
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs2:
        cs2.connect((host, port))
        Thread._start_new_thread(IM, (host, (portb+1)))
        while True:
            data = cs2.recv(1024).decode()
            if data:
                WinTex.pop(0)
                if(Debug == True):
                    print(data)
                WinTex.append(data)
                recv = True
                update()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    sk()
    root.mainloop()