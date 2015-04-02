# Définition d'un client réseau gérant en parallèle l'émission
# et la réception des messages (utilisation de 2 THREADS).

host = ''
port = 12002

import socket, sys, threading
from ThreadEmission import *
from ThreadReception import *
    


# Programme principal - Établissement de la connexion :
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connexion.connect((host, port))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()    
print("Connexion établie avec le serveur.")
            
# Dialogue avec le serveur : on lance deux threads pour gérer
# indépendamment l'émission et la réception des messages :
th_E = ThreadEmission(connexion)
th_R = ThreadReception(connexion)
th_E.start()
th_R.start() 