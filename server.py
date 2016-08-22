import socket
import botogram
import config
from wakeonlan import wol

bot = botogram.create(config.token)


@bot.command("off")
def shutdown(chat):
    # Check the chat id, continue only if it matches
    if chat.id in config.allowed_ids:
        s = socket.socket()
        s.connect((config.client_ip, config.port))
        s.send(b"spegniti")
        s.close()
        chat.send("Richiesta di spegnimento inviata con successo.")
    else:
        chat.send("Non hai i permessi per eseguire questo comando.")


@bot.command("on")
def switchon(chat):
    if chat.id in config.allowed_ids:
        wol.send_magic_packet(config.client_mac)
        chat.send("Richiesta di accensione inviata con successo.")
    else:
        chat.send("Non hai i permessi per eseguire questo comando.")


@bot.command("id")
def displayid(chat):
    chat.send(str(chat.id))

if __name__ == "__main__":
    bot.run()
