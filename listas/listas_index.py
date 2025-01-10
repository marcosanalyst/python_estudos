cidade1 = "São Paulo"
cidade2 = "Rio de Janeiro"
cidade3 = "Curitiba"
cidade4 = "Santa Catarina"
cidade5 = "Manaus"

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Santa Catarina", "Manaus"]
# INDEX!!        0            1            2                3            4

# Como imprimir um INDEX específico?

print(cidades[0])
print(cidades[1])
print(cidades[2])
print(cidades[3])
print(cidades[4])

print(cidades[-1]) # começa do último elemento da direita para esquerda

# Como trocar o valor de um dado?
# ou seja, o index "0" São Paulo será substituido pelo valor que eu definir!

cidades[0] = "Brasilia"
print(cidades)
