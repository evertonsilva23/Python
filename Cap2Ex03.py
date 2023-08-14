# Exercício 3: Escreva um programa que solicite ao usuário as horas e o
# valor da taxa por horas para calcular o valor a ser pago por horas de
# serviço.
# Digite as horas: 35
# Digite a taxa: 2.75
# Valor a ser pago: 96.25

hour = input("Digite as horas: ")
ihour = int(hour)
tax = input("Digite a taxa: ")
itax = float(tax)

print("Valor a ser pago:", ihour * itax)