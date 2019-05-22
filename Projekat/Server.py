import socket
import random
import time
import threading
import tkinter
from tkinter import *

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()



class MojaNit(threading.Thread):
    def __init__(self, soc):
      self.soc = soc
      thread = threading.Thread(target=self.run, args=())
      thread.daemon = True
      thread.start()

    def run(self):
        while True:
            conn, addr = s.accept()
            request = conn.recv(1024).decode()
            if(request == "uzmivreme"):
                for i in range(1):
                    request1 = conn.recv(1024).decode()
                    request2 = conn.recv(1024).decode()
                    request3 = conn.recv(1024).decode()
                    request4 = conn.recv(1024).decode()
                    response = random.randint(1,5)
                    conn.send(str.encode(str(response)))
                    listbox1.insert(END, request1)
                    listbox1.insert(END, request2)
                    listbox1.insert(END, request3)
                    listbox1.insert(END, request4)
                for j in range(response, -1, -1):
                    if(j > 0):
                        listbox1.delete(END, j)
                        listbox1.insert(END, j)
                        time.sleep(1)
                    else:
                        listbox2.insert(END, "Isporuceno:")
                        listbox2.insert(END, request1)
                        listbox2.insert(END, request2)
                        listbox2.insert(END, request3)
                        listbox2.insert(END, request4)
                        listbox2.insert(END, "---------------------------------")
                        listbox1.delete(0, END)




root = tkinter.Tk()
label1 = Label(root, text = "VREME PORUDZBINE")
label1.pack()
listbox1 = tkinter.Listbox(root, width = 50)
listbox1.pack()
label2 = Label(root, text = "VREME ISPORUKE")
label2.pack()
listbox2 = tkinter.Listbox(root, width = 50)
listbox2.pack(side = RIGHT)
mojanit = MojaNit()
root.mainloop()