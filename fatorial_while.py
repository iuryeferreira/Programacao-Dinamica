n = int(input("Digite um valor:"))
aux = 1
fatorial=1
while aux <= n:

    fatorial = fatorial*aux

    aux+=1

print(f"O fatorial do valor {n} é {fatorial}")
