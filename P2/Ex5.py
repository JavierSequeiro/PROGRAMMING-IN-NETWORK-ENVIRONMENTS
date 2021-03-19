from Client0 import Client
from pathlib import Path

print()
Client.ping()
s = Client("192.168.1.38", 8080)
gene = Path("../Session-04/U5.txt").read_text()
print(s.talk("Sending U5 gene to the server..."))
print(s.talk(gene))
