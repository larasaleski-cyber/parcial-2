# Programa de calculadora simples

# Solicita ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Mostra as opções de operação
print("Escolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# Solicita a escolha da operação
operacao = input("Digite o número da operação desejada: ")

# Realiza a operação escolhida
if operacao == "1":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacao == "2":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacao == "3":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operação inválida. Escolha entre 1, 2, 3 ou 4.")
