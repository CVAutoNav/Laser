import socket
import time

HEADERSIZE = 10 # this will determine how many characters will be in the header
HOST = socket.gethostbyname(socket.gethostname())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is tcp
sock.bind((HOST, 1234))
sock.listen(5) # queue of 5 if lots of communications come in at once
print(f"The servers IP is {HOST}, use this to connect the client.")

while True:
    print("In the first while True loop")
    clientsocket, address = sock.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg # the < here means the message is left aligned

    clientsocket.send(bytes(msg, "utf-8")) # info to be sent to the client

    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg # the < here means the message is left aligned
        clientsocket.send(bytes(msg, "utf-8")) # info to be sent to the client