# estudar mais!

lista1 = [1,2,3,4,5]
'''
def multiplicar(x):
    return x * 2

lista2 = map(multiplicar, lista1)

print(list(lista2)) # [2, 4, 6, 8, 10]
'''

# Chegar no mesmo resultado com uma linha de código!

# PASSO 1

'''Transformar def multiplicar(x):
    return x * 2 em uma função LAMBDA associada a uma variável
    ===> lista2 = lambda x: x *2
'''

# PASSO 2
# chamo a função MAP no lugar da variável
print(list(map(lambda x: x *2, lista1)))