# While Loops
# Mostrar a comissão que será cobrada com a publicação do produto

valor = int(input('Digite o Valor do Produto em R$ '))

while valor > 20:
    valor = (valor * 0.10)
    print(f'O valor da comissão será R$ {valor}')
    break