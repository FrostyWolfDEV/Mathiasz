lista=[10,20,30,40,50,60,70,80] ; x=0 ; runtime=len(lista)
for i in range(len(lista)):
    if x==len(lista): x+=-1
    if lista[x]<24 or lista[x]>52: lista.pop(x) 
    else: x+=1
print(lista)