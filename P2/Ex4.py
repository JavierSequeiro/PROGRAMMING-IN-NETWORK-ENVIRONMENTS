from Client0 import Client
import colorama
print("------| Practice 2, Exercise 4 |------")

s = Client("192.168.1.38", 8080)
m = Client("192.168.1.38", 8080)
print(s)
colorama.init(autoreset=True)

message = "Hello dude"
client, server = s.debug_talk(f"{message}")
print(client)
print(server)
message_2 = "See you man!"
client2, server2 = m.debug_talk(f"{message_2}")
print(client2)
print(server2)
