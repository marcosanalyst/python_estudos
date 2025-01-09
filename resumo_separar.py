# Functions (funções)
    # DRY - Don't repeat yourself.abs

# def (significa função) + (nome da função) + (4 espaços do index)
def boas_vindas():
    print("Olá nome seja bem-vindo!")
    print("Temos 5 laptops em estoque.")

# ao excecutar o código a função não será exibida, devo chama-la com o seguinte comando:

boas_vindas()

#===

#

def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)

def somar_dois_numeros2():
    numero1 = 20
    numero2 = 10
    resultado = numero1 + numero2
    print(resultado)

somar_dois_numeros()
somar_dois_numeros2()

# no caso acima eu tenho variáveis LOCAIS com o mesmo nome, porém estão dentro de funções diferente(são dois blocos independentes), por isso Python não reclama por elas terem o mesmo nome!


#===

# Functions (funções)
    # Parametro --> Argumento
#def boas_vindas("Aqui dentro vem os PARAMETROS"):
# ARGUMENTO você coloca ao chamar a função!
# por exemplo: boas_vindas("Marcos", 5)

def boas_vindas(nome, quantidade):
    print(f'Olá {str(nome)}.')
    print(f'Temos {int(quantidade)} laptops em estoque.')

boas_vindas('Marilene', 9 )
boas_vindas('Marcos', 8 )
boas_vindas('Giovana', 5 )

#===

#Default = Aquele que você define o valor no parametro
# Non-Default = Aquele que você NÃO define o valor no parametro

def boas_vindas(quantidade, nome="Irineu"):
    print(f"Olá {nome}!")
    print(f"Temos {quantidade} laptops em estoque.")


boas_vindas(3)


#===

def cliente1(nome):
    print(f"Olá {nome} !")

def cliente2(nome):
    return f"Olá {nome}!"

x = cliente1("Maria")
y = cliente2("José")

print(x)
print(y)


#===

# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Vários Argumentos (xargs)
# Criar uma função que soma vários números!


def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


x = soma(1,2,3,4,5)
print(x)


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