# Set (Listas)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

lista1 = [10, 20, 30, 40, 50]
lista2 = [10,20,90]

num1 = set(lista1)
num2 = set(lista2)

print(num1) # {} você perderá a indexação {40, 10, 50, 20, 30}
print(num2) # {} {10, 20, 90}

# operadores básicos

# UNION junta as duas listas, retirando os repetidos!
print(num1 | num2) # {50, 20, 90, 40, 10, 30}

# DIFFERENCE remove os itens repetidos da lista
print(num1 - num2) # {40, 50, 30}

# SYMMETRIC DIFFERENCE remove todos os valores repetidos de ambas as listas
print(num1 ^ num2) # {40, 50, 90, 30}

# AND o que é duplicado em ambas as listas, deixa apenas a intercção
print(num1 & num2) #

print(len(num1)) # 5 itens | len = length (comprimento)
print(len(num2)) # 3 itens