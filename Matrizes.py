
num_linha_matriz = int(input("Digite o número de linhas desejadas:"))
num_coluna_matriz = int(input("Digite o número de colunas desejadas:"))

matriz = []

#print(f"Matriz {num_linha_matriz} x {num_coluna_matriz}")
print("-----------------------------------------------------")

for i in range(num_linha_matriz):
    coluna_matriz = []
    for j in range(num_coluna_matriz):
        coluna_matriz.append(input(f"Digite os valor da posição {i+1}x{j+1}: "))
        
    matriz.append(coluna_matriz)

for i in matriz:
    print(i)
