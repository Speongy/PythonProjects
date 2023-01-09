import socket

target = 'mf uhhhh'    #LOCALHOST or my own machine

def port_scan(port):    #pass a port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port_scan))
        return True
    except:
        return False
'''AF_INET tells us if internet socket and not UNIX socket
SOCK_STREAM lets us use TCP and not UDP'''


'''
not multithreaded slower version

for port in range(1, 1024):
    result = port_scan(port)
    if result:
        print("Port {} is open.".format(port))
    else:
        print("Port {} is closed".format(port))

this version checks ports one at a time. super lame and not poggers (help me)
Let's multithread it! >:D
and also use queues
'''

import threading
from queue import Queue
'''
queue is a collection, sequence, or list where everytime we get an element, 
it's no longer in the collection, seq, or list

In this case, we're queueing port #'s 1 to 1024

The queue shifts when we get a new one or something like that idk man

'''

queue = Queue()
open_port = []

def fill_queue(port_list):      #fill queue
    for port in port_list:
        queue.put(port)         #FIFO

def worker():                   #function our threads use
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print("Port {} is open.".format(port))
            open_port.append(port)
            #prints True otherwise print nothing so it doesn't clog the terminal and make it gross

port_list = range(1, 1024)      #now we can fill our queue
fill_queue(port_list)  

thread_list = []        #empty thread list that's important for last part

for t in range(10):
    thread = threading.Thread(target = worker) #not a function call
    thread_list.append(thread)

for thread in thread_list:      #runs threads
    thread.start()

for thread in thread_list:      
    thread.join()

print("Open ports are: ", open_port)

'''
So, we need an empty thread list for the thread.join()
thread.join() waits until every thread is finished before if goes to the print statement
'''