#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import queue
import socket
import threading

from ClientWorker import ClientThread
from MessageQueues import clientPool
from MessageCollector import CollectThread
from SendWorker import SendThread

# start message collector thread
CollectThread().start()

# start two send threads
for x in range(2):
    SendThread().start()

# start two client threads
for x in range(2):
    ClientThread().start()

# set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 2727))
server.listen(5)

# have the server serve "forever"
while True:
    clientPool.put(server.accept())
