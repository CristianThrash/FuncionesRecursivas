'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna el maximo comun divisor entre 2 numeros dados.'''
def mcd(numero1, numero2):
    if(numero1%numero2==0):
        return numero2
    else:
        return mcd(numero2,numero1%numero2)
    
numero1 = input("Ingrese un numero: ")
numero2 = input("Ingrese otro numero: ")
print "mcd("+str(numero1)+","+str(numero2)+") = "+str(mcd(numero1, numero2))
