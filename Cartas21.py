'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

import random

'''Retorna el valor de una carta entregada'''
def valorCarta(carta, acumulado):
    if(carta[0]=="J" or carta[0]=="Q" or carta[0]=="K"):
        return 10
    if carta[0]=="A" and acumulado+11>21:
        return 1
    elif carta[0]=="A" and acumulado+11<=21:
        return 11
    else:
        return carta[0]

'''Retorna el valor de una mano de cartas estilo 21'''
def contarMano(listaDeCartas, acumulado):
    if len(listaDeCartas)==1:
        return valorCarta(listaDeCartas[0], acumulado)
    else:
        return valorCarta(listaDeCartas[0], acumulado)+contarMano(listaDeCartas[1:],acumulado+valorCarta(listaDeCartas[0],acumulado))
    
palos = ["Diamantes", "Picas", "Treboles", "Corazones"]
numeros = [2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
opcion = 1
mano = []
valorMano = 0;

while(opcion==1):
    carta = [numeros[random.randint(0,11)],palos[random.randint(0,3)]]
    mano.append(carta)
    valorMano = contarMano(mano, 0)
    print "Su carta es " + str(carta)
    if(valorMano < 21):
        opcion = input("Desea otra carta? 1=Si, 2=No: ")
    else:
        opcion = 2

if(valorMano==21):
    print "21 blackjack"
elif(valorMano < 21):
    print "Su mano ha sumado " + str(valorMano) 
else:
    print "Fuera de rango. Lo sentimos"
