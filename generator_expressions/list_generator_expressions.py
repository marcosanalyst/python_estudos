# Se necessário estudar mais, valores de memória não condizem com o console do exemplo

from sys import getsizeof

# Generator Expressions
    # Uma forma mais rápida para Listas, dicionários, etc
    # MENOR MEMÓRIA ALOCADA!
    # Valores em bytes

numeros = [x * 10 for x in range(11)]
print(numeros) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(type(numeros)) # <class 'list'>
print(getsizeof(numeros)) # 184 b de memória

# Aplicado o GENERATOR EXPRESSION
# REMOVO os CONCHETES e troco pelos PARENTESES

numeros = (x * 10 for x in range(11))
print(numeros) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(type(numeros)) # <class 'generator'>
print(getsizeof(numeros)) # 200 b de memória
