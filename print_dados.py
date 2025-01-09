# O Anderson tem 30 anos e mora em São Paulo.

nome = 'Erik Defalt'
idade = str(18)
cidade = 'São Paulo'


print(" O " + nome + " tem " + idade + " anos e mora em " + cidade + ".")

# Pode-se converter idade para str usando: idade = str (abaixo da linha 35)


# Cliente inserindo dados com input


nome = input("Qual é o seu nome?: ")
idade = input("Qual é sua idade?: ")
idade = str(idade)
cidade = input("Qual cidade você mora?: ")

print(" O " + nome + " tem " + idade + " anos e mora em " + cidade + ".")

# calculo de idade baseado no ano de nascimento

ano_nascimento = input("Digite o seu ano de nascimento: ")
idade = 2023 - int(ano_nascimento)

print(idade)