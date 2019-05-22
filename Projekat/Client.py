import tkinter
from tkinter import *
from tkinter import  font
import tkinter.ttk
import socket
from tkinter import messagebox
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))


def enableEntry():
    entryKartica.configure(state = NORMAL)
    entryDatumIsticanja.configure(state = NORMAL)
    entryCV.config(state = NORMAL)

def disableEntry():
    entryKartica.delete(first = 0, last = 100)
    entryDatumIsticanja.delete(first=0, last=100)
    entryCV.delete(first=0, last=100)
    entryKartica.configure(state=DISABLED)
    entryDatumIsticanja.configure(state=DISABLED)
    entryCV.config(state=DISABLED)

def naruci():

    porukaZaImePice = "Pica: "
    porukaZaDodatke = "Dodaci: \n"
    porukaZaVelicinuPice = "Velicina pice: "
    porukaNacinPlacanja = "Nacin placanja: "



    if(checkbox1Var.get()==1):
        porukaZaDodatke += "Kecap\n"
    if(checkbox2Var.get()==1):
        porukaZaDodatke += "Majonez\n"
    if(checkbox3Var.get()==1):
        porukaZaDodatke += "Pavlaka\n"
    if(checkbox4Var.get()==1):
        porukaZaDodatke += "Cili\n"
    if(checkbox5Var.get()==1):
        porukaZaDodatke += "Masline\n"
    if(checkbox6Var.get()==1):
        porukaZaDodatke += "Pecurke\n"
    if(checkbox7Var.get()==1):
        porukaZaDodatke += "Jaja\n"
    if(checkbox8Var.get()==1):
        porukaZaDodatke += "Origano\n"

    if(radiobuttonVar.get()==1):
        porukaZaVelicinuPice += "25cm\n"
    elif(radiobuttonVar.get()==2):
        porukaZaVelicinuPice += "32cm\n"
    elif (radiobuttonVar.get() == 3):
        porukaZaVelicinuPice += "50cm\n"

    if(radiobutton2Var.get() == 1):
        porukaNacinPlacanja += "Kes"
    elif(radiobutton2Var.get() == 2):
        porukaNacinPlacanja += "Kartica"


    for i in listbox.curselection():
        if(i == 0):
            porukaZaImePice += "MARGARITA\n"
        elif(i == 1):
            porukaZaImePice += "CAPRICCIOSA\n"
        elif(i == 2):
            porukaZaImePice += "VEGETERIJANA\n"
        elif(i == 3):
            porukaZaImePice += "QUATTRO STAGIONI\n"
    if not listbox.curselection():
        messagebox.showwarning("GRESKA", "Niste selektovali picu")
    elif not radiobuttonVar.get():
        messagebox.showwarning("GRESKA", "Niste selektovali velicinu pice")
    elif entry1.get() == "" or entry2.get() == "":
        messagebox.showwarning("GRESKA", "Niste uneli Adresu ili Broj telefona")
    elif not radiobutton2Var.get():
        messagebox.showwarning("GRESKA", "Niste izabrali nacin placanja")
    elif radiobutton2Var.get() == 2 and (entryKartica.get()=="" or entryDatumIsticanja.get()=="" or entryCV.get() == ""):
        messagebox.showwarning("GRESKA", "Popunite potrebne podatke o vasoj kartici")
    else:
        poruka = porukaZaImePice + "**************************\n" + porukaZaVelicinuPice + \
                 "**************************\n" + porukaZaDodatke + "**************************\n" + porukaNacinPlacanja + \
                 "\n**************************\n" + "Vreme isporuke: "
        s.send(str.encode("uzmivreme"))
        time.sleep(0.01)
        s.send(str.encode(porukaZaImePice))
        time.sleep(0.01)
        s.send(str.encode(porukaZaVelicinuPice))
        time.sleep(0.01)
        s.send(str.encode(porukaZaDodatke))
        time.sleep(0.01)
        s.send(str.encode(porukaNacinPlacanja))
        request = s.recv(1024).decode()
        messagebox.showinfo("Hvala na porudzbini", porukaZaImePice + "**************************\n" + porukaZaVelicinuPice +
                            "**************************\n" + porukaZaDodatke + "**************************\n" + porukaNacinPlacanja  + "\n**************************\n" +
                            "Vreme isporuke: " + request + "min")



root = tkinter.Tk()


fontZaNaslov = font.Font(root, family = "Segoi UI", size = 12)
fontZaOstalo = font.Font(root, family = "Segoi UI", size = 9)

labelVrstaPice = tkinter.Label(root, text = "Vrsta pice", font = fontZaNaslov)
labelVrstaPice.grid(row = 0 , column = 0)

listbox = tkinter.Listbox(root, selectmode = SINGLE, width = 50, height = 6)
listbox.grid(row = 1, column = 0, padx = 20, pady = 5)
listbox.insert(0, "MARGARITA - 530rsd  /  730rsd  /  1000rsd")
listbox.insert(1, "CAPRICCIOSA - 600rsd  /  780rsd  /  1050rsd")
listbox.insert(2, "VEGETERIJANA - 530rsd  /  710rsd  /  950rsd")
listbox.insert(3, "QUATTRO STAGIONI - 640rsd  /  790rsd  /  1080rsd")

tkinter.ttk.Separator(root, orient = HORIZONTAL).grid(row = 2, columnspan = 1, sticky = EW)
tkinter.ttk.Separator(root, orient = HORIZONTAL).grid(row = 5, columnspan = 1, sticky = EW)
tkinter.ttk.Separator(root, orient = HORIZONTAL).grid(row = 11, columnspan = 3, sticky = EW)
tkinter.ttk.Separator(root, orient = VERTICAL).grid(row = 18, rowspan = 3, sticky = NS) #seperator linija

labelVelicinaPice = tkinter.Label(root, text = "Velicina pice", font = fontZaNaslov)
labelVelicinaPice.grid(row = 3, column = 0)

radiobuttonVar = IntVar()
radiobutton25cm = tkinter.Radiobutton(root, text = "25cm", font = fontZaOstalo, variable = radiobuttonVar, value = 1)
radiobutton25cm.grid(row = 4, sticky = W, padx = 25)
radiobutton32cm = tkinter.Radiobutton(root, text = "32cm", font = fontZaOstalo, variable = radiobuttonVar, value = 2)
radiobutton32cm.grid(row = 4)
radiobutton50cm = tkinter.Radiobutton(root, text = "50cm", font = fontZaOstalo, variable = radiobuttonVar, value = 3)
radiobutton50cm.grid(row = 4, sticky = E, padx = 25)

labelDodaci = tkinter.Label(root, text = "Dodaci", font = fontZaNaslov)
labelDodaci.grid(row = 6, column = 0)

checkbox1Var = IntVar()
checkbox2Var = IntVar()
checkbox3Var = IntVar()
checkbox4Var = IntVar()
checkbox5Var = IntVar()
checkbox6Var = IntVar()
checkbox7Var = IntVar()
checkbox8Var = IntVar()

checkbox1 = Checkbutton(root, text = "Kecap", variable = checkbox1Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox1.grid(row = 7, column = 0, sticky = W)
checkbox2 = Checkbutton(root, text = "Majonez", variable = checkbox2Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox2.grid(row = 8, column = 0, sticky = W)
checkbox3 = Checkbutton(root, text = "Pavlaka", variable = checkbox3Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox3.grid(row = 9, column = 0, sticky = W)
checkbox4 = Checkbutton(root, text = "Cili", variable = checkbox4Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox4.grid(row = 7, sticky = W, padx = 140)
checkbox5 = Checkbutton(root, text = "Masline", variable = checkbox5Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox5.grid(row = 8, column = 0, sticky = W, padx = 140)
checkbox6 = Checkbutton(root, text = "Pecurke", variable = checkbox6Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox6.grid(row = 9, column = 0, sticky = W, padx = 140)
checkbox7 = Checkbutton(root, text = "Jaja", variable = checkbox7Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox7.grid(row = 7, column = 0, sticky = E, padx = 21)
checkbox8 = Checkbutton(root, text = "Origano", variable = checkbox8Var, onvalue = 1, offvalue = 0, font = fontZaOstalo)
checkbox8.grid(row = 8, column = 0, sticky = E)

labelAdresa = Label(root, text = "Adresa: ", font = fontZaOstalo)
labelAdresa.grid(row = 12, sticky = W, pady = 7, padx = 30)
entry1 = Entry(root)
entry1.grid(row = 12)

labelBrojTelefona = Label(root, text = "Broj telefona: ", font = fontZaOstalo)
labelBrojTelefona.grid(row = 13, sticky = W)
entry2 = Entry(root)
entry2.grid(row = 13)

labelNapomena = Label(root, text = "Napomena =>", font = fontZaOstalo)
labelNapomena.grid(row = 14, column = 0, sticky = NW, pady = 7)
entryDopuna = Text(root,height = 6, width = 26)
entryDopuna.grid(row = 14, column = 0, sticky = E, padx = 27, pady = 7)

labelNacinPlacanja = Label(root, text = "Nacin placanja:", font = fontZaOstalo)
labelNacinPlacanja.grid(row = 15, sticky = W)

radiobutton2Var = IntVar()

radiobuttonKes = Radiobutton(root, text = "Kes", font = fontZaOstalo,variable = radiobutton2Var, value = 1, command = disableEntry)
radiobuttonKes.grid(row = 15, sticky = W, padx = 104)
radiobuttonKartica = Radiobutton(root, text = "Kartica", font = fontZaOstalo,variable = radiobutton2Var, value = 2, command = enableEntry)
radiobuttonKartica.grid(row = 15, sticky = E, padx = 104)

labelKartica = Label(root, text = "Broj:", font = fontZaOstalo)
labelKartica.grid(row = 18, sticky = E, padx = 133)

entryKartica = Entry(root, width = 17, state = DISABLED)
entryKartica.grid(row = 18, sticky = E, padx = 22)

labelDatumIsticanja = Label(root, text = "Datum isticanja:", font = fontZaOstalo)
labelDatumIsticanja.grid(row = 19, sticky = E, padx = 72)

entryDatumIsticanja = Entry(root, width = 7, state = DISABLED)
entryDatumIsticanja.grid(row = 19, sticky = E, padx = 22, pady = 7)

labelCV = Label(root, text = "CV broj:", font = fontZaOstalo)
labelCV.grid(row = 20, sticky = E, padx = 72)

entryCV = Entry(root, width = 7, state = DISABLED)
entryCV.grid(row = 20, sticky = E, padx = 22)

buttonNaruci = Button(root, text = "Naruci", width = 45, command = naruci, font = fontZaOstalo)
buttonNaruci.grid(row = 21, pady = 5)


root.mainloop()