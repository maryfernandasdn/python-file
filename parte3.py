def calcular_media_pares_impares():
    soma_pares = 0
    soma_impares = 0
    cont_pares = 0
    cont_impares = 0

    while True:
        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break

        if numero % 2 == 0:  # Número par
            soma_pares += numero
            cont_pares += 1
        else:  # Número ímpar
            soma_impares += numero
            cont_impares += 1

    # Cálculo das médias
    media_pares = soma_pares / cont_pares if cont_pares > 0 else 0
    media_impares = soma_impares / cont_impares if cont_impares > 0 else 0

    print(f"Média dos números pares: {media_pares}")
    print(f"Média dos números ímpares: {media_impares}")


# Chama a função
calcular_media_pares_impares()
