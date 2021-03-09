import socket

# SERVER IP, PORT
# WRITE CORRECT PARAMETER FOR CONNECTING TO TEACHER'S SERVER

PORT = 8080
IP = "192.168.124.179"

# NOW WE CREATE THE SOCKET
# ALWAYS USE PARAMETERS (AF_INET,  SOCK_STREAM)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# STABLISH CONNECTION WITH SERVER (IP, PORT)

s.connect((IP, PORT))

# NOW WE SEND THE DATA
# STRINGS CAN'T BE SEND, SO WE NEED TO ENCODE THEM AS BYTES

s.send(str.encode("HELLO FROM THE CLIENT!!!"))

#FINALLY WE CLOSE THE SOCKET

s.close()