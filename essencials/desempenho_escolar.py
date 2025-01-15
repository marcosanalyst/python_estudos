'''
O professor digita a nota e o sistema calcula de acordo:

Menor que 0, nota inválida
Maior ou igual a 9, A
Maior ou igual a 7, B
Maior ou igual a 5, C
Menor do que 5,


'''

nota_do_aluno = int(input('Digite a nota do aluno: '))

if nota_do_aluno <0:
    print('Nota inválida!')
elif nota_do_aluno >= 9:
    print('Nota A')
elif nota_do_aluno >= 7:
    print('Nota B')
elif nota_do_aluno >= 5:
    print('Nota C')
else:
    print('Nota D')


