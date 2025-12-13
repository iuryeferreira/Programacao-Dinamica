import math

p_x = []
p_y = []

for i in range(2):
    valor = int(input(f"Didite o valor da coordenada X do ponto {i+1}: "))
    p_x.append(valor)

for i in range(2):
    valor = int(input(f"Didite o valor da coordenada y do ponto {i+1}: "))
    p_y.append(valor)

euclidiana = math.sqrt(((p_x[0]-p_x[1])**2)+((p_y[0]-p_y[1])**2))

print(euclidiana)