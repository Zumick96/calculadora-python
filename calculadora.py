
while True:
    operacao = input("Qual operação deseja fazer? (+, /, *, -): ")
    if operacao not in ["+", "/", "*", "-"]:
        print("Operação inválida! Tente novamente.")
        continue

    try:
        numero1 = float(input("Digite um número: "))
        numero2 = float(input("Digite outro número: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if operacao == "+":
        resultado = numero1 + numero2
        print("Resultado da soma:", resultado)
    elif operacao == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print("Resultado da divisão:", resultado)
        else:
            print("Não é possível dividir por zero!")
    elif operacao == "*":
        resultado = numero1 * numero2
        print("Resultado da multiplicação:", resultado)
    elif operacao == "-":
        resultado = numero1 - numero2
        print("Resultado da subtração:", resultado)
    else:
        print("Operação inválida!")

    continuar = input("Deseja fazer outra operação? (s/n): ").lower()
    if continuar == "s":
        continue
    elif continuar == "n":
        print("Obrigado por usar a calculadora!")
        break  
    else:
        print("Opção inválida! Encerrando o programa.")
        break