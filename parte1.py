def main():
    valores = []

    while True:
        try:
            valor = float(input("Digite um valor real (ou 'sair' para encerrar): "))
            valores.append(valor)
        except ValueError:
            break  # Encerra o loop se o usuário digitar algo que não seja um número

    quantidade = len(valores)
    soma = sum(valores)
    media = soma / quantidade if quantidade > 0 else 0
    maior_que_20 = sum(1 for v in valores if v > 20)

    print(f"Quantidade de valores digitados: {quantidade}")
    print(f"Soma dos valores digitados: {soma}")
    print(f"Média aritmética dos valores digitados: {media}")
    print(f"Quantidade de valores digitados maior que 20: {maior_que_20}")


if __name__ == "__main__":
    main()