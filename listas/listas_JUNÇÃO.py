# JUNÇÃO DE LISTAS de acordo com o INDEX (sequêncial)
# Index 0 de uma lista com Index 0 de outra lista

#isso chama zip!

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores =[10, 20, 30, 40]

duas_listas = zip(cores, valores
                  )
print(list(duas_listas))

# [('amarelo', 10), ('verde', 20), ('azul', 30), ('vermelho', 40)]


