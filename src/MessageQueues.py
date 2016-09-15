#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#

import queue

# create client connection pool queue
clientPool = queue.Queue(0)

# create send queue
sendQueue = queue.Queue(0)

# create message collector queue
collectQueue = queue.Queue(0)

# create deadletter queue
deadletter = queue.Queue(0)


# init dict of client queues
qlist = {}
