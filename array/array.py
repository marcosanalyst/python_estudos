import array
# posso armazenar MILHARES de itens em um ARRAY
# devo utilizar o ARRAY quando tenho problemas de performace usando listas!

letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 10, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)


letras = array.array('u', ['a', 'b', 'c', 'd']) # adicionei mais um array, pois estava com erro
numeros_i = array.array('i', [10, 10, 30, 40])
numeros_f = array.array('f', [1.2, 2.2, 3.2])

print(letras)
