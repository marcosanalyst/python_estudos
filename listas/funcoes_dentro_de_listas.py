cidade1 = "São Paulo"
cidade2 = "Rio de Janeiro"
cidade3 = "Curitiba"
cidade4 = "Santa Catarina"
cidade5 = "Manaus"

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Santa Catarina", "Manaus"]
# INDEX!!        0            1            2                3            4

cidades.append('Salvador') # append (acrescentar): adiciona o item no final da lista
cidades.remove('Rio de Janeiro') # remove: remove um item da lista
cidades.insert(0, 'Santo Anastácio') # insert: insere o item na posição que eu definir!
cidades.pop(0) # pop: remove um item da lista de acordo com o INDEX
cidades.sort() # sort: organiza a lista em ordem alfabética

print(cidades)