import socket, sys, threading
from varGlobale import *

class ThreadClient(threading.Thread):
    '''dérivation d'un objet thread pour gérer la connexion avec un client'''
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.connexion = conn
        
    def run(self):
        # Dialogue avec le client :
        nom = self.getName()        # Chaque thread possède un nom
        while 1:
            msgClient = self.connexion.recv(1024)
            if msgClient.upper() == "FIN" or msgClient =="":
                break
            message = "%s> %s" % (nom, msgClient)
            print(message)
            # Faire suivre le message à tous les autres clients :
            for cle in conn_client:
                if cle != nom:      # ne pas le renvoyer à l'émetteur
                    conn_client[cle].send(message.encode())
                    
        # Fermeture de la connexion :
        self.connexion.close()      # couper la connexion côté serveur
        del(conn_client[nom])        # supprimer son entrée dans le dictionnaire
        print("Client %s déconnecté." % nom)
        # Le thread se termine ici 