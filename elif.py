# Decisões IF, ELSE e ELFI

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade < 60:    # simplificado: 18 <= idade <60:
    print("Maior de idade")
else:
    print('Idoso')