# Unpacking Lists (desempacotando listas)

produtos = ['arroz', 'feijão', 'laranja', 'banana', 5,6,7,8]
#index         0        1          2        3

# errado
# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
# item4 = produtos[3]

# correto

item1, item2, *outrosItens, item8 = produtos # criarei uma associação sequêncial!

print(item1)
print(item2)
print(item8)
