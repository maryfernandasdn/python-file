def main():
    alunos_aprovados = 0
    alunos_reprovados = 0
    total_alunos = 0

    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para encerrar): ")

        if nota.lower() == 'sair':
            break

        try:
            nota = float(nota)
            total_alunos += 1

            if nota >= 5:
                alunos_aprovados += 1
            else:
                alunos_reprovados += 1

        except ValueError:
            print("Por favor, insira uma nota válida ou 'sair' para encerrar.")

    print("\nResultados:")
    print(f"Quantidade de alunos que fizeram a prova: {total_alunos}")
    print(f"Quantidade de alunos aprovados: {alunos_aprovados}")
    print(f"Quantidade de alunos reprovados: {alunos_reprovados}")

if __name__ == "__main__":
    main()
