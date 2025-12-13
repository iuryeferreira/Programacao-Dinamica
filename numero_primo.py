valor = int(input("Digite um valor: "))
while valor > 1000:
    print("O valor precisa ser menor do que 1000")
    valor = int(input("Digite um valor: "))

cont = 1
aux=0
cont_2=0

while cont <= valor:
    
    aux = valor % cont
    if aux == 0:
        cont_2+=1

    cont+=1

if cont_2 > 2:
    print(f"O número {valor} não é primo")
    

elif cont_2 == 2:
    print(f"O número {valor} é primo")
    