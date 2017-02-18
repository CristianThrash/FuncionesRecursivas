'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna el factorial de un numero dado.'''
def factorial(numero):
    if(numero==0):
        return 1;
    else:
        return numero*factorial(numero-1)
    
numero = input("Bienvenido. Escriba un numero entero: ")
print str(numero)+"! = "+str(factorial(numero))