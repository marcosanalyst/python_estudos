
list1 = set([1, 2, 3, 4, 5,6])
s1 ={1, 2, 3, 4, 5,6}

s1.add(7) # add adiciona item
s1.add(1) # se eu adicionar um item que já existe ele ignorará
s1.update([7, 8, 9, 10])
s1.remove(10) # remover
s1.discard(9) # descartar não gera erro se o remove tentar remover um item que não existe!

print(type(list1)) # <class 'set'>
print(s1)

