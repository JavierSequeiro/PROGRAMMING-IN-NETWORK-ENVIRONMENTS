from Client0  import Client

print("------| Practice 2, Exercise 3 |------")
s = Client("192.168.1.38", 8080)
print(s)
print("Sending message to the server...")

response = s.talk("Hello dude!!")
print(response)