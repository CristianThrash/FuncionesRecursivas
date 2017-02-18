'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna la suma de los digitos de un numero dado.'''
def sumarDigitos(numero):
    if(numero<10):
        return numero
    else:
        return numero%10+sumarDigitos(numero/10);
    
numero = input("Ingrese un numero")
print "La suma de los digitos de " + str(numero) + " es " + str(sumarDigitos(numero))