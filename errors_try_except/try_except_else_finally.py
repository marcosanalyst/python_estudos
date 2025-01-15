# ESTUDAR MAIS

try:
    valorProduto = int(input('Digite o valor do seu produto: '))
    print(type(valorProduto))
except  ValueError:
    print('Favor inserir apenas números!')
finally:
    print('Código ok')

# else: # se não houver erro!
#     print('Valor inserido com sucesso!')
#     resultado = valorProduto * 2
#     print(resultado)

print('Mais código abaixo!')