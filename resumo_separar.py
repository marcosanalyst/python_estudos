


#===
# Vários Argumentos (xargs) indentificando o Parametro
# criar uma função que armazena números e strings (dados)

def agencia(**carro):
    return carro

print(agencia(marca = "Honda", modelo = "Civic", motor= 2.0, placa= "AAA2222"))
print(agencia(marca = "Honda", modelo = "Civic", motor= 2.0,))
print(agencia(marca = "Honda", modelo = "Civic", motor= 1.8, placa= "AAA999"))

#===
# Qual o número fatorial de 4? 4 * 3 * 2 * 1 = 24

# errado
fatorial1 = 4 * 3 * 2 * 1

print(fatorial1)

# correto

import math

#===

# Listas
    # Armazenas mais de uma informação em variáveis
    # Manter a sequência dos dados em uma variável

cidade1 = "São Paulo"
cidade2 = "Rio de Janeiro"
cidade3 = "Curitiba"
cidade4 = "Santa Catarina"
cidade5 = "Manaus"

print(cidade1,cidade2,cidade3,cidade4,cidade5)
# errado

# vamos criar uma variável para armazenar em lista
# "nome da variável" + "=" + "[elementos que formarão a lista]""

#correto
cidades = ["São Paulo","Rio de Janeiro","Curitiba","Santa Catarina","Manaus"]

print(cidades)

#===
'''

cidade1 = "São Paulo"
cidade2 = "Rio de Janeiro"
cidade3 = "Curitiba"
cidade4 = "Santa Catarina"
cidade5 = "Manaus"

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Santa Catarina", "Manaus"]
# INDEX!!        0            1            2                3            4

# Como imprimir um INDEX específico?

print(cidades[0])

# Como trocar o valor de um dado?
# ou seja, o index "0" São Paulo será substituido pelo valor que eu definir!
cidades[0] = "Brasilia"
print(cidades)
'''