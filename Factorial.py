'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna el factorial de un numero dado.'''
def factorial(numero):
    if(numero==0):
        return 1;
    else:
        return numero*factorial(numero-1)
    
numero = input("Bienvenido. Escriba un numero entero: ")
print str(numero)+"! = "+str(factorial(numero))
