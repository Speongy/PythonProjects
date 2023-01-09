#I added too many comments into my first port scan so here's one without any giant comments
#I wrote main.py like that bc I need as much explanation as possible or else I forget everything

'''
**PORT SCANNING IS ILLEGAL IF USED MALICIOUSLY**
Don't scan hosts that you don't have permission to
Scan your own hostst or have documented permission
I do not take any responsibility for what you do. This is for educational purposes only.
If you use it for something bad, it's your own fault.
**I DO NOT ADVISE IT**
'''

import socket
import threading
from queue import Queue

target = 'mf uhhhh'    #LOCALHOST(127.0.0.1) or any host

def port_scan(port):    #pass a port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port_scan))
        return True
    except:
        return False
    
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
