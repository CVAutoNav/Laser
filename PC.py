import socket
import time
import subprocess

first_flag = True

HOST = socket.gethostbyname(socket.gethostname())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet is ipv4, sock_stream is tcp
sock.bind((HOST, 1234))
# sock.listen(5) # queue of 5 if lots of communications come in at once
print(f"The servers IP is {HOST}, use this to connect the client.")
clientsocket, address = sock.accept()
print(f"Connection from {address} has been established!")



while True:

        Nano_msg = ''        
        Nano_msg = clientsocket.recv(50)                                    
        if Nano_msg == '': 
            continue

        else: 
            if Nano_msg == b'start_1st_scanning': 
                printing_msg = Nano_msg.decode("utf-8")
                print("message received is:")
                print(printing_msg)
                Nano_msg = ''
                #Switch WIFI Network to FARO SCENE
                subprocess.run('netsh wlan connect name=LLS081915376', shell = True)

                #FARO API Trigger first scan, 360, -60, 90

                #while not receive_First_Scan_Complete_Signal: 
                    #Idle here and do nothing 

                #Reveived scan complete signal: 1. change WIFI Network
                subprocess.run('netsh wlan connect name=<Nano_WIFI>', shell = True) 

                #2. Rebuild PC Scaner connection 
                HOST = socket.gethostbyname(socket.gethostname())#Need static IP Address
                sock_after1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                sock_after1.bind((HOST, 1234))
                print(f"The PC's IP is {HOST}, Accepting Nano connections.")
                clientsocket, address = sock.accept()
                print(f"Connection from Nano IP {address} has been established!")

                #3. send message
                clientsocket.send(bytes("1st_scanning_Done", "utf-8"))
                print("1st_scanning_Done")
                clientsocket.send(bytes("1st_scanning_Done", "utf-8"))

            if Nano_msg == b'start_2nd_scanning':


                break


                printing_msg = Nano_msg.decode("utf-8")
                print("message received is:")
                print(printing_msg)
                Nano_msg = ''
                #Switch WIFI Network to FARO SCENE
                subprocess.run('netsh wlan connect name=LLS081915376', shell = True)

                #FARO API Trigger first scan, 360, -60, 90

                #while not receive_First_Scan_Complete_Signal: 
                    #Idle here and do nothing 

                #Reveived scan complete signal: 1. change WIFI Network
                subprocess.run('netsh wlan connect name=<Nano_WIFI>', shell = True) 

                #2. Rebuild PC Scaner connection 
                HOST = socket.gethostbyname(socket.gethostname())#Need static IP Address
                sock_after1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                sock_after1.bind((HOST, 1234))
                print(f"The PC's IP is {HOST}, Accepting Nano connections.")
                clientsocket, address = sock.accept()
                print(f"Connection from Nano IP {address} has been established!")

                #3. send message
                clientsocket.send(bytes("2nd_scanning_Done", "utf-8"))
                print("2nd_scanning_Done")   

            # if client_msg == b'start_2nd_scanning': 
            #     printing_msg += client_msg.decode("utf-8")
            #     print("message received is:")
            #     print(printing_msg)
            #     client_msg = ''
            #     clientsocket.send(bytes("2nd_scanning_Done", "utf-8"))
            #     print("sent message: 2nd_scanning_Done")

            else: 
                 print("Incorrect message received, please check configurations")
                 break
            

        

        
        

        # time.sleep(3)
