import pickle
import socket
import threading
import queue

# connect to the server:
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect (('localhost', 2727))

# non block user input release
userInput = queue.Queue(0)
class InputThread(threading.Thread):
    def run(self):
        while True:
            msg = input()
            userInput.put(msg)
InputThread().start()

# non block recive release
class ReciveThread(threading.Thread):
    def run(self):
        while True:
           print ('ready to recive...')
           # send ticket nah!
           client.send(pickle.dumps('ready'))

           put_time, put_queue, put_msg = pickle.loads(client.recv(1024))
           print (self.getName(),put_time, put_queue, put_msg)
ReciveThread().start()

msg = ''

while msg != 'quit':
    # get from queue and send messages:
    if userInput.qsize():
        msg = userInput.get()
        pickledMsg = pickle.dumps(msg)
        client.send(pickledMsg)

# close the connection
client.close()
