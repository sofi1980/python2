# desarrolle un algoritmo que defina dos listas de 10 elementos cada uno las cuales seran 
#llenadas con valores digitados por el usuario decir si es par o  y  si guardan en cada lista
#ejerciio 12 de mayo
listauno=[]
listados=[]

for i in range(10):
    valor=int(input('digite nro'))
    if valor %2==0:
        listauno.append(valor)
    else:    
        listados.append(valor)
print(listauno)
print(listados)