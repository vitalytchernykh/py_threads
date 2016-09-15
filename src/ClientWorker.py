#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import pickle
import queue
import socket
import threading

from MessageQueues import qlist
from MessageQueues import clientPool
from MessageQueues import sendQueue
from MessageQueues import collectQueue

#
class ClientThread(threading.Thread):
    def run(self):
        while True:
            # get a client socket out of the queue
            client = clientPool.get()
            threadName = self.getName()
            # check if we actually have an actual client in the client variable:
            if client != None:
                # calculate queue name
                qname = client[1][0]
                # touch client's queue
                try:
                    qlist[qname].qsize()
                # create new client's queue if not exist
                except:
                    qlist[qname] = queue.Queue(0)

                cli = str(client[1][0]) + ':' + str(client[1][1])
                print ('%s: Received connection %s, used queue %s' % (threadName,cli,qname))
                collectQueue.put(['Join threads',qname])

                # get client messages
                while True:
                    msg = None
                    print ('%s: queue %s has % unread messages' % (threadName,qname,qlist[qname].qsize()))

                    try:
                        msg = pickle.loads(client[0].recv(1024))
                    except:
                        client[0].close()
                        print ('%s: Closed connection %s' % (threadName,cli))
                        collectQueue.put(['Leave threads',qname])
                        break
                    if msg == 'ready':
                        sendQueue.put([client,qname])
                    elif msg:
                        print ('%s: %s> %s' % (threadName,cli,msg))
                        collectQueue.put([msg,qname])
