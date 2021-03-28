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
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response

    def debug_talk(self, message):
        import colorama
        from colorama import Fore
        colorama.reinit()
        colored_client_message = f"{Fore.GREEN} {message}"
        response = f" {Fore.GREEN} {self.talk(colored_client_message)}"
        print_response = f"From server: {response}"
        client_msg = f"{Fore.BLUE} {message}"
        print_client_msg = f"To server: {client_msg}"
        return print_client_msg, print_response



