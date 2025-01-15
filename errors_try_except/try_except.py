# Erro
    # Excelentes para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

letras = ['a', 'b', 'c']

try:
    print(letras[5]) # Index 5, não existe
except  IndexError:
    print('Index inexistente!')