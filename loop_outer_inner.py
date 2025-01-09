# == for loop nested ===

    # Outer loop
        # Inner loop

for numero1 in range(1,6):
    print("Produto " + str(numero1))
    for numero2 in range(1,11):
        print(numero1,numero2)

#===

palavra = "ALEATÓRIA"

for space in palavra:
    print(f' {space}', end= '')
