#gs
import operator
meses= {'Enero': 100,'Febrero': 200,'Marzo': 500,'Marzo':300,'Abril':1000,'Mayo':230,'Junio':450,'Julio':600,'Agosto':700,'Septiembre':1500,'Octubre':2000,'Noviembre':650,'Diciembre':450}
# print(meses)
a=((meses.values()))
nrodemeses=len(a)
print(a)
total=0
print(nrodemeses)
for key,  value  in meses.items():
    total+=meses[key]
    promedio=total/nrodemeses
  
    maximo = max(meses, key = meses.get)
    
    minimo = min(meses, key = meses.get)
    
print('el valor maximo es',maximo,'y su valor es ',meses[maximo])

print(f'el mes con menor produccion es : {minimo}')
print(f'el promedio es:{promedio}')


for key in meses.keys():
    if (meses[key]>=promedio):
    
        print('el mes',key,'es mayor que el promedio')
        
        
    elif (meses[key]<=promedio):
        
        print(f'el mes: {key}, es menor que el promedio')
        
 
