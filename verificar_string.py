string = input("Digite uma string: ")

n_string = string.split('.')

cont = 0

for i in n_string:       
    if i.isdigit() == True:
        cont+=1

if cont==2:
    print("A string é um número")
elif cont > 2:
    print("A string não é um número")
elif string.isdigit() == True:
    print("A string é um número")

