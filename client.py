
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096



def music_window():
    
    window = Tk()
    window.title('MUSIC SHARER')
    window.geometry('300x300')
    window.configure(bg = 'LightSkyBlue')

    select_label = Label(window,text='Select Song', font = ('Calibri',10), bg="LightSkyBlue")
    select_label.place(x = 2, y = 1)

    listbox = Listbox(window, height = 10, width = 39, activestyle= 'dotbox', bg ="LightSkyBlue", borderwidth = 2, font = ('Calibri',10))
    listbox.place(x=10, y = 20)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1, relx = 1)
    scrollbar1.config(command = Listbox.yview)   

    playbtn  = Button(window, text = "Play", width = 10, bd =1, bg = "SkyBlue", font = ("Calibri, 10"))
    playbtn.place(x = 30, y = 200)

    stopbtn  = Button(window, text = "Stop", width = 10, bd =1, bg = "SkyBlue", font = ("Calibri, 10"))
    stopbtn.place(x =200, y = 200)

    uploadbtn  = Button(window, text = "Upload", width = 10, bd =1, bg = "SkyBlue", font = ("Calibri, 10"))
    uploadbtn.place(x = 30, y = 250)

    
    downloadbtn  = Button(window, text = "Download", width = 10, bd =1, bg = "SkyBlue", font = ("Calibri, 10"))
    downloadbtn.place(x = 200, y = 250)

    info_label = Label(window, text ="", fg = 'blue', font = ('Calibri', 10))
    info_label.place(x = 4, y =280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    music_window()


setup()

