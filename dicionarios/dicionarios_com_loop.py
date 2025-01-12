
# Dicionário com loop

aluno = {'nome': 'Luiz', 'idade': 19, 'nota_final': 'A','aprovacao': True }
            # {key: , value}

for x in aluno:
    print(x) # imprimirá as KEYS: nome, nota_final e aprovacao

# é a mesma coisa que:
for x in aluno.keys():
    print(x)

# imprimindo os valores:
for x in aluno.values():
    print(x) # imprimirá os VALUES: Luiz, 19, A e True

# imprimir ITENS, puxará as KEYS e VALUES

for x in aluno.items():
    print(x) # imprimirá no formato de Taples

# para remover os ITENS dentro da TUPLE

for keys, values in aluno.items():
    print(keys, values)
'''
nome Luiz
idade 19
nota_final A
aprovacao True
'''