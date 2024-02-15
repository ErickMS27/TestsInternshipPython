while True:
    nota_1 = float(input("Digite a sua primeira nota: "))
    while nota_1 < 0 or nota_1 > 10:
        print("Nota inválida. Por favor, digite uma nota entre 0 a 10:")
        nota_1 = float(input("Digite a sua primeira nota novamente: "))

    nota_2 = float(input("\nDigite a sua segunda nota: "))
    while nota_2 < 0 or nota_2 > 10:
        print("Nota inválida. Por favor, digite uma nota entre 0 a 10:")
        nota_2 = float(input("Digite a sua segunda nota novamente: "))

    nota_3 = float(input("\nDigite a sua terceira nota: "))
    while nota_3 < 0 or nota_3 > 10:
        print("Nota inválida. Por favor, digite uma nota entre 0 a 10:")
        nota_3 = float(input("Digite a sua terceira nota novamente: "))

    nota_4 = float(input("\nDigite a sua quarta nota: "))
    while nota_4 < 0 or nota_4 > 10:
        print("Nota inválida. Por favor, digite uma quarta entre 0 a 10:")
        nota_4 = float(input("Digite a sua quarta nota novamente: "))

    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

    print("\nNotas inseridas:\n")
    print("Primeira nota:", nota_1)
    print("Segunda nota:", nota_2)
    print("Terceira nota:", nota_3)
    print("Quarta nota:", nota_4)

    print("\nMédia das notas =", media)

    if media >= 7:
        print("\nVocê está aprovado(a)!")
    elif 4 <= media < 7:
        print("\nVocê está em recuperação.")
    else:
        print("\nVocê está reprovado(a).")

    restart = input("\nDeseja reiniciar a aplicação? Se SIM clique Y, caso não queira, clique N:\n")
    if reiniciar != 'y':
        print("Aplicação encerrada.")
        break
