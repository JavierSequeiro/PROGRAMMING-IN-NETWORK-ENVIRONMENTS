from Client0 import Client
import termcolor

print("------| Practice 2, Exercise 4 |------")

s = Client("192.168.1.38", 8080)
m = Client("192.168.1.38", 8080)
print(s)
message = "Hello dude"
client, server = s.debug_talk(message)
print(f"To server: {client}")
print(f"From server: {server}")

client2, server2 = m.debug_talk("See you man!")
print(f"To server: {client2}")
print(f"From server: {server2}")