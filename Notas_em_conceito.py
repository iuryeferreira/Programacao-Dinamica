#converter notas em conceitos

nome = str(input("Didite o nome do aluno: "))
nota_n = float(input("Didite a nota: "))
alternativa = str('s')

list_nome = []
list_nota_c = []

while alternativa !='n':
   
   if nota_n >= 8 and nota_n <= 10:
      nota_c = str('A')
      print(f'A nota teve conceito {nota_c}')

   elif nota_n >= 7 and nota_n < 8:
      nota_c = str('B')
      print(f'A nota teve conceito {nota_c}')

   elif nota_n >= 6 and nota_n < 7:
      nota_c = str('C')
      print(f'A nota teve conceito {nota_c}')

   elif nota_n < 6:
      nota_c = str('D')
      print(f'A nota teve conceito {nota_c}')

   list_nome.append(nome)
   list_nota_c.append(nota_c)
   dic_alunos = dict(zip(list_nome,list_nota_c))

   alternativa = str(input("Gostaria de continuar giditando as notas: sim [s] ou não [n] : "))
   if(alternativa) == 'n':
      break


   nome = str(input("Didite o nome do aluno: "))
   nota_n = float(input("Didite a nota: "))

print(dic_alunos)


