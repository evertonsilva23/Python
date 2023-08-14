# Exercício 3: Escreva um programa que solicite ao usuário as horas e o
# valor da taxa por horas para calcular o valor a ser pago por horas de
# serviço.
# Digite as horas: 35
# Digite a taxa: 2.75
# Valor a ser pago: 96.25
# Exercício 1: Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária de pagamento pelo tempo
# trabalhado acima de 40 horas
# Digite as Horas: 45
# Digite a taxa: 10
# Pagamento: 475.0

hour = input("Digite as horas: ")
ihour = int(hour)
tax = input("Digite a taxa: ")
itax = float(tax)
if ihour > 40:
    extra_tax = itax * 1.5
    extra_hour = ihour - 40
    print("Pagamento:", (40 * itax) + (extra_hour * extra_tax))
else:
    print("Valor a ser pago:", ihour * itax)