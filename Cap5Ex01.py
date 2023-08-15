# Exercício 1: Escreva um programa que lê repetitivamente números até
# que o usuário digite “pronto”. Quando “pronto” for digitado, mostre a
# soma total, a quantidade e a média dos números digitados. Se o usuário
# digitar qualquer coisa que não seja um número, detecte o erro usando
# o trye o except e mostre na tela uma mensagem de erro e pule para o
# próximo número.
# Digite um número: 4
# Digite um número: 5
# Digite um número: dado errado
# Entrada Inválida
# Digite um número: 7
# Digite um número: pronto
# 16 3 5.333333333333333

xcontrol = ""
i = 0
soma = 0
while xcontrol != "pronto":
    try:
        control = input("Digite um número: ")
        if control == "pronto":
            break
        else:
            xcontrol = int(control)
    except:
        print("Dado errado")
    if type(xcontrol) == int:
        i = i + 1
        soma = soma + xcontrol
print("A soma total é: ", soma)
print("A quantidade de números é: ")
print("A média dos números é: ", soma / i)
