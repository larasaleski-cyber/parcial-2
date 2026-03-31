# determinar juros simples

# valores
C = float(input("Digite o capital (C): "))     # Capital investido
I = float(input("Digite a taxa de juros (I) %: "))  # Taxa de juros em porcentagem
T = float(input("Digite o tempo (T) em meses ou anos: "))  # Tempo do investimento

# Fórmula de juros simples: J = (C * I * T) / 100
J = (C * I * T) / 100

# Mostrar o resultado
print(f"O valor dos juros simples é: {J:.2f}")
