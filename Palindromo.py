'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna cierto si la palabra ingresada es palindroma, de lo cntrario retorna falso.'''
def comprobarPalindromo(a):
    return a == a[::-1]

palabra = raw_input("Ingrese una palabra: ")
if(comprobarPalindromo(palabra)):
    print palabra + " es un palindromo"
else:
    print palabra + " no es un palindromo"
