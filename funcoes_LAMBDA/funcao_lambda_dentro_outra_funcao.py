
# Evitar escrever duas funções

# Supondo que eu quero
def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))