# Exercício 2: Reescreva seu programa de pagamento utilizando try e
# except, de forma que o programa consiga lidar com entradas não numéricas graciosamente, mostrando uma mensagem e saindo do programa. A
# seguir é mostrado duas execuções do programa
# Digite as Horas: 20
# Digite a taxa: nove
# Erro, por favor utilize uma entrada numérica
# Digite as Horas: quarenta
# Erro, por favor utilize uma entrada numérica
try:
    hour = input("Digite as horas: ")
    ihour = int(hour)
except:
    print("Erro, por favor utilize uma entrada numérica")
    quit()
try:
    tax = input("Digite a taxa: ")
    itax = float(tax)
except:
    print("Erro, por favor utilize uma entrada numérica")
    quit()
if ihour > 40:
    extra_tax = itax * 1.5
    extra_hour = ihour - 40
    print("Pagamento:", (40 * itax) + (extra_hour * extra_tax))
else:
    print("Valor a ser pago:", ihour * itax)