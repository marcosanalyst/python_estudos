
numeros = [1,2,3,4,5]
letras = ['a', 'b','c','d','e']

listasSomadas = numeros + letras

print(listasSomadas)
# [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

# Também posso:

numeros.extend(letras) # numeros extende letras, terei o mesmo resultado
print(numeros)
            #lista 0                #lista 1
itens = [['item1', 'item2'], ['item3', 'item4', 'item5', 'item6']] # sublistas

print(itens[0]) # ['item1', 'item2']
print(itens[1]) # ['item3', 'item4', 'item5']

print(itens[1][3]) # Lista 1, Index 3 | Imprimirá: 'item6'

