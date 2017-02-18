'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna el numero base elevado a la potencia indicada.'''
def potencia(base,exponente):
    if(exponente == 0):
        return 1
    else:
        return base * potencia(base, exponente -1)
    
base = input("Bienvenido. Escriba un numero entero: ")
exponente = input("Escriba la potencia a la que quiere elevar el numero")
print str(base)+"^"+str(exponente)+" = "+str(potencia(base, exponente))