#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import queue
import threading
from datetime import datetime

from MessageQueues import qlist
from MessageQueues import collectQueue


# message collector thread
class CollectThread(threading.Thread):
    def run(self):
        threadName = self.getName()
        while True:
            print ('%s: message collector waiting for messages...' % threadName)
            msg,qname = collectQueue.get()
            print ('%s: message collector start working...' % threadName)
            if msg != None:
                for q in qlist:
                    qlist[q].put([datetime.now().strftime('%Y-%m-%d %H:%M:%S'),qname,msg])
                    print ('%s: message collector serialize message %s to queue %s' % (threadName,msg,q))
