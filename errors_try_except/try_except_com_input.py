
# Quero que um usuário digite um valor inteiro no meu site de vendas online

try:
    valorProduto = int(input('Digite o valor do seu produto: '))
    print(type(valorProduto))
except  ValueError:
    print('Favor inserir apenas números!')

print('Mais código abaixo!')