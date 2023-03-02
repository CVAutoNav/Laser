import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.155.7.233", 1234))


new_msg = True # initiate the variable that tells us when we've started receiving a new message

while True:
    full_msg = '' # place to store the whole message

    while True:
        
        messge_to_send = 'start_scanning'
        sock.send(bytes(messge_to_send, "utf-8"))
        time.sleep(1)
        msg = ""
        msg = sock.recv(50) # bytes of data coming in
        if msg == "":
            break

        else:
            # print(f"new message length: {msg[:HEADERSIZE]}")
            msglength = int(len(msg)) # python automatically removes the spaces that fill up the unused characters
            new_msg = False # says we've received the header and are now getting the message

            full_msg += msg.decode("utf-8")

            # print("full msg received")
            print(full_msg)
            msg = ""


        

    # print(full_msg)