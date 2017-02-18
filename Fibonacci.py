'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna el termino n-esimo de la sucesion de fibonacci.'''
def fibonacci(n):
    if(n==0 or n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

numero = input("Bienvenido. Escriba un numero entero: ")
print "El termino "+str(numero)+" de la sucesion de fibonacci es "+str(fibonacci(numero))