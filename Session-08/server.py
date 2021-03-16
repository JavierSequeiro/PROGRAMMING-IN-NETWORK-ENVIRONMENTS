import socket

# SERVER'S IP, PORT

PORT = 8080
IP = "192.168.1.38"
MAX_OPEN_REQUESTS = 5

# TO COUNT NUMBER OF CONNECTIONS
connection_count = 0

# CREATE AN INET, STREAMING SOCKET
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    #WE ARE A SERVER SOCKET NOW
    # MAX OPEN REQUESTS CONNECTS REQUESTS UNTIL LIMIT SET
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        #ACCEPT CONNECTIONS FROM OUTSIDE
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # NEW CONNECTION
        connection_count += 1

        # Print connection info
        print("CONNECTION: {}. From the IP {}".format(connection_count, address))

        #NOW WE READ THE MESSAGE FROM THE CLIENT
        message = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(message))

        #NOW SEND OUR MESSAGE, USING BYTES
        server_message = "Hello from the Javier's server"
        send_bytes = str.encode(server_message)

        clientsocket.send(send_bytes)
        clientsocket.close()
except socket.error:
    print(f"Problems using port {PORT}. Do you have permission?")

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
