# teste de função com input

def boas_vindas(nome, quantidade):
    print(f'Olá {str(nome)}.')
    print(f'Temos {int(quantidade)} laptops em estoque.')


boas_vindas(nome = input('Digite seu nome: '),
quantidade = input('Digite a quantidade desejada: '))