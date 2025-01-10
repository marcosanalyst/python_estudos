# Função criada
def somaNumeros(*variosNumeros):
    resultado = 0 # Valor de resultado inicia no ZERO que será somado com variosNumeros
    for cadaNumero in variosNumeros:
        resultado += cadaNumero
    return resultado

# Chamar função

numeros = list(map(int, input('Digite os números separados por espaço: ').split()))
soma = somaNumeros(*numeros)
print(f'A soma dos números é: {soma}')

