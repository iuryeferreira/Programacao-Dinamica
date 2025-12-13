valor = float(input("Digite o valor: "))
desconto = float (input("Digite o valor do esconto: "))

res = valor - (valor* desconto/100)

print(f"O valor do desconto é de {desconto} e o valor final é {res}")