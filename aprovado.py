alunos = {'pedro':10, 'luiza':6.5, 'caio':4.5, 'bernardo': 3.5}

for i in alunos:
    if alunos[i] < 6:
        print(f"aluno reprovado : {i} : {alunos[i]}")

    elif alunos[i] >= 6:
        print(f"aluno aprovado : {i} : {alunos[i]}")

