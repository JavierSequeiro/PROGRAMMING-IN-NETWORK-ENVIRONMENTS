from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

s = Client("192.168.1.38", 8080)
s.ping()
print(f"IP: {s.ip}, {s.port}")
