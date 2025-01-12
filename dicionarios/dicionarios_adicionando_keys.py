
# adicionando uma key que tem vários itens dentro. Por exemplo matérias:
# pois tenho Matemática, Português, Física, Inglês, etc

aluno = {'nome': 'Luiz',
         'idade': 19,
         'nota_final': 'A',
         'aprovacao': True,
         'materias': ['Fisica', 'Matematica', 'Ingles']} # coloco VALUES dentro de uma Lista
print(aluno) # {'nome': 'Luiz', 'idade': 19, 'nota_final': 'A', 'aprovacao': True, 'materias': ['Fisica', 'Matematica', 'Ingles']}

print(aluno.get('materias')) # ['Fisica', 'Matematica', 'Ingles']

# lenght, qual o tamanho das minhas KEYS dentro de aluno?
print(len(aluno)) # 5

print(aluno.keys()) # dict_keys(['nome', 'idade', 'nota_final', 'aprovacao', 'materias'])
print(aluno.values()) # dict_values(['Luiz', 19, 'A', True, ['Fisica', 'Matematica', 'Ingles']])

print(aluno.items())
# dict_items([('nome', 'Luiz'), ('idade', 19), ('nota_final', 'A'), ('aprovacao', True), ('materias', ['Fisica', 'Matematica', 'Ingles'])])



