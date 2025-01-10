# Vários Argumentos (xargs) indentificando o Parâmetro
# criar uma função que armazena números e strings (dados)

def agencia(**carro): # para utilizar vários parâmetros coloco **
    return carro

print(agencia(marca = "Honda", modelo = "Civic", motor= 2.0, placa= "AAA2222")) # coloco o parâmetro aqui 'marca', 'modelo' e 'placa'
print(agencia(marca = "Honda", modelo = "Civic", motor= 2.0,))
print(agencia(marca = "Honda", modelo = "Civic"))