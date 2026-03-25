 Programa para converter segundos em horas, minutos e segundos

# dando o número de segundos
total_segundos = int(input("Digite o número de segundos: "))

# Calculando horas, minutos e segundos
horas = total_segundos // 3600  # cada hora tem 3600 segundos
resto = total_segundos % 3600
minutos = resto // 60           # cada minuto tem 60 segundos
segundos = resto % 60

# Mostrando  o resultado
print(f"{total_segundos} segundos correspondem a {horas}h {minutos}m {segundos}s")


# Programa para converter horas, minutos e segundos em segundos

# Solicita horas, minutos e segundos
horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

# Calcula o total de segundos
total_segundos = horas * 3600 + minutos * 60 + segundos

# Exibe o resultado
print(f"{horas}h {minutos}m {segundos}s correspondem a {total_segundos} segundos")
