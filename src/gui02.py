#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import sys
import socket
import pickle
import threading

from tkinter import *

# non block receive release
class RecieveThread(threading.Thread):
    def run(self):
        while True:
           log.see(END)
           # send ticket nah!
           try:
               put_time, put_queue, put_msg = pickle.loads(client.recv(1024))
               client.send(pickle.dumps('ready'))
           except:
               break
           output =  put_queue + ', ' +  put_time + '> ' + put_msg + '\n'
           log.insert(END,output)

def send(event):
    msg = text.get()
    if msg == 'ready':
        msg = msg + ' !dont use ticket reserved, mazafaka! server transform needed'
    client.send(pickle.dumps(msg))
    text.set('')

th1 = RecieveThread()

tk=Tk()

tk.title('Pythono-lozhka test client')
tk.geometry('700x300')
text=StringVar()

# button
btns = Frame(tk)       
btns.pack()
b1 = Button(btns,text="this is button",command=None)
b1.pack(side='right')

log = Text(tk)
msg = Entry(tk, textvariable=text)
msg.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')


text.set('')
msg.focus_set()
msg.bind('<Return>',send)

# connect server:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect (('localhost', 2727))

client.send(pickle.dumps('ready'))
th1.start()

tk.mainloop()

client.close()
th1.join()
