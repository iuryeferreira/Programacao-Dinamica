char = str(input("Digite uma letra: "))
string = str(input("Digite uma palavra: "))

cont = 0

aux_string = list(string)
for i in aux_string:
    if i == char:
        cont+=1

print(f"O número de vezes que o caractere '{char}' aparece na string '{string}' é {cont} vezes")