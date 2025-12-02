
fatorial =1

n = int(input("Digite um número:"))
aux = n
for i in range(aux):
    
    fatorial = fatorial *(aux)

    aux-=1
 
print(f"O fatorial do valor {n} é {fatorial}")


