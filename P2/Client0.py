import socket
class Client:

    def __init__(self, ip, port):
        # IP will be a string
        self.ip = ip
        # PORT will be an integer number
        self.port = port

    def __str__(self):
        message = f"Connection to SERVER at {self.ip}, PORT: {self.port}"
        return message

    def ping(self):
        print("OK!")

    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.ip, self.port))
            print("SERVER WORKS FINE")
        except ConnectionRefusedError:
            print("COULDN'T FIND THAT SERVER")


    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port))
        #print(f"To server: {msg}")
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

    def debug_talk(self, message):
        import termcolor
        # print(f"To server: {msg}")
        client_msg = termcolor.cprint(message, "blue")
        response = self.talk(message)
        coloured_response = termcolor.cprint(response, "green")
        return client_msg, coloured_response



