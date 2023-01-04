from Lib import *


HOST = "127.0.0.1"


class Part_Out(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # initialiser le port du noud voisin
        self.port_next_Neighbor = 0

        # crrer socket appelees s (self s) 
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # thred event 
        self.__flag = threading.Event()
        self.__flag.set()


    def run(self):
        print("## YOU ARE THE CLIENT OF NODE ##")
        try :
            # se connecter au socket Sd_In du noud suivant
            # avec la port "self.port_next_Neighbor"
            self.s.connect((HOST, self.port_next_Neighbor))
        except socket.error as e :
            print("La partie OUT n'arrive pas a se connecter voisin")
            print("Error occurred while creating socket. Error code: " + e[0] + " Error message : " + e[1])
            sys.exit(1) 

        while True : 
            self.__flag.wait()    
            self.s.send(b"TOKEN")   
            self.__flag.clear()

    def resume(self)    :\
        self.__flag.set()