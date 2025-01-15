# classe + Nome da classe com letra maíuscula

# criar a Classe
class Funcionarios:
# CONSTRUTOR!!
    def __init__(self, nome, sobre_nome, data_nascimento): # self vai ser o OBJETO.ARGUMENTO
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobre_nome


usuario1 = Funcionarios('Marcos', 'Silva', '12/01/1912')
usuario2  = Funcionarios('Carol','Santana', '12/01/1999')

print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.nome_completo(usuario2))

