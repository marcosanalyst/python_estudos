aluno = {'nome': 'Luiz', 'idade': 19, 'nota_final': 'A','aprovacao': True }

print(aluno)

aluno['nome'] = 'Beatriz' # atualizou a KEY nome

print(aluno)

# Também posso utilizar o UPDATE

aluno.update({'nome': 'José', 'nota_final': 'B'})
print(aluno)

# Adicinar itens na minha lista.

aluno.update({'endereco': 'Rua Central'})
print(aluno)

print(aluno.get('endereco'))
print(aluno.get('campo_inexistente')) # retornará None

# deletar uma KEY específica

del aluno['idade']
print(aluno)

