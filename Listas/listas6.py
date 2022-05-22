import math
from unicodedata import decimal
lista=[1,2,3,4,5]
print ("lista sin modificar orginal", lista )
for  i in range (0, len(lista)):
    # lista[i]= round((math.sqrt(lista[i])),2)
    lista[i]= math.sqrt((lista[i]))
print('la raiz cuadrada de la lista es:',lista)