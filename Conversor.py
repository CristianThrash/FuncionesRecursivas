'''
Created on 18/02/2017

@author: Grabriela Ladino 20151020073, Brian Rodriguez 20151020600, Cristian Bernal 20151020523
'''

'''Retorna el equivalente en binario para un numero dado en base decimal.'''
def decimalABinario(decimal):
    if (decimal==1):
        return 1
    else:
        return decimal%2+10*decimalABinario(decimal/2)
  
'''Retorna el equivalente decimal para un numero dado en binario.'''
def binarioADecimal(binario):
    if (binario<=1):
        return binario
    else:
        return binario%10+2*binarioADecimal(binario/10)

numero = input("Digite un numero")
opcion = input("1 - Decimal a binario\n2 - Binario a decimal\n Seleccione una opcion: ")
if(opcion==1):
    print decimalABinario(numero)
elif(opcion==2):
    print binarioADecimal(numero)
