'''
XARGS = FUNÇÃO QUE SOMA VÁRIOS NÚMEROS (ARGUMENTOS!)
usarei o FOR para percorrer meus argumentos!
'''

# Vários Argumentos (xargs)
# Criar uma função que soma vários números!

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(1,2,3,4,5)
print(x)