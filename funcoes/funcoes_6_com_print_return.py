'''
Neste caso ocorre SIM a soma, porém não retornará nada no console.
Aparecerá o input do numero1 e numero2, o programa roda e soma os dois números
porém sem print, pois estou utilizando o RETURN. O resultado estará armazenado na memória.

'''
def soma():
    numero1 = int(input('Digite o num1 '))
    numero2 = int(input('Digite o num2 '))
    return
    (numero1 + numero2)

soma()

'''
Agora utilizando PRINT
'''
def calcular():
    numero1 = int(input('Digite o num1 '))
    numero2 = int(input('Digite o num2 '))
    resultado = (numero1 + numero2)
    print(resultado)

calcular()