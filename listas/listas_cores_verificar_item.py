
cor_cliente = input('Digite a cor desejada: ')

cores = ['amarelo', 'verde', 'azul', 'vermelho']

if cor_cliente.lower() in cores: # caso o cliente digite a cor com LETRA MAÍUSCULA o .lower converte para letra minúscula
    print ('Em estoque')
else:
    print('Não temos esta cor em estoque')