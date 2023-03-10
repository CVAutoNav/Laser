import socket
import time
first_flag = True

HOST = socket.gethostbyname(socket.gethostname())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is tcp
sock.bind((HOST, 1234))
sock.listen(5) # queue of 5 if lots of communications come in at once
print(f"The servers IP is {HOST}, use this to connect the client.")


while True:
    clientsocket, address = sock.accept()
    if first_flag == True: 
        print(f"Connection from {address} has been established!")
        # msg = "Scanner Controler connection: Established"
        # clientsocket.send(bytes(msg, "utf-8")) # info to be sent to the client
        first_flag = False 


    while True:

        # if KeyboardInterrupt:
        #     break
        printing_msg = ''
        
        client_msg = clientsocket.recv(50)
        if client_msg == '': 
            break

        if client_msg == b'start_1st_scanning': 
            printing_msg += client_msg.decode("utf-8")
            print("message received is:")
            print(printing_msg)
            client_msg = ''
            clientsocket.send(bytes("1st_scanning_Done", "utf-8"))
            print("sent message: 1st_scanning_Done")

        if client_msg == b'start_2nd_scanning': 
            printing_msg += client_msg.decode("utf-8")
            print("message received is:")
            print(printing_msg)
            client_msg = ''
            clientsocket.send(bytes("2nd_scanning_Done", "utf-8"))
            print("sent message: 2nd_scanning_Done")

        
        

        # time.sleep(3)
