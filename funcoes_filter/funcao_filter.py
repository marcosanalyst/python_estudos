# Filter Function (FILTRO)
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, filtrando items. (list, tuple, dic, etc.)

# Criar uma função que filtra (remove) valores abaixo de 20!

valores = [10, 20, 30, 40, 50]

def removerValores(x):
    return  x > 20

print(map(removerValores, valores)) # <map object at 0x0000024FF882EF20>

print(list(map(removerValores, valores))) # [False, False, True, True, True]

# Aplicando o filter
print(list(filter(removerValores, valores))) # [30, 40, 50]

# melhorando a função
# deste modo posso remover a função removerValores e adicionar o lambda
print(list(filter(lambda x: x> 20, valores))) # [30, 40, 50]
