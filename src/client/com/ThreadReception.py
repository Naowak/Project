import socket, sys, threading

class ThreadReception(threading.Thread):
	"""objet thread gérant la réception des messages"""

	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connexion = conn # réf. du socket de connexion

	def run(self):
		while 1:
			message_recu = self.connexion.recv(1024)
			print("*" + message_recu.decode() + "*")
			if message_recu.decode() =='' or message_recu.decode().upper() == "FIN":
				break
				# Le thread <réception> se termine ici.
				# On force la fermeture du thread <émission> :
		th_E._Thread__stop()
		print("Client arrêté. Connexion interrompue.")
		self.connexion.close()