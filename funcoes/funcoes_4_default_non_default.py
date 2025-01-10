
#Default = Aquele que você define o valor no parametro
# Non-Default = Aquele que você NÃO define o valor no parêmetro

def boas_vindas(quantidade, nome="Jean"): # parâmetro NON-Default não pode estar no final!
    print(f"Olá {nome}!")
    print(f"Temos {quantidade} laptops em estoque.")


boas_vindas(3)

# parâmetro NON-Default não pode estar no final!