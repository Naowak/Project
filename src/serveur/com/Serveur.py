# Définition d'un serveur réseau gérant un système de CHAT simplifié.
# Utilise les threads pour gérer les connexions clientes en parallèle.

HOST = ''
PORT = 12002

import socket, sys, threading
from ThreadClient import *
from varGlobale import *

   

# Initialisation du serveur - Mise en place du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print("Serveur prêt, en attente de requêtes ...")
mySocket.listen(5)

# Attente et prise en charge des connexions demandées par les clients :
while 1:    
    connexion, adresse = mySocket.accept()
    # Créer un nouvel objet thread pour gérer la connexion :
    th = ThreadClient(connexion)
    th.start()
    # Mémoriser la connexion dans le dictionnaire : 
    it = th.getName()        # identifiant du thread
    conn_client[it] = connexion
    print("Client %s connecté, adresse IP %s, port %s." %\
           (it, adresse[0], adresse[1]))
    # Dialogue avec le client :
    connexion.send("Vous êtes connecté. Envoyez vos messages.".encode())