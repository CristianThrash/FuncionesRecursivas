'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna el producto de los numeros ingresados.'''
def multiplicar(numero1, numero2):
    if numero2 == 0: 
        return 0
    else:
        return (numero1 + multiplicar(numero1, numero2 - 1))
    
numero1 = input("Escriba un numero entero: ")
numero2 = input("Escriba otro numero entero")
print str(numero1)+"*"+str(numero2)+" = "+str(multiplicar(numero1, numero2))