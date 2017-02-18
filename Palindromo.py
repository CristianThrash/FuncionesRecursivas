'''
Created on 18/02/2017

@author: Grabriela Ladino, Brian Rodriguez, Cristian Bernal
'''

'''Retorna cierto si la palabra ingresada es palindroma, de lo cntrario retorna falso.'''
def comprobarPalindromo(a):
    return a == a[::-1]

palabra = raw_input("Ingrese una palabra: ")
if(comprobarPalindromo(palabra)):
    print palabra + " es un palindromo"
else:
    print palabra + " no es un palindromo"