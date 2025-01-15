# Multiplas entradas na mesma linha de Input()

dados = input('Digite o seu nome, sobre nome e idade: ').split() # Marcos 32
nome = dados[0]
sobrenome = dados[1]
idade = dados[2]


print(f'Meu nome é {nome.upper()} {sobrenome.lower()} e tenho {idade}')