# classe + Nome da classe com letra maíuscula

# criar a Classe
class Funcionarios:
# CONSTRUTOR!!
    def __init__(self, nome, sobre_nome, data_nascimento): # self vai ser o o OBJETO.ARGUMENTO
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.data_nascimento = data_nascimento

# agora não importa quantos OBJETOS eu tenha, esse objeto sempre será troca da pelo SELF

# depois disso passos meus parâmetros

usuario1 = Funcionarios('Marcos', 'Silva', '12/01/1912')
usuario2  = Funcionarios('Carol','Santana', '12/01/1999')

''' TENHO O MESMO RESULTADO QUE O ABAIXO EM APENAS 2 LINHAS!
Caso eu tenho que cadastrar milhares de usuário, esta forma não funcionará!
Por isso devemos utilizar os CONSTRUTORES
# criar os parâmetros do usuario1
usuario1.nome = 'Marcos'
usuario1.sobre_nome = 'Silva'
usuario1.data_nascimento = '12/01/1912'

# criar os parâmetros do usuario2
usuario2.nome = 'Carol'
usuario2.sobre_nome = 'Santana'
usuario2.data_nascimento = '12/01/1999'
'''

# print
print(usuario1.nome)
print(usuario1.sobre_nome)
print(usuario1.data_nascimento)

# print
print(usuario2.nome)
print(usuario2.sobre_nome)
print(usuario2.data_nascimento)

