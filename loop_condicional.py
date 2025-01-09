compra_confirmada = False
dados_compra = "Compra no valor de R$ 10,00 confirmada"

# range(3) tentativas!
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviados para seu email!")
        break
else:
    print("Falha na compra!")