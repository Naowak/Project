import socket, sys, threading

class ThreadEmission(threading.Thread):
    """objet thread gérant l'émission des messages"""
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn           # réf. du socket de connexion
        
    def run(self):
        while 1:
            message_emis = input()
            self.connexion.send(message_emis.encode())