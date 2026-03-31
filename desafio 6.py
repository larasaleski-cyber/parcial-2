# Ganha o número de segundos do usuário
total_segundos = int(input("Digite o número de segundos: "))

# Conta horas, minutos e segundos
horas = total_segundos // 3600  # 1 hora = 3600 segundos
resto = total_segundos % 3600
minutos = resto // 60            # 1 minuto = 60 segundos
segundos = resto % 60

# Exibe o resultado
print(f"{total_segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos} segundos.")



# Recebe horas, minutos e segundos do usuário
horas = int(input("Digite o número de horas: "))
minutos = int(input("Digite o número de minutos: "))
segundos = int(input("Digite o número de segundos: "))

# Converte tudo para segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Exibe o resultado
print(f"{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {total_segundos} segundos.")
