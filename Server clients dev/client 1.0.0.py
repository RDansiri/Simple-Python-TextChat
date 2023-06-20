import tkinter as tk
import socket
import time
import threading as Thread
stop = 0
name = 'Pon'
porta = 49153
portb = 49154
host = '10.201.1.66'
WinTex = ['---ERR---'] * 10
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
            print("mat")
        else:
            mat = 0
            print("nomat")
        rep = rep + 1
        
    if(mat == 0):
        inptl = len(inpt)
        outln1 = []
        outln2 = []
        print(inptl)
        rep = 34
        if(inptl > 34):
            t = 0
            inpos = 34
            while(t == 0):
                inptte = inpt[inpos]
                if(inptte == ' '):
                    print("YES")
                    while(rep < inptl):
                        outln2.append(inpt[(rep)])
                        rep = rep + 1
                        print(rep)
                    t = 1
                else:
                    inpos = inpos - 1
                    print("NO")
                    print(inpos)
                    rep = inpos
            rep = inpos + 1
            while(rep != 0):
                outln1.append(inpt[(rep-1)])
                rep = rep - 1
            a = (''.join(reversed(outln1)))
            print(len(a))
            print(a)
            if(outln2[0] == ' '):
                outln2.pop(0)
            b = (''.join(outln2))
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
    inpt = entry1.get()
    msgo = str(inpt)
    print(msgo)
    print(msgo[0:8])
    if(msgo[0:7] == "admin -"):
        msgo = str(name + msgo)
        cs1.send((msgo).encode())
    else:
        cs1.send((msgo).encode())

def Send2(t):
    global entry1
    global msgo
    global cs1
    inpt = entry1.get()
    msgo = str(inpt)
    print(msgo)
    if(msgo[0:7] == "admin -"):
        cs1.send((msgo).encode())
    else:
        msgo = str(name + msgo)
        cs1.send((msgo).encode())
    
def sk():
    print("sk") 
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
    canvas1 = tk.Canvas(root, width = 600, height = 300)
    canvas1.pack()
    canvas1.create_line(180,0,180,300)
    canvas1.create_line(180,230,600,230)
    entry1 = tk.Entry(root,width = 50) 
    canvas1.create_window(350, 270, window=entry1)
    canvas1.create_line(180,0,180,300)
    canvas1.create_line(180,230,600,230)
    label0 = tk.Label(root, text= WinTex[9]) ##Bottom
    canvas1.create_window(200,210,window = label0,anchor = 'w')
    label1 = tk.Label(root, text= WinTex[8])
    canvas1.create_window(200,190,window = label1,anchor = 'w')
    label2 = tk.Label(root, text= WinTex[7])
    canvas1.create_window(200,170,window = label2,anchor = 'w')
    label3 = tk.Label(root, text= WinTex[6])
    canvas1.create_window(200,150,window = label3,anchor = 'w')
    label4 = tk.Label(root, text= WinTex[5])
    canvas1.create_window(200,130,window = label4,anchor = 'w')
    label5 = tk.Label(root, text= WinTex[4])
    canvas1.create_window(200,110,window = label5,anchor = 'w')
    label6 = tk.Label(root, text= WinTex[3])
    canvas1.create_window(200,90,window = label6,anchor = 'w')
    label7 = tk.Label(root, text= WinTex[2])
    canvas1.create_window(200,70,window = label7,anchor = 'w')
    label8 = tk.Label(root, text= WinTex[1])
    canvas1.create_window(200,50,window = label8,anchor = 'w')
    label9 = tk.Label(root, text= WinTex[0]) ##Top
    canvas1.create_window(200,30,window = label9,anchor = 'w')
    button0 = tk.Button(text='Send', command = Send)
    canvas1.create_window(550, 270, window = button0)
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

def socka(host, port):
    global cs1
    global msgo
    global name
    global portb
    print("SockA")
    cs1 = socket.socket()
    cs1.connect((host, port))
    print("SockA connect")
    Thread._start_new_thread(sockb, (host, portb))
    msgo = str(name + " has joined the chat")
    name = name + ": "
    cs1.send((msgo).encode())

def sockb(host, port):
    global WinTex 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cs2:
        cs2.connect((host, port))
        while True:
            data = cs2.recv(1024).decode()
            if data:
                WinTex.pop(0)
                print(data)
                WinTex.append(data)
                update()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    Thread._start_new_thread(socka, (host, porta))
    sk()
    root.mainloop()