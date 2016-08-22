import socket
import subprocess
import config

s = socket.socket()
s.bind((socket.gethostname(), config.port))
s.listen(1)

while True:
    print("Listening...")
    (c, a) = s.accept()
    rbytes = c.recv(128)
    c.close()
    if rbytes == b"spegniti":
        print("Richiesta di spegnimento ricevuta.")
        subprocess.run("shutdown /s /t 15 /c \"Ricevuto comando off da Spegnimi Bot.\"")
