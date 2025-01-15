'''
X == Y IGUAL A
X != Y DIFERENTE DE
X > Y MAIOR QUE
X < Y MENOR QUE
X >= Y MAIOR IGUAL A
X <= Y MENOR IGUAL A
'''

X = 5
Y = 10

# IGUAL A
resultado_igual = X == Y
print(f"X == Y: {resultado_igual}")  # False, pois 5 não é igual a 10

# DIFERENTE DE
resultado_diferente = X != Y
print(f"X != Y: {resultado_diferente}")  # True, pois 5 é diferente de 10

# MAIOR QUE
resultado_maior_que = X > Y
print(f"X > Y: {resultado_maior_que}")  # False, pois 5 não é maior que 10

# MENOR QUE
resultado_menor_que = X < Y
print(f"X < Y: {resultado_menor_que}")  # True, pois 5 é menor que 10

# MAIOR IGUAL A
resultado_maior_igual = X >= Y
print(f"X >= Y: {resultado_maior_igual}")  # False, pois 5 não é maior nem igual a 10

# MENOR IGUAL A
resultado_menor_igual = X <= Y
print(f"X <= Y: {resultado_menor_igual}")  # True, pois 5 é menor ou igual a 10

