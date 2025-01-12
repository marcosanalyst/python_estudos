
# Lambda Function
    # É uma função  (pequena) sem nome (associar a uma varíavel)
    # Pode ter vários argumentos mas somente 1 expressão
    # Muito utilizada dentro de outras funções!
    # Mantém o código mais limpo

# Lambda é executada somente uma vez dentro de outra função!

# Etapa 1
'''
def somar(x):
    return x + 10

print(somar(5))
'''

# Etapa 2 - Melhoria

# atribuindo a função a uma variável!
'''
variavel_somar_10 = lambda x: x + 10
print(variavel_somar_10(5))
# Terei o mesmo resultado
'''

# Etapa 3 - com mais Argumentos!
# x e y são os argumentos

somar10 = lambda x,y: x + y + 10
print(somar10(3,2))

# mesmo resultado!

