# Função para realizar as operações
def calculadora():
    print("Escolha uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    operacao = input("Digite o número da operação: ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == '1':
        print(f"O resultado da soma é: {num1 + num2}")
    elif operacao == '2':
        print(f"O resultado da subtração é: {num1 - num2}")
    elif operacao == '3':
        print(f"O resultado da multiplicação é: {num1 * num2}")
    elif operacao == '4':
        if num2 != 0:
            print(f"O resultado da divisão é: {num1 / num2}")
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação inválida.")
        
calculadora()
