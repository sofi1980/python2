lista=[]

for x in range (5):
        valor=int(input('Escriba un número: '))
        if valor<=0:
            input('solo se acpeta nro postivos, oprima enter para continar ')
    
        else:
            lista.append(valor)
          
    
print(lista)