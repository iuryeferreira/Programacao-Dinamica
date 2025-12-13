caracter = str(input("Digite um caracter: "))

string = list(input("Digite uma string: "))

list_caracter = []


#print([i for i, n in enumerate(string) if n == caracter]) 

for indice ,valor in enumerate(string):
    if valor == caracter:     
     list_caracter.append(indice)

print(list_caracter)