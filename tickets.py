import random

#Prograa que  simula la  generacion d un ticket con cinco numeros al azar que pedira al usuario un numero entre 1 y 5 si el usuario aciierta en el ultimo numero generado en el ticket tendra 50% de descuento en su compra


#Funcion que genera los numeros del ticket 
def ticket():
    numeros_tikcet=[]
    
    for k in range(5):
        numeros_tikcet=[random.randint(1, 5)]
        print(numeros_tikcet, end="")
        
    return numeros_tikcet



#Funcion que compara el numero ingresado del cliente con el ultimo generado del ticket
def comparacion(numeros_tikcet):
    print("Dame un numero entre 1 y 5: ")
    
    cliente_numero=int(input())
    
    
    
    if len(numeros_tikcet)>0:      #Si el largo de la lista numeros_ticket es mayor a 0
    
        ultimo_numero= numeros_tikcet[-1]   #La variable creada ultimo_numero sera igual
                                            #al numero que hay en el ultimo espacio de la
                                            #lista numeros_ticket
                                            
                                            
        if ultimo_numero==cliente_numero:
            print("50% de descuento")
         
        else:
            print("no hay descuento :(")


#Llamamos a las funciones
numeros_tikcet=ticket()
cliente_numero=comparacion(numeros_tikcet)
    
