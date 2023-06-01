#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from main import start

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
answer = ""

while True:
    #  Wait for next request from client
    message = socket.recv()
    m = message.decode('UTF-8')
    if m == "screen1":
        print(f"taken: {m}")
        time.sleep(5)
        print("sending: waiting screen2")
        answer = "waiting screen2"
    elif m == "screen2":
        print("start working")
        answer = start()
        print(f"send answer {answer}")
    elif m == "":
        break
    #  Do some 'work'.
    #  Try reducing sleep time to 0.01 to see how blazingly fast it communicates
    #  In the real world usage, you just need to replace time.sleep() with
    #  whatever work you want python to do, maybe a machine learning task?

    #  Send reply back to client
    #  In the real world usage, after you finish your work, send your output here
    socket.send(answer.encode('UTF-8'))
