valor = 100
dia = 0

while valor > 40:
    dia += 1
    print(f' No dia {dia} o produto será vendido por R${valor}')
    valor -= 5

# While loops

# Excelente para loops dependentes de uma condição

# Publicar um produto com comissão de 10% se for acima de R$ 20

valor = int(input("Digite o valor do produto em R$ "))

while valor > 20:
    valor = (valor * 1.1)
    print(f' O valor total do produto será R$ {valor}')
    break

'''
Python While Loop é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita.
E quando a condição se torna falsa, a linha imediatamente após o loop no programa é executada. 
O loop while cai na categoria de iteração indefinida . 
Iteração indefinida significa que o número de vezes que o loop é executado não é especificado explicitamente com antecedência.



As instruções representam todas as instruções recuadas pelo mesmo número de espaços de caracteres depois 
que uma construção de programação é considerada parte de um único bloco de código. 
Python usa endentação como seu método de agrupamento de declarações. 
Quando um loop while é executado, expr é avaliado primeiro em um contexto booleano e, se for verdadeiro, 
o corpo do loop é executado. 
Em seguida, a expr é verificada novamente, se ainda for verdadeira, 
o corpo é executado novamente e continua até que a expressão se torne falsa.
'''
