import socket
import time


HOST = socket.gethostbyname(socket.gethostname())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is tcp
sock.bind((HOST, 1234))
sock.listen(5) # queue of 5 if lots of communications come in at once
print(f"The servers IP is {HOST}, use this to connect the client.")
first_flag = True

while True:
    clientsocket, address = sock.accept()
    if first_flag == True: 
        print(f"Connection from {address} has been established!")
        msg = "Scanner Controler connection: Established"
        clientsocket.send(bytes(msg, "utf-8")) # info to be sent to the client
        first_flag = False 


    while True:
        printing_msg = ''
        client_msg = clientsocket.recv(50)
        if client_msg == '': 
            break
        else: 
            printing_msg += client_msg.decode("utf-8")
            print(printing_msg)

        time.sleep(1)

        msg = ''

        msg = "Scanning_Done"
        clientsocket.send(bytes(msg, "utf-8")) # info to be sent to the client