from Lib import *
from component_node.Part_In import *
from component_node.Part_out import *
from Checking import *


if verif_nb_arg() == True :

    remove_file()
    
    # recuperer les paramaetres d'entre
    PORT_In = int(sys.argv[1])
    Have_Token = int(sys.argv[2]) # 1: have it 0 : else

    # lancer un thread pour Part_out
    Sd_Out = Part_Out()

    # lancer un thread pour Part_In
    Sd_In = Part_In(PORT_In, Have_Token, Sd_Out)
    Sd_In.start()

    # activer le thread Sd_Out
    # port_next_Neighbor =  int(input("Numero de port du voisin \n"))

    # port_in = verif_PORT_In_List(port_next_Neighbor)

    while True :
        port =  (input("Numero de port du voisin \n"))
        is_int = verif_type_Port(port)

        if is_int == False :
            print("Numero de port du voisin est un entier \n")
            print("Ressayer svp \n")

        else :   
            port_next_Neighbor = int(port) 
            port_in = verif_PORT_In_List(port_next_Neighbor)
            
            if port_in == False :
                add_Port_List(port_next_Neighbor)
                break
            print("Port est attacher a un notre node")
            print("Ressayer svp \n")
        

    # add_Port_List(port_next_Neighbor)
    Sd_Out.port_next_Neighbor = port_next_Neighbor
    Sd_Out.start()
