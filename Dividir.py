'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna el cociente de dividir el numero1 entre en numero2.'''
def dividir(numero1, numero2): 
    if (numero1-numero2) < 0:
        return 0
    else:
        return 1+dividir(numero1-numero2, numero2)
    
numero1 = input("Escriba un numero entero: ")
numero2 = input("Escriba otro numero entero")
print str(numero1)+"*"+str(numero2)+" = "+str(dividir(numero1, numero2))
