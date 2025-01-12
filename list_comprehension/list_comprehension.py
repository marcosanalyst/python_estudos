#  List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisar criar uma nova lista a partir de uma existente!!
    # [expressão for iten in intens]

frutas1 = ['abacate', 'banana', 'morango', 'abacaxi', 'kiwi']
'''

frutas2 = []

for iten in frutas1:
    if 'n' in iten:
        frutas2.append(iten)

print(frutas2)
'''

# Resolvendo em uma linha

frutas2 = [iten for iten in frutas1 if 'k' in iten]
print(frutas2)