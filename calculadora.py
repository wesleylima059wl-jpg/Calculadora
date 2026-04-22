while True:
    try:
        print("\n--- NOVA CONTA ---") # O \n pula uma linha para ficar organizado
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /, **): ")
        num2 = float(input("Digite o segundo número: "))

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero!"
        elif operacao == "**": # Nova operação de Potência!
            resultado = num1 ** num2
        else:
            resultado = "Operação inválida!"

        print(f"O resultado é: {resultado}")

        # Pergunta se quer continuar
        sair = input("Deseja sair? (s/n): ")
        if sair.lower() == "s":
            print("Até logo!")
            break # O 'break' serve para quebrar o loop e fechar o programa

    except ValueError:
        print("Erro: Digite apenas números.")