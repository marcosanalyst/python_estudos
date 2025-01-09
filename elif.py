# Decisões IF, ELSE e ELFI

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade < 60:    # simplificado: 18 <= idade <60:
    print("Maior de idade")
else:
    print('Idoso')

# Estrutura if and else

velocidade = 85

if velocidade > 120:
    print("Você está acima da velocidade permitida! ATENÇÃO REDUZA A VELOCIDADE!")
elif velocidade < 60:
    print("Você está abaixo da velocidade permitida! ATENÇÃO AUMENTE A VELOCIDADE PARA 80 KM/h!")
else:
    print("Velocidade OK!")

# Posso usar quantos ELFI eu quiser dentro da estrutura do IF / ELSE


renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print("Financiamento APROVADO")
else:
    print("Financiamento NEGADO")
