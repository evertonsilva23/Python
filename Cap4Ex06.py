# Exercício 6: Reescreva seu programa de cálculo de pagamento com um
# 1.5 o valor de hora de trabalho por hora extra, crie uma função chamada
# calculoPagamento que aceita dois parâmetros(horas e TaxaHora).
# Insira as Horas: 45
# Insira o valor da Hora de Trabalho: 10
# pagamento: 475.0

def calculoPagamento(horas, taxaHora):
    try:
        horas = input("Digite as horas: ")
        ihour = int(horas)
    except:
        print("Erro, por favor utilize uma entrada numérica")
        quit()
    try:
        taxaHora = input("Digite a taxa: ")
        itax = float(taxaHora)
    except:
        print("Erro, por favor utilize uma entrada numérica")
        quit()
    if ihour > 40:
        extra_tax = itax * 1.5
        extra_hour = ihour - 40
        print("Pagamento:", (40 * itax) + (extra_hour * extra_tax))
    else:
        print("Valor a ser pago:", ihour * itax)
calculoPagamento(45, 10)
