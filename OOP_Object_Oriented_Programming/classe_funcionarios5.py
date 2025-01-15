from datetime import datetime

# classe + Nome da classe com letra maíuscula

# criar a Classe
class Funcionarios:
# CONSTRUTOR!!
    def __init__(self, nome, sobre_nome, ano_nascimento): # self vai ser o OBJETO.ARGUMENTO
        self.nome = nome
        self.sobre_nome = sobre_nome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobre_nome + ' ' + self.ano_nascimento

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento



usuario1 = Funcionarios('Marcos', 'Silva', 1992)
usuario2  = Funcionarios('Carol','Santana', 1993)

print(Funcionarios.idade_funcionario(usuario1))
print(Funcionarios.idade_funcionario(usuario2))

