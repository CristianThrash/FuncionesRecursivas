'''
Created on 11/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna el valor absoluto de un numero dado.'''
def valorAbsoluto(numero):
    if numero >= 0:
        return numero
    else:
        return valorAbsoluto(-1*numero)
    
numero = input("Bienvenido. Escriba un numero: ")
print "abs("+str(numero)+") = "+str(valorAbsoluto(numero))
