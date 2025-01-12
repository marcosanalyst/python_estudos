# Map Function
    # Muito utilizado com listas
    # Aplicar uma função a um Iterable, por item
    # (list, tuple, dictnary, etc.)

lista1 = [1,2,3,4,5]

def multiplicar(x):
    return x * 2

# print(multiplicar(2)) # 2x2 retornará 4

# Agora quero que minha função multiplique todos os itens da lista. Uso o MAP.
# Ele vai fazer o ITERABLE (iteração)

lista2 = map(multiplicar, lista1)

print(lista2) # vai me retornar um OBJECT <map object at 0x000001FB46E79210>

# devo converter para o tipo LIST

print(list(lista2)) # [2, 4, 6, 8, 10]