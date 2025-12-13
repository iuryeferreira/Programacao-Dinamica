import math

lados_tringulos = []
cont = 0
valor = -1

# hipotenusa = 0
# cateto_1 = 0
# cateto_2 = 0

while valor <  0 or cont < 3:
    
    valor = int(input("Didite um valor positivo:"))
    if valor < 0:
        print("O valor é invalido")
    elif valor > 0:
        cont+=1
        lados_tringulos.append(valor)


# for i in range(len(lados_tringulos)):
#     if(lados_tringulos[0]> lados_tringulos[1] and lados_tringulos[0]> lados_tringulos[2]):
#         hipotenusa = lados_tringulos[0]
#         cateto_1 = lados_tringulos[1]
#         cateto_2 = lados_tringulos[2]

#     if(lados_tringulos[1]> lados_tringulos[0] and lados_tringulos[1]> lados_tringulos[2]):
#         hipotenusa = lados_tringulos[1]
#         cateto_1 = lados_tringulos[0]
#         cateto_2 = lados_tringulos[2]

#     if(lados_tringulos[2]> lados_tringulos[0] and lados_tringulos[2]> lados_tringulos[1]):
#         hipotenusa = lados_tringulos[2]
#         cateto_1 = lados_tringulos[0]
#         cateto_2 = lados_tringulos[1]

if (lados_tringulos[0]+lados_tringulos[1]>lados_tringulos[2]) and (lados_tringulos[0]+lados_tringulos[2]>lados_tringulos[1] and (lados_tringulos[2]+lados_tringulos[1]>lados_tringulos[0])):
    
    print("é possível formar um triângulo com esses valores")
else:
    print("Não é possível formar um triângulo com esses valores")