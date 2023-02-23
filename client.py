import socket

HEADERSIZE = 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))

while True:
    full_msg = '' # place to store the whole message
    new_msg = True # variable that tells us when we've started receiving a new message

    while True:
        msg = sock.recv(16) # bytes of data coming in

        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglength = int(msg[:HEADERSIZE]) # python automatically removes the spaces that fill up the unused characters
            new_msg = False # says we've received the header and are now getting the message

        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglength:
            print("full msg received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg) #