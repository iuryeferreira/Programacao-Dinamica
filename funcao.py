def triangulo(a, b, c):
    if a <= 0 or b <= 0 or c <=0:
        return False
    elif ((a+b>c) and (a+c>b) and (b+c>a)):
        return True

a = float(input("Didite o primeiro valor: "))
b = float(input("Didite o segundo valor: "))
c = float(input("Didite o sterceiro valor: "))

if triangulo(a,b,c):
    print("é possível formar um triângulo")
else:
    print("não é possível formar um triângulo")