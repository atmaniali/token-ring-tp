from Lib import *


HOST = "127.0.0.1"

def Handle_Neighbor(connexion, add, t, Sortie):
    while True : 
        # verifie if have token
        if t == 0:
            # don't have token wait for receve msg
            msg = connexion.recv(1024)
            if msg.decode() == "TOKEN":
                print("Vous avez recu le token")
                print("Vous avez le droit a la parole")
                print("Pour liberer la parole, il faut saisir le mot --TOKEN--")
                while True:
                    expression = input("Vous pouvez vous exprimer : ")
                    if expression == "TOKEN":
                        break

        if t == 1 :
            input("Vous etes l'initiateur du token tapez entrer pour le libirer")

        # Sortie is present thread Sd_Out
        Sortie.resume()
        
        t = 0 # si il etait l'initiateur il ne l'est plus



class Part_In(threading.Thread) : 
    
    def __init__(self, port , T, S) :
        threading.Thread.__init__(self)

        # initialiser la port
        self.port = port
        # initialiser le serveur T 
        self.T = T
        # thread sd_outt
        self.Sortie = S

        # creer socket appelee ss (self.ss)
        self.ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

        try:

            # attacher le socket declarer a une adresse IP <<localhost>>
            # et numero port recuperer dans <<self.port>>
            self.ss.bind(("127.0.0.1", self.port))
            # print(f"Le Sd_In s'attacher a l'adresse {HOST}  & numero de port {self.port} ")
            
        except :
            print(f"Le Sd_In n'arrive pas a s'attacher a l'adresse {HOST}  & numero de port {self.port} ")  
            print(socket.error, "error")
            sys.exit() 

        # metre socket en mode passive ecoute
        self.ss.listen()   


    def run(self):
        print("## YOU ARE THE SERVER OF NODE ##")
        # dans la methode run (), socket accept une seul demande de connexion
        self.connexion, self.add = self.ss.accept()      

        # appel de la fonction <<Handle_Neighbor qui est defini en haute de ce module  
        # Part_In.py 
        Handle_Neighbor(self.connexion, self.add, self.T, self.Sortie)