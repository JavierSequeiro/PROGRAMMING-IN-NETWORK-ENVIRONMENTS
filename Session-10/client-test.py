import colorama
from Client0 import Client

colorama.init(autoreset=True)
for i in range(0, 5):
    s = Client("192.168.1.39", 8080)
    message = f"Message {i}"
    client, server = s.debug_talk(f"{message}")
    print(client)
    print(server)