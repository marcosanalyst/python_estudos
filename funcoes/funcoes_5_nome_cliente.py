
def cliente1(nome):
    print(f"Olá {nome} !")

def cliente2(nome):
    return f"Olá {nome}!" # não imprimirá, pois não tem print, tem apenas return!

x = cliente1("Maria")
y = cliente2("José")

print(x)
print(y)
# print só imprimirá na tela, porém não armazenará em uma variável
# return é para utilizar o dado depois! Posso armazenar em um variável