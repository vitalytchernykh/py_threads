#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import pickle
import queue
import socket
import threading
from MessageQueues import qlist
from MessageQueues import sendQueue
from MessageQueues import deadletter


# send thread
class SendThread(threading.Thread):
    def run(self):
        while True:
           client,qname = sendQueue.get()
           threadName = self.getName()
           msg = qlist[qname].get()
           try:
               client[0].send(pickle.dumps(msg))
               print ('%s: send to client %s message %s' % (threadName,client[1][0],msg))
           except:
               print ('%s: save to deadletter: %s' % (threadName,msg))
               deadletter.put(msg)
               print ('%s: deadletter have %s message(s)' % (threadName,deadletter.qsize()))
