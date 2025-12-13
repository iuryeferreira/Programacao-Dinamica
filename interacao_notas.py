#nota = float(input("Digite uma nota: "))

for i in range(3):
    nota = float(input("Digite uma nota: "))
    if nota >= 0:
        break
    print("Nota inválida")

print("Fim do programa")