'''
Compra de qualquer valor = 5% de desconto
Compra acima de R$ 100 = 10% de desconto
compra acima de R$ 200 = 20% de desconto
'''

valor_compra = 250
if valor_compra <0:
    print('Valor de compra inválido!')
elif   valor_compra <100:
    print(valor_compra * 0.95)
elif valor_compra <200:
    print(valor_compra * 0.90)
else: # valor_compra >= 200:
    print(valor_compra * 0.80)