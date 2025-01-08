import math

#print
print('Hello World!')

#atalho comentário: ctrl + /

''''
Comentário de múltiplas linhas
...
...
'''

# variáveis

nome = "Andrew S2"
print(nome)

#int, float, string, boolean, none

idade = 32 #  (int) para números inteiros
peso = 80.5 # (float) para números com casa flutuante
nome = 'Marcos' # (String) caraceteres
user_status = True # (Bool) Valores lógicos
resultado = None # (None) Ausência de valor

#type
print(type(idade))
print(type(peso))
print(type(user_status))
print(type(None))

# concatenação de String
# Meu nome é Marcos e tenho 32 anos

print('Meu nome é', nome, 'e tenho', idade, 'anos de idade!')

# realizando cálculo

num1 = 10
num2 = 5
resultado2 = num1 + num2

print(resultado2)
print(9-9)
print(9+9)
print(9/9)
print(9*9)

# módulo
resultado3 = num1 % num2
print(resultado3)
# resultado de módulo 10 % 5 = 0

alunos_presentes = 23
alunos_ausentes = 17

# exemplo de soma
total_alunos =alunos_ausentes + alunos_presentes
print(total_alunos)

# Operador de atribuição aumentada

prod1 = 10
prod1 += 3
resultado2 = prod1

print(resultado2)

# funções básicas para números

num3 = 3.3425
num4 = 8.9425

print(round(num3)) # 3 # remove as casas decimais, arredonda para cima ou par baixo
print(round(num4)) # 9 #

print(round(num3,2)) # Duas casas decimais!

# potência

num5 = 2

print(pow(2,3)) # 2 elevado a 3 = 8

# max e min
print(max(2,3,4,18,99)) # 99
print(min(2,3,4,18,99)) # 2
print(sum([1,2,3])) # 6

# ordem dos operadores
'''
1. Parênteses ()
2. Exponenciação **
3. Multiplicação *
4. Divisão /
5. Divisão Inteira //
6. Módulo %
7. Adição +
8. Subtração - 

'''

# Módulo Math
# https://docs.python.org/3/library/math.html
# Devo importar o módulo "import math"

print(math.floor(4.2)) # 4
print(math.ceil(4.2)) # 5
print(math.pow(2,3)) # 2 elevado a 3 é 8
print(math.sqrt(9)) # raiz quadrada de 9 é 3
print((math.gamma(10)))

# Strgin multilinhas

mensagem = "Este curso é muito bom!"

mensagem2 = '''
Você está indo muito bem!
Parabéns!
:)
'''

print(mensagem)
print(mensagem2)

# Indexação

print(mensagem[0]) # "E" # Index ZERO é o primeiro caracter!

# Fatiamento (slicing)

print(mensagem[0:4]) # "Este" # Index ZERO até o index 4.
print(mensagem[-1]) # "!" # Último index

# Métodos comuns em Strings

#print(mensagem.) # . acesso os métodos da mensagem
print(mensagem.upper()) # ESTE CURSO É MUITO BOM!
print(mensagem.lower()) # este curso é muito bom!
print(mensagem.strip()) # remove os espaços em branco no início da String
print(mensagem.replace('bom', 'excelente')) # substitui 'bom' por 'excelente'
print(mensagem.split()) # separa todas as palavras # ['Este', 'curso', 'é', 'muito', 'bom!']

# Usando F-string format string

print(f'O meu nome é {nome} e tenho {idade} anos de idade!')

# Sequência de escape Escape Sequence

# quebra de linha \n
mensagem3 = 'Aprender Python é \n muito simples'
print(mensagem3)

# tabulação
mensagem4 = 'Coluna1\t Coluna2\t Coluna3\t'
print(mensagem4)

# mostrar caminho de algum arquivo

mensagem5 = 'c:\\users\\YAMAN'
print(mensagem5) # devo usar barra invertida dupla

mensagem6 = 'Aprender \'Python\' é muito fácil'
print(mensagem6)

# tabulações com String

mensagem7 = 'Nome:\tJoão Silva\nIdade:\t25\nPaís:\tBrasil'
print(mensagem7)

# Caracteres Unicode
mensagem8 = 'Coração: \u2764'
print(mensagem8)

# Função Input
# Criando uma sequência de input

# nome2 = input('Digite o seu nome: ')
# idade2= input('Digite a sua idade: ')
# pais_mora = input('Digite o país onde mora: ')
# print(f'Olá, meu nome é {nome2}, tenho {idade2} anos de idade e moro no {pais_mora}')

# Tipos de dados no input STRG, INT, FLOAT

nome3 = input('Digite o seu nome: ')
idade3 = int(input('Digite a sua idade: ')) # converto o input de STRG para INT



