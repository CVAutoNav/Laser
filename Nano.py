import socket
import time
start_1st_scanning_message = True
start_2nd_scanning_message = False
start_3rd_scanning_message = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.159", 1234))
# sock.listen(5)


while True:
    full_msg = '' # place to store the whole message



    while True:
        
        if start_1st_scanning_message == True:
            time.sleep(3)
            #send scan instruction 
            messge_to_send = 'start_1st_scanning'
            sock.send(bytes(messge_to_send, "utf-8"))
            print("sent message: start_1st_scanning")           
            sock.send(bytes(messge_to_send, "utf-8")) 
            messge_to_send = ''
            start_1st_scanning_message = False

            #expect connection outages
            
            print("First Scan in Progress") 
            time.sleep(13)

            #Scan Complete, rebuld connection  **Timing is important*
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(("192.168.1.159", 1234)) 

            #Detect Scan Complete Message
            msg = ""
            msg = sock.recv(50) #Listen to scan comple signal
            while msg == "":
                msg = sock.recv(50) #Fault Safe

            full_msg = msg.decode("utf-8")
            print("message received from PC is:")
            print(full_msg)
            if msg == b"1st_scanning_Done":
                print("All Tests Passed")
                #Instruct UGV to move to second location 

                #Get confirmation for location 

                #Set start_2nd_scanning_message = True

                break
            break
    break



            




        
        # # if start_2nd_scanning_message == True:
        # #     messge_to_send = 'start_2nd_scanning'
        # #     sock.send(bytes(messge_to_send, "utf-8"))
        # #     print("sent message: start_2nd_scanning")
        # #     messge_to_send = ''
          
            
        # # msg = ""
        # # msg = sock.recv(50) # bytes of data coming in
        # # if msg == "":
        # #     break
        # # if msg == b"1st_scanning_Done":
        # #     # print(f"new message length: {msg[:HEADERSIZE]}")
        # #     full_msg += msg.decode("utf-8")
        # #     print("message received is:")
        # #     print(full_msg)
        # #     full_msg = ''
        # #     start_1st_scanning_message = False
        # #     start_2nd_scanning_message = True
        # #     msg = ""
        # #     # time.sleep(3)

        # # if msg == b"2nd_scanning_Done":
        # #     full_msg += msg.decode("utf-8")
        # #     print("message received is:")
        # #     print(full_msg)
        # #     start_2nd_scanning_message = False
        # #     msg = ""
        # #     # time.sleep(3)




